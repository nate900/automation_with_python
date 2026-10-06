import sys
if len(sys.argv) > 1:
    numbers = sys.argv[1:]
    try:
        total = 0
        for num in numbers:
            total = total + int(num)
        print(total)
    except Exception as e:
        print("please enter a number or don't use this program!")
else:
    print('Think you forgot to enter command line arguments. Try again please!')