import json
import slack_sdk
import random
from datetime import date, datetime, timezone, timedelta

token_path = './token.json'
with open(token_path, 'r') as token_json:
    secret_token = json.load(token_json)

image_path = './image.json'
with open(image_path, 'r') as image_json:
    image_array = json.load(image_json)
    image_array = list(image_array)
num = random.randint(0, len(image_array)-1)
image = image_array[num]

SLACK_TOKEN = secret_token["token"]
SLACK_CHANNEL = "#ch-slackbot-test"

json_path = './birthlist.json'
with open(json_path, 'r') as birth_json:
    b_dict = json.load(birth_json)

def chuucar_send_msg(slack_msg):
    client = slack_sdk.WebClient(token=SLACK_TOKEN)
    data = {
        "attachments":[{
            "image_url": image
        }]
    }
    client.chat_postMessage(channel=SLACK_CHANNEL,text=slack_msg, data=json.dumps(data))

KST = timezone(timedelta(hours=9))
today=datetime.now(KST)

for key,val in b_dict.items():   
    date_of_birth = date(int(val[0:4]), int(val[4:6]), int(val[6:8]))

    if today.month==date_of_birth.month and today.day == date_of_birth.day:
        chat = "오늘은 바로바로 귀여운 클둥이, "+ key + "의 생일입니다!"+" 다들 소리질러~!!"
        chuucar_send_msg(chat)
