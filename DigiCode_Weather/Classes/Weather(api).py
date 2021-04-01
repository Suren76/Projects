class Weather:
    def __init__(self, humidity, temp):
        self.__humidity = humidity
        self.__temp = temp

    def get_weather(self):
        return self.__temp, self.__humidity
