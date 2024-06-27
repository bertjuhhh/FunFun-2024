class Effect:
    def __init__(self, name, color = None):
        self.name = name
        
        # Incoming color is formatted as rgb(255, 255, 255), so convert it to a tuple
        self.color = tuple(map(int, color[4:-1].split(','))) if color else None