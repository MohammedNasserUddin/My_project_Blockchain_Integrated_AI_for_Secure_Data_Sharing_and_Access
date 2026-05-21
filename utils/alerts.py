import os
from datetime import datetime

ALERT_FILE = "alerts.log"


def trigger_alert(message):
    """
    Trigger alert when high-risk data is detected
    """

    timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")

    alert_message = f"[{timestamp}] ALERT: {message}"

    # Print in terminal
    print(alert_message)

    # Save to file
    with open(ALERT_FILE, "a") as f:
        f.write(alert_message + "\n")