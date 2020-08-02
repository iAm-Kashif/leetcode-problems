class Logger:

    def __init__(self):
        self.dict = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        if message in self.dict:
            if timestamp >= self.dict[message] + 10:
                self.dict[message] = timestamp
                return True
            else:
                return False
        else:
            self.dict[message] = timestamp
            return True


obj = Logger()
print(obj.shouldPrintMessage(1, "foo"))  # True
print(obj.shouldPrintMessage(2, "bar"))  # True
print(obj.shouldPrintMessage(3, "foo"))  # False
print(obj.shouldPrintMessage(8, "bar"))  # False
print(obj.shouldPrintMessage(10, "foo"))  # False
print(obj.shouldPrintMessage(11, "foo"))  # True
