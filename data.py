"""Get data."""
from pprint import pprint
from slackclient import SlackClient

import json
import langid
import time
import os
import numpy as np

sc = SlackClient(os.environ['SLACK_TOKEN'])


has_more = True
i = 0
samples = []
labels = []   

while (has_more):
    data = sc.api_call(
    "channels.history",
    channel="C025W938C",
    count=100)

    messages = data["messages"]

    for message in messages: 
        if "client_msg_id" in message:
            message_text = message["text"]
            user = message["user"]

            lang = langid.classify(message_text)[0]
            if (lang is not "en"):
                samples.append(message_text)
                labels.append(user)

    has_more = data["has_more"]
    time.sleep(2)
    i += 1
    print(i)

pprint(samples)
np.save('samples.npy', np.array(samples))
np.save('labels.npy', np.array(labels))
