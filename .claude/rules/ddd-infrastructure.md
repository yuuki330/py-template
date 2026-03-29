---
paths:
  - "src/**/infrastructure/**"
---

# Infrastructure Layer Rules

This is the infrastructure layer. It implements domain interfaces (repository ABCs, etc.), database access, and external API clients.

Import restrictions:
- May import from the domain layer to implement its interfaces.
- Do not import from application or presentation layers.
- Domain never imports from infrastructure; the dependency is one-way.
