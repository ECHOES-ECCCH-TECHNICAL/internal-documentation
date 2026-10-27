# VTL SEC-03 endpoint classification: public evidence summary

Review month: October 2026. Source: provider-reviewed security configuration, route observations and representative access-control checks. The complete inventory of URL matchers, exact endpoint paths, privileged functions, infrastructure topology and internal ports has been removed from this public version for defensive security reasons. The original is retained by the resource provider.

| Function category | Classification | Supporting finding / scope |
|---|---|---|
| Public web entry and approved published content | PUBLIC | Selected anonymous browsing responses tested. Private resources assessed separately |
| Authentication entry and recovery | PUBLIC entry | Sign-in entry points are accessible anonymously. Token handling requires separate tests |
| User profile and private content | RESTRICTED | Anonymous requests rejected (401). Authenticated profile request succeeded (200) |
| Administrative operations | RESTRICTED, privileged | Anonymous access denied (401). Non-admin access denied (403) |
| Internal metrics, cluster and database surfaces | INTERNAL | Not present in the six recorded public Routes. This is not a complete reachability scan |
| Public IIIF and discovery services | PUBLIC-facing | Per-object publication/access policy may still restrict individual content |

**Working result:** classification prepared in the reviewed scope (SEC-03). The provider retains the full route list and reviewed matcher configuration for authorised assessment. This summary does not confirm enforcement of every resource-level policy (SEC-09) or assign a formal interoperability level. Approval of anonymous public content and outputs remains a matter of provider policy.
