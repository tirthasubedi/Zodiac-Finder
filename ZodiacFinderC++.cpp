// Course: CSC 236 Data Structures
   // Name: Tirtha Subedi
   // Assignment 19: This program going to calculate Age and find their zodic.
   /*
      Purpose: I have always wonder about my zodiac so I'm writing a program to help find any user zodiac.
   */


//small class called DayOfYear
#include <iostream>

#include "stdlib.h"
using namespace std;

class DayOfYear
{
public:
   void input( );
   void output( );

   void set(int new_month, int new_day);
   //Precondition: new_month and new_day form a possible date.
   //Postcondition: The date is reset according to the arguments.

   int get_month( );
   //Returns the month, 1 for January, 2 for February, etc.

   int get_day( );
   //Returns the day of the month.
   int get_year();
//    returns the year
   int calculateage( );
//    this function calculate age of that person

    int zadioc(int month, int date);
// finding zadioc by inserting month and day

private:
   void check_date( );
   int month;
   int day;
   int year;
};

int main( )
{
   DayOfYear zadiocs, birthyear;

   cout <<"Welcome! You'll Be Amazed!!!\n";
   cout <<"Please Enter your Date of Birth to Calculate your Age. \n";
   birthyear.input();
   cout << "Your age is: "<< birthyear.calculateage( ) << endl;

    if (birthyear.calculateage() > 122){
    cout << "YOU ARE Really Old, you can't be that Old: \n";}





    cout << "Enter your Birth Month and date to Find your Zodic: \n ";
    int month, date;
    cout << "Enter your birth month:";
    cin >> month;
    cout << "Enter your birth day:";
    cin >> date;

    zadiocs.zadioc(month, date);


    return 0;
};

//Uses iostream:
void DayOfYear:: input() {


   cout << "Enter your Birth Month: ";
   cin >> month;
   check_date();
   cout << "Enter your birth day: ";
   cin >> day;
   check_date();
   cout <<"Please your birth year: ";
   cin >> year;
   check_date();

}
// below method calculate age of a user

int DayOfYear:: calculateage( ){
   int thisyear= 2018;
    // int gety= get_year();
    return(thisyear- year);

}
// Uses iostream:
void DayOfYear::output( )
{
   cout << "month = " << month
        << ", day = " << day <<
          ", year = "<< year<< endl;
}

void DayOfYear::set(int new_month, int new_day)
{
   month = new_month;
   day = new_day;
   check_date();
}

void DayOfYear::check_date( ) {
   if ((month < 1) || (month > 12) & (day < 1) || (day > 31) & (year > 2018) || (year < 1000)) {
      cout << "Illegal date. Aborting program.\n";

      exit(1);
   }

}

int DayOfYear::get_month( ) {
   return month;
}

int DayOfYear::get_day( ) {
   return day;
}

int DayOfYear::get_year( ){

   return year;

}

//this method find our user zodiac using their birth month and date

int DayOfYear::zadioc(int month, int date) {

    if ((month == 1 && date >= 20) || (month == 2 && date <= 18)) {
        cout << "Your zodiac sign is AQUARIUS\n";

    } else if ((month == 2 && date >= 19) || (month == 3 && date <= 20)) {
        cout << "Your zodiac sign is PISCES\n";
    } else if ((month == 3 && date >= 21) || (month == 4 && date <= 19)) {
        cout << "Your zodiac sign is ARIES\n";
    } else if ((month == 4 && date >= 20) || (month == 5 && date <= 20)) {
        cout << "Your zodiac sign is TAURUS\n";
    } else if ((month == 5 && date >= 21) || (month == 6 && date <= 20)) {
        cout << "Your zodiac sign is GEMINI\n";
    } else if ((month == 6 && date >= 21) || (month == 7 && date <= 22)) {
        cout << "Your zodiac sign is CANCER\n";
    } else if ((month == 7 && date <= 23) || (month == 8 && date <= 22)) {
        cout << "Your zodiac sign is LEO\n";
    } else if ((month == 8 && date >= 23) || (month == 9 && date <= 22)) {
        cout << "Your zodiac sign is VIRGO\n";
    } else if ((month == 9 && date >= 23) || (month == 10 && date <= 22)) {
        cout << "Your zodiac sign is LIBRA\n";
    } else if ((month == 10 && date >= 23) || (month == 11 && date <= 21)) {
        cout << "Your zodiac sign is SCORPIO\n";
    } else if ((month == 11 && date >= 22) || (month == 12 && date <= 21)) {
        cout << "Your zodiac sign is SAGUITTARIUS\n";
    } else if ((month == 12 && date >= 22) || (month == 1 && date <= 19)) {
        cout << "Your zodiac sign is CAPRICORN\n";
    } else {
        cout << "INVALID INPUT";
    }
}








