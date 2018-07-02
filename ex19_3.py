def stringCombiner(str1, str2):
    print(f"{str1} and {str2} combine to form...{str1}{str2}!")

first = "Nick"
last = "Cummings"

stringCombiner(first, last)
stringCombiner(last, first)
stringCombiner(first, first)
stringCombiner(last, last)
stringCombiner("Nick", last)
stringCombiner("Nick", "Cummings")
stringCombiner(first + first, last + last)
stringCombiner(len(first), len(last))
stringCombiner(len(first + last), first + " " + last)
