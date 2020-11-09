import requests
def send_message_to_slack(text):
    url = "https://hooks.slack.com/services/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"
    payload = {"text": text}
    requests.post(url, json=payload)
    return "send message!"
    
def send_to_kyoung(text):
    url = "https://hooks.slack.com/services/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"
    payload = {"text": text}
    requests.post(url, json=payload)
    return "send message!"
