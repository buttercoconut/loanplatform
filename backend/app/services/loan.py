import asyncio

def calculate_credit_score(income: float, debt: float) -> int:
    # Simple heuristic: higher income and lower debt -> higher score
    ratio = debt / income if income else 1
    if ratio < 0.2:
        return 750
    elif ratio < 0.4:
        return 650
    else:
        return 550

async def process_application(app):
    # Simulate async call to credit agency
    await asyncio.sleep(0.1)
    score = calculate_credit_score(app.income, app.debt)
    app.credit_score = score
    # Simple approval logic
    if score >= 650 and app.amount <= app.income * 0.5:
        app.status = "approved"
    else:
        app.status = "rejected"
    return app
