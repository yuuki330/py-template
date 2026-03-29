---
paths:
  - "src/**/application/**"
---

# Application Layer Rules

This is the application layer. It contains use cases and application services.

Import restrictions:
- May import from the domain layer only.
- Do not import from infrastructure or presentation layers.
- Orchestrate domain objects to fulfill use cases.
