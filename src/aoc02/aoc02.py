# Advent of Code 2021 Day 2

# Import dataset
dataset = []
with open("aoc02data.txt") as f:
  for line in (f.readlines()):
    split_line = line.split(" ")
    dataset.append((split_line[0], int(split_line[1])))

# Part 1
pos = [0, 0]
for command, value in dataset:
  if command.lower() == "forward":
    pos[0] += value
  if command.lower() == "up":
    pos[1] -= value
  if command.lower() == "down":
    pos[1] += value

# The solution is x * y
print("Part 1:", str(pos[0] * pos[1]))

# Part 2
# horizontal, depth, aim
pos = [0, 0, 0]
for command, value in dataset:
  if command.lower() == "forward":
    pos[0] += value
    pos[1] += pos[2] * value
  if command.lower() == "up":
    pos[2] -= value
  if command.lower() == "down":
    pos[2] += value

# The solution is x * y
print("Part 2:", str(pos[0] * pos[1]))
