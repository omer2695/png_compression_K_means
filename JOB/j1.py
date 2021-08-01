#!/bin/python3

import math
import random
import re
import traceback


def calc_angle(time):
    Hours = int(time[0:2])
    Minutes = int(time[3:5])
    Circle_Degree = 360
    if (Hours >= 12):
        Hours -= 12

    Calculate_Minutes_Degree = (Minutes * Circle_Degree) / 60
    while (Calculate_Minutes_Degree >= 360):
        Calculate_Minutes_Degree -= 360
    if (Calculate_Minutes_Degree == 0):
        Calculate_Minutes_Degree = 360
    Calculate_Hours_Degree = (Hours * Circle_Degree) / 12 + (Minutes * Circle_Degree) / (60 * 12)
    if (Calculate_Hours_Degree == 0):
        Calculate_Hours_Degree = 360



    #print(Calculate_Hours_Degree)
    #print(Calculate_Minutes_Degree)
    Degree_Between_Hour_And_Minutes=Calculate_Minutes_Degree - Calculate_Hours_Degree
    if (Degree_Between_Hour_And_Minutes==int(Degree_Between_Hour_And_Minutes)):
        print(int(Degree_Between_Hour_And_Minutes))
    else:
        print(Degree_Between_Hour_And_Minutes)


Time_As_String = "09:00"
#Time_As_String1= "13:17"
#Time_As_String2= "00:00"

calc_angle(Time_As_String)

#calc_angle(Time_As_String1)
#calc_angle(Time_As_String2)