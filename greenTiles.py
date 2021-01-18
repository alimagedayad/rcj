from l289n import l289n as MotorDriver
Driver = MotorDriver(1,2,3,4,testing=1)

def colorSensorGreen(r,g,b):
    if r == 0 and g == 100 and b == 0:
        return True
    else:
        return False

def greenTile(colorS1, colorS2):
    if colorS1 == True and colorS2 == False:
        Driver.right()
    elif colorS2 == True and colorS1 == False:
        Driver.left()
    elif colorS1[2] == 255 and colorS2[2] == 255:
        Driver.uturn()