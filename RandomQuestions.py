# 
# Program with random options based on my new skills
# By Yovany Bartolome
#


def main():
    # import modules
    from datetime import datetime 
    from time import strftime
    import calendar

    # Function that displays current time 
    def currentTime():
        yer = datetime.now()
        return yer.strftime("Current Time: %I:%M %p")

    # Function that displays today's date 
    def todayDate():
        today = datetime.today()
        return today.strftime("Today's Date: %B %d, %Y") 

    # Function that reverses user's input (string)
    def nameBackwards(name):
        return name [::-1]

    # Function that asks for user's name and uses nameBackwards()
    def choiceC():
        userName = input("What is your name? ")
        return nameBackwards(userName)

    # Function that displays current month's calendar 
    def physicalCalendar():
        cal = calendar.TextCalendar()
        today = datetime.today()
        yer = cal.formatmonth(today.year, today.month)
        return yer

    
        
    def header():
        print ("-----------------------------")
        print ("Which one do you want to know?")
        print ("A. Current Time\nB. Today's Date\nC. Name Backwards\nD. Display Month's Calendar\
        \nE. End Program")

    def question():
        
        while True:
            print("")
            header()
            userChoice = input("Answer: ")
            userChoice = userChoice.lower()
            if userChoice == "a":
                print(currentTime())
            elif userChoice == "b":
                print(todayDate())
            elif userChoice == "c":
                print(choiceC())
            elif userChoice == "d":
                print(physicalCalendar())   
            elif userChoice == 'e':
                print("Programming is ending...")
                break            
            
# You would import this into a different file to make it look simpler 
    question()        











if __name__ == "__main__":
    main()       


