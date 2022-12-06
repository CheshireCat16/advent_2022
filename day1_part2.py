import heapq

# Open the input file
f = open("input.txt", "r")

# Variable to hold highest totals
max_totals = []

# Variable to hold current total
cur_total = 0

# Read in file contents, keeping track of current total and resetting at each blank line
for line in f:
    if line == "\n":
        if len(max_totals) < 3:
            heapq.heappush(max_totals, cur_total)
        elif cur_total > max_totals[0]:
            heapq.heappop(max_totals)
            heapq.heappush(max_totals, cur_total)
        cur_total = 0
    else:
        cur_total = cur_total + int(line)

# Check the last line
if cur_total > max_totals[0]:
        heapq.heappop(max_totals)
        heapq.heappush(max_totals, cur_total)

top_three = sum(max_totals)

print(max_totals)
print(top_three)

# Close the file
f.close()
