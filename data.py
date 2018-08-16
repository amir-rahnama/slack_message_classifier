"""Get data."""
from pprint import pprint
from slackclient import SlackClient

import json
import langid
import time
import os
import sys
import numpy as np
from pymongo import MongoClient
client = MongoClient()

db = client.sc
messages_collection = db.messages

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
                messages_collection.insert_one(message)

    has_more = data["has_more"]
    time.sleep(5)
    i += 1
    print(i)