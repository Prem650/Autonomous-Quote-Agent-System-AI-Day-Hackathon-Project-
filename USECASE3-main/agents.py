def risk_profiler(accidents):

    if accidents > 2:
        return "High Risk"

    elif accidents > 0:
        return "Medium Risk"

    else:
        return "Low Risk"



def conversion_predictor():

    import random

    return random.randint(10,95)



def premium_advisor(premium):

    if premium > 1200:
        return "Premium too high — recommend discount"

    else:
        return "Premium acceptable"



def decision_router(risk,conversion):

    if risk == "High Risk":
        return "Escalate to Underwriter"

    elif conversion < 40:
        return "Agent Follow Up"

    else:
        return "Auto Approve"
