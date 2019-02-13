# Read the variables from the CSV
import csv

file = csv.reader(open('santa.csv'))

# Create the empty array to place the values into
chronal_array = []

# iterate over the file to place the values into the array
for row in file:
    chronal_array += row

# convert the values from a str to int

chronal_array = map(int, chronal_array)

# print the results

print(sum(chronal_array))