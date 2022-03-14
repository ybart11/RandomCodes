def cal(a,operator,c):
    # Compute operations
    if operator == "+":
        out = a + c
    elif operator == "-":
        out = a - c
    elif operator == "*":
        out = a * c
    elif operator == "/":
        out = a / c

    # Display result
    return out

def quizTitle():
    print('\t\tQUIZ')
    name = input("Name: ")
    date = input("Date: ")

def quiz():
    # Title of quiz
    quizTitle()

    # Counts how many question the user has correct
    count = 0

    #question 1
    print("\nQuestion 1")
    print("What is 10 + 12?")
    ans1 = int(input("Type your answer: "))

    if ans1 == cal(10, '+', 12):
        count = count + 1
        print("Correct.")
    else:
        print("Incorrect.")


    #question 2
    print("\nQuestion 2")
    print("What is 20 + 19?")
    ans2 = int(input("Type your answer: "))

    if ans2 == cal(20,'+',19):
        count = count + 1
        print("Correct.")
    else:
        print("Incorrect.")


    #question 3
    print("\nQuestion 3")
    print("What is 13 + 15?")
    ans3 = int(input("Type your answer: "))

    if ans3 == cal(13,'+',15):
        count = count + 1
        print("Correct.")
    else:
        print("Incorrect.")

    # question 4
    print("\nQuestion 4")
    print("What is 11 + 11?")
    ans4 = int(input("Type your answer: "))

    if ans4 == cal(11,'+', 11):
        count = count + 1
        print("Correct.")
    else:
        print("Incorrect.")

    #question 5
    print("\nQuestion 5")
    print("What is 25 - 10?")
    ans5 = int(input("Type your answer: "))

    if ans5 == cal(25,'-',10):
        count = count + 1
        print("Correct.")
    else:
        print("Incorrect.")

    #question 6
    print("\nQuestion 6")
    print("What is 7 + 6?")
    ans6 = int(input("Type your answer: "))

    if ans6 == cal(7, '+', 6):
        count = count + 1
        print("Correct.")
    else:
        print("Incorrect.")

    #question 7
    print("\nQuestion 7")
    print("What is 33 + 11?")
    ans7 = int(input("Type your answer: "))

    if ans7 == cal(33, '+', 11):
        count = count + 1
        print("Correct.")
    else:
        print("Incorrect.")

    #question 8
    print("\nQuestion 8")
    print("What is 14 + 17?")
    ans8 = int(input("Type your answer: "))

    if ans8 == cal(14, '+', 17):
        count = count + 1
        print("Correct.")
    else:
        print("Incorrect.")

    #question 9
    print("\nQuestion 9")
    print("What is 15 + 15?")
    ans9 = int(input("Type your answer: "))

    if ans9 == cal(15, '+', 15):
        count = count + 1
        print("Correct.")
    else:
        print("Incorrect.")

    #question 10
    print("\nQuestion 10")
    print("What is 20 - 11?")
    ans10 = int(input("Type your answer: "))

    if ans10 == cal(20, '-', 11):
        count = count + 1
        print("Correct.")
    else:
        print("Incorrect.")

    print("\nYou got", count,"out of 10 correct.")
