import time
from SlackClient import SlackClient
import json

token = "xoxb-17086236055-nu0QI6f0AmsB2DNEBU1Ynxh5"  # found at https://api.slack.com/web#authentication
sc = SlackClient(token)
channelDetails = json.loads(sc.api_call("im.open", user="U0H2DPVHB"))

channelId = ""
if channelDetails['ok']:
    channelId = str(channelDetails['channel']['id'])

print type(channelId)

if channelId:
    gretting = "Hey"
    print sc.api_call("chat.postMessage", as_user="true:", channel=channelId, text=gretting)

print sc.api_call("im.history", channel=channelId)
