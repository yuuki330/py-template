# AGENTS.md

This file provides guidance to AI coding agents when working with code in this repository.

# Project rules

## Stack
- This repository uses Python only.
- Use uv for Python, dependency, and environment management.
- Do not introduce TypeScript, JavaScript tooling, or Rust components.
- Adding new dependencies requires explicit approval.

## Commands

| Task | Command |
|------|---------|
| Show available commands | `make help` |
| Install dependencies | `make sync` |
| Format code | `make format` |
| Lint | `make lint` |
| Run all tests | `make test` |
| Lint + test | `make check` |
| Remove cache files | `make clean` |
| Run a single test | `uv run pytest tests/path/to/test_file.py::test_function_name` |

Always validate with `make format && make check` before finishing.

## Architecture

- `src/` — application source code. All modules live here.
- `tests/` — pytest test suite. pytest adds `src/` to `sys.path`, so tests import directly (e.g. `from app import greet`).
- Python 3.12 required (see `.python-version`).
- ruff is configured with `line-length = 100`.

## Working style
- Prefer small, local changes over broad refactors.
- Prefer editing existing files over adding abstractions.
- For non-trivial changes, propose a short plan first.

## CI/CD policy
- Do not modify CI files unless explicitly asked.
- Keep CI limited to lint and test at first.
- Do not add deployment steps unless explicitly asked.

## Code style
- Prefer readable Python over clever Python.
- Avoid over-abstraction.

## DDD Architecture

This project follows Domain-Driven Design.

Directory names are flexible — adapt per project (e.g. `core/` instead of `domain/`).
Dependency rules are NOT flexible — ALWAYS enforce these regardless of naming.

### Layers

| Layer | Recommended dir | Responsibility |
|-------|----------------|----------------|
| Domain | `domain/` | Entities, Value Objects, Domain Services, Repository interfaces (ABC). No external dependencies. |
| Application | `application/` | Use cases / application services. Depends only on Domain layer. |
| Infrastructure | `infrastructure/` | Repository implementations, DB, external API clients. Implements Domain interfaces. |
| Presentation | `presentation/` | CLI, API endpoints, request/response handling. Calls Application layer. |

All layers live under `src/`.

### Dependency rules

- **Domain layer has zero dependencies** on other layers and external packages (stdlib only).
- **Application layer depends only on Domain.**
- **Infrastructure implements Domain interfaces** (Repository ABC, etc.) — never import Infrastructure from Domain.
- **Presentation calls Application** — never bypasses to Infrastructure directly.

Direction: Presentation → Application → Domain ← Infrastructure
