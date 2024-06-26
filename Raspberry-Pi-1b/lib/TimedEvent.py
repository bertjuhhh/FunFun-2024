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
        
        if (self.hasStopped):
            return False
        
        shouldStop = self.end <= relativeCurrentTime - relativeStartTime
        
        if shouldStop:
            self.hasStopped = True
        
        return shouldStop
    
    def shouldStart(self, relativeCurrentTime, relativeStartTime):
        if (self.hasStarted):
            return False
        
        shouldStart = self.start <= relativeCurrentTime - relativeStartTime

        if shouldStart:
            self.hasStarted = True

        return shouldStart
        
    def isStarted(self):
        return self.hasStarted
    
    def isStopped(self):
        return self.hasStopped
    
    def formatCommand(self):
        return f"{self.effect.value}_{self.group.value}_{self.color}"