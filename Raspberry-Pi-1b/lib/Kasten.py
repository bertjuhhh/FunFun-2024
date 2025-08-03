from enum import Enum

class KASTEN(Enum):
    # LED Strips (Pico controlled)
    LEDKAST_1 = "LEDKAST_1"
    LEDKAST_2 = "LEDKAST_2"
    LEDKAST_3 = "LEDKAST_3"
    LEDKAST_4 = "LEDKAST_4"
    
    # DMX Devices (Pi 1B controlled)
    DMX_PAR_1 = "DMX_PAR_1"
    DMX_PAR_2 = "DMX_PAR_2"
    DMX_PAR_3 = "DMX_PAR_3"
    DMX_PAR_4 = "DMX_PAR_4"
    DMX_WASH_1 = "DMX_WASH_1"
    DMX_WASH_2 = "DMX_WASH_2"
    DMX_STROBE_1 = "DMX_STROBE_1"
    DMX_STROBE_2 = "DMX_STROBE_2"
    DMX_MOVING_HEAD_1 = "DMX_MOVING_HEAD_1"
    DMX_MOVING_HEAD_2 = "DMX_MOVING_HEAD_2"
    
    # Groups
    ALL = "ALL"
    ALL_DMX = "ALL_DMX"
    ALL_LED = "ALL_LED"


    