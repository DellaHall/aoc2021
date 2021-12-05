# Advent of Code 2021 Day 1

# Import dataset
dataset = []
with open("aoc01data.txt") as f:
  for line in (f.readlines()):
    dataset.append(int(line))

# Part 1
# For thru the list, collect instances where number increases
# Could do this while doing the import, but not gonna bother
increases = 0
for i in range(len(dataset)):
  # Handle the first value with nothing to compare to
  try:
    j_value = dataset[i - 1]
  except IndexError:
    j_value = dataset[i]
  if dataset[i] > j_value:
    increases +=1
# Part 1 answer = 1184
print("Part 1:", str(increases))

# Part 2
# Count how often the 3-measurement window increases
increases = 0
for i in range(len(dataset)):
  # If there aren't at least 4 values to compare, we don't care
  if i - 3 < 0:
    continue
  first_set = dataset[i - 3] + dataset[i - 2] + dataset[i - 1]
  second_set = dataset[i - 2] + dataset[i - 1] + dataset[i]
  if second_set > first_set:
    increases +=1
# Part 2 answer = 1158
print("Part 2:", str(increases))