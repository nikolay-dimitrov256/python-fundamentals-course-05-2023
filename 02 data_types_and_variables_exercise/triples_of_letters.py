number = int(input())

for ch1 in range(number):
    for ch2 in range(number):
        for ch3 in  range(number):
            triple_of_letters = chr(97 + ch1) + chr(97 + ch2) + chr(97 + ch3)
            print(triple_of_letters)
