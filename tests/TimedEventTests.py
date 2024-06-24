import unittest

import sys
sys.path.append('..')
from lib.TimedEvent import TimedEvent


class Effect:
    def __init__(self, value):
        self.value = value

class Group:
    def __init__(self, value):
        self.value = value

class TimedEventTest(unittest.TestCase):
    def setUp(self):
        # Arrange
        self.start = 5
        self.end = 10
        self.effect = Effect("EFFECT")
        self.group = Group("GROUP")
        self.color = "COLOR"
        self.event = TimedEvent(self.start, self.end, self.effect, self.group, self.color)

    def test_shouldStop(self):
        # Arrange
        relativeCurrentTime_stop = 16
        relativeStartTime = 0
        self.event.end = 15

        # Act and Assert for stop
        result_stop = self.event.shouldStop(relativeCurrentTime_stop, relativeStartTime)
        self.assertTrue(result_stop)
        self.assertTrue(self.event.isStopped())
        
    def test_shouldStart(self):
        # Arrange
        relativeCurrentTime_start = 6
        relativeStartTime = 0
        self.event.start = 5

        # Act and Assert for start
        result_start = self.event.shouldStart(relativeCurrentTime_start, relativeStartTime)
        self.assertTrue(result_start)
        self.assertTrue(self.event.isStarted())
        
    def test_shouldNotStart(self):
        # Arrange
        relativeCurrentTime_notStart = 4
        relativeStartTime = 0
        self.event.start = 5

        # Act and Assert for not start
        result_notStart = self.event.shouldStart(relativeCurrentTime_notStart, relativeStartTime)
        self.assertFalse(result_notStart)
        self.assertFalse(self.event.isStarted())
        
    def test_shouldNotStop(self):
        # Arrange
        relativeCurrentTime_notStop = 9
        relativeStartTime = 0
        self.event.end = 15

        # Act and Assert for not stop
        result_notStop = self.event.shouldStop(relativeCurrentTime_notStop, relativeStartTime)
        self.assertFalse(result_notStop)
        self.assertFalse(self.event.isStopped())
        
    def test_shouldNotStopInfinite(self):
        # Arrange
        relativeCurrentTime_notStop = 9
        relativeStartTime = 0
        self.event.end = 0

        # Act and Assert for not stop
        result_notStop = self.event.shouldStop(relativeCurrentTime_notStop, relativeStartTime)
        self.assertFalse(result_notStop)
        self.assertFalse(self.event.isStopped())
        
    def test_formatCommand(self):
        # Act
        result = self.event.formatCommand()

        # Assert
        self.assertEqual(result, "EFFECT GROUP COLOR")

if __name__ == '__main__':
    unittest.main()
