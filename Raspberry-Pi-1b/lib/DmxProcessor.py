from lib.DmxController import dmx_controller, DmxFixtureType
from lib.Effects import Effect
from lib.Kasten import KASTEN
from lib.Colors import *
import time
import threading
import random

class DmxProcessor:
    """Processes DMX commands and controls DMX fixtures"""
    
    def __init__(self):
        self.controller = dmx_controller
        self.active_effects = {}  # Track active effects per fixture
        self.effect_threads = {}  # Track running effect threads
        
    def initialize(self):
        """Initialize the DMX processor"""
        return self.controller.initialize()
        
    def start(self):
        """Start the DMX processor"""
        return self.controller.start()
        
    def stop(self):
        """Stop the DMX processor"""
        self.controller.stop()
        
    def process_command(self, command: str, bpm: int = 120):
        """Process a DMX command string"""
        try:
            # Parse command format: "DMX_EFFECT-DEVICE-COLOR-INTENSITY-STROBE_SPEED-DURATION"
            parts = command.split("-")
            if len(parts) < 3:
                print(f"⚠️ Invalid DMX command format: {command}")
                return
                
            effect_name = parts[0]
            device_name = parts[1]
            color_str = parts[2]
            intensity = int(parts[3]) if len(parts) > 3 else 255
            strobe_speed = int(parts[4]) if len(parts) > 4 else 0
            duration = int(parts[5]) if len(parts) > 5 else 0
            
            # Convert string to enum
            try:
                effect = Effect(effect_name)
                device = KASTEN(device_name)
            except ValueError as e:
                print(f"⚠️ Invalid effect or device: {e}")
                return
                
            # Execute the effect
            self._execute_effect(effect, device, color_str, intensity, strobe_speed, duration, bpm)
            
        except Exception as e:
            print(f"⚠️ Error processing DMX command: {e}")
            
    def _execute_effect(self, effect: Effect, device: KASTEN, color_str: str, 
                       intensity: int, strobe_speed: int, duration: int, bpm: int):
        """Execute a specific DMX effect"""
        
        # Stop any running effect for this device
        self._stop_effect(device)
        
        # Parse color
        color = self._parse_color(color_str)
        
        # Execute effect based on type
        if effect == Effect.DMX_DIMMER:
            self._effect_dimmer(device, intensity)
            
        elif effect == Effect.DMX_STROBE:
            self._effect_strobe(device, strobe_speed, duration)
            
        elif effect == Effect.DMX_BLACKOUT:
            self._effect_blackout(device)
            
        elif effect == Effect.DMX_COLOR:
            self._effect_color(device, color, intensity)
            
        elif effect == Effect.DMX_FADE_UP:
            self._effect_fade_up(device, color, duration if duration > 0 else 2000)
            
        elif effect == Effect.DMX_FADE_DOWN:
            self._effect_fade_down(device, duration if duration > 0 else 2000)
            
        elif effect == Effect.DMX_FLASH:
            self._effect_flash(device, color, bpm, duration)
            
        elif effect == Effect.DMX_PULSE:
            self._effect_pulse(device, color, bpm, duration)
            
        elif effect == Effect.DMX_CHASE:
            self._effect_chase(device, color, bpm, duration)
            
        else:
            print(f"⚠️ Unknown DMX effect: {effect}")
            
    def _stop_effect(self, device: KASTEN):
        """Stop any running effect for a device"""
        if device in self.effect_threads:
            self.effect_threads[device] = False  # Signal thread to stop
            
    def _parse_color(self, color_str: str) -> tuple:
        """Parse color string to RGB tuple"""
        if color_str.startswith("rgb(") and color_str.endswith(")"):
            rgb_str = color_str[4:-1]
            r, g, b = map(int, rgb_str.split(", "))
            return (r, g, b)
        return (0, 0, 0)
        
    # DMX Effect implementations
    
    def _effect_dimmer(self, device: KASTEN, intensity: int):
        """Set dimmer level"""
        self.controller.set_fixture_dimmer(device, intensity)
        print(f"🔆 DMX Dimmer: {device.value} -> {intensity}")
        
    def _effect_strobe(self, device: KASTEN, strobe_speed: int, duration: int):
        """Strobe effect"""
        self.controller.set_strobe(device, strobe_speed)
        
        if duration > 0:
            def stop_strobe():
                time.sleep(duration / 1000.0)
                if self.effect_threads.get(device, True):  # Check if not cancelled
                    self.controller.set_strobe(device, 0)
                    
            thread = threading.Thread(target=stop_strobe, daemon=True)
            self.effect_threads[device] = True
            thread.start()
            
        print(f"⚡ DMX Strobe: {device.value} -> {strobe_speed}")
        
    def _effect_blackout(self, device: KASTEN):
        """Blackout fixture"""
        self.controller.blackout_fixture(device)
        print(f"⚫ DMX Blackout: {device.value}")
        
    def _effect_color(self, device: KASTEN, color: tuple, intensity: int):
        """Set static color"""
        self.controller.set_fixture_color(device, color, intensity)
        print(f"🎨 DMX Color: {device.value} -> {color} @ {intensity}")
        
    def _effect_fade_up(self, device: KASTEN, color: tuple, duration: int):
        """Fade up effect"""
        def fade_up():
            steps = 50
            step_time = duration / 1000.0 / steps
            self.effect_threads[device] = True
            
            for i in range(steps + 1):
                if not self.effect_threads.get(device, False):
                    break
                    
                intensity = int((i / steps) * 255)
                self.controller.set_fixture_color(device, color, intensity)
                time.sleep(step_time)
                
        thread = threading.Thread(target=fade_up, daemon=True)
        thread.start()
        print(f"📈 DMX Fade Up: {device.value} -> {color} ({duration}ms)")
        
    def _effect_fade_down(self, device: KASTEN, duration: int):
        """Fade down effect"""
        def fade_down():
            steps = 50
            step_time = duration / 1000.0 / steps
            self.effect_threads[device] = True
            
            for i in range(steps + 1):
                if not self.effect_threads.get(device, False):
                    break
                    
                intensity = int(((steps - i) / steps) * 255)
                self.controller.set_fixture_dimmer(device, intensity)
                time.sleep(step_time)
                
        thread = threading.Thread(target=fade_down, daemon=True)
        thread.start()
        print(f"📉 DMX Fade Down: {device.value} ({duration}ms)")
        
    def _effect_flash(self, device: KASTEN, color: tuple, bpm: int, duration: int):
        """Flash effect synchronized to BPM"""
        def flash():
            flash_interval = 60.0 / bpm  # Convert BPM to seconds per beat
            end_time = time.time() + (duration / 1000.0) if duration > 0 else float('inf')
            self.effect_threads[device] = True
            
            while time.time() < end_time and self.effect_threads.get(device, False):
                # Flash on
                self.controller.set_fixture_color(device, color, 255)
                time.sleep(0.1)  # 100ms flash
                
                # Flash off
                self.controller.blackout_fixture(device)
                time.sleep(flash_interval - 0.1)
                
        thread = threading.Thread(target=flash, daemon=True)
        thread.start()
        print(f"💥 DMX Flash: {device.value} -> {color} @ {bpm} BPM")
        
    def _effect_pulse(self, device: KASTEN, color: tuple, bpm: int, duration: int):
        """Pulse effect synchronized to BPM"""
        def pulse():
            pulse_interval = 60.0 / bpm
            end_time = time.time() + (duration / 1000.0) if duration > 0 else float('inf')
            self.effect_threads[device] = True
            
            while time.time() < end_time and self.effect_threads.get(device, False):
                # Pulse up
                for i in range(26):  # 0-255 in 25 steps
                    if not self.effect_threads.get(device, False):
                        break
                    intensity = i * 10
                    self.controller.set_fixture_color(device, color, intensity)
                    time.sleep(pulse_interval / 50)
                    
                # Pulse down
                for i in range(25, -1, -1):
                    if not self.effect_threads.get(device, False):
                        break
                    intensity = i * 10
                    self.controller.set_fixture_color(device, color, intensity)
                    time.sleep(pulse_interval / 50)
                    
        thread = threading.Thread(target=pulse, daemon=True)
        thread.start()
        print(f"🫧 DMX Pulse: {device.value} -> {color} @ {bpm} BPM")
        
    def _effect_chase(self, device: KASTEN, color: tuple, bpm: int, duration: int):
        """Chase effect for groups of fixtures"""
        # This would be implemented for groups of fixtures
        # For now, just apply color
        self._effect_color(device, color, 255)
        print(f"🏃 DMX Chase: {device.value} -> {color} @ {bpm} BPM")

# Global DMX processor instance
dmx_processor = DmxProcessor()