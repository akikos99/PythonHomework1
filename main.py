# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


year = 2021

# Press the green button in the gutter to run the script.
if year % 4 == 0:
   if year % 100 == 0:
       if year % 400 == 0:
           print("True")
       else:
           print("False")
   else:
       print("False")
else:
   print("False")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
