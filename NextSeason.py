# 
# Program that lets you know when the next season starts
# By Yovany Bartolome
#

from datetime import date


def main():
    # Display directions and questions
    def questions(): 
        print ("\nSelect which season you want to know until it starts.")
        print ("A. Fall")
        print ("B. Winter")
        print ("C. Spring")
        print ("D. Summer")
        print ("E. End Program")

    # Days until Fall 
    def Fall():
        # Today's date
        today = date.today() 
        # Date of when fall starts
        fallStarts = date(today.year, 9, 22)
        untilFall = fallStarts - today
        print("There are", untilFall.days, "days left until next Fall starts")

    # Days until Winter 
    def Winter():
        today = date.today()
        # Date of when winter starts 
        WinterStarts = date(today.year, 12, 21)
        untilWinter = WinterStarts - today
        print("There are", untilWinter.days, "days left until next Winter starts")

    # Days until Spring 
    def Spring():
        today = date.today()
        # Date of when spring starts
        SpringStarts = date(today.year, 3, 20)
        # if the season already happened in the current year 
        if SpringStarts < today:
            SpringStarts = SpringStarts.replace(year = today.year + 1)
        untilSpring = SpringStarts - today
        print("There are", untilSpring.days, "days left until next Spring starts")

    # Days until Summer     
    def Summer():
        today = date.today()
        # Date of when summer starts
        SummerStarts = date(today.year, 6, 21)
        # if the season already happened in the current year 
        if SummerStarts < today:
            SummerStarts = SummerStarts.replace(year = today.year + 1)
        untilSpring = SummerStarts - today
        print("There are", untilSpring.days, "days left until next Summer starts")    

    # loop that allows the user to keep answering until they input "e"
    while True:
        questions()
        userAns = input("Answer: ")

        if userAns.lower() == "a":
            Fall()
        elif userAns.lower() == "b":
            Winter()
        elif userAns.lower() == "c":        
            Spring()
        elif userAns.lower() == "d":
            Summer()
        elif userAns.lower() == 'e':
            print("Program is ending...")
            break # ends program

        





if __name__ == "__main__":
    main()            




    





 