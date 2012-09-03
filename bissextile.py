# -*-coding:utf-8 -*

#
# Prompt the user to enter a year and check if it is bissextile
##

year = int(input("Enter a year :"))

if year%400 == 0 or (year%4 == 0 and year%100 != 0):
  print("Hourray, the year « %i » you entered is bissextile." % year)