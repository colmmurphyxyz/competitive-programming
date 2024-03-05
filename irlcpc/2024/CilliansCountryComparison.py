c = int(input())
countries = {}
for i in range(c):
    country, number = input().split(" ")
    countries[int(number)] = country

h, w = input().split(" ")
h = int(h); w = int(w)
occurences = {}
for i in range(h):
    numbers = input().split(" ")
    for number in numbers:
        number = int(number)
        if number in occurences:
            occurences[number] += 1
        else:
            occurences[number] = 1
    pass
most_common_numbers = list(occurences.items())
most_common_numbers.sort(reverse=True, key=lambda x: x[1])
# print(most_common_numbers)
for i in range(3):
    print(countries[most_common_numbers[i][0]])
