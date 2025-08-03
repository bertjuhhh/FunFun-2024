from lib.Kasten import KASTEN

# LED strips buiten
windroos = [KASTEN.LEDKAST_3, KASTEN.LEDKAST_4]
cartografen = [KASTEN.LEDKAST_1]
zeelui = [KASTEN.LEDKAST_2]

# DMX light groups
dmx_pars = [KASTEN.DMX_PAR_1, KASTEN.DMX_PAR_2, KASTEN.DMX_PAR_3, KASTEN.DMX_PAR_4]
dmx_wash = [KASTEN.DMX_WASH_1, KASTEN.DMX_WASH_2]
dmx_strobes = [KASTEN.DMX_STROBE_1, KASTEN.DMX_STROBE_2]
dmx_moving_heads = [KASTEN.DMX_MOVING_HEAD_1, KASTEN.DMX_MOVING_HEAD_2]

# Combined groups
all_dmx_lights = dmx_pars + dmx_wash + dmx_strobes + dmx_moving_heads
all_led_strips = windroos + cartografen + zeelui