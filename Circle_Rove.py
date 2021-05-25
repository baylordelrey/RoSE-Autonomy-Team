from roboclaw import Roboclaw
from time import sleep

if __name__ == "__main__":
    
    address1 = 0x80
    address2 = 0x81
    address3 = 0x82
    roboclaw = Roboclaw("/dev/ttyS0", 38400)
    roboclaw.Open()
    
    while True:
        roboclaw.ForwardM1(address1,64)
        roboclaw.ForwardM2(address1, 64)
        roboclaw.ForwardM1(address2,64)
        roboclaw.ForwardM2(address2, 10)
        roboclaw.ForwardM1(address3,10)
        roboclaw.ForwardM2(address3, 10)
        sleep(4)
        roboclaw.ForwardM1(address1,0)
        roboclaw.ForwardM2(address1,0)
        roboclaw.ForwardM1(address2,0)
        roboclaw.ForwardM2(address2,0)
        roboclaw.ForwardM1(address3,0)
        roboclaw.ForwardM2(address3,0)
        sleep(2)
        
    
   
  
    
    