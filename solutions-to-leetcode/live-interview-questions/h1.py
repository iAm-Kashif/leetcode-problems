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
    phoneMap = {}
    differentNamesWithSamePhonenumber = {}
    differentPhonenumberWithSameName = {}

    def analyze(self, log: 'List[str]') -> str:

        for item in log:
            item = item.split(", ")
            log_name = item[0]
            log_phone = item[1]

            # when name is already there in the phoneMap
            numInPhoneMapforName = self.valInPhoneMap(log_name)
            if not numInPhoneMapforName == "-1":
                # name is in the phoneMap, so number is being updated
                # remove name from PhoneMap with link from old number
                # Add new number with the name in PhoneMap will be done down in the else.
                self.phoneMap[numInPhoneMapforName].remove(log_name)

                # As number got updated, add to differentNamesWithSamePhoneNumber for old PhoneNumber
                # Need to check if Phonenumber already exists in differentNamesWithSamePhonenumber
                # if Yes, append name
                # else add a new entry
                if numInPhoneMapforName in self.differentNamesWithSamePhonenumber.keys():
                    self.differentNamesWithSamePhonenumber[numInPhoneMapforName].append(log_name)
                else:
                    self.differentNamesWithSamePhonenumber[numInPhoneMapforName] = [log_name]

                # As same name is encountered, we need to track the same name for different numbers too.
                # Add to differentPhonenumberWithSameName
                if log_name in self.differentNamesWithSamePhonenumber.keys():
                    self.differentPhonenumberWithSameName[log_name].append(numInPhoneMapforName)
                else:
                    self.differentPhonenumberWithSameName[log_name] = log_phone


            if log_phone in self.phoneMap.keys():
                # if phoneNumber is already in the phoneMap
                # Update the phoneNumber to have multiple names
                self.phoneMap[log_phone].append(log_name)
            else:
                # phoneNumber is the first of its kind.
                self.phoneMap[log_phone] = [log_name]

        print(">>Map", self.phoneMap)
        print(">>Same#", self.differentNamesWithSamePhonenumber)
        print(">>SameName", self.differentPhonenumberWithSameName)


    # Returns the key (phoneNumber) if the Name is in the [] of any key.
    def valInPhoneMap(self, isSameName: str) -> str:
        for key, v in self.phoneMap.items():
            for x in v:
                if x == isSameName:
                    return key
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


if __name__ == "__main__":
    main()
