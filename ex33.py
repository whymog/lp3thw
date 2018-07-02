from sys import argv

script, loopCount, incrementAmount = argv

def numberLoop(limit, increment):
    i = 0
    numbers = []
    
    for i in range(0, limit, increment):
        print(f"At the top i is {i}")
        numbers.append(i)

        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")
    
    
    print("The numbers: ")
    
    for num in numbers:
        print(num)

numberLoop(int(loopCount), int(incrementAmount))
