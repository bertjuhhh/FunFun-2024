import serial
import time
import threading
from enum import Enum
from lib.Kasten import KASTEN

class DmxFixtureType(Enum):
    """DMX fixture types with their channel configurations"""
    PAR_RGB = "PAR_RGB"  # 3 channels: R, G, B
    PAR_RGBW = "PAR_RGBW"  # 4 channels: R, G, B, W
    WASH_RGBW_DIMMER = "WASH_RGBW_DIMMER"  # 5 channels: Dimmer, R, G, B, W
    STROBE = "STROBE"  # 2 channels: Dimmer, Strobe
    MOVING_HEAD_BASIC = "MOVING_HEAD_BASIC"  # 8 channels: Pan, Tilt, Dimmer, R, G, B, Gobo, Strobe

class DmxFixture:
    """Represents a single DMX fixture with its configuration"""
    def __init__(self, kasten_id: KASTEN, start_channel: int, fixture_type: DmxFixtureType):
        self.kasten_id = kasten_id
        self.start_channel = start_channel
        self.fixture_type = fixture_type
        self.current_values = [0] * self.get_channel_count()
        
    def get_channel_count(self) -> int:
        """Get number of channels for this fixture type"""
        channel_counts = {
            DmxFixtureType.PAR_RGB: 3,
            DmxFixtureType.PAR_RGBW: 4,
            DmxFixtureType.WASH_RGBW_DIMMER: 5,
            DmxFixtureType.STROBE: 2,
            DmxFixtureType.MOVING_HEAD_BASIC: 8
        }
        return channel_counts.get(self.fixture_type, 1)

class DmxController:
    """DMX512 controller using RS485 interface"""
    
    def __init__(self, serial_port='/dev/ttyUSB0', baudrate=250000):
        self.serial_port = serial_port
        self.baudrate = baudrate
        self.ser = None
        self.universe = [0] * 512  # DMX universe (512 channels)
        self.fixtures = {}
        self.running = False
        self.update_thread = None
        self.lock = threading.Lock()
        
        # Initialize default fixture configuration
        self.setup_default_fixtures()
        
    def setup_default_fixtures(self):
        """Setup default DMX fixture configuration"""
        self.fixtures = {
            KASTEN.DMX_PAR_1: DmxFixture(KASTEN.DMX_PAR_1, 1, DmxFixtureType.PAR_RGB),
            KASTEN.DMX_PAR_2: DmxFixture(KASTEN.DMX_PAR_2, 4, DmxFixtureType.PAR_RGB),
            KASTEN.DMX_PAR_3: DmxFixture(KASTEN.DMX_PAR_3, 7, DmxFixtureType.PAR_RGB),
            KASTEN.DMX_PAR_4: DmxFixture(KASTEN.DMX_PAR_4, 10, DmxFixtureType.PAR_RGB),
            KASTEN.DMX_WASH_1: DmxFixture(KASTEN.DMX_WASH_1, 15, DmxFixtureType.WASH_RGBW_DIMMER),
            KASTEN.DMX_WASH_2: DmxFixture(KASTEN.DMX_WASH_2, 20, DmxFixtureType.WASH_RGBW_DIMMER),
            KASTEN.DMX_STROBE_1: DmxFixture(KASTEN.DMX_STROBE_1, 30, DmxFixtureType.STROBE),
            KASTEN.DMX_STROBE_2: DmxFixture(KASTEN.DMX_STROBE_2, 32, DmxFixtureType.STROBE),
            KASTEN.DMX_MOVING_HEAD_1: DmxFixture(KASTEN.DMX_MOVING_HEAD_1, 40, DmxFixtureType.MOVING_HEAD_BASIC),
            KASTEN.DMX_MOVING_HEAD_2: DmxFixture(KASTEN.DMX_MOVING_HEAD_2, 48, DmxFixtureType.MOVING_HEAD_BASIC),
        }
        
    def initialize(self):
        """Initialize the DMX controller"""
        try:
            self.ser = serial.Serial(
                self.serial_port,
                self.baudrate,
                bytesize=serial.EIGHTBITS,
                parity=serial.PARITY_NONE,
                stopbits=serial.STOPBITS_TWO
            )
            print(f"✅ DMX Controller initialized on {self.serial_port}")
            return True
        except Exception as e:
            print(f"❌ Failed to initialize DMX controller: {e}")
            return False
            
    def start(self):
        """Start continuous DMX output"""
        if not self.ser:
            if not self.initialize():
                return False
                
        self.running = True
        self.update_thread = threading.Thread(target=self._update_loop, daemon=True)
        self.update_thread.start()
        print("🚀 DMX update loop started")
        return True
        
    def stop(self):
        """Stop DMX output"""
        self.running = False
        if self.update_thread:
            self.update_thread.join()
        if self.ser:
            self.ser.close()
        print("🛑 DMX controller stopped")
        
    def _update_loop(self):
        """Continuous DMX output loop (runs at ~44Hz)"""
        while self.running:
            try:
                with self.lock:
                    self._send_dmx_frame()
                time.sleep(0.023)  # ~44Hz refresh rate
            except Exception as e:
                print(f"⚠️ DMX update error: {e}")
                
    def _send_dmx_frame(self):
        """Send a complete DMX512 frame"""
        if not self.ser:
            return
            
        # DMX512 frame structure:
        # Break (88-1000µs low), Mark After Break (8-1000000µs high), Start Code (0x00), Data (512 bytes)
        
        frame = bytearray()
        frame.append(0x00)  # Start code
        frame.extend(self.universe[:512])  # 512 channels
        
        self.ser.write(frame)
        
    def set_fixture_color(self, kasten_id: KASTEN, color: tuple, intensity: int = 255):
        """Set color for a specific fixture"""
        if kasten_id not in self.fixtures:
            print(f"⚠️ Unknown DMX fixture: {kasten_id}")
            return
            
        fixture = self.fixtures[kasten_id]
        r, g, b = self._parse_color(color)
        
        with self.lock:
            if fixture.fixture_type == DmxFixtureType.PAR_RGB:
                self._set_channels(fixture.start_channel, [r, g, b])
            elif fixture.fixture_type == DmxFixtureType.PAR_RGBW:
                w = min(r, g, b)  # White channel as minimum of RGB
                self._set_channels(fixture.start_channel, [r, g, b, w])
            elif fixture.fixture_type == DmxFixtureType.WASH_RGBW_DIMMER:
                w = min(r, g, b)
                self._set_channels(fixture.start_channel, [intensity, r, g, b, w])
                
    def set_fixture_dimmer(self, kasten_id: KASTEN, intensity: int):
        """Set dimmer for a specific fixture"""
        if kasten_id not in self.fixtures:
            return
            
        fixture = self.fixtures[kasten_id]
        intensity = max(0, min(255, intensity))
        
        with self.lock:
            if fixture.fixture_type == DmxFixtureType.STROBE:
                self._set_channels(fixture.start_channel, [intensity, 0])  # Dimmer, no strobe
            elif fixture.fixture_type == DmxFixtureType.WASH_RGBW_DIMMER:
                self.universe[fixture.start_channel - 1] = intensity  # Channel 1 is dimmer
            elif fixture.fixture_type == DmxFixtureType.MOVING_HEAD_BASIC:
                self.universe[fixture.start_channel + 2 - 1] = intensity  # Channel 3 is dimmer
                
    def set_strobe(self, kasten_id: KASTEN, strobe_speed: int):
        """Set strobe speed for strobe fixtures"""
        if kasten_id not in self.fixtures:
            return
            
        fixture = self.fixtures[kasten_id]
        if fixture.fixture_type not in [DmxFixtureType.STROBE, DmxFixtureType.MOVING_HEAD_BASIC]:
            return
            
        strobe_speed = max(0, min(255, strobe_speed))
        
        with self.lock:
            if fixture.fixture_type == DmxFixtureType.STROBE:
                self.universe[fixture.start_channel] = strobe_speed  # Channel 2 is strobe
            elif fixture.fixture_type == DmxFixtureType.MOVING_HEAD_BASIC:
                self.universe[fixture.start_channel + 7 - 1] = strobe_speed  # Channel 8 is strobe
                
    def blackout_fixture(self, kasten_id: KASTEN):
        """Turn off a specific fixture"""
        if kasten_id not in self.fixtures:
            return
            
        fixture = self.fixtures[kasten_id]
        
        with self.lock:
            for i in range(fixture.get_channel_count()):
                self.universe[fixture.start_channel + i - 1] = 0
                
    def blackout_all(self):
        """Turn off all DMX fixtures"""
        with self.lock:
            self.universe = [0] * 512
            
    def _set_channels(self, start_channel: int, values: list):
        """Set multiple DMX channels starting from start_channel"""
        for i, value in enumerate(values):
            channel_index = start_channel + i - 1  # DMX channels are 1-based
            if 0 <= channel_index < 512:
                self.universe[channel_index] = max(0, min(255, value))
                
    def _parse_color(self, color) -> tuple:
        """Parse color string or tuple to RGB values"""
        if isinstance(color, str):
            if color.startswith("rgb(") and color.endswith(")"):
                # Parse "rgb(255, 0, 0)" format
                rgb_str = color[4:-1]
                r, g, b = map(int, rgb_str.split(", "))
                return (r, g, b)
        elif isinstance(color, (tuple, list)) and len(color) >= 3:
            return (int(color[0]), int(color[1]), int(color[2]))
            
        # Default to off
        return (0, 0, 0)

# Global DMX controller instance
dmx_controller = DmxController()