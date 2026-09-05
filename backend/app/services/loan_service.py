# Domain service for loan approval logic
from typing import Tuple

class LoanApprovalService:
    def __init__(self, credit_score_threshold: int = 650, max_dti: float = 0.4):
        self.credit_score_threshold = credit_score_threshold
        self.max_dti = max_dti

    def evaluate(self, amount: float, term_months: int, annual_income: float,
                  debt_to_income_ratio: float, credit_score: int) -> Tuple[bool, float, float, str]:
        """Return (approved, approved_amount, interest_rate, message)"""
        # Basic checks
        if credit_score < self.credit_score_threshold:
            return False, 0.0, 0.0, "Credit score below threshold"
        if debt_to_income_ratio > self.max_dti:
            return False, 0.0, 0.0, "Debt-to-income ratio too high"
        # Simple interest calculation
        base_rate = 5.0  # base annual rate
        # Adjust rate based on credit score
        if credit_score >= 750:
            base_rate -= 1.0
        elif credit_score <= 650:
            base_rate += 1.5
        # Adjust rate based on term
        if term_months > 60:
            base_rate += 0.5
        # Approved amount capped at 80% of income per month
        max_approved = (annual_income / 12) * 0.8 * term_months
        approved_amount = min(amount, max_approved)
        if approved_amount <= 0:
            return False, 0.0, 0.0, "Approved amount too low"
        return True, approved_amount, base_rate, "Approved"
