# Reflection Brief

Replace each prompt with observations from your actual runs and cite the corresponding artifacts.

## 1. Agentic loop
Describe routing/escalation and what the trace's per-turn `stop_reason` shows. Cite `summary.md` and a trace.

## 2. Context strategy
Report token reduction, evaluation results, and the control regression. Cite `budget.json`, `eval.jsonl`, and `eval_control.jsonl`.

## 3. Claude Code configuration
Describe the `.claude/` rules, review command, and forked deploy-check skill. Explain `context: fork` and `allowed-tools`. Cite validator output and configuration structure.

## 4. Shift monitor
Report defects returned versus warm-tier total, `hot_state.json` size, and scratchpad append evidence. Explain atomic replacement and SQL timestamp filtering.

## 5. Synthesis across systems
Compare deterministic enforcement with prompt guidance, and context within one conversation with durable state across sessions. Cite at least two of your run artifacts.

## Limitations
This ZIP is a starter reconstructed from screenshots, not the original course source. Be transparent about any differences.
