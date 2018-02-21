#!!!By Ankush

import os
from os import path
from burp import IBurpExtender
from burp import IProxyListener
from burp import IInterceptedProxyMessage
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
            messageInform = message.getMessageInfo()
            for hostToDrop in self.hostsToForward:
                currentHost = messageInform.getHttpService().getHost()
                if hostToDrop in currentHost:
                    print "Request bypassed from proxy for: " + str(self._helpers.analyzeRequest(messageInform).getUrl())
                    message.setInterceptAction(IInterceptedProxyMessage.ACTION_DONT_INTERCEPT)
                    break
        return
