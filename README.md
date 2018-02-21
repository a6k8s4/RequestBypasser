RequesteBypasser
================================================================================================

A python extension script for Burp Suite to bypass unnecessary request from being intercepted

# PreRequisite

* Burp Suite(any)
* Jython 2.7 Standalone [Download](http://search.maven.org/remotecontent?filepath=org/python/jython-standalone/2.7.0/jython-standalone-2.7.0.jar)

# Why it is needed?

* Sometime after even exclude the url it is being intercepted by Burp Suite proxy and it is very irritating while analysis.

# Solution

RequestBypasser

# How to use 

* Go to Burp Extender tab then Option > Python Environment > there add Jython Standalone jar file
* Then Return to Extender > Extension tab > Burp Extensions > there slect Add > choose Python > then add path to RequestBypasser > Slect Next, if everything will perfect you will get one message " Everything seems Perfect"
* Now you can add site which you do not want to intercept in the list.txt file.
* Keep  both RequestBypasser.py and list.txt in one folder/directory



Thank you


