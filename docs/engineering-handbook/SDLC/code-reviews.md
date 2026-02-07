# Code Reviews

Code reviews improve quality, reduce regressions, and build shared ownership across partners. In the CH Cloud context, reviews also help prevent interoperability drift by enforcing consistent API and security practices.


## Baseline expectations

- all changes to shared branches go through PR/MR review
- at least one peer reviewer approves before merge
- CI checks run automatically (tests, linting, security scans where applicable)


## Review workflow (recommended)

1. create a branch (`feature/...` or `fix/...`)
2. commit small, focused changes with meaningful messages
3. open PR/MR linked to an issue/work item
4. CI runs (tests, lint, security gates)
5. review discussion and revisions
6. approval
7. merge according to branching strategy


## Review checklist (practical)

| Area | What to check |
|---|---|
| Correctness | behaviour matches intent; edge cases handled |
| Clarity | readable structure; meaningful names; minimal complexity |
| Security | no secrets; inputs validated; authz preserved |
| Testing | appropriate tests added/updated; no flakes introduced |
| Docs | interface docs and changelog updated where relevant |
| Interoperability | API contracts stable; error model consistent; version bump if breaking |


## “Small PR” guidance

Aim for PRs that are easy to review:
- keep scope focused (avoid mixing refactors + features + formatting)
- keep change size manageable
- include screenshots/videos for UI changes
- include migration notes for breaking changes


## Review etiquette (keeps collaboration healthy)

- be specific and constructive (“what/why/how”)
- focus on code, not the person
- ask questions when intent is unclear
- resolve long threads via quick call if needed


## Related pages
- [Testing](testing.md)
- [CI/CD](CICD.md)
- [Code versioning and open-source practice](code-versioning-and-open-source.md)
