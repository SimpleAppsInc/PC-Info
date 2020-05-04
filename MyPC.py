import socket
import platform
import subprocess
from datetime import date
while True:
    today = date.today() #Today adli degiskene bugunun tarihini atadik.
    dt = today.strftime("%B %d, %Y") # Month (str) - Day - Year.
    print("*****************************************")
    print("* 1] Continue" + "\n* 2] Exit")
    print("*****************************************")
    x = input(">>>> ") #kullanicinin secimini aldik
    #print(type(x)) #X'in turunu yazdirdik
    if x == "1":
        subprocess.Popen("cls", shell=True).communicate()
        print("We have it done for you..." + "\n Would you like to get more information?" + "\n" + "\n1] Yes, I'd like to get more information about my system" + "\n2] No PC name and IP is emough for me" + "\n3] Just show me infos (Do not save)")
        y = input(">>>> ")
        if y == "1":
            a = "You PC's name: "
            b = "Your IP Address: "
            d = "Last time used program is: "
            m = "System type: "
            v = "Version: "
            p = "Windows version: "
            hostname = socket.gethostname()
            IP = socket.gethostbyname(hostname)
            mach = platform.machine() # x64 or x86
            version = platform.version() # version
            platform = platform.platform() # Windows surumu
            print("                " + "Date" + "                  ")
            print("************************************************")
            print(d + dt)
            print("************************************************")
            print("                " + "Name" + "                  ")
            print("************************************************")
            print(a + hostname)
            print("************************************************")
            print("                " + " IP " + "                  ")
            print("************************************************")
            print(b + IP)
            print("************************************************")
            print("                " + "Info" + "                  ")
            print("************************************************")
            print(m + mach)
            print("*******************")
            print("\n" + v + version)
            print("*******************")
            print("\n" + p + platform)
            print("************************************************")
            print("****************" + "SAVED" + "*****************")
            f = open("MyIP.txt","w+") #MyIP adli bir txt dosyasini yazma ile olusturduk (w+)
            for i in range (1):
                f.write("\nDATE:")
                f.write("\n----------------------------------------")
                f.write("\nLast time used program is: " + dt) #dosyaya yazma islemlerini gerceklestirdik. (Lines: 38-44)
                f.write("\n")
                f.write("\n")
                f.write("\nPC NAME:")
                f.write("\n----------------------------------------")
                f.write("\nPC Name: " + hostname)
                f.write("\n")
                f.write("\n") 
                f.write("\nIP ADDRESS:")
                f.write("\n----------------------------------------")
                f.write("\nIP Address: " + IP)
                f.write("\n")
                f.write("\n")
                f.write("\nSYSTEM INFORMATION:")
                f.write("\n----------------------------------------")
                f.write("\nSystem Type: " + mach)
                f.write("\n----------------------")
                f.write("\nVersion: " + version)
                f.write("\n----------------------")
                f.write("\nWindows Version: " + platform)
                f.write("\n-----------------SAInc------------------")
            break;
        if y == "2":
            subprocess.Popen("cls", shell=True).communicate()
            a = "You PC's name: "
            b = "Your IP Address: "
            d = "Last time used program is: "
            hostname = socket.gethostname()
            IP = socket.gethostbyname(hostname)
            print("                " + "Date" + "                  ")
            print("************************************************")
            print(d + dt)
            print("************************************************")
            print("                " + "Name" + "                  ")
            print("************************************************")
            print(a + hostname)
            print("************************************************")
            print("                " + " IP " + "                  ")
            print("************************************************")
            print(b + IP)
            print("************************************************")
            f = open("MyIPJustBasic.txt","w+") #MyIP adli bir txt dosyasini yazma ile olusturduk (w+)
            for i in range (1):
                f.write("\nDATE:")
                f.write("\n----------------------------------------")
                f.write("\nLast time used program is: " + dt) #dosyaya yazma islemlerini gerceklestirdik. (Lines: 38-44)
                f.write("\n")
                f.write("\n")
                f.write("\nPC NAME:")
                f.write("\n----------------------------------------")
                f.write("\nPC Name: " + hostname)
                f.write("\n")
                f.write("\n")
                f.write("\nIP ADDRESS:")
                f.write("\n----------------------------------------")
                f.write("\nIP Address: " + IP)
                f.write("\n----------------------------------------")
            break;
        if y == "3":
            subprocess.Popen("cls", shell=True).communicate()
            a = "You PC's name: "
            b = "Your IP Address: "
            d = "Last time used program is: "
            m = "System type: "
            v = "Version: "
            p = "Windows version: "
            hostname = socket.gethostname()
            IP = socket.gethostbyname(hostname)
            mach = platform.machine() # x64 or x86
            version = platform.version() # version
            platform = platform.platform() # Windows surumu
            print("                " + "Date" + "                  ")
            print("************************************************")
            print(d + dt)
            print("\n")
            print("                " + "Name" + "                  ")
            print("************************************************")
            print(a + hostname)
            print("\n")
            print("                " + " IP " + "                  ")
            print("************************************************")
            print(b + IP)
            print("\n")
            print("                " + "Info" + "                  ")
            print("************************************************")
            print(m + mach)
            print("*******************")
            print("\n" + v + version)
            print("*******************")
            print("\n" + p + platform)
            print("************************************************")
            print("\n")
            print("\n")
    if x == "2":
        print("Good bye see you soon!")
        break;