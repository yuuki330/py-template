---
paths:
  - "src/**/domain/**"
---

# Domain Layer Rules

This is the domain layer. It contains entities, value objects, domain services, and repository interfaces (ABCs).

Import restrictions:
- Use only Python standard library. No external packages.
- Do not import from application, infrastructure, or presentation layers.
- Nothing outside domain depends inward from here; domain depends on nothing.

Keep domain logic pure and framework-free.
