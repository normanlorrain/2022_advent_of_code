import string

test="""vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""

letters = string.ascii_letters # 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', which is convenient.

sumPriorities = 0
f = test.splitlines()
f = open("day3.txt")
for i in f:
    half = int(len(i)/2)
    firstcompartment = i[:half]
    secondcompartment = i[half:]
    for letter in firstcompartment:
        if letter in secondcompartment: # only supposed to happen once
            priority  = letters.index(letter) + 1 # Find the letter in the list, 0 index so add 1
            sumPriorities+=priority 
            break

print(sumPriorities)


# Part Two
sumPriorities = 0
f = iter(test.splitlines())
f = open("day3.txt")

while True:
    first = next(f,None)
    if first == None:
        break
    second = next(f)
    third = next(f)

    for letter in first:
        if letter in second and letter in third:
            priority  = letters.index(letter) + 1 # Find the letter in the list, 0 index so add 1
            sumPriorities+=priority
            break
print(sumPriorities)