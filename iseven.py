def even():
    num = raw_input("enter 1 to find even number in a range, enter 2 to find odd numbers in a range, enter 3 to check if the number is even: ")
    if num == str(1):
        an1 = raw_input("Enter your first number: ")
        an2 = raw_input("Enter your second number: ")
        x = range(int(an1),int(an2))
        for i in x:
            if i % 2 == 0:
                print i
    if num == str(2):
        num1 = raw_input("Enter your fisrt number: ")
        num2 = raw_input("Enter your second number: ")
        x = range(int(num1),int(num2))
        for i in x:
            if i % 2 == 1:
                print i
    if num == str(3):
        eq1 = raw_input ("Enter a number: ")
        if int(eq1) % 2 == 0:
            print eq1 + " is even"
        else:
            print eq1 + " is odd"
while True:
    even()