class SensorConnectionError(Exception):
    def __init__(self, message):
        super().__init__(message)
#        self.errors = errors
