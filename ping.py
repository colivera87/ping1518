#!/bin/python3
import os

#Qualnet Connections
ap = [["szg-60gig-son-3-ap-0", "szg-60gig-son-3-ap-1", "szg-60gig-son-3-ap-2"],["down","down","down"]]
#10Gig Connections
tenGig = [["192.168.100.101","192.168.100.102","192.168.100.111","192.168.100.112","192.168.100.121"],["down","down","down","down","down"]]


#Ping Qualnet connetions
i = 0
while(i < 3):
    response = os.system("ping -c 1 " + ap[0][i])
    if response == 0:
        ap[1][i] = "up"
    i+=1

#Ping 10Gig connections
i = 0
while(i < 5):
    response = os.system("ping -c 1 " + tenGig[0][i])
    if response == 0:
        tenGig[1][i] = "up"
    i+=1

#print all connections and status
print("SON-3 Status:")
i = 0
while(i < 3):
    print("Qualnet - " +  ap[0][i] + " " + ap[1][i]) 
    i+=1

i = 0
while(i < 5):
    print("10Gig - " +  tenGig[0][i] + " " + tenGig[1][i]) 
    i+=1

