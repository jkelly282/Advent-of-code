# Read the variables from the CSV
import csv



file = csv.reader(open("/Users/jkelly2/Documents/santa.csv"))

# Create the empty array to place the values into
chronal_array = []

# iterate over the file to place the values into the array
for row in file:
    chronal_array.append(row)

    # convert the values from a str to int

chronal_array = list(map(int, chronal_array))
running_total = 0
duplicates = []
# generate a cumulative total array
cumulative_total = []
solved = False
iteration = 0
while True:
  iteration += 1
  print(iteration)
  for i in chronal_array:
    running_total += i

    if running_total in set(cumulative_total):
        print(running_total)
        solved = True
        break
    else:
        cumulative_total.add(running_total)
  if solved:
      break
