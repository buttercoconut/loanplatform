# Dummy credit service
from typing import Dict

# In real scenario, call external API
CREDIT_DB: Dict[int, int] = {1: 720, 2: 650, 3: 580}

def check_credit(customer_id: int, credit_score: int) -> bool:
    # Simple rule: score must be >= 600
    return credit_score >= 600
