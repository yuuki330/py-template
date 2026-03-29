---
paths:
  - "tests/**"
---

# Testing Rules

- Use pytest. Tests live in `tests/` mirroring the `src/` structure.
- pytest adds `src/` to sys.path, so import directly (e.g., `from app import greet`).
- Prefer small, focused test functions with descriptive names.
- Test naming: `test_<behavior_description>`
- Run a single test: `uv run pytest tests/path/to/test_file.py::test_function_name`
- Run all tests: `make test`
