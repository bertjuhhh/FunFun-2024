# DMX512 Hardware Setup Guide

## Required Hardware

### 1. DMX Interface for Raspberry Pi 1B
**Option A: USB to DMX Interface (Recommended)**
- **Enttec DMX USB Pro** (~€100) - Professional grade, very reliable
- **FTDI USB-DMX** (~€50) - Good budget option
- **Chinese USB-DMX interfaces** (~€20) - Basic functionality

**Option B: GPIO to RS485 Converter**
- **RS485 to TTL Module** (~€5-10)
- **MAX485 chip** with supporting components
- Requires manual wiring to Pi GPIO pins

### 2. DMX Cables and Connectors
- **DMX cables** with 3-pin or 5-pin XLR connectors
- **DMX terminator** (120Ω resistor) for the last device in chain
- **DMX splitter** (optional) for branching to multiple runs

### 3. DMX Lights (Examples)
- **PAR lights** (RGB or RGBW) - €30-100 each
- **LED wash lights** - €50-200 each  
- **Strobe lights** - €40-150 each
- **Moving head lights** - €100-500 each

## Wiring Setup

### Option A: USB DMX Interface
```
Raspberry Pi 1B
├── USB Port → USB-DMX Interface
│   └── DMX Output (XLR Male)
│       ├── DMX Light 1 (XLR Female → XLR Male)
│       ├── DMX Light 2 (XLR Female → XLR Male)
│       ├── DMX Light 3 (XLR Female → XLR Male)
│       └── DMX Light N → DMX Terminator (120Ω)
```

### Option B: GPIO RS485 Interface
```
Raspberry Pi GPIO → RS485 Module → DMX Lights
Pin 14 (TX)     → DI
Pin 15 (RX)     → RO  
5V              → VCC
GND             → GND
                → A (DMX+) → Pin 3 of XLR
                → B (DMX-) → Pin 2 of XLR
                            Pin 1 of XLR → GND
```

## DMX Address Configuration

Each DMX light needs a unique starting address:

### Default Configuration (as programmed):
- **DMX_PAR_1**: Channel 1-3 (RGB)
- **DMX_PAR_2**: Channel 4-6 (RGB)  
- **DMX_PAR_3**: Channel 7-9 (RGB)
- **DMX_PAR_4**: Channel 10-12 (RGB)
- **DMX_WASH_1**: Channel 15-19 (Dimmer, R, G, B, W)
- **DMX_WASH_2**: Channel 20-24 (Dimmer, R, G, B, W)
- **DMX_STROBE_1**: Channel 30-31 (Dimmer, Strobe)
- **DMX_STROBE_2**: Channel 32-33 (Dimmer, Strobe)
- **DMX_MOVING_HEAD_1**: Channel 40-47 (Pan, Tilt, Dimmer, R, G, B, Gobo, Strobe)
- **DMX_MOVING_HEAD_2**: Channel 48-55 (Pan, Tilt, Dimmer, R, G, B, Gobo, Strobe)

### Setting DMX Addresses on Lights:
1. Use the light's menu/display to set DMX address
2. Or use DIP switches (older lights)
3. Match the address to your configuration in `DmxController.py`

## Software Configuration

### 1. Update DMX Serial Port (if using USB interface):
Edit `Raspberry-Pi-1b/lib/DmxController.py`:
```python
dmx_controller = DmxController(serial_port='/dev/ttyUSB0')  # USB interface
# OR
dmx_controller = DmxController(serial_port='/dev/ttyAMA0')  # GPIO RS485
```

### 2. Install Required Dependencies:
```bash
pip install pyserial
```

### 3. Configure Light Fixtures:
Edit the `setup_default_fixtures()` method in `DmxController.py` to match your actual lights.

## Testing DMX Setup

### 1. Check USB Interface Detection:
```bash
lsusb  # Should show your DMX interface
ls /dev/tty*  # Should show /dev/ttyUSB0
```

### 2. Test DMX Output:
```python
# Run this in Python to test
from lib.DmxController import dmx_controller
from lib.Kasten import KASTEN

dmx_controller.initialize()
dmx_controller.start()

# Test red color on PAR 1
dmx_controller.set_fixture_color(KASTEN.DMX_PAR_1, (255, 0, 0), 255)
```

### 3. DMX Signal Verification:
- Use a DMX tester/analyzer to verify signal integrity
- Check for proper termination (120Ω resistor on last device)
- Verify cable integrity and connections

## Troubleshooting

### No DMX Output:
1. Check USB interface connection and drivers
2. Verify serial port permissions: `sudo usermod -a -G dialout $USER`
3. Check DMX cable connections and termination

### Lights Not Responding:
1. Verify DMX addresses match your configuration
2. Check light power and DMX mode settings
3. Test with a simple DMX controller first

### Performance Issues:
1. Monitor CPU usage during operation
2. Ensure stable power supply for all equipment
3. Keep DMX cable runs under 300m without repeaters

## Safety Notes

- Always power off lights before connecting DMX cables
- Use proper DMX cables (impedance-matched, shielded)
- Ground all equipment properly
- Consider using DMX opto-isolators for protection
- Test thoroughly before live events

## Cost Estimate

**Basic Setup (4 PAR lights + USB interface):**
- USB-DMX interface: €50
- 4x RGB PAR lights: €200
- DMX cables and terminator: €50
- **Total: ~€300**

**Advanced Setup (Mixed lights + professional interface):**
- Enttec DMX USB Pro: €100
- 4x PAR + 2x Wash + 2x Strobe + 1x Moving head: €800
- Professional DMX cables and distribution: €150
- **Total: ~€1050**