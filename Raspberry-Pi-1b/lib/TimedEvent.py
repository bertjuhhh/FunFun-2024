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
        return shouldStop
    
    def shouldStart(self, relativeCurrentTime, relativeStartTime):
        shouldStart = self.start <= relativeCurrentTime - relativeStartTime

        return shouldStart
        
    def isStarted(self):
        return self.hasStarted
    
    def isStopped(self):
        return self.hasStopped
    
    def formatCommand(self):
        return f"{self.effect} {self.group.value} {self.color}"

    def markStarted(self):
        self.hasStarted = True

    def markStopped(self):
        self.haStopped = True