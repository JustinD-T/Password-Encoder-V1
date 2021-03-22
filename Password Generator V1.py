# Collect Service Name - Make Case-Unsensitive
# Collect Foudning of the Service Company Year
# Isolate each letter of string into list
# Reduce each list letter into numbers using for/list, put corresponding num into new list
# Use for/list to multiply each numeber in the num list by the founding service company year - compile into new list
# run each num in list through a re-simplfier

# Collecting service name and founding year, making case unsensitive, and removing spaces in CompName.
print("Hey, welcome to my passoword generator!")
CompName = input("Please enter the name of the company you are registering for.   ")
YearNum = int(input("Please enter the year that this service was made/founded.   "))
CompName = str.lower(CompName)
CompName = CompName.replace(" ", "")
# Isolating each letter of CompName into list, then compiling their num equvalents to NumList
LtrList = list(CompName)
CypherDict = {'a': 1, 'c': 3, 'b': 2, 'e': 5, 'd': 4, 'g': 7, 'f': 6, 'i': 9, 'h': 8, 'k': 11, 'j': 10, 'm': 13, 'l': 12, 'o': 15, 'n': 14, 'q': 17, 'p': 16, 's': 19, 'r': 18, 'u': 21, 't': 20, 'w': 23, 'v': 22, 'y': 25, 'x': 24, 'z': 26}
CypherDictReverse = {1: 'a', 3: 'c', 2: 'b', 5: 'e', 4: 'd', 7: 'g', 6: 'f', 9: 'i', 8: 'h', 11: 'k', 10: 'j', 13: 'm', 12: 'l', 15: 'o', 14: 'n', 17: 'q', 16: 'p', 19: 's', 18: 'r', 21: 'u', 20: 't', 23: 'w', 22: 'v', 25: 'y', 24: 'x', 26: 'z'}
NumList = []
for TempLtr in LtrList:
    TempNum = CypherDict[TempLtr]
    NumList.append(TempNum)
# Multiplying NumList by YearNum and compiling into MultiNumList
MultipliedNumList = []
for TempMultiNum in NumList:
    MultipliedNumList.append(TempMultiNum * int(YearNum))
# Resimplfying the MultipliedNumList into Numbers
# Take first 2 digits of num, check if under 27, if not divide by 2 until it is, then remove decimal.
StrMultipliedNumList = []
First2MultiNumList = []
PreUncypherNumList = []
for TempMultiNumStr in MultipliedNumList:
    StrMultipliedNumList.append(str(TempMultiNumStr))
for TempNum in StrMultipliedNumList:
    First2MultiNumList.append(TempNum[0:2])
for TempNum in First2MultiNumList:
    if int(TempNum) <= 26:
        PreUncypherNumList.append(TempNum)
    elif int(TempNum) > 26:
        while True:
            TempNum = float(TempNum) / 2
            if float(TempNum) <= 26:
                PreUncypherNumList.append(int(TempNum))
                break
# Takes the simplified muntiplied numbers and runs it through a dict to get the letter corresponding numbers for each value.
FinalLtrList = []
for TempNum in PreUncypherNumList:
    TempLtr = CypherDictReverse[int(TempNum)]
    FinalLtrList.append(TempLtr)
# Appends a number, capital, and special charecter to the password.
FinalLtrList.append("57")
FinalLtrList.append("DT")
FinalLtrList.append("_")
FinalStr = ""
# Appends the encrypted list of letters into a single string
for TempLtr in FinalLtrList:
    FinalStr = FinalStr + TempLtr
# Prints final string
print("This is your password:   " + FinalStr)
ShellStall = input("Press enter to exit:   ")