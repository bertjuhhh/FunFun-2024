class Effect:
    def __init__(self, name, bpm, color = None):
        self.name = name
        self.bpm = int(bpm) if bpm else 0
        
        # Incoming color is formatted as rgb(255, 255, 255), so convert it to a tuple
        self.color = tuple(map(int, color[4:-1].split(','))) if color else (0, 0, 0)