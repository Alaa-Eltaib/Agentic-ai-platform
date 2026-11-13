# PulseFlow AI — Triage & Priority Agent Module

This module implements the **Triage & Priority Agent** for the **PulseFlow AI** multi-agent hospital intake and clinical triage system[cite: 2, 3]. It parses incoming hospital support tickets, enforces structured JSON outputs using Pydantic schemas, classifies urgency levels, routes requests to the appropriate hospital departments, and benchmarks prediction accuracy.

## Project Structure

```text
├── structured/
│   ├── schemas.py        # Pydantic models enforcing structured JSON output (TicketOutput)
│   └── parser.py         # Output sanitizer and JSON schema validator
├── prompts/
│   └── classifier.py     # Triage & priority classification prompt template
└── evaluation/
    ├── models.py         # Evaluation result tracking schema (EvaluationResult)
    ├── evaluator.py      # End-to-end dataset evaluation pipeline
    └── metrics.py        # Validity rate and field-level accuracy metrics
