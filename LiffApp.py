import requests
import json


def template_Test():
    'Authorization: Bearer {channel access token}'
    channel_access_token = "3NqAthvdJGNPUROa/OumvcEIS/xZgjhlfEJfOq5iVIVRqGQ49d26nfN2t/KogkPzBdNolK8sDhEF5xbxK9ygvU0h8TiC1tgKHlGHGMSNoNC2OP8dcXHDDRB/VI+wVP7NwDyPDqtNq1mNzJSfW0L/IgdB04t89/1O/w1cDnyilFU="
    Line_tokens = f"Bearer {channel_access_token}"
    header = {
        "Authorization": Line_tokens,
        "Content-Type": "application/json"
    }
    datas = {
        "to": "U92af9821502fd20d89ea33eb22c1ac44",
        "messages": [
            {
                "type": "text",
                "text": "ข้อมูลการสั่งซื้อ",
            }
        ]
    }
    url = f"https://api.line.me/v2/bot/message/push"
    response = requests.post(url, headers=header, data=json.dumps(datas))
    Get_json = response.json()
    return Get_json


if __name__ == "__main__":
    print(template_Test())
