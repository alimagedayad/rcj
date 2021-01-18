from l289n import l289n as MotorDriver

#motor setup

driver1 = MotorDriver(1,2,3,4,testing=1)

driver1 = driver1.backwards()

# forward motion