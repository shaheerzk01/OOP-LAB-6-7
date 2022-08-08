# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 15:33:14 2021

@author: 21A-003-SE
"""

class TV:
    
    def __init__(self):
        self.channel = 1
        self.volume = 1
        self.on = False
        
    def turnOn(self):
        if self.on==False:
            self.on = True
            
    def turnOff(self):
        if self.on==True:
            self.on = False
            
    def getchannel(self):
        return self.channel
    
    def setchannel(self, new_channel):
        if isinstance(new_channel, int) and new_channel <=120 and new_channel > 1 and self.on == True:
            self.channel = new_channel
        
    def getvolume(self):
        return self.volume
        
    def setvolume(self, new_volume):
        if isinstance(new_volume, int) and new_volume >=1 and new_volume <=7 and self.on == True:
            self.volume = new_volume
        
    def channelup(self):
        if self.channel <120 and self.on == True:
            self.channel +=1
            
    def channeldown(self):
        if self.channel >1 and self.on == True:
            self.channel -=1
        
    def volumeup(self):
        if self.volume <=7 and self.on == True:
            self.volume +=1
                                                  
    def volumedown(self):
        if self.volume >1  and self.on == True:
            self.volume -=1
            
def main():
    
    my_tv = TV()
    my_tv2 = TV()
    my_tv.turnOn()
    my_tv.setchannel(30)
    my_tv.setvolume(3)
    print(my_tv.on, my_tv.getchannel(), my_tv.getvolume())
    my_tv2.turnOn()
    my_tv2.channelup()
    my_tv2.channelup()
    my_tv2.volumeup()
    print(my_tv2.on, my_tv2.getchannel(), my_tv2.getvolume())
    
main()