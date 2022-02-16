#!/usr/bin/env python3

def to_seconds(hours, minutes, seconds):
  return hours*3600 + minutes*60 + seconds

print("Welcome to this time converter")
cont = 'y'

while (cont == 'y'):
  hours = int(input("Enter the number of hours:"))
  minutes = int(input("Enter the number of minutes:"))
  seconds = int(input("Enter the number of minutes:"))

  print("That's {} seconds.".format(to_seconds(hours, minutes, seconds)))
  print()
  cont = input("Do you want to continue?")

print("Good bye!")
