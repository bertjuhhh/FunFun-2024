class TimedEvent:
    def __init__(self, start, effect, group, color = None):
        self.start = start
        self.effect = effect
        self.group = group
        self.color = color
        self.hasStarted = False
        self.hasStopped = False
        
        if self.color == None:
            self.color = (0, 0, 0)
        
        
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
        # make sure the event starts 200ms before the actual start time because of the delay in the DMX signal
        shouldStart = self.start <= relativeCurrentTime + 1500 - relativeStartTime

        if shouldStart:
            self.hasStarted = True

        return shouldStart
        
    def isStarted(self):
        return self.hasStarted
    
    def isStopped(self):
        return self.hasStopped
    
    def formatCommand(self):
        return f"{self.effect.value}-{self.group.value}-{self.color}"