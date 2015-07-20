# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 14:00:59 2015

@author: Pierre Jacquot
"""
#This code give five different orders to five NAOs located at five different ports.
from naoqi import ALProxy
from threading import Thread

def StiffnessOn(proxy):
  pNames = "Body"
  pStiffnessLists = 1.0
  pTimeLists = 1.0
  proxy.stiffnessInterpolation(pNames, pStiffnessLists, pTimeLists)


def main(robotIP,port,postureName,speed=1.0):
    ''' Example showing a path of two positions
    Warning: Needs a PoseInit before executing
    '''
    # Init proxies.
    try:
        motionProxy = ALProxy("ALMotion", robotIP, port)
    except Exception, e:
        print "Could not create proxy to ALMotion"
        print "Error was: ", e

    try:
        postureProxy = ALProxy("ALRobotPosture", robotIP, port)
	print robotIP
	print port

	# Set NAO in Stiffness On
	StiffnessOn(motionProxy)

	# Send NAO to postureName
	postureProxy.goToPosture(postureName,speed)

    except Exception, e:
        print "Could not create proxy to ALRobotPosture"
        print "Error was: ", e

if __name__== "__main__":
    Thread(target = main, args= ('127.0.0.1',9559,'Crouch',0.5)).start()
    Thread(target = main, args= ('127.0.0.1',9558,'Sit',0.5)).start()
    Thread(target = main, args= ('127.0.0.1',9557,'SitRelax',0.5)).start()
    Thread(target = main, args= ('127.0.0.1',9556,'LyingBelly',0.5)).start()
    Thread(target = main, args= ('127.0.0.1',9555,'LyingBack',0.5)).start()
