"""
This tool is used to create a number of directories, each of which correspond to an index.
This index represents a hex for the hex map of the region in which my Dungeons and Dragons campaign is set.
"""

import os
import string

workingDir = "C:\\Users\\Blue\\Dropbox\\D&D\\Ashor Wildlands"
alphabetRange = ["A", "AZ"]
numericRange = [1, 10]

# print(os.listdir(workingDir))
# os.makedirs(os.path.join(workingDir, "Test"))
# os.rmdir(os.path.join(workingDir, "Test"))

alphabetUsed = string.ascii_uppercase
# Options for upper or lowercase only, or both,
# using string.ascii_uppercase, string.ascii_lowercase, or string.ascii_letters respectively
alphabetListToUse = []
alphabetStartIndex = alphabetUsed.index(str(alphabetRange[0]))

if len(alphabetRange[1]) > 1:
    for i in range(len(alphabetRange[1])):
        if i == 0:
            for j in range(alphabetStartIndex, len(alphabetUsed) ):
                alphabetListToUse.append(str(alphabetUsed[i] + alphabetUsed[j]))

        elif i < len(alphabetRange[1]):
            for j in range(0, len(alphabetUsed)):
                alphabetListToUse.append(str(alphabetUsed[i] + alphabetUsed[j]))

        else:
            for j in range(0, alphabetUsed.index(str(alphabetRange[1][len(alphabetRange[1])])) ):
                alphabetListToUse.append(str(alphabetUsed[i] + alphabetUsed[j]))


else:
    alphabetEndIndex = alphabetUsed.index(str(alphabetRange[1])) + 1
    for i in range(alphabetStartIndex, alphabetEndIndex):
        alphabetListToUse.append(str(alphabetUsed[i]))

print(alphabetListToUse)

numericListToUse = [str(i).zfill(len(str(numericRange[1]))) for i in range(numericRange[0], numericRange[1] + 1)]


print(numericListToUse)
"""
for letter in alphabetListToUse:
    for number in numericListToUse:
        os.mkdir(os.path.join(workingDir, letter + number))
"""
