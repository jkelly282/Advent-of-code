# Storing the letters of the alphabet into a variable
chars = "abcdefghijklmnopqrstuvwxyz"
# Open the text file not a generic name which python already uses
text_file = open("/Users/jkelly2/Documents/testcheck.txt", "r")
# intitialising the variables for how many repeats
two = 0
three = 0  # type: int

for i in range(0, 10000):
    string = text_file.readline()
    two_check = 0  # type: int
    three_check = 0
    for char in chars:
        count = string.count(char)
        if count > 1:

            if count == 2 and two_check == 0:
                two += 1
                two_check += 1
            elif count == 3 and three_check == 0:
                three += 1
                three_check += 1
checksum = two * three
print(checksum)
