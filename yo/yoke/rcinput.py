from yoke import events
import os
from mmap import mmap
fh=0

file_handle = os.open("/dev/uio0", os.O_RDWR|os.O_NONBLOCK)
mem_access = mmap(file_handle, 4)
fh = file_handle
class rcinput:

    # input mapping
    input_default = {
        'ABS_X': 128,
        'ABS_Y': 128,

        'ABS_RX': 128,
        'ABS_RY': 128,

        'ABS_GAS': 0,

        'BTN_MODE': 0
    }
    input = dict(input_default)

    active = 0

    def __init__(self):
        1+1

    def destroy(self):
        1+1

    ## done foreach input => value every update
    ## updates the input object with the given input events
    def emit(self, event, value, nothing):
        # Mode button to toggle activation
        if event == events.BTN_MODE:
            if self.input['BTN_MODE'] != value:
                if value == 1:
                    self.active = not(self.active)
                    print("toggling active state")
            self.input['BTN_MODE'] = value
        # input axis
        elif event == events.ABS_X:
            self.input['ABS_X'] = value
        elif event == events.ABS_Y:
            self.input["ABS_Y"] = value
        elif event == events.ABS_RX:
            self.input["ABS_RX"] = value
        elif event == events.ABS_RY:
            self.input["ABS_RY"] = value
        # gas pedel if you may want to override the speed (not programmed yet)
        elif event == events.ABS_GAS:
            self.input["ABS_GAS"] = value

    ## done after each full update
    def syn(self):
        # get right Axis for the 2 modes
        if self.active == 1:
            X = self.input["ABS_X"]
            Y = self.input["ABS_Y"]
            RX = self.input["ABS_RX"]
            RY = self.input["ABS_RY"]
            G = self.input["ABS_GAS"]
        else:
            X = self.input_default["ABS_X"]
            Y = self.input_default["ABS_Y"]
            RX = self.input_default["ABS_RX"]
            RY = self.input_default["ABS_RY"]
            G = self.input_default["ABS_GAS"]

        #TODO put your processing under here
        if(Y<127):
            Y -= 127
            if(Y <0):
                Y *= -1
        if(Y==128):
            Y=0

        if(RX<127):
            RX -= 127
            if(RX<0):
                RX*= -1
#            if(RX>128):
#                RX =RX- 128
        Motor1 = Motor2 = Motor3 = Motor4 = 0
        if(RX==128):
            RX=0
        if(Y !=0 and RX ==0):
            Motor1 = Motor2 = Motor3 = Motor4 = Y
        if(RX >128 and Y == 0 and RX!=0):
            Motor2 = Motor3 = RX
            Motor1 = Motor4 = RX - 128
        if(RX < 128 and Y==0 and RX != 0):
            Motor2 = Motor3 = RX 
            Motor1 = Motor4 = RX + 128
       # Motor3 = 
        #Motor4 = 0
        print(Motor1 ,' ', Motor2 ,' ', Motor3,' ',Motor4)
        mem_access[0] = Motor1
        mem_access[1] = Motor2
        mem_access[2] = Motor3
        mem_access[3] = Motor4

os.close(fh)
