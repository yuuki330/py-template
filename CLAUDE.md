# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

@AGENTS.md

## Claude Code notes

- ruff format and ruff check --fix run automatically on every .py file edit via PostToolUse hooks.
- DDD layer import rules are in `.claude/rules/` and load automatically per file path.
- Use `arch-validator` subagent to check DDD compliance across the codebase.
- Use `test-writer` subagent for generating pytest tests.
- For non-trivial changes, use plan mode to align on approach before implementation.

## Observability

Log these events via `.claude/scripts/emit_event.py` for harness improvement:
- When invoking a subagent: `echo '{"event":"agent.call","detail":"<agent-name>"}' | python3 .claude/scripts/emit_event.py`
- When re-reading a file already read in this session: `echo '{"event":"context.reread","detail":"<file-path>"}' | python3 .claude/scripts/emit_event.py`
- When the user corrects your approach: `echo '{"event":"user.correction","detail":"<brief-description>"}' | python3 .claude/scripts/emit_event.py`
- Use `harness-reviewer` subagent to analyze logs and get improvement recommendations.
