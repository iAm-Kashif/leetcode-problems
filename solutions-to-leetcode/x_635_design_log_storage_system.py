"""
635. Design Log Storage System
https://leetcode.com/problems/design-log-storage-system/

_author:            Kashif Memon
_python_version:    3.7.2
"""


class LogSystem:

    def __init__(self):
        self.log = {}

    def put(self, id: int, timestamp: str) -> None:
        from datetime import datetime
        self.log[id] = datetime.strptime(timestamp, '%Y:%m:%d:%H:%M:%S')
        print("Added", self.log)

    def retrieve(self, s: str, e: str, gra: str) -> 'List[int]':
        from datetime import datetime
        s = datetime.strptime(s, '%Y:%m:%d:%H:%M:%S')
        e = datetime.strptime(e, '%Y:%m:%d:%H:%M:%S')
        out = []

        for key, val in self.log.items():
            if gra == "Year":
                if s.year <= val.year <= e.year:
                    out.append(key)
            elif gra == "Month":
                if s.year <= val.year <= e.year and s.month <= val.month <= e.month:
                    out.append(key)
            elif gra == "Day":
                if s.year <= val.year <= e.year and s.month <= val.month <= e.month and s.day <= val.day <= e.day:
                    out.append(key)
            elif gra == "Hour":
                if s.year <= val.year <= e.year and s.month <= val.month <= e.month and s.day <= val.day <= e.day and s.hour <= val.hour <= e.hour:
                    out.append(key)
            elif gra == "Minute":
                if s.year <= val.year <= e.year and s.month <= val.month <= e.month and s.day <= val.day <= e.day and s.hour <= val.hour <= e.hour and s.minute <= val.minute <= e.minute:
                    out.append(key)
            elif gra == "Second":
                if s.year <= val.year <= e.year and s.month <= val.month <= e.month and s.day <= val.day <= e.day and s.hour <= val.hour <= e.hour and s.minute <= val.minute <= e.minute and s.second <= val.second <= e.second:
                    out.append(key)
        return out


def main():
    obj = LogSystem()
    obj.put(1, "2017:01:01:23:59:59")
    obj.put(2, "2017:01:02:23:59:59")
    # obj.put(3, "2016:01:01:00:00:00")
    # print(obj.retrieve("2016:01:01:01:01:01", "2017:01:01:23:00:00", "Year"))
    # print(obj.retrieve("2016:01:01:01:01:01", "2017:01:01:23:00:00", "Hour"))
    print(obj.retrieve("2017:01:01:23:59:58", "2017:01:02:23:59:58", "Second"))

if __name__ == "__main__":
    main()
