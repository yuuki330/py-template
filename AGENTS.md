# Project rules

## Stack
- This repository uses Python only.
- Use uv for Python, dependency, and environment management.
- Do not introduce TypeScript, JavaScript tooling, or Rust components.
- Adding new dependencies requires explicit approval.

## Working style
- Prefer small, local changes over broad refactors.
- Prefer editing existing files over adding many abstractions.
- For non-trivial changes, propose a short plan first.

## Validation
Always validate changes with:
1. make format
2. make lint
3. make test
4. make check

## CI/CD policy
- Do not modify CI files unless explicitly asked.
- Keep CI limited to lint and test at first.
- Do not add deployment steps unless explicitly asked.

## Code style
- Prefer readable Python over clever Python.
- Avoid over-abstraction.
