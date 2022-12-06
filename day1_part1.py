
# Open the input file
f = open("input.txt", "r")

# Variable to hold highest total
max_total = -1

# Variable to hold current total
cur_total = 0

# Read in file contents, keeping track of current total and resetting at each blank line
for line in f:
    if line == "\n":
        if cur_total > max_total:
            max_total = cur_total
        cur_total = 0
    else:
        cur_total = cur_total + int(line)

# Check the last line
if cur_total > max_total:
    max_total = cur_total

print(max_total)

# Close the file
f.close()
