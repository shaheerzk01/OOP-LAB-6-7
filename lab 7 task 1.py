# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 15:07:50 2021

@author: 21A-003-SE
"""

class Fan:
    SLOW = 1
    MEDIUM = 2
    FAST = 3
    def __init__(self, speed=SLOW, radius=5.0, color="blue", on=False):
        self.__speed = speed
        self.__radius = radius
        self.__on = on
        self.__color = color
        
    def get_speed(self):
        return self.__speed
    
    def get_radius(self):
        return self.__radius
    
    def get_on(self):
        return self.__on
    
    def get_color(self):
        return self.__color
    
    def set_speed(self, new_speed):
        if isinstance(new_speed, int) and new_speed >= 1 and new_speed <= 3:
            self.__speed = new_speed
        else:
            print("enter valid data")
            
    def set_color(self, new_color):
        if isinstance(new_color, str):
            self.__color = new_color
        else:
            print("enter valid data")
            
    def set_radius(self, new_radius):
        if isinstance(new_radius, float):
            self.__radius = new_radius
        else:
            print("enter valid data")
            
    def set_on(self, new_on):
        if isinstance(new_on, bool):
            self.__on = new_on
        else:
            print("enter valid data")
            
def main():
    
    fan1 = Fan()
    fan1.set_speed(Fan.FAST)
    fan1.set_radius(10.0)
    fan1.set_color("yellow")
    fan1.set_on(True)
    fan2 = Fan()
    fan2.set_speed(Fan.MEDIUM)
    fan2.set_radius(5.0)
    fan2.set_color("blue")
    fan2.set_on(False)
    print(fan1.get_speed(), fan1.get_radius(), fan1.get_color(), fan1.get_on())
    print(fan2.get_speed(), fan2.get_radius(), fan2.get_color(), fan2.get_on())
    
main()