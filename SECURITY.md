# Security Policy

This is a personal learning grimoire of notebooks, mini-projects, and experiments. The pinned dependency set in `Project_02/requirements.txt` is large; every security-relevant pin is set to a version at or above the one that closes the matching Dependabot advisory, so a clean install gets a patched set.

## Reporting a Vulnerability

**Do not open a public GitHub issue for security vulnerabilities.**

Email: shauryapunj404@gmail.com
Subject: `[GRIMOIRE SECURITY] <brief description>`

Provide repro + impact + suggested fix. Acknowledgement within 48 hours. GitHub's "Security › Report a vulnerability" tab is also accepted.

## Security Controls

- Dependabot weekly security + version updates on three pip directories + GitHub Actions; semver-major version-updates are ignored to stop the PR-list churn while still letting security PRs through automatically.
- CodeQL `security-extended` on push, PR, and weekly schedule (Python).
- Branch protection on `main`: required CodeQL status check, linear history, no force-push, no deletion, conversation resolution required.
