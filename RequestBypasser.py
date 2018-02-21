#!!!By Ankush

import os
from os import path
from burp import IBurpExtender
from burp import IInterceptedProxyMessage
from burp import IProxyListener
rootp = os.getcwd()
fileplace = path.abspath(path.join(rootp, "list.txt"))
listfile = open(fileplace, "r+")
list = listfile.read().splitlines()
class BurpExtender(IBurpExtender, IProxyListener):
    def registerExtenderCallbacks(self, callbacks):
        self._callbacks = callbacks
        self._helpers = callbacks.getHelpers()
        callbacks.setExtensionName("Request Bypasser")
        callbacks.registerProxyListener(self)
        self.hostsToForward = list
		print "EveryThing Seems Perfect"
    def processProxyMessage(self, messageIsRequest, message):
        if messageIsRequest:
            messageInfo = message.getMessageInfo()
            for hostToDrop in self.hostsToForward:
                currentHost = messageInfo.getHttpService().getHost()
                if hostToDrop in currentHost:
                    print "Request bypassed from proxy for: " + str(self._helpers.analyzeRequest(messageInfo).getUrl())
                    message.setInterceptAction(IInterceptedProxyMessage.ACTION_DONT_INTERCEPT)
                    break
        return