class Effect:
    def __init__(self, name, value, color = None):
        self.name = name
        self.callback = value
        
        # Incoming color is formatted as rgb(255, 255, 255), so convert it to a tuple
        self.color = tuple(map(int, color[4:-1].split(','))) if color else None
        
    def execute(self, ledstrip):
        self.callback(ledstrip, self.color)