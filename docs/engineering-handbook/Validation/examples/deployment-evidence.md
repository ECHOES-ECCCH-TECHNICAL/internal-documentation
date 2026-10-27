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
