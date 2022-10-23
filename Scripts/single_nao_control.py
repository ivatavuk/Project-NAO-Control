# -*- coding: utf-8 -*-
"""
@author: Pierre Jacquot
"""
#For more informations please check : http://www.coppeliarobotics.com/helpFiles/en/apiFunctions.htm
import vrep,sys
from naoqi import ALProxy
from manage_joints import get_first_handles,CustomJointControl

print '================ Program Sarted ================'

vrep.simxFinish(-1)
clientID=vrep.simxStart('127.0.0.2',19999,True,True,5000,5)
if clientID!=-1:
	print 'Connected to remote API server'

else:
	print 'Connection non successful'
	sys.exit('Could not connect')


print "================ Choregraphe's Initialization ================"
#print 'Enter your NAO IP'
#naoIP = raw_input()
naoIP = "127.0.0.1"
#naoIP = map(str,naoIP.split())
#print 'Enter your NAO port'
#naoPort = raw_input()
naoPort = 9559
#naoPort=int(naoPort)
#naoPort = map(int,naoPort.split())

motionProxy = ALProxy("ALMotion",naoIP, naoPort)
postureProxy = ALProxy("ALRobotPosture", naoIP, naoPort)
memoryProxy = ALProxy("ALMemory", naoIP, naoPort)

#Go to the posture StandInitZero
posture = 'StandZero'
print 'Posture Initialization : ' + posture
motionProxy.stiffnessInterpolation('Body', 1.0, 1.0)
postureProxy.goToPosture(posture,1.0)

Head_Yaw=[];Head_Pitch=[];
L_Hip_Yaw_Pitch=[];L_Hip_Roll=[];L_Hip_Pitch=[];L_Knee_Pitch=[];L_Ankle_Pitch=[];L_Ankle_Roll=[];
R_Hip_Yaw_Pitch=[];R_Hip_Roll=[];R_Hip_Pitch=[];R_Knee_Pitch=[];R_Ankle_Pitch=[];R_Ankle_Roll=[];
L_Shoulder_Pitch=[];L_Shoulder_Roll=[];L_Elbow_Yaw=[];L_Elbow_Roll=[];L_Wrist_Yaw=[]
R_Shoulder_Pitch=[];R_Shoulder_Roll=[];R_Elbow_Yaw=[];R_Elbow_Roll=[];R_Wrist_Yaw=[]
R_H=[];L_H=[];R_Hand=[];L_Hand=[];
Body = [Head_Yaw,Head_Pitch,L_Hip_Yaw_Pitch,L_Hip_Roll,L_Hip_Pitch,L_Knee_Pitch,L_Ankle_Pitch,L_Ankle_Roll,R_Hip_Yaw_Pitch,R_Hip_Roll,R_Hip_Pitch,R_Knee_Pitch,R_Ankle_Pitch,R_Ankle_Roll,L_Shoulder_Pitch,L_Shoulder_Roll,L_Elbow_Yaw,L_Elbow_Roll,L_Wrist_Yaw,R_Shoulder_Pitch,R_Shoulder_Roll,R_Elbow_Yaw,R_Elbow_Roll,R_Wrist_Yaw,L_H,L_Hand,R_H,R_Hand]

get_first_handles(clientID,Body)
print "================ Handles Initialization ================"
commandAngles = motionProxy.getAngles('Body', False)
print '========== NAO is listening =========='

err,data_gyro = vrep.simxGetObjectHandle(clientID,'imported_part_20_sub0',vrep.simx_opmode_oneshot_wait)
err,data_LFsrFL = vrep.simxGetObjectHandle(clientID,'NAO_LFsrFL',vrep.simx_opmode_oneshot_wait)
err,data_LFsrFR = vrep.simxGetObjectHandle(clientID,'NAO_LFsrFR',vrep.simx_opmode_oneshot_wait)
err,data_LFsrRL = vrep.simxGetObjectHandle(clientID,'NAO_LFsrRL',vrep.simx_opmode_oneshot_wait)
err,data_LFsrRR = vrep.simxGetObjectHandle(clientID,'NAO_LFsrRR',vrep.simx_opmode_oneshot_wait)
err,data_RFsrFL = vrep.simxGetObjectHandle(clientID,'NAO_RFsrFL',vrep.simx_opmode_oneshot_wait)
err,data_RFsrFR = vrep.simxGetObjectHandle(clientID,'NAO_RFsrFR',vrep.simx_opmode_oneshot_wait)
err,data_RFsrRL = vrep.simxGetObjectHandle(clientID,'NAO_RFsrRL',vrep.simx_opmode_oneshot_wait)
err,data_RFsrRR = vrep.simxGetObjectHandle(clientID,'NAO_RFsrRR',vrep.simx_opmode_oneshot_wait)

memoryProxy.insertData("ankle_pitch_stiff", 1.0)
memoryProxy.insertData("ankle_roll_stiff", 1.0)
memoryProxy.insertData("hip_pitch_stiff", 1.0)
memoryProxy.insertData("hip_roll_stiff", 1.0)
memoryProxy.insertData("LFsrFL", 0.0)
memoryProxy.insertData("LFsrFR", 0.0)
memoryProxy.insertData("LFsrRL", 0.0)
memoryProxy.insertData("LFsrRR", 0.0)
memoryProxy.insertData("RFsrFL", 0.0)
memoryProxy.insertData("RFsrFR", 0.0)
memoryProxy.insertData("RFsrRL", 0.0)
memoryProxy.insertData("RFsrRR", 0.0)
CustomJointControl(clientID,motionProxy,memoryProxy,0,Body,data_gyro,data_LFsrFL,data_LFsrFR,data_LFsrRL,data_LFsrRR,data_RFsrFL,data_RFsrFR,data_RFsrRL,data_RFsrRR)

