import json
import slack_sdk
from datetime import date, datetime, timezone, timedelta

#깃허브 슬랙봇 test
with open('../GitOps-SlackBot/token.json', 'r') as token_json:
    secret_token = json.load(token_json)

SLACK_TOKEN = secret_token["token"]
SLACK_CHANNEL = "#ch-slackbot-test"

b_day='{"ch": "20000817","yg": "20000207","jw": "19990311","test": "20001110","test2":"119911111"}'
b_dict = json.loads(b_day)

def chuucar_send_msg(slack_msg):
    client = slack_sdk.WebClient(token=SLACK_TOKEN)
    client.chat_postMessage(channel=SLACK_CHANNEL,text=slack_msg)

#datetime 한국시간 변경
KST = timezone(timedelta(hours=9))
today=datetime.now(KST)

for key,val in b_dict.items():   
    date_of_birth = date(int(val[0:4]), int(val[4:6]), int(val[6:8]))

    if today.month==date_of_birth.month and today.day == date_of_birth.day:
        chat = "Today is "+ key + "'s Birthday."+" Let's Celebrate Together!!"
        chuucar_send_msg(chat)


