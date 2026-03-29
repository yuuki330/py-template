---
paths:
  - "src/**/presentation/**"
---

# Presentation Layer Rules

This is the presentation layer. It contains CLI commands, API endpoints, and request/response handling.

Import restrictions:
- May import from the application layer only.
- Do not import directly from infrastructure or domain layers.
- Dependency direction: Presentation -> Application -> Domain <- Infrastructure.
