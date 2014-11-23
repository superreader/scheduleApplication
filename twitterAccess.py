#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import twitter
import json


class TwitterApiAccesser:
    def consumerSetter(self):
        f = open("config.ini","r")
        consumerData = {}
        for line in f:
            line = line.replace("\n","")
            consumerData[(line.split("="))[0]] = (line.split("="))[1]
        self.api = twitter.Api(consumerData["consumer_key"],consumerData["consumer_secret"],consumerData["access_token_key"],consumerData["access_token_secret"])

    def getText(self):
        statuses = self.api.GetUserTimeline("super_tester_tw")
        for s in statuses:
	        print(s.text)

    def postMessage(self,postmsg):
        status = self.api.PostUpdate(postmsg.decode('utf-8'))
        
    def postDirectMessage(self,user,postDM):
        print(user)
        print(postDM)
        status = self.api.PostDirectMessage(postDM,user)


if __name__ == '__main__':
    twaa = TwitterApiAccesser()
    twaa.consumerSetter()
    text = "テストですよ"
    user = "22922327"
    twaa.postMessage("てすと")
    #twaa.postDirectMessage(user, text)
    twaa.getText()
