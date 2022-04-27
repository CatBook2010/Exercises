import time

class Time:
    def __init__(self, hour, minute, second):
        self.__hour = int(hour)
        self.__minute = int(minute)
        self.__second = int(second)
    
    def getHour(self):
        return self.__hour
    
    def getMinute(self):
        return self.__minute
    
    def getSecond(self):
        return self.__second
    
    def setTime(self, elapseTime):
        self.__second = elapseTime % 3600
        self.__minute = (elapseTime - self.getSecond()) % 60
        self.__hour = (elapseTime - self.getHour() - self.getMinute()) % 60