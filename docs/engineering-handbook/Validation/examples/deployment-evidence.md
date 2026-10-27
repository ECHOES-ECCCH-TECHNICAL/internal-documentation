# Deployment and Release Evidence

Deployment evidence links a source revision to the build, configuration and observed runtime state. CI and registry records identify the produced image. Deployment manifests describe the intended state, and runtime checks show what was actually running.

The examples cover OCI builds, GitOps and a Helm-managed application. They use demonstration values for registries and environments. See the [deployment and rollback guidance](../../SDLC/Deployment/pipelines-and-rollback.md) when adapting them.

## Build and release

The [CI excerpt](assets/deployment/ci-image-job.yml) shows a commit-based image tag, source revision label and Trivy vulnerability scan. Keep the test and OpenAPI lint reports, image scan results and OCI image digest. A published image has passed the configured pipeline checks. Any remaining vulnerabilities still need review.

The example mounts the host Docker socket for scanning. Use it only on an appropriately controlled runner, or choose a scanner that does not require access to the Docker daemon.

The [tag and digest example](assets/deployment/image-tag-digest.txt) illustrates image traceability. A digest identifies the exact image artefact. The [registry command reference](assets/deployment/harbor-commands.txt) is a command example, with credentials and image-pull secrets supplied separately through approved mechanisms.

| Stage | Evidence to retain | Related checks |
|---|---|---|
| Build | Source revision, test results and scan reports | Contract and build validation |
| Registry | Image tag, digest and access settings | Image traceability and access |
| Deployment | Rendered manifests, configuration and image reference | Applicable REQ-DEP-004/005/007/008 |
| Runtime | Actual image ID, rollout status and health responses | REQ-DEP-010 and applicable REQ-MON requirements |

## Container registry selection, naming, access and retention

This section provides a concrete Platform Core release record and recommended practices for other ECHOES providers. The GHCR identifiers below come from an October 2026 Platform Core build record. The Harbor commands are reusable examples.

### Registry options and access boundary

**GHCR is the recommended default** for publishing ECHOES application images. Platform Core uses `ghcr.io/echoes-eccch-technical/platform-api` in its CI/CD workflow. **PCSS Harbor is an alternative** operated by PCSS as an independent registry service outside the OpenShift/OKD PaaS. Using Harbor requires connectivity through the PCSS VPN and credentials authorised for the relevant Harbor project. The exact Harbor hostname and access configuration are provided by its operator.

An application running on OpenShift/OKD may pull from either registry **only if its cluster has a working network path and appropriate image-pull permissions**. A developer's VPN session does not establish connectivity from an OKD node to Harbor. This must be verified in the target environment before choosing Harbor as the deployment source.

### Real release example: Platform Core on GHCR

The retained October 2026 release evidence identifies one exact image:

| Field | Recorded value |
| --- | --- |
| OCI repository | `ghcr.io/echoes-eccch-technical/platform-api` |
| Source revision / image tag | `b5e809251eb2cdf90ed3f45eac988ea3b0a7de14` |
| OCI digest | `sha256:23bd8abcad257c3b76388404acc73443f8c756925d97e9a5c81475d10fc4d974` |
| GitHub Actions run (retained provider evidence) | `36863329968` |
| Recorded QA results | 462 tests passed; OpenAPI lint: five warnings; Trivy: 27 HIGH, zero CRITICAL |

The configured CRITICAL-severity vulnerability gate passed. The 27 HIGH findings were not cleared by that result and still require review or documented acceptance. A tag identifies a named build, whereas the digest identifies the precise OCI artefact. **production/staging promotion should reuse the same digest**, without rebuilding the image.

For a reader with permission to access this GHCR package, the recorded artefact can be checked with:

```bash
IMAGE=ghcr.io/echoes-eccch-technical/platform-api
COMMIT=b5e809251eb2cdf90ed3f45eac988ea3b0a7de14
DIGEST=sha256:23bd8abcad257c3b76388404acc73443f8c756925d97e9a5c81475d10fc4d974

docker manifest inspect "${IMAGE}@${DIGEST}" > /dev/null
# Optional, when pulling the image is authorised:
docker pull "${IMAGE}@${DIGEST}"
```

These are verification commands based on retained release identifiers, **not a claim that anonymous pulls currently work**. The published [image-tag-digest record](assets/deployment/image-tag-digest.txt) is the public example.

For a digest-pinned Kubernetes deployment, the image reference would be:

```yaml
containers:
  - name: platform-core
    image: ghcr.io/echoes-eccch-technical/platform-api@sha256:23bd8abcad257c3b76388404acc73443f8c756925d97e9a5c81475d10fc4d974
```

This is a **recommended deployment reference**, not an export from the running cluster. The published [staging Kustomize example](assets/deployment/staging-kustomization.yaml) currently uses a commit-based `newTag`.

### Harbor example: image publication and OKD access

The published [Harbor command example](assets/deployment/harbor-commands.txt) uses `registry.example.org` as a **placeholder**. After the operator supplies a reachable hostname, Harbor project and suitable robot/CLI credentials, a provider may publish an image as follows:

```bash
# Run where the PCSS VPN/network path to Harbor is available.
HARBOR_HOST='<operator-provided-hostname>'
HARBOR_PROJECT='<assigned-project>'
COMMIT=b5e809251eb2cdf90ed3f45eac988ea3b0a7de14

# Assumes the image has already been built/pulled locally and tagged with COMMIT.
docker login "${HARBOR_HOST}"  # prompts for authorised credentials
docker tag "platform-api:${COMMIT}" \
  "${HARBOR_HOST}/${HARBOR_PROJECT}/platform-api:${COMMIT}"
docker push "${HARBOR_HOST}/${HARBOR_PROJECT}/platform-api:${COMMIT}"
```

This shows the naming pattern `<registry>/<project>/<image>:<commit>`but it **does not mean Platform Core has been pushed to PCSS Harbor**. An approved OpenShift pull secret must then be associated with the workload's actual ServiceAccount. The repository's demonstration Deployment uses `image-puller`:

```bash
# Only after an administrator has provisioned the secret in the target namespace:
oc -n '<namespace>' secrets link image-puller '<pull-secret>' --for=pull
```

Before deployment, the operator must verify **both** network reachability from the target cluster and authorised image pulls. Successful developer access over VPN is not sufficient proof. The [operator verification commands](assets/deployment/operator-verification.txt) show how to compare configured image references, observed Pod image IDs and rollout status after deployment.

### Release naming and retention baseline (recommendation)

1. **Naming:** Use one application repository per deployable component, a meaningful project/namespace, and a source commit SHA or immutable release identifier as the image tag. Record the resulting digest and CI run with each release. Do not use `latest` as the only traceable deployment reference.
2. **Promotion:** Build and scan the image once. Run the deployment checks in staging, then promote the **same digest** to the next environment.
3. **Credentials:** Limit push rights to designated publishers or CI identities. Give OpenShift workloads only the pull permissions they need. Keep tokens, Docker auth files and pull secrets out of source control and public evidence. Apply the PCSS VPN requirement to Harbor users/runners, and confirm a separate allowed cluster-to-registry path for runtime pulls.
4. **Retention:** Protect all digests used by active workloads in each environment and retain **at least the last two or three known-good releases** for rollback, as recommended in [Deployment Pipelines and Rollback Strategies](../../SDLC/Deployment/pipelines-and-rollback.md). Do not delete a tagged image until its deployment references and rollback dependencies have been checked. An automated age-based deletion rule, quota or immutable-tag policy must be confirmed with the relevant registry operator; none is asserted here.

**Evidence to retain for an assessed release:** source revision, CI run and checks, OCI repository/tag/digest, registry access classification (public/private), deployment configuration revision, observed workload image ID, readiness/smoke-test results, and rollback references. Exclude credentials and internal network details from public records.

**Scope and limitations:** This section defines recommended provider practices and documents one real GHCR release. It does not establish the deployed configuration of every provider's registry, the live availability of the example image, formal registry-level RBAC/retention settings, or verified OKD connectivity to the independently operated PCSS Harbor service. Those facts require operator evidence where relevant.

## Kubernetes and GitOps

The [Kustomize overlay](assets/deployment/staging-kustomization.yaml) sets example staging values and replaces the image reference. The [Deployment fragment](assets/deployment/base-deployment-excerpt.yaml) includes configuration and Secret references, a ServiceAccount and a readiness probe. Both need the rest of the application configuration before use.

The [Argo CD Application](assets/deployment/staging-argocd-application.yaml) demonstrates the GitOps source and destination. For a real assessment, record the Git revision, rendered manifests and deployed image. Verify the workload's readiness in the target environment.

The [operator commands](assets/deployment/operator-verification.txt) cover manifest rendering, a server-side dry-run, application status and rollout checks. Keep the actual command outputs as evidence of execution.

## Helm-managed applications

The [Helm CI excerpt](assets/deployment/zammad-ci-validation.yml) renders environment values. The [deployment command](assets/deployment/zammad-helm-deploy.sh) uses a fixed chart version and `--atomic --wait`. The [image overrides](assets/deployment/zammad-image-overrides.yaml) show a separate configuration for component image sources.

Retain the chart version, effective values with secrets redacted, rendered manifests and release status. Verify readiness after deployment. Helm rollback covers Helm-managed resources. Other resources need their own rollback process.

## Keeping release evidence

For each assessed release, record the environment, software revision, checks executed and observed outcomes. Changes to APIs, authentication, image versions or deployment configuration may require reassessment.

Public evidence should exclude credentials, internal host inventories and detailed access rules. Store sensitive source logs and cluster information in an appropriately restricted location, and publish a reviewable summary where needed.
