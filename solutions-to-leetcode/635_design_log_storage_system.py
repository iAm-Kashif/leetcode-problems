"""
635. Design Log Storage System
https://leetcode.com/problems/design-log-storage-system/

_author:            Kashif Memon
_python_version:    3.7.2
"""


class LogSystem:

    def __init__(self):
        self.logs = []

    def put(self, id: int, timestamp: str) -> None:
        self.logs.append((id, timestamp))

    def retrieve(self, s: str, e: str, gra: str) -> 'List[int]':
        index = {"Year": 5, "Month": 8, "Day": 11,
                 "Hour": 14, "Minute": 17, "Second": 20}[gra]

        start = s[:index]
        end = e[:index]
        for id, timestamp in self.logs:
            print(id, start, timestamp, end)
            print(start <= timestamp <= end)

        return sorted(tid for tid, timestamp in self.logs
                      if start <= timestamp <= end)


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
