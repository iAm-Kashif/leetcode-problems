"""
Read input from STDIN, Print output to STDOUT
Analyze a log file
Question: You are given log entries that indicate a user setting a new phone number.
Each user can have at most one associated phone number, so setting a new number abandons the previous one.
There is no explicit requirement that only one user may use a phone number, however, each phone number can have multiple
users linked to it.
Using these logs, find the users that use the same phone number at the same time.
Format of log [username, phone#, timestamp] ex. Sam,980-869-4998, 0
Output: Phone number: 980-869-4998 shared by [Jane, Sam]

_author:            Kashif Memon
_python_version:    3.7.2
"""


class Solution:
    phoneHashMap = {}
    common = {}

    def analyze(self, log: 'List[str]') -> str:

        for item in log:
            item = item.split(", ")
            # item[0] = name
            # item[1] = #

            # check if name is coming second time
            keyNum = self.valInHashMap(item[0])
            if not keyNum == "-1":
                self.phoneHashMap[keyNum].remove(item[0])
                if keyNum in self.common.keys():
                    self.common[keyNum].append(item[0])
                else:
                    self.common[keyNum] = [item[0]]

            # check if number is already in keys
            if item[1] in self.phoneHashMap.keys():
                self.phoneHashMap[item[1]].append(item[0])
            else:
                # number incoming first time
                self.phoneHashMap[item[1]] = [item[0]]
        print(self.phoneHashMap)
        print(self.common)

    def valInHashMap(self, val: str) -> str:
        for k, v in self.phoneHashMap.items():
            for x in v:
                if x == val:
                    return k
        return "-1"


def main():
    input1 = [
        "Sam, 980-869-4998, 0",
        "John, 984-978-9849, 15",
        "Jane, 980-869-4998, 45",
        "Sam, 894-894-9839, 100",
        "Jane, 889-898-6548, 103",
        "Joe, 980-869-4998, 117"
    ]
    print(Solution().analyze(log=input1))

    # name for first time = add to hashmap
    # name for second time = remove from hashmap, add to common
    # number for first time = add to hashmap
    # number for second time, update hashmap to multiple values


if __name__ == "__main__":
    main()
