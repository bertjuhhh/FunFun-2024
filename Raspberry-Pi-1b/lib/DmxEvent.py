from lib.TimedEvent import TimedEvent
from lib.Effects import Effect
from lib.Kasten import KASTEN

class DmxEvent(TimedEvent):
    """Extended TimedEvent class for DMX-specific effects with additional parameters"""
    
    def __init__(self, start, effect: Effect, group, color=None, intensity=255, strobe_speed=0, duration=0):
        super().__init__(start, effect, group, color)
        self.intensity = max(0, min(255, intensity))  # DMX intensity (0-255)
        self.strobe_speed = max(0, min(255, strobe_speed))  # Strobe speed (0-255)
        self.duration = duration  # Effect duration in milliseconds (0 = infinite)
        self.end = start + duration if duration > 0 else 0
        
    def formatCommand(self):
        """Format DMX command with additional parameters"""
        base_command = f"{self.effect.value}-{self.group.value}-{self.color}"
        return f"{base_command}-{self.intensity}-{self.strobe_speed}-{self.duration}"
        
    def is_dmx_effect(self) -> bool:
        """Check if this is a DMX effect"""
        return self.effect.value.startswith("DMX_")
        
    def get_dmx_parameters(self) -> dict:
        """Get DMX-specific parameters as dictionary"""
        return {
            'intensity': self.intensity,
            'strobe_speed': self.strobe_speed,
            'duration': self.duration,
            'color': self.color
        }

def addDmxToGroup(loop, start, effect: Effect, group, color=None, intensity=255, strobe_speed=0, duration=0):
    """Helper function to add DMX events to a group of fixtures"""
    for kast in group:
        loop.append(DmxEvent(
            start=start, 
            effect=effect, 
            group=kast, 
            color=color,
            intensity=intensity,
            strobe_speed=strobe_speed,
            duration=duration
        ))

def addDmxSingle(loop, start, effect: Effect, kast, color=None, intensity=255, strobe_speed=0, duration=0):
    """Helper function to add a single DMX event"""
    loop.append(DmxEvent(
        start=start, 
        effect=effect, 
        group=kast, 
        color=color,
        intensity=intensity,
        strobe_speed=strobe_speed,
        duration=duration
    ))