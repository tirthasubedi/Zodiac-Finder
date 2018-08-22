#Author Ram Bastola & Tirtha Subedi

import turtle

#This program is the enhance of A19 in python
#This program will help you find you astrogical or zodiac sign when you Enter your date of birth


class zodiocs():        # this class ask for user input, calculate age, find astrologocal sign, and display image


    def __init__(self, screen):
         """Turtle Constructor"""
         self.screen=screen
         self.varb=""
    #     self.year=year
    #     self.astro_sign=astro_sign
    #
    #     # turtle.Turtle.__init__(self, shape="turtle")


    def dayofyear(self, screen):              # this method ask user for their date of birth and check if its right or not
        # self.trys = screen.textinput("promt", "TYpe yo")
        self.month=screen.numinput("Birthday", "Type your birth month")#int(input("Enter your Birth Month: "))
        # self.check_date()
        self.day=screen.numinput("Birthday", "Type your birth day") #int(input("Enter your Birth Day: "))
        # self.check_date()
        self.year=screen.numinput("Birthday", "Type your birth year ") #int(input("Enter your Birth Year: "))
        self.check_date(screen)
    
    def store_data(self):
        self.list=[]
        self.list.append(self.month)
        self.list.append(self.day)
        self.list.append(self.year)

        print(self.list)

    def check_date(self, screen):   # this method verify whether date is correct or not 
        if self.month < 1 or self.month > 12 or self.day >31 or self.day <1 or self.year >2018 or self.year <1000:
            print("Illegal date. Aborting program.\n")

            return self.dayofyear(screen)


    def get_month(self): # this method is to get month
        return self.month

    def get_day(self):     # this method is to get day
        return self.day

    def get_year(self):      # this method is to get year
        return self.year

    def calculate_age(self, james):       # this method calculate the age of a user by their birthday
        self.this_year= 2018
        self.age= self.this_year - self.year
        james.color('red')                      # this making text color to red when displaying in window
        james.write("Your current age is: " + str(int(self.age)), font=("Arial", 20, "normal")) # this display age of user on screen


    def find_astrological(self):     # this method will find out the astrological or zodiac of a user by their birth day and month
        if self.month == 12:
            astro_sign = 'Sagittarius' if (self.day < 22) else 'capricorn'
            print("Your Astrological sign is :" ,  astro_sign)
            self.varb='Sagittarius'
        elif self.month == 1 :
            astro_sign = 'Capricorn' if (self.day < 20) else 'aquarius'
            print("Your Astrological sign is :" ,  astro_sign)
            self.varb='Capricorn'
        elif self.month == 2 :
            astro_sign = 'Aquarius' if (self.day < 19) else 'pisces'
            print("Your Astrological sign is :" ,  astro_sign)
            self.varb='Aquarius'
        elif self.month == 3 :
            astro_sign = 'Pisces' if (self.day < 21) else 'aries'
            print("Your Astrological sign is :" ,  astro_sign)
            self.varb='Pisces'
        elif self.month == 4 :
            astro_sign = 'Aries' if (self.day < 20) else 'taurus'
            print("Your Astrological sign is :" ,  astro_sign)
            self.varb='Aries'
        elif self.month == 5 :
            astro_sign = 'Taurus' if (self.day < 21) else 'gemini'
            print("Your Astrological sign is :" ,  astro_sign)
            self.varb='Taurus'
        elif self.month == 6 :
            astro_sign = 'Gemini' if (self.day < 21) else 'cancer'
            print("Your Astrological sign is :" ,  astro_sign)
            self.varb='Gemini'
        elif self.month == 7 :
            astro_sign = 'Cancer' if (self.day < 23) else 'leo'
            print("Your Astrological sign is :" ,  astro_sign)
            self.varb='Cancer'
        elif self.month == 8 :
            astro_sign = 'Leo' if (self.day < 23) else 'virgo'
            print("Your Astrological sign is :" ,  astro_sign)
            self.varb='Leo'
        elif self.month == 9 :
            astro_sign = 'Virgo' if (self.day < 23) else 'libra'
            print("Your Astrological sign is :" ,  astro_sign)
            self.varb='Virgo'
        elif self.month == 10 :
            astro_sign = 'Libra' if (self.day < 23) else 'scorpio'
            print("Your Astrological sign is :" ,  astro_sign)
            self.varb='Libra'
        elif self.month == 11 :
            astro_sign = 'scorpio' if (self.day < 22) else 'sagittarius'
            print("Your Astrological sign is :" ,  astro_sign)
            self.varb='scorpio'
        # return astro_sign

    def display_image(self, james):                 # this method display the finded astrological sign to the window
        # for i in range(4):
        #     james.forward(50)
        #     james.right(90)

        self.screen=turtle.Screen()
        self.screen.setup(400, 400)                     # there are 12 astrological sign and this method will display the sign that
                                                        # meet the conditioned statement
        print(self.find_astrological())
        if self.varb =="Sagittarius":
            self.screen.bgpic("sagittarus.gif")

        elif self.varb=="Aries":
            self.screen.bgpic("aries.gif")

        elif self.varb=="Cancer":
            self.screen.bgpic("cancer.gif")

        elif self.varb=="Capricorn":
            self.screen.bgpic("capricorn.gif")

        elif self.varb=="Taurus":
            self.screen.bgpic("taurus.gif")

        elif self.varb=="Leo":
            self.screen.bgpic("leo.gif")

        elif self.varb=="Scorpio":
            self.screen.bgpic("scorpio.gif")

        elif self.varb=="Aquarius":
            self.screen.bgpic("Aquarius.gif")

        elif self.varb=="Gemini":
            self.screen.bgpic("gemini.gif")

        elif self.varb=="Virgo":
            self.screen.bgpic("virgo.gif")

        elif self.varb=="Pisces":
            self.screen.bgpic("pisces.gif")

        elif self.varb=="Libra":
            self.screen.bgpic("libra.gif")
        turtle.done()


def main():

    screen=turtle.Screen()
    t = zodiocs(screen)
    t.dayofyear(screen)
                                        # this is where everything is called in order to display in the window.

    t.store_data()
    james= turtle.Turtle()
    t.calculate_age(james)
    t.find_astrological()
    t.display_image(james)
    screen.exitonclick()
main()
if __name__ == '__main__':
    pass

