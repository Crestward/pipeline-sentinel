# pipeline-sentinel

An event-triggered incident agent for data pipelines. It compresses logs, triages most failures with a cheap deterministic tier (System 1) and escalates only hard ones to an LLM agent (System 2) that uses lineage and blast-radius tools, then proposes gated, audited remediation.

Part of a pair of linked portfolio projects that share [`warehouse-graph`](https://github.com/Crestward/warehouse-graph), a lineage/metadata graph served over MCP. The sibling project is [`warehouse-qa`](https://github.com/Crestward/warehouse-qa).

> **Status: Phase 0 (setup).** Repo tooling and CI only; the system arrives in later phases.

## Quick start
```bash
uv sync
make check
```

## Licence
MIT. See [LICENSE](LICENSE).
