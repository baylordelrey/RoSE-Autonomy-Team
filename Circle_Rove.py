from roboclaw import Roboclaw
from time import sleep

if __name__ == "__main__":
    
    addresses = [0x80,0x81,0x82]
    roboclaw = Roboclaw("/dev/ttyS0", 38400)
    roboclaw.Open()
    
    while True:
        
        for address = 0x80
        
        roboclaw.ForwardM1(address,64)
        sleep(2)
        roboclaw.ForwardM2(address, 64)
        sleep(2)
        roboclaw.ForwardM1(address,0)
        sleep(2)
        roboclaw.ForwardM2(address,0)
        sleep(2)
        
        for address = 0x81
        roboclaw.ForwardM1(address,64)
        sleep(2)
        roboclaw.ForwardM2(address, 20)
        sleep(2)
        roboclaw.ForwardM1(address,0)
        sleep(2)
        roboclaw.ForwardM2(address,0)
        sleep(2)
        
        for address = 0x82
        roboclaw.ForwardM1(address,20)
        sleep(2)
        roboclaw.ForwardM2(address, 20)
        sleep(2)
        roboclaw.ForwardM1(address,0)
        sleep(2)
        roboclaw.ForwardM2(address,0)
        sleep(2)
        
    

