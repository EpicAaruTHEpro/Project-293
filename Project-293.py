"""Project-293 controller."""

from controller import Robot

robot = Robot()

timestep = 64
flag = 0

motorRPC = robot.getDevice("RPC")
motorRPF = robot.getDevice("RPF")
motorRMC = robot.getDevice("RMC")
motorRMF = robot.getDevice("RMF")
motorRAC = robot.getDevice("RAC")
motorRAF = robot.getDevice("RAF")

motorLPC = robot.getDevice("LPC")
motorLPF = robot.getDevice("LPF")
motorLMC = robot.getDevice("LMC")
motorLMF = robot.getDevice("LMF")
motorLAC = robot.getDevice("LAC")
motorLAF = robot.getDevice("LAF")


while robot.step(timestep) != -1:
    if(flag%12==0):
        motorRPC.setPosition(-0.3)
        motorLPC.setPosition(-0.3)
    elif(flag%12==2):
        motorRPF.setPosition(-0.3)
        motorLPF.setPosition(-0.3)
    elif(flag%12==4):
        motorRMC.setPosition(-0.3)
        motorLMC.setPosition(-0.3)
    elif(flag%12==6):
        motorRMF.setPosition(-0.3)
        motorLMF.setPosition(-0.3)
    elif(flag%12==8):
        motorRAC.setPosition(-0.3)
        motorLAC.setPosition(-0.3)
    elif(flag%12==10):
        motorRAF.setPosition(-0.3)
        motorLAF.setPosition(-0.3)
        
    elif(flag%12==11):
        motorRPC.setPosition(0)
        motorLPC.setPosition(0)
        motorRPF.setPosition(0)
        motorLPF.setPosition(0)
        motorRMC.setPosition(0)
        motorLMC.setPosition(0)
        motorRAF.setPosition(0)
        motorLAF.setPosition(0)
        motorRAC.setPosition(0)
        motorLAC.setPosition(0)
        motorRMF.setPosition(0)
        motorLMF.setPosition(0)
        
    flag+=1