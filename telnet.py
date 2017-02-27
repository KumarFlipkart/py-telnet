import getpass
import sys
import telnetlib

HOST = "192.168.1.1"

user = "admin"

password = "admin123"

tn = telnetlib.Telnet(HOST,23)

tn.read_until("login: ")


tn.write(user + "\n")


if password:
    tn.read_until("Password: ")
    tn.write(password + "\n")

tn.read_until(">")
tn.write("cont bsnl.in" + "\n")
tn.read_until(">")
def routene():
    outer_vlan=raw_input("Enter the Outer Vlan: ")
    tn.write("show sub act username bbtest@bsnl.in" + " | include " + outer_vlan + "\n")
    portx = tn.read_until(">" or "pppoe")
    if portx[196:206]=="":
        print raw_input("Port not Found on bbtest" + "\n Press Enter to cont...")
        tn.write("show sub act username multiplay@bsnl.in" + " | include " + outer_vlan + "\n")
        porty = tn.read_until(">" or "pppoe")
        if porty[196:206]=="":
            print ("Port not in multiplay also try again")
            routene()
        if porty[196:206]!="":
            print ("port Found on multiplay with inner vlan : " + porty[196:206])
            print raw_input("press enter to exit")
            tn.close()
    elif portx[196:206]!="":
        print ("port Found on bbtest with inner vlan : " + portx[196:206])
        print raw_input("Press enter to exit")
        tn.close()
routene()
