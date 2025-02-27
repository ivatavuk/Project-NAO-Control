# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 14:09:03 2015

@author: Pierre Jacquot
"""

import vrep

#Get the handles of all NAO in the scene
def get_all_handles(nbrOfNao,clientID,Body):
    print '-> Head for NAO : '+ str(1)
    Body[0].append(vrep.simxGetObjectHandle(clientID,'HeadYaw#',vrep.simx_opmode_oneshot_wait)[1])
    Body[1].append(vrep.simxGetObjectHandle(clientID,'HeadPitch#',vrep.simx_opmode_oneshot_wait)[1])
    #Left Leg
    print '-> Left Leg for NAO : ' + str(1)
    Body[2].append(vrep.simxGetObjectHandle(clientID,'LHipYawPitch3#',vrep.simx_opmode_oneshot_wait)[1])
    Body[3].append(vrep.simxGetObjectHandle(clientID,'LHipRoll3#',vrep.simx_opmode_oneshot_wait)[1])
    Body[4].append(vrep.simxGetObjectHandle(clientID,'LHipPitch3#',vrep.simx_opmode_oneshot_wait)[1])
    Body[5].append(vrep.simxGetObjectHandle(clientID,'LKneePitch3#',vrep.simx_opmode_oneshot_wait)[1])
    Body[6].append(vrep.simxGetObjectHandle(clientID,'LAnklePitch3#',vrep.simx_opmode_oneshot_wait)[1])
    Body[7].append(vrep.simxGetObjectHandle(clientID,'LAnkleRoll3#',vrep.simx_opmode_oneshot_wait)[1])
    #Right Leg
    print '-> Right Leg for NAO : ' + str(1)
    Body[8].append(vrep.simxGetObjectHandle(clientID,'RHipYawPitch3#',vrep.simx_opmode_oneshot_wait)[1])
    Body[9].append(vrep.simxGetObjectHandle(clientID,'RHipRoll3#',vrep.simx_opmode_oneshot_wait)[1])
    Body[10].append(vrep.simxGetObjectHandle(clientID,'RHipPitch3#',vrep.simx_opmode_oneshot_wait)[1])
    Body[11].append(vrep.simxGetObjectHandle(clientID,'RKneePitch3#',vrep.simx_opmode_oneshot_wait)[1])
    Body[12].append(vrep.simxGetObjectHandle(clientID,'RAnklePitch3#',vrep.simx_opmode_oneshot_wait)[1])
    Body[13].append(vrep.simxGetObjectHandle(clientID,'RAnkleRoll3#',vrep.simx_opmode_oneshot_wait)[1])
    #Left Arm
    print '-> Left Arm for NAO : ' + str(1)
    Body[14].append(vrep.simxGetObjectHandle(clientID,'LShoulderPitch3#',vrep.simx_opmode_oneshot_wait)[1])
    Body[15].append(vrep.simxGetObjectHandle(clientID,'LShoulderRoll3#',vrep.simx_opmode_oneshot_wait)[1])
    Body[16].append(vrep.simxGetObjectHandle(clientID,'LElbowYaw3#',vrep.simx_opmode_oneshot_wait)[1])
    Body[17].append(vrep.simxGetObjectHandle(clientID,'LElbowRoll3#',vrep.simx_opmode_oneshot_wait)[1])
    Body[18].append(vrep.simxGetObjectHandle(clientID,'LWristYaw3#',vrep.simx_opmode_oneshot_wait)[1])
    #Right Arm
    print '-> Right Arm for NAO : ' + str(1)
    Body[19].append(vrep.simxGetObjectHandle(clientID,'RShoulderPitch3#',vrep.simx_opmode_oneshot_wait)[1])
    Body[20].append(vrep.simxGetObjectHandle(clientID,'RShoulderRoll3#',vrep.simx_opmode_oneshot_wait)[1])
    Body[21].append(vrep.simxGetObjectHandle(clientID,'RElbowYaw3#',vrep.simx_opmode_oneshot_wait)[1])
    Body[22].append(vrep.simxGetObjectHandle(clientID,'RElbowRoll3#',vrep.simx_opmode_oneshot_wait)[1])
    Body[23].append(vrep.simxGetObjectHandle(clientID,'RWristYaw3#',vrep.simx_opmode_oneshot_wait)[1])
    #Left fingers
    print '-> Left Fingers for NAO : ' + str(1)
    Body[24].append(vrep.simxGetObjectHandle(clientID,'NAO_LThumbBase#',vrep.simx_opmode_oneshot_wait)[1])
    Body[24].append(vrep.simxGetObjectHandle(clientID,'Revolute_joint8#',vrep.simx_opmode_oneshot_wait)[1])
    Body[24].append(vrep.simxGetObjectHandle(clientID,'NAO_LLFingerBase#',vrep.simx_opmode_oneshot_wait)[1])
    Body[24].append(vrep.simxGetObjectHandle(clientID,'Revolute_joint12#',vrep.simx_opmode_oneshot_wait)[1])
    Body[24].append(vrep.simxGetObjectHandle(clientID,'Revolute_joint14#',vrep.simx_opmode_oneshot_wait)[1])
    Body[24].append(vrep.simxGetObjectHandle(clientID,'NAO_LRFinger_Base#',vrep.simx_opmode_oneshot_wait)[1])
    Body[24].append(vrep.simxGetObjectHandle(clientID,'Revolute_joint11#',vrep.simx_opmode_oneshot_wait)[1])
    Body[24].append(vrep.simxGetObjectHandle(clientID,'Revolute_joint13#',vrep.simx_opmode_oneshot_wait)[1])
    Body[25].append(Body[24][0:8])
    #Right Fingers
    print '-> Right Fingers for NAO : ' + str(1)
    Body[26].append(vrep.simxGetObjectHandle(clientID,'NAO_RThumbBase#',vrep.simx_opmode_oneshot_wait)[1])
    Body[26].append(vrep.simxGetObjectHandle(clientID,'Revolute_joint0#',vrep.simx_opmode_oneshot_wait)[1])
    Body[26].append(vrep.simxGetObjectHandle(clientID,'NAO_RLFingerBase#',vrep.simx_opmode_oneshot_wait)[1])
    Body[26].append(vrep.simxGetObjectHandle(clientID,'Revolute_joint5#',vrep.simx_opmode_oneshot_wait)[1])
    Body[26].append(vrep.simxGetObjectHandle(clientID,'Revolute_joint6#',vrep.simx_opmode_oneshot_wait)[1])
    Body[26].append(vrep.simxGetObjectHandle(clientID,'NAO_RRFinger_Base#',vrep.simx_opmode_oneshot_wait)[1])
    Body[26].append(vrep.simxGetObjectHandle(clientID,'Revolute_joint2#',vrep.simx_opmode_oneshot_wait)[1])
    Body[26].append(vrep.simxGetObjectHandle(clientID,'Revolute_joint3#',vrep.simx_opmode_oneshot_wait)[1])
    Body[27].append(Body[26][0:8]) 
    for i in range(0, nbrOfNao-1):
        print '-> Head for NAO : '+ str(i+2)
        Body[0].append(vrep.simxGetObjectHandle(clientID,'HeadYaw#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        Body[1].append(vrep.simxGetObjectHandle(clientID,'HeadPitch#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        #Left Leg
        print '-> Left Leg for NAO : ' + str(i+2)
        Body[2].append(vrep.simxGetObjectHandle(clientID,'LHipYawPitch3#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        Body[3].append(vrep.simxGetObjectHandle(clientID,'LHipRoll3#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        Body[4].append(vrep.simxGetObjectHandle(clientID,'LHipPitch3#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        Body[5].append(vrep.simxGetObjectHandle(clientID,'LKneePitch3#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        Body[6].append(vrep.simxGetObjectHandle(clientID,'LAnklePitch3#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        Body[7].append(vrep.simxGetObjectHandle(clientID,'LAnkleRoll3#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        #Right Leg
        print '-> Right Leg for NAO : ' + str(i+2)
        Body[8].append(vrep.simxGetObjectHandle(clientID,'RHipYawPitch3#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        Body[9].append(vrep.simxGetObjectHandle(clientID,'RHipRoll3#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        Body[10].append(vrep.simxGetObjectHandle(clientID,'RHipPitch3#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        Body[11].append(vrep.simxGetObjectHandle(clientID,'RKneePitch3#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        Body[12].append(vrep.simxGetObjectHandle(clientID,'RAnklePitch3#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        Body[13].append(vrep.simxGetObjectHandle(clientID,'RAnkleRoll3#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        #Left Arm
        print '-> Left Arm for NAO : ' + str(i+2)
        Body[14].append(vrep.simxGetObjectHandle(clientID,'LShoulderPitch3#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        Body[15].append(vrep.simxGetObjectHandle(clientID,'LShoulderRoll3#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        Body[16].append(vrep.simxGetObjectHandle(clientID,'LElbowYaw3#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        Body[17].append(vrep.simxGetObjectHandle(clientID,'LElbowRoll3#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        Body[18].append(vrep.simxGetObjectHandle(clientID,'LWristYaw3#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        #Right Arm
        print '-> Right Arm for NAO : ' + str(i+2)
        Body[19].append(vrep.simxGetObjectHandle(clientID,'RShoulderPitch3#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        Body[20].append(vrep.simxGetObjectHandle(clientID,'RShoulderRoll3#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        Body[21].append(vrep.simxGetObjectHandle(clientID,'RElbowYaw3#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        Body[22].append(vrep.simxGetObjectHandle(clientID,'RElbowRoll3#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        Body[23].append(vrep.simxGetObjectHandle(clientID,'RWristYaw3#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        #Left fingers
        print '-> Left Fingers for NAO : ' + str(i+2)
        Body[24].append(vrep.simxGetObjectHandle(clientID,'NAO_LThumbBase#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        Body[24].append(vrep.simxGetObjectHandle(clientID,'Revolute_joint8#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        Body[24].append(vrep.simxGetObjectHandle(clientID,'NAO_LLFingerBase#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        Body[24].append(vrep.simxGetObjectHandle(clientID,'Revolute_joint12#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        Body[24].append(vrep.simxGetObjectHandle(clientID,'Revolute_joint14#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        Body[24].append(vrep.simxGetObjectHandle(clientID,'NAO_LRFinger_Base#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        Body[24].append(vrep.simxGetObjectHandle(clientID,'Revolute_joint11#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        Body[24].append(vrep.simxGetObjectHandle(clientID,'Revolute_joint13#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        Body[25].append(Body[24][i*8:(i+1)*8])
        #Right Fingers
        print '-> Right Fingers for NAO : ' + str(i+2)
        Body[26].append(vrep.simxGetObjectHandle(clientID,'NAO_RThumbBase#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        Body[26].append(vrep.simxGetObjectHandle(clientID,'Revolute_joint0#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        Body[26].append(vrep.simxGetObjectHandle(clientID,'NAO_RLFingerBase#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        Body[26].append(vrep.simxGetObjectHandle(clientID,'Revolute_joint5#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        Body[26].append(vrep.simxGetObjectHandle(clientID,'Revolute_joint6#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        Body[26].append(vrep.simxGetObjectHandle(clientID,'NAO_RRFinger_Base#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        Body[26].append(vrep.simxGetObjectHandle(clientID,'Revolute_joint2#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        Body[26].append(vrep.simxGetObjectHandle(clientID,'Revolute_joint3#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        Body[27].append(Body[26][i*8:(i+1)*8])    

#Get the Handles of all NAOs except the first one
def get_new_nao_handles(nbrOfNao,clientID,Body):
    for i in range(0, nbrOfNao-1):
        print '-> Head for NAO : '+ str(i+2)
        Body[0].append(vrep.simxGetObjectHandle(clientID,'HeadYaw#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        Body[1].append(vrep.simxGetObjectHandle(clientID,'HeadPitch#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        #Left Leg
        print '-> Left Leg for NAO : ' + str(i+2)
        Body[2].append(vrep.simxGetObjectHandle(clientID,'LHipYawPitch3#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        Body[3].append(vrep.simxGetObjectHandle(clientID,'LHipRoll3#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        Body[4].append(vrep.simxGetObjectHandle(clientID,'LHipPitch3#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        Body[5].append(vrep.simxGetObjectHandle(clientID,'LKneePitch3#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        Body[6].append(vrep.simxGetObjectHandle(clientID,'LAnklePitch3#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        Body[7].append(vrep.simxGetObjectHandle(clientID,'LAnkleRoll3#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        #Right Leg
        print '-> Right Leg for NAO : ' + str(i+2)
        Body[8].append(vrep.simxGetObjectHandle(clientID,'RHipYawPitch3#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        Body[9].append(vrep.simxGetObjectHandle(clientID,'RHipRoll3#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        Body[10].append(vrep.simxGetObjectHandle(clientID,'RHipPitch3#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        Body[11].append(vrep.simxGetObjectHandle(clientID,'RKneePitch3#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        Body[12].append(vrep.simxGetObjectHandle(clientID,'RAnklePitch3#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        Body[13].append(vrep.simxGetObjectHandle(clientID,'RAnkleRoll3#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        #Left Arm
        print '-> Left Arm for NAO : ' + str(i+2)
        Body[14].append(vrep.simxGetObjectHandle(clientID,'LShoulderPitch3#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        Body[15].append(vrep.simxGetObjectHandle(clientID,'LShoulderRoll3#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        Body[16].append(vrep.simxGetObjectHandle(clientID,'LElbowYaw3#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        Body[17].append(vrep.simxGetObjectHandle(clientID,'LElbowRoll3#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        Body[18].append(vrep.simxGetObjectHandle(clientID,'LWristYaw3#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        #Right Arm
        print '-> Right Arm for NAO : ' + str(i+2)
        Body[19].append(vrep.simxGetObjectHandle(clientID,'RShoulderPitch3#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        Body[20].append(vrep.simxGetObjectHandle(clientID,'RShoulderRoll3#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        Body[21].append(vrep.simxGetObjectHandle(clientID,'RElbowYaw3#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        Body[22].append(vrep.simxGetObjectHandle(clientID,'RElbowRoll3#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        Body[23].append(vrep.simxGetObjectHandle(clientID,'RWristYaw3#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        #Left fingers
        print '-> Left Fingers for NAO : ' + str(i+2)
        Body[24].append(vrep.simxGetObjectHandle(clientID,'NAO_LThumbBase#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        Body[24].append(vrep.simxGetObjectHandle(clientID,'Revolute_joint8#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        Body[24].append(vrep.simxGetObjectHandle(clientID,'NAO_LLFingerBase#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        Body[24].append(vrep.simxGetObjectHandle(clientID,'Revolute_joint12#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        Body[24].append(vrep.simxGetObjectHandle(clientID,'Revolute_joint14#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        Body[24].append(vrep.simxGetObjectHandle(clientID,'NAO_LRFinger_Base#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        Body[24].append(vrep.simxGetObjectHandle(clientID,'Revolute_joint11#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        Body[24].append(vrep.simxGetObjectHandle(clientID,'Revolute_joint13#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        Body[25].append(Body[24][i*8:(i+1)*8])
        #Right Fingers
        print '-> Right Fingers for NAO : ' + str(i+2)
        Body[26].append(vrep.simxGetObjectHandle(clientID,'NAO_RThumbBase#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        Body[26].append(vrep.simxGetObjectHandle(clientID,'Revolute_joint0#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        Body[26].append(vrep.simxGetObjectHandle(clientID,'NAO_RLFingerBase#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        Body[26].append(vrep.simxGetObjectHandle(clientID,'Revolute_joint5#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        Body[26].append(vrep.simxGetObjectHandle(clientID,'Revolute_joint6#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        Body[26].append(vrep.simxGetObjectHandle(clientID,'NAO_RRFinger_Base#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        Body[26].append(vrep.simxGetObjectHandle(clientID,'Revolute_joint2#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        Body[26].append(vrep.simxGetObjectHandle(clientID,'Revolute_joint3#'+str(i),vrep.simx_opmode_oneshot_wait)[1])
        Body[27].append(Body[26][(i+1)*8:(i+2)*8])  
#Allow the joint to move in the VRep Simulation
def JointControl(clientID,motionProxy,i,Body):
    #Head
    while(vrep.simxGetConnectionId(clientID)!=-1):
        #Getting joint's angles from Choregraphe (please check your robot's IP)
        commandAngles = motionProxy.getAngles('Body', False)
        #Allow the robot to move in VRep using choregraphe's angles
        
        vrep.simxSetJointTargetPosition(clientID,Body[0][i],commandAngles[0],vrep.simx_opmode_streaming)
        vrep.simxSetJointTargetPosition(clientID,Body[1][i],commandAngles[1],vrep.simx_opmode_streaming)
        #Left Leg
        vrep.simxSetJointTargetPosition(clientID,Body[2][i],commandAngles[8],vrep.simx_opmode_streaming)
        vrep.simxSetJointTargetPosition(clientID,Body[3][i],commandAngles[9],vrep.simx_opmode_streaming)
        vrep.simxSetJointTargetPosition(clientID,Body[4][i],commandAngles[10],vrep.simx_opmode_streaming)
        vrep.simxSetJointTargetPosition(clientID,Body[5][i],commandAngles[11],vrep.simx_opmode_streaming)
        vrep.simxSetJointTargetPosition(clientID,Body[6][i],commandAngles[12],vrep.simx_opmode_streaming)
        vrep.simxSetJointTargetPosition(clientID,Body[7][i],commandAngles[13],vrep.simx_opmode_streaming)
        #Right Leg
        vrep.simxSetJointTargetPosition(clientID,Body[8][i],commandAngles[14],vrep.simx_opmode_streaming)
        vrep.simxSetJointTargetPosition(clientID,Body[9][i],commandAngles[15],vrep.simx_opmode_streaming)
        vrep.simxSetJointTargetPosition(clientID,Body[10][i],commandAngles[16],vrep.simx_opmode_streaming)
        vrep.simxSetJointTargetPosition(clientID,Body[11][i],commandAngles[17],vrep.simx_opmode_streaming)
        vrep.simxSetJointTargetPosition(clientID,Body[12][i],commandAngles[18],vrep.simx_opmode_streaming)
        vrep.simxSetJointTargetPosition(clientID,Body[13][i],commandAngles[19],vrep.simx_opmode_streaming)
        #Left Arm
        vrep.simxSetJointTargetPosition(clientID,Body[14][i],commandAngles[2],vrep.simx_opmode_streaming)
        vrep.simxSetJointTargetPosition(clientID,Body[15][i],commandAngles[3],vrep.simx_opmode_streaming)
        vrep.simxSetJointTargetPosition(clientID,Body[16][i],commandAngles[4],vrep.simx_opmode_streaming)
        vrep.simxSetJointTargetPosition(clientID,Body[17][i],commandAngles[5],vrep.simx_opmode_streaming)
        vrep.simxSetJointTargetPosition(clientID,Body[18][i],commandAngles[6],vrep.simx_opmode_streaming)
        #Right Arm
        vrep.simxSetJointTargetPosition(clientID,Body[19][i],commandAngles[20],vrep.simx_opmode_streaming)
        vrep.simxSetJointTargetPosition(clientID,Body[20][i],commandAngles[21],vrep.simx_opmode_streaming)
        vrep.simxSetJointTargetPosition(clientID,Body[21][i],commandAngles[22],vrep.simx_opmode_streaming)
        vrep.simxSetJointTargetPosition(clientID,Body[22][i],commandAngles[23],vrep.simx_opmode_streaming)
        vrep.simxSetJointTargetPosition(clientID,Body[23][i],commandAngles[24],vrep.simx_opmode_streaming)
        #Left Fingers
        vrep.simxSetJointTargetPosition(clientID,Body[25][i][0],1.0-commandAngles[7],vrep.simx_opmode_streaming)
        vrep.simxSetJointTargetPosition(clientID,Body[25][i][1],1.0-commandAngles[7],vrep.simx_opmode_streaming)
        vrep.simxSetJointTargetPosition(clientID,Body[25][i][2],1.0-commandAngles[7],vrep.simx_opmode_streaming)
        vrep.simxSetJointTargetPosition(clientID,Body[25][i][3],1.0-commandAngles[7],vrep.simx_opmode_streaming)
        vrep.simxSetJointTargetPosition(clientID,Body[25][i][4],1.0-commandAngles[7],vrep.simx_opmode_streaming)
        vrep.simxSetJointTargetPosition(clientID,Body[25][i][5],1.0-commandAngles[7],vrep.simx_opmode_streaming)
        vrep.simxSetJointTargetPosition(clientID,Body[25][i][6],1.0-commandAngles[7],vrep.simx_opmode_streaming)
        vrep.simxSetJointTargetPosition(clientID,Body[25][i][7],1.0-commandAngles[7],vrep.simx_opmode_streaming)
        #Right Fingers
        vrep.simxSetJointTargetPosition(clientID,Body[27][i][0],1.0-commandAngles[25],vrep.simx_opmode_streaming)
        vrep.simxSetJointTargetPosition(clientID,Body[27][i][1],1.0-commandAngles[25],vrep.simx_opmode_streaming)
        vrep.simxSetJointTargetPosition(clientID,Body[27][i][2],1.0-commandAngles[25],vrep.simx_opmode_streaming)
        vrep.simxSetJointTargetPosition(clientID,Body[27][i][3],1.0-commandAngles[25],vrep.simx_opmode_streaming)
        vrep.simxSetJointTargetPosition(clientID,Body[27][i][4],1.0-commandAngles[25],vrep.simx_opmode_streaming)
        vrep.simxSetJointTargetPosition(clientID,Body[27][i][5],1.0-commandAngles[25],vrep.simx_opmode_streaming)
        vrep.simxSetJointTargetPosition(clientID,Body[27][i][6],1.0-commandAngles[25],vrep.simx_opmode_streaming)
        vrep.simxSetJointTargetPosition(clientID,Body[27][i][7],1.0-commandAngles[25],vrep.simx_opmode_streaming)
    print 'End of simulation'

#Get the Handle of only one NAO
def get_first_handles(clientID,Body):    
    print '-> Head for NAO : '+ str(1)
    Body[0].append(vrep.simxGetObjectHandle(clientID,'HeadYaw#',vrep.simx_opmode_oneshot_wait)[1])
    Body[1].append(vrep.simxGetObjectHandle(clientID,'HeadPitch#',vrep.simx_opmode_oneshot_wait)[1])
    #Left Leg
    print '-> Left Leg for NAO : ' + str(1)
    Body[2].append(vrep.simxGetObjectHandle(clientID,'LHipYawPitch3#',vrep.simx_opmode_oneshot_wait)[1])
    Body[3].append(vrep.simxGetObjectHandle(clientID,'LHipRoll3#',vrep.simx_opmode_oneshot_wait)[1])
    Body[4].append(vrep.simxGetObjectHandle(clientID,'LHipPitch3#',vrep.simx_opmode_oneshot_wait)[1])
    Body[5].append(vrep.simxGetObjectHandle(clientID,'LKneePitch3#',vrep.simx_opmode_oneshot_wait)[1])
    Body[6].append(vrep.simxGetObjectHandle(clientID,'LAnklePitch3#',vrep.simx_opmode_oneshot_wait)[1])
    Body[7].append(vrep.simxGetObjectHandle(clientID,'LAnkleRoll3#',vrep.simx_opmode_oneshot_wait)[1])
    #Right Leg
    print '-> Right Leg for NAO : ' + str(1)
    Body[8].append(vrep.simxGetObjectHandle(clientID,'RHipYawPitch3#',vrep.simx_opmode_oneshot_wait)[1])
    Body[9].append(vrep.simxGetObjectHandle(clientID,'RHipRoll3#',vrep.simx_opmode_oneshot_wait)[1])
    Body[10].append(vrep.simxGetObjectHandle(clientID,'RHipPitch3#',vrep.simx_opmode_oneshot_wait)[1])
    Body[11].append(vrep.simxGetObjectHandle(clientID,'RKneePitch3#',vrep.simx_opmode_oneshot_wait)[1])
    Body[12].append(vrep.simxGetObjectHandle(clientID,'RAnklePitch3#',vrep.simx_opmode_oneshot_wait)[1])
    Body[13].append(vrep.simxGetObjectHandle(clientID,'RAnkleRoll3#',vrep.simx_opmode_oneshot_wait)[1])
    #Left Arm
    print '-> Left Arm for NAO : ' + str(1)
    Body[14].append(vrep.simxGetObjectHandle(clientID,'LShoulderPitch3#',vrep.simx_opmode_oneshot_wait)[1])
    Body[15].append(vrep.simxGetObjectHandle(clientID,'LShoulderRoll3#',vrep.simx_opmode_oneshot_wait)[1])
    Body[16].append(vrep.simxGetObjectHandle(clientID,'LElbowYaw3#',vrep.simx_opmode_oneshot_wait)[1])
    Body[17].append(vrep.simxGetObjectHandle(clientID,'LElbowRoll3#',vrep.simx_opmode_oneshot_wait)[1])
    Body[18].append(vrep.simxGetObjectHandle(clientID,'LWristYaw3#',vrep.simx_opmode_oneshot_wait)[1])
    #Right Arm
    print '-> Right Arm for NAO : ' + str(1)
    Body[19].append(vrep.simxGetObjectHandle(clientID,'RShoulderPitch3#',vrep.simx_opmode_oneshot_wait)[1])
    Body[20].append(vrep.simxGetObjectHandle(clientID,'RShoulderRoll3#',vrep.simx_opmode_oneshot_wait)[1])
    Body[21].append(vrep.simxGetObjectHandle(clientID,'RElbowYaw3#',vrep.simx_opmode_oneshot_wait)[1])
    Body[22].append(vrep.simxGetObjectHandle(clientID,'RElbowRoll3#',vrep.simx_opmode_oneshot_wait)[1])
    Body[23].append(vrep.simxGetObjectHandle(clientID,'RWristYaw3#',vrep.simx_opmode_oneshot_wait)[1])
    #Left fingers
    print '-> Left Fingers for NAO : ' + str(1)
    Body[24].append(vrep.simxGetObjectHandle(clientID,'NAO_LThumbBase#',vrep.simx_opmode_oneshot_wait)[1])
    Body[24].append(vrep.simxGetObjectHandle(clientID,'Revolute_joint8#',vrep.simx_opmode_oneshot_wait)[1])
    Body[24].append(vrep.simxGetObjectHandle(clientID,'NAO_LLFingerBase#',vrep.simx_opmode_oneshot_wait)[1])
    Body[24].append(vrep.simxGetObjectHandle(clientID,'Revolute_joint12#',vrep.simx_opmode_oneshot_wait)[1])
    Body[24].append(vrep.simxGetObjectHandle(clientID,'Revolute_joint14#',vrep.simx_opmode_oneshot_wait)[1])
    Body[24].append(vrep.simxGetObjectHandle(clientID,'NAO_LRFinger_Base#',vrep.simx_opmode_oneshot_wait)[1])
    Body[24].append(vrep.simxGetObjectHandle(clientID,'Revolute_joint11#',vrep.simx_opmode_oneshot_wait)[1])
    Body[24].append(vrep.simxGetObjectHandle(clientID,'Revolute_joint13#',vrep.simx_opmode_oneshot_wait)[1])
    Body[25].append(Body[24][0:8])
    #Right Fingers
    print '-> Right Fingers for NAO : ' + str(1)
    Body[26].append(vrep.simxGetObjectHandle(clientID,'NAO_RThumbBase#',vrep.simx_opmode_oneshot_wait)[1])
    Body[26].append(vrep.simxGetObjectHandle(clientID,'Revolute_joint0#',vrep.simx_opmode_oneshot_wait)[1])
    Body[26].append(vrep.simxGetObjectHandle(clientID,'NAO_RLFingerBase#',vrep.simx_opmode_oneshot_wait)[1])
    Body[26].append(vrep.simxGetObjectHandle(clientID,'Revolute_joint5#',vrep.simx_opmode_oneshot_wait)[1])
    Body[26].append(vrep.simxGetObjectHandle(clientID,'Revolute_joint6#',vrep.simx_opmode_oneshot_wait)[1])
    Body[26].append(vrep.simxGetObjectHandle(clientID,'NAO_RRFinger_Base#',vrep.simx_opmode_oneshot_wait)[1])
    Body[26].append(vrep.simxGetObjectHandle(clientID,'Revolute_joint2#',vrep.simx_opmode_oneshot_wait)[1])
    Body[26].append(vrep.simxGetObjectHandle(clientID,'Revolute_joint3#',vrep.simx_opmode_oneshot_wait)[1])
    Body[27].append(Body[26][0:8]) 

def CustomJointControl(clientID,motionProxy,memoryProxy,i,Body,data_gyro,data_LFsrFL,data_LFsrFR,data_LFsrRL,data_LFsrRR,data_RFsrFL,data_RFsrFR,data_RFsrRL,data_RFsrRR):
    #Head
    while(vrep.simxGetConnectionId(clientID)!=-1):
        #Getting joint's angles from Choregraphe (please check your robot's IP)
        commandAngles = motionProxy.getAngles('Body', False)
        #Allow the robot to move in VRep using choregraphe's angles
        
        vrep.simxSetJointTargetPosition(clientID,Body[0][i],commandAngles[0],vrep.simx_opmode_streaming)
        vrep.simxSetJointTargetPosition(clientID,Body[1][i],commandAngles[1],vrep.simx_opmode_streaming)
        #Left Leg
        vrep.simxSetJointTargetPosition(clientID,Body[2][i],commandAngles[8],vrep.simx_opmode_streaming)
        vrep.simxSetJointTargetPosition(clientID,Body[3][i],commandAngles[9],vrep.simx_opmode_streaming)
        vrep.simxSetJointTargetPosition(clientID,Body[4][i],commandAngles[10],vrep.simx_opmode_streaming)
        vrep.simxSetJointTargetPosition(clientID,Body[5][i],commandAngles[11],vrep.simx_opmode_streaming)
        vrep.simxSetJointTargetPosition(clientID,Body[6][i],commandAngles[12],vrep.simx_opmode_streaming)
        vrep.simxSetJointTargetPosition(clientID,Body[7][i],commandAngles[13],vrep.simx_opmode_streaming)
        #Right Leg
        vrep.simxSetJointTargetPosition(clientID,Body[8][i],commandAngles[14],vrep.simx_opmode_streaming)
        vrep.simxSetJointTargetPosition(clientID,Body[9][i],commandAngles[15],vrep.simx_opmode_streaming)
        vrep.simxSetJointTargetPosition(clientID,Body[10][i],commandAngles[16],vrep.simx_opmode_streaming)
        vrep.simxSetJointTargetPosition(clientID,Body[11][i],commandAngles[17],vrep.simx_opmode_streaming)
        vrep.simxSetJointTargetPosition(clientID,Body[12][i],commandAngles[18],vrep.simx_opmode_streaming)
        vrep.simxSetJointTargetPosition(clientID,Body[13][i],commandAngles[19],vrep.simx_opmode_streaming)
        #Left Arm
        vrep.simxSetJointTargetPosition(clientID,Body[14][i],commandAngles[2],vrep.simx_opmode_streaming)
        vrep.simxSetJointTargetPosition(clientID,Body[15][i],commandAngles[3],vrep.simx_opmode_streaming)
        vrep.simxSetJointTargetPosition(clientID,Body[16][i],commandAngles[4],vrep.simx_opmode_streaming)
        vrep.simxSetJointTargetPosition(clientID,Body[17][i],commandAngles[5],vrep.simx_opmode_streaming)
        vrep.simxSetJointTargetPosition(clientID,Body[18][i],commandAngles[6],vrep.simx_opmode_streaming)
        #Right Arm
        vrep.simxSetJointTargetPosition(clientID,Body[19][i],commandAngles[20],vrep.simx_opmode_streaming)
        vrep.simxSetJointTargetPosition(clientID,Body[20][i],commandAngles[21],vrep.simx_opmode_streaming)
        vrep.simxSetJointTargetPosition(clientID,Body[21][i],commandAngles[22],vrep.simx_opmode_streaming)
        vrep.simxSetJointTargetPosition(clientID,Body[22][i],commandAngles[23],vrep.simx_opmode_streaming)
        vrep.simxSetJointTargetPosition(clientID,Body[23][i],commandAngles[24],vrep.simx_opmode_streaming)
        #Left Fingers
        vrep.simxSetJointTargetPosition(clientID,Body[25][i][0],1.0-commandAngles[7],vrep.simx_opmode_streaming)
        vrep.simxSetJointTargetPosition(clientID,Body[25][i][1],1.0-commandAngles[7],vrep.simx_opmode_streaming)
        vrep.simxSetJointTargetPosition(clientID,Body[25][i][2],1.0-commandAngles[7],vrep.simx_opmode_streaming)
        vrep.simxSetJointTargetPosition(clientID,Body[25][i][3],1.0-commandAngles[7],vrep.simx_opmode_streaming)
        vrep.simxSetJointTargetPosition(clientID,Body[25][i][4],1.0-commandAngles[7],vrep.simx_opmode_streaming)
        vrep.simxSetJointTargetPosition(clientID,Body[25][i][5],1.0-commandAngles[7],vrep.simx_opmode_streaming)
        vrep.simxSetJointTargetPosition(clientID,Body[25][i][6],1.0-commandAngles[7],vrep.simx_opmode_streaming)
        vrep.simxSetJointTargetPosition(clientID,Body[25][i][7],1.0-commandAngles[7],vrep.simx_opmode_streaming)
        #Right Fingers
        vrep.simxSetJointTargetPosition(clientID,Body[27][i][0],1.0-commandAngles[25],vrep.simx_opmode_streaming)
        vrep.simxSetJointTargetPosition(clientID,Body[27][i][1],1.0-commandAngles[25],vrep.simx_opmode_streaming)
        vrep.simxSetJointTargetPosition(clientID,Body[27][i][2],1.0-commandAngles[25],vrep.simx_opmode_streaming)
        vrep.simxSetJointTargetPosition(clientID,Body[27][i][3],1.0-commandAngles[25],vrep.simx_opmode_streaming)
        vrep.simxSetJointTargetPosition(clientID,Body[27][i][4],1.0-commandAngles[25],vrep.simx_opmode_streaming)
        vrep.simxSetJointTargetPosition(clientID,Body[27][i][5],1.0-commandAngles[25],vrep.simx_opmode_streaming)
        vrep.simxSetJointTargetPosition(clientID,Body[27][i][6],1.0-commandAngles[25],vrep.simx_opmode_streaming)
        vrep.simxSetJointTargetPosition(clientID,Body[27][i][7],1.0-commandAngles[25],vrep.simx_opmode_streaming)

        # =====================================gyro=====================================

        ret,arr = vrep.simxGetObjectOrientation(clientID, data_gyro , -1, vrep.simx_opmode_streaming)
        arr[0]=arr[0]*180/3.1415
        arr[1]=arr[1]*180/3.1415
        arr[2]=arr[2]*180/3.1415
        memoryProxy.insertData("gyro_pitch", arr[0])
        memoryProxy.insertData("gyro_roll", arr[1])
        memoryProxy.insertData("gyro_yaw", arr[2])

        # =====================================gyroDer=====================================

        angularVariationX = vrep.simxGetFloatSignal(clientID, 'gyroX', vrep.simx_opmode_streaming)
        angularVariationY = vrep.simxGetFloatSignal(clientID, 'gyroY', vrep.simx_opmode_streaming)
        angularVariationZ = vrep.simxGetFloatSignal(clientID, 'gyroZ', vrep.simx_opmode_streaming)
        memoryProxy.insertData("gyroDerX", angularVariationX[1])
        memoryProxy.insertData("gyroDerY", angularVariationY[1])
        memoryProxy.insertData("gyroDerZ", angularVariationZ[1])

        # =====================================stiffness=====================================

        anklePitchStiffness = memoryProxy.getData("ankle_pitch_stiff")
        ankleRollStiffness = memoryProxy.getData("ankle_roll_stiff")
        hipPitchStiffness = memoryProxy.getData("hip_pitch_stiff")
        hipRollStiffness = memoryProxy.getData("hip_roll_stiff")
        vrep.simxSetJointForce(clientID, Body[6][0], anklePitchStiffness*30.0, vrep.simx_opmode_streaming)
        vrep.simxSetJointForce(clientID, Body[12][0], anklePitchStiffness*30.0, vrep.simx_opmode_streaming)
        vrep.simxSetJointForce(clientID, Body[4][0], hipPitchStiffness * 30.0, vrep.simx_opmode_streaming)
        vrep.simxSetJointForce(clientID, Body[10][0], hipRollStiffness * 30.0, vrep.simx_opmode_streaming)

        vrep.simxSetJointForce(clientID, Body[7][0], ankleRollStiffness*30.0, vrep.simx_opmode_streaming)
        vrep.simxSetJointForce(clientID, Body[13][0], ankleRollStiffness*30.0, vrep.simx_opmode_streaming)
        vrep.simxSetJointForce(clientID, Body[3][0], hipRollStiffness * 30.0, vrep.simx_opmode_streaming)
        vrep.simxSetJointForce(clientID, Body[9][0], hipRollStiffness * 30.0, vrep.simx_opmode_streaming)
        # =====================================force=====================================

        #ret,state,arr1,arr2 = vrep.simxReadForceSensor(clientID, data_LFsrFL, vrep.simx_opmode_streaming)
        #memoryProxy.insertData("LFsrFL", arr1[2])
        #ret,state,arr1,arr2 = vrep.simxReadForceSensor(clientID, data_LFsrFR, vrep.simx_opmode_streaming)
        #memoryProxy.insertData("LFsrFR", arr1[2])
        #ret,state,arr1,arr2 = vrep.simxReadForceSensor(clientID, data_LFsrRL, vrep.simx_opmode_streaming)
        #memoryProxy.insertData("LFsrRL", arr1[2])
        #ret,state,arr1,arr2 = vrep.simxReadForceSensor(clientID, data_LFsrRR, vrep.simx_opmode_streaming)
        #memoryProxy.insertData("LFsrRR", arr1[2])
        
        #ret,state,arr1,arr2 = vrep.simxReadForceSensor(clientID, data_RFsrFL, vrep.simx_opmode_streaming)
        #memoryProxy.insertData("RFsrFL", arr1[2])
        #ret,state,arr1,arr2 = vrep.simxReadForceSensor(clientID, data_RFsrFR, vrep.simx_opmode_streaming)
        #memoryProxy.insertData("RFsrFR", arr1[2])
        #ret,state,arr1,arr2 = vrep.simxReadForceSensor(clientID, data_RFsrRL, vrep.simx_opmode_streaming)
        #memoryProxy.insertData("RFsrRL", arr1[2])
        #ret,state,arr1,arr2 = vrep.simxReadForceSensor(clientID, data_RFsrRR, vrep.simx_opmode_streaming)
        #memoryProxy.insertData("RFsrRR", arr1[2])

        # =====================================encoders=====================================
        a, HeadPitch_pos = vrep.simxGetJointPosition(clientID, Body[0][0], vrep.simx_opmode_streaming)
        a, HeadYaw_pos = vrep.simxGetJointPosition(clientID, Body[1][0], vrep.simx_opmode_streaming)

        a,LHipYawPitch_pos = vrep.simxGetJointPosition(clientID, Body[2][0], vrep.simx_opmode_streaming)
        a,LHipRoll_pos = vrep.simxGetJointPosition(clientID, Body[3][0], vrep.simx_opmode_streaming)
        a,LHipPitch_pos = vrep.simxGetJointPosition(clientID, Body[4][0], vrep.simx_opmode_streaming)
        a,LKneePitch_pos = vrep.simxGetJointPosition(clientID, Body[5][0], vrep.simx_opmode_streaming)
        a,LAnklePitch_pos = vrep.simxGetJointPosition(clientID, Body[6][0], vrep.simx_opmode_streaming)
        a,LAnkleRoll_pos = vrep.simxGetJointPosition(clientID, Body[7][0], vrep.simx_opmode_streaming)

        a, RHipYawPitch_pos = vrep.simxGetJointPosition(clientID, Body[8][0], vrep.simx_opmode_streaming)
        a,RHipRoll_pos = vrep.simxGetJointPosition(clientID, Body[9][0], vrep.simx_opmode_streaming)
        a,RHipPitch_pos = vrep.simxGetJointPosition(clientID, Body[10][0], vrep.simx_opmode_streaming)
        a,RKneePitch_pos = vrep.simxGetJointPosition(clientID, Body[11][0], vrep.simx_opmode_streaming)
        a,RAnklePitch_pos = vrep.simxGetJointPosition(clientID, Body[12][0], vrep.simx_opmode_streaming)
        a,RAnkleRoll_pos = vrep.simxGetJointPosition(clientID, Body[13][0], vrep.simx_opmode_streaming)

        a, LShoulderPitch_pos = vrep.simxGetJointPosition(clientID, Body[14][0], vrep.simx_opmode_streaming)
        a, LShoulderRoll_pos = vrep.simxGetJointPosition(clientID, Body[15][0], vrep.simx_opmode_streaming)
        a, LElbowYaw_pos = vrep.simxGetJointPosition(clientID, Body[16][0], vrep.simx_opmode_streaming)
        a, LElbowRoll_pos = vrep.simxGetJointPosition(clientID, Body[17][0], vrep.simx_opmode_streaming)
        a, LWristYaw_pos = vrep.simxGetJointPosition(clientID, Body[18][0], vrep.simx_opmode_streaming)

        a, RShoulderPitch_pos = vrep.simxGetJointPosition(clientID, Body[19][0], vrep.simx_opmode_streaming)
        a, RShoulderRoll_pos = vrep.simxGetJointPosition(clientID, Body[20][0], vrep.simx_opmode_streaming)
        a, RElbowYaw_pos = vrep.simxGetJointPosition(clientID, Body[21][0], vrep.simx_opmode_streaming)
        a, RElbowRoll_pos = vrep.simxGetJointPosition(clientID, Body[22][0], vrep.simx_opmode_streaming)
        a, RWristYaw_pos = vrep.simxGetJointPosition(clientID, Body[23][0], vrep.simx_opmode_streaming)


        memoryProxy.insertData("HeadPitch_pos", HeadPitch_pos)
        memoryProxy.insertData("HeadYaw_pos", HeadYaw_pos)

        memoryProxy.insertData("LHipYawPitch_pos", LHipYawPitch_pos)
        memoryProxy.insertData("LHipRoll_pos", LHipRoll_pos)
        memoryProxy.insertData("LHipPitch_pos", LHipPitch_pos)
        memoryProxy.insertData("LKneePitch_pos", LKneePitch_pos)
        memoryProxy.insertData("LAnklePitch_pos", LAnklePitch_pos)
        memoryProxy.insertData("LAnkleRoll_pos", LAnkleRoll_pos)

        memoryProxy.insertData("RHipYawPitch_pos", RHipYawPitch_pos)
        memoryProxy.insertData("RHipRoll_pos", RHipRoll_pos)
        memoryProxy.insertData("RHipPitch_pos", RHipPitch_pos)
        memoryProxy.insertData("RKneePitch_pos", RKneePitch_pos)
        memoryProxy.insertData("RAnklePitch_pos", RAnklePitch_pos)
        memoryProxy.insertData("RAnkleRoll_pos", RAnkleRoll_pos)

        memoryProxy.insertData("RShoulderPitch_pos",RShoulderPitch_pos)
        memoryProxy.insertData("RShoulderRoll_pos",RShoulderRoll_pos)
        memoryProxy.insertData("RElbowYaw_pos",RElbowYaw_pos)
        memoryProxy.insertData("RElbowRoll_pos",RElbowRoll_pos)
        memoryProxy.insertData("RWristYaw_pos",RWristYaw_pos)

        memoryProxy.insertData("LShoulderPitch_pos", LShoulderPitch_pos)
        memoryProxy.insertData("LShoulderRoll_pos", LShoulderRoll_pos)
        memoryProxy.insertData("LElbowYaw_pos", LElbowYaw_pos)
        memoryProxy.insertData("LElbowRoll_pos", LElbowRoll_pos)
        memoryProxy.insertData("LWristYaw_pos", LWristYaw_pos)

    print 'End of simulation'