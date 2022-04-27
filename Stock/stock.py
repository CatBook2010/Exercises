class Stock:
    def __init__(self, symbol:str, name:str, previousClosingPrice:float, currentPrice:float) -> None:
        self.__symbol = symbol
        self.__name = name
        self.__previousClosingPrice = previousClosingPrice
        self.__currentPrice = currentPrice
    
    def getSymbol(self):
        return self.__symbol
    
    def getName(self):
        return self.__name
    
    def getPreviousClosingPrice(self):
        return self.__previousClosingPrice
    
    def getCurrentPrice(self):
        return self.__currentPrice

    def setPreviousPrice(self, newPreviousClosingPrice):
        self.__previousClosingPrice = newPreviousClosingPrice
    
    def setCurrentPrice(self, newCurrentPrice):
        self.__currentPrice = newCurrentPrice
    
    def getChangePercent(self):
        return (self.__currentPrice - self.__previousClosingPrice) / self.__previousClosingPrice * 100