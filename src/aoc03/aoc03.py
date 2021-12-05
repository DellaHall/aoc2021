# Advent of Code 2021 Day 3

# Import dataset
dataset = []
with open("aoc03data.txt") as f:
  for line in (f.readlines()):
    dataset.append(line.strip("\n"))

# Part 1
# Gamma = most common bit in each position
# Epsilon = lest common bit
bit_length = len(dataset[0])
zeroes = [0] * bit_length
ones = [0] * bit_length

for data_point in dataset:
  for index, value in enumerate(data_point):
    if value == "0":
      zeroes[index] += 1
    else:
      ones[index] +=1

gamma = ""
epsilon = ""
for index, value in enumerate(zeroes):
  if value > ones[index]:
    gamma += "0"
    epsilon += "1"
  else:
    gamma += "1"
    epsilon += "0"
dec_gamma = int(gamma, 2)
dec_epsilon = int(epsilon, 2)

print(dec_gamma * dec_epsilon)

# Part 2
oxygen = dataset
i = 0
while len(oxygen) > 1:
  oxygen_b = []
  zero = 0
  one = 0
  for data_point in oxygen:
    if data_point[i] == "0":
      zero += 1
    else:
      one += 1
  check_number = "0"
  if one >= zero:
    check_number = "1"
  for data_point in oxygen:
    if data_point[i] == check_number:
      oxygen_b.append(data_point)
  oxygen = oxygen_b
  i += 1


co2 = dataset
i = 0
while len(co2) > 1:
  co2_b = []
  zero = 0
  one = 0
  for data_point in co2:
    if data_point[i] == "0":
      zero += 1
    else:
      one += 1
  check_number = "0"
  if one < zero:
    check_number = "1"
  for data_point in co2:
    if data_point[i] == check_number:
      co2_b.append(data_point)
  co2 = co2_b
  i += 1

dec_oxygen = int(oxygen[0], 2)
dec_co2 = int(co2[0], 2)

print(dec_oxygen * dec_co2)