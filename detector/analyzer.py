import re

# Simple keyword-based risk detection
HIGH_RISK_KEYWORDS = [
    "password", "credit card", "cvv", "otp", "ssn",
    "bank account", "ifsc", "pin", "aadhaar"
]

MEDIUM_RISK_KEYWORDS = [
    "email", "phone", "address", "dob"
]


def analyze_data(text):
    text_lower = text.lower()

    findings = []

    # Check high risk
    for word in HIGH_RISK_KEYWORDS:
        if re.search(rf"\b{word}\b", text_lower):
            findings.append(f"High risk keyword detected: {word}")

    # Check medium risk
    for word in MEDIUM_RISK_KEYWORDS:
        if re.search(rf"\b{word}\b", text_lower):
            findings.append(f"Medium risk keyword detected: {word}")

    # Decide risk level
    if any("High" in f for f in findings):
        risk = "High"
    elif any("Medium" in f for f in findings):
        risk = "Medium"
    else:
        risk = "Low"

    return risk, findings