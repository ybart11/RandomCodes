from curses.ascii import isalpha
from datetime import time
from datetime import date
from datetime import datetime 
from datetime import timedelta


def main():

    # converts month from string to integer 
    def month_converter(month):
        months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',\
            'August', 'September', 'October', 'November', 'December']
        return months.index(month) + 1

    # function that determines how many days until user's next birthday 
    def nextBday():
        userMonth1 = input("\nWhat month is your birthday(spelled out)? ")
        userDate = int(input("What date is your birthday? "))
    
        # takes away any extra space at the end of user's input 
        userMonth2 = ""
        for letter in userMonth1:
            if letter.isalpha():
                userMonth2 += letter            

        # today's date 
        today = date.today()

        # user's bday 
        birthday = date(today.year, month_converter(userMonth2.capitalize()), userDate)

        # what if bday already past 
        if birthday < today:
            print ("Your birthday was", (today - birthday).days, "days ago.")
            birthday = birthday.replace(year = today.year + 1)


        # days until next birthday 
        nextBirthday = birthday - today 
        print (nextBirthday.days, "days until your next birthday!")

    # runs program      
    nextBday()
    


if __name__ == "__main__":
    main()