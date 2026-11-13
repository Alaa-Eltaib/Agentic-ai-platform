from collections.abc import Sequence
from .models import EvaluationResult


def validity_rate(results: Sequence[EvaluationResult]) -> float:
    return sum(r.success for r in results) / len(results) if results else 0.0


def category_accuracy(results: Sequence[EvaluationResult]) -> float:
    successful = [r for r in results if r.success]
    return sum(r.category_correct for r in successful) / len(successful) if successful else 0.0


def department_accuracy(results: Sequence[EvaluationResult]) -> float:
    successful = [r for r in results if r.success]
    return sum(r.department_correct for r in successful) / len(successful) if successful else 0.0


def priority_accuracy(results: Sequence[EvaluationResult]) -> float:
    successful = [r for r in results if r.success]
    return sum(r.priority_correct for r in successful) / len(successful) if successful else 0.0


def overall_success_rate(results: Sequence[EvaluationResult]) -> float:
    if not results:
        return 0.0
    success_count = sum(
        r.success and r.category_correct and r.department_correct and r.priority_correct
        for r in results
    )
    return success_count / len(results)