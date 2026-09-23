"""
Business logic for loan approval.
"""
from typing import Dict
from . import orm

# Simple scoring thresholds
BASE_INTEREST = 5.0
MAX_INTEREST = 15.0


def calculate_approval(application: orm.LoanApplication) -> Dict:
    # Basic risk score
    debt_ratio = application.debt / application.income if application.income else 1.0
    score = application.credit_score - debt_ratio * 100

    approved = score >= 600
    interest = BASE_INTEREST
    if approved:
        if score > 750:
            interest = BASE_INTEREST
        elif score > 700:
            interest = BASE_INTEREST + 1
        else:
            interest = BASE_INTEREST + 3
    else:
        interest = MAX_INTEREST

    return {
        "approved": approved,
        "interest_rate": interest,
        "approved_amount": application.amount if approved else 0.0,
    }
