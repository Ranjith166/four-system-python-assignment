def process_claim(claim):
    required = ("claim_id", "customer", "description")
    missing = [key for key in required if not claim.get(key)]
    if missing:
        return {"status": "escalated", "reason": "missing_fields", "missing": missing}
    if any(word in claim["description"].lower() for word in ("fraud", "injury", "lawsuit")):
        return {"status": "escalated", "reason": "high_risk"}
    return {"status": "routed", "queue": "standard_claims"}
