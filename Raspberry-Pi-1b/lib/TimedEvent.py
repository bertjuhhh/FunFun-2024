class TimedEvent:
    def __init__(self, start, end, effect, group, color = None):
        self.start = start
        self.end = end
        self.effect = effect
        self.group = group
        self.color = color
        self.hasStarted = False
        self.hasStopped = False
        
        
    def shouldStop(self, relativeCurrentTime, relativeStartTime):
        # 0 is infinite
        if (self.end == 0):
            return False
                
        shouldStop = self.end <= relativeCurrentTime - relativeStartTime
        if (shouldStop):
            self.hasStopped = True
        return shouldStop
    
    def shouldStart(self, relativeCurrentTime, relativeStartTime):
        print(f"Checking if event should start: {self.start} <= {relativeCurrentTime - relativeStartTime}")
        shouldStart = self.start <= relativeCurrentTime - relativeStartTime
        print(f"Should Start: {shouldStart} | Has Started: {self.hasStarted} | Has Stopped: {self.hasStopped}")
        
        if (shouldStart):
            self.hasStarted = True
        return shouldStart
        
    def isStarted(self):
        return self.hasStarted
    
    def isStopped(self):
        return self.hasStopped
    
    def formatCommand(self):
        return f"{self.effect} {self.group.value} {self.color}"