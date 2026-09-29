"""TRG (Timing-Recovery-Grounded) evaluation pipeline.

A minimum reporting standard for real-time voice agents, plus the tooling
to check compliance and compare systems that already report against it.

Companion package to *Evaluating Real-Time Voice Agents: From Component
Quality to Grounded Outcomes* (arXiv:2609.30798).
"""

from trg_eval.validator import Report, validate_data, validate_file

__all__ = ["Report", "validate_data", "validate_file"]
__version__ = "1.1.0"
