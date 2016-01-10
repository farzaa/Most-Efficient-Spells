#Built by Farzain Majeed
#Riot QA 2015 Internship Test Program
#University of Central Florida

import requests
import sys
from RiotAPI import RiotAPI
from Champion import Champion

#Before my main method, I declare this printing function to get it out of the way.
def _easyPrinter(winnerQ, winnerQName, winnerW, winnerWName, winnerE, winnerEName, winnerR, winnerRName):
    print "Most Efficient Q at Level 1 ", "      ", winnerQName[0], "%.2f"  %winnerQ[0],  "Damage Per Second"
    print "Most Efficient Q at Level 5 ", "      ", winnerQName[1], "%.2f"  %winnerQ[1], "Damage Per Second"
    print "Most Efficient Q at Level 9 ", "      ", winnerQName[2],"%.2f" %winnerQ[2], "Damage Per Second"
    print "Most Efficient Q at Level 13", "      ", winnerQName[3], "%.2f" %winnerQ[3],"Damage Per Second"
    print "Most Efficient Q at Level 18", "      ", winnerQName[4], "%.2f" %winnerQ[4], "Damage Per Second"
    print "\n"
    print "Most Efficient W at Level 1 ", "      ", winnerWName[0], "%.2f"  %winnerW[0],  "Damage Per Second"
    print "Most Efficient W at Level 5 ", "      ", winnerWName[1], "%.2f"  %winnerW[1], "Damage Per Second"
    print "Most Efficient W at Level 9 ", "      ", winnerWName[2],"%.2f" %winnerW[2], "Damage Per Second"
    print "Most Efficient W at Level 13", "      ", winnerWName[3], "%.2f" %winnerW[3],"Damage Per Second"
    print "Most Efficient W at Level 18", "      ", winnerWName[4], "%.2f" %winnerW[4], "Damage Per Second"
    print "\n"
    print "Most Efficient E at Level 1 ", "      ", winnerEName[0], "%.2f"  %winnerE[0],  "Damage Per Second"
    print "Most Efficient E at Level 5 ", "      ", winnerEName[1], "%.2f"  %winnerE[1], "Damage Per Second"
    print "Most Efficient E at Level 9 ", "      ", winnerEName[2],"%.2f" %winnerE[2], "Damage Per Second"
    print "Most Efficient E at Level 13", "      ", winnerEName[3], "%.2f" %winnerE[3],"Damage Per Second"
    print "Most Efficient E at Level 18", "      ", winnerEName[4], "%.2f" %winnerE[4], "Damage Per Second"
    print "\n"
    print "Most Efficient R at Level 9 ", "      ", winnerRName[0],"%.2f" %winnerR[0], "Damage Per Second"
    print "Most Efficient R at Level 13", "      ", winnerRName[1], "%.2f" %winnerR[1],"Damage Per Second"
    print "Most Efficient R at Level 18", "      ", winnerRName[2], "%.2f" %winnerR[2], "Damage Per Second"
  

def main():

    #Lets start our program by calling this function.
    #It will create an object that will help us to connect to Riot API.
    api = RiotAPI('9c971f8a-e6f3-44ce-b85a-7e3c78cc96a7')

    baseADPerLevel = [50, 60, 70, 80, 100]
    addedAD = [0, 100, 300, 400, 500]
    addedAP = [0, 10, 20, 30, 40]
    addedCDR = [0, 0.05, 0.10, 0.15, 0.4]

    winnerQ = [0, 0, 0, 0, 0]
    winnerQName = [0, 0, 0, 0, 0]
    winnerW = [0, 0, 0, 0, 0]
    winnerWName = [0, 0, 0, 0, 0]
    winnerE = [0, 0, 0, 0, 0]
    winnerEName = [0, 0, 0, 0, 0]
    winnerR = [0, 0, 0, 0, 0]
    winnerRName = [0, 0, 0, 0, 0]


    #Here is my big list of champion IDs.  This is what I use the grab each champs static data using Riot API.
    champIDList =  ['266','412','23', '79', '69', '13', '78', '14', '1',
                    '111', '43', '99', '103','2','112', '34',  '86', '27',
                    '127', '57', '25', '28', '105', '74', '238', '68', '37',
                    '82', '96', '55', '117', '22', '30', '12', '122', '67', '77',
                    '110', '89','126','134', '80', '92', '121',
                    '76', '3', '85', '45', '432', '150', '90', '254', '10',
                    '39', '64', '60', '106', '20', '4',  '24', '102', '429', '36', '223',
                    '63', '131', '113', '8', '154', '421', '133', '84', '18', '120', '15',
                    '236', '107', '19', '72', '54', '157', '101', '17', '75', '58', '119', '35',
                    '50', '115', '91', '40', '245', '61', '114', '9', '33', '31', '7', '16', '26',
                    '56', '222', '83', '6', '203', '21', '62',  '53', '98', '201', '5', '29', '11', '44',
                    '32', '41', '48', '38', '161', '143', '267', '59', '81',
                    '42', '104', '51', '268', '115']

  
    #champIDList = ['266','412','23', '79', '69', '13', '78', '14', '1']

    print "Hello User. Welcome to the RitoPlsNerf Skills Calculator (Only compatible with Patch 5.22). Before using this program, I recommend taking a look at readme.txt and rules.txt included in the ZIP file.\n"
    print "I also highly recommend running this program in IDLE or some full screen interface.  Command Prompt may alter the formatting of certain things. If you are using a Terminal"
    print "than be sure to make the window as big as possible\n"
    raw_input("PRESS ENTER to continue.........")
    print ("\n")
    print "In order to begin I first need to grab each champions JSON Data (using Riot API) and parse the data I need into an object made just for that champion.\n"
    print "This will allow me to use that data efficiently instead of constantly going through Riot's API.\n"
    print "Grabbing all the data I need may take 30-60 SECONDS depending on your internet/computer.  The good part is, once this is done you don't need to do it again!\n"
    print "Type in the word BEGIN  below to st" \
          "art making our objects, it may take a minute!\n"
    
    #Basic user input here.
    userInput01 = (str)(raw_input('Type BEGIN here: '))
    userInput01 = userInput01.lower()
    #I include this in case the user types something incorrect.
    while (userInput01 != 'begin'):
        print "Incorrect input! Try again."
        userInput01 = (str)(raw_input('Type here: '))
        userInput01 = userInput01.lower()

    if (userInput01 == 'begin'):
        print "Preparing to hack into Riot Games Kappa Kappa Kappa TSM DoubleLift"
        championObjectList =[]
        #This is where I grab each champs JSON and parse it into an object.
        #I then put that object in a list I can reference later.
        for id in champIDList:
            championJSON = api.get_champion_by_id(id)  
            champObject = Champion(championJSON)
            #champObject._printValues()
            championObjectList.append(champObject)

    else:
        print "Your input was incorrect! The program will now exit...\n"
        sys.exit()

    print "Okay! I have made an object for each champion. Now we can do a bunch of fun stuff!\n"
    print "Before we start, let me run down how this program works. You will be prompted to input varying amounts of CDR, AP, and AD ALL according to a champions level. This program uses Levels 1, 5, 9, 13, and 18.\n"
    raw_input("PRESS ENTER to continue.........\n")

    print "As an example I have included some predefined sample input below.  These are the stats for a Hybrid AD champion (like Corki), which is why it gains some AP per level.\n"

    print "Remember you can customize this all you want later in the program!\n"

    print "              AD", "         ","AP", "       ","CDR"
    print "Level 1:     ","%.2f" %addedAD[0],  "       ", "%.2f" %addedAP[0],  "      ", "%.2f" %addedCDR[0]
    print "Level 5:     ","%.2f" %addedAD[1],  "     ", "%.2f" %addedAP[1],  "     ", "%.2f" %addedCDR[1]
    print "Level 9:     ","%.2f" %addedAD[2],  "     ", "%.2f" %addedAP[2],  "     ", "%.2f" %addedCDR[2]
    print "Level 13:    ","%.2f" %addedAD[3],  "     ", "%.2f" %addedAP[3],  "     ", "%.2f" %addedCDR[3]
    print "Level 18:    ","%.2f" %addedAD[4],  "     ", "%.2f" %addedAP[4],  "     ", "%.2f" %addedCDR[4]

    print "\n"
    i = 0
    while (i == 0):
        print "RiotPlsNerf Skills Calculator Menu\n"
        print "Note: Typing in an option incorrectly will cause program to exit\n"
        print "Type in the word RUN to use my predefined values for AP, AD, and CDR (I HIGHLY recommend doing this first)\n"
        print "Type in the word CUSTOM to use your own values for AP, AD, and CDR\n"
        print "Type in the word SKILLS to look at the efficiency of a specific champion's skill. (Note: This only works properly if you use RUN or CUSTOM beforehand)\n"
        print "Type in the word GET to look at a specific champions object\n"
        print "Type in the word LEAVE to exit from the program"

        userInput01 = (str)(raw_input('Type preferred option here: '))
        userInput01 = userInput01.lower()


        if (userInput01 == 'RUN' or userInput01 == 'run' or userInput01 == 'Run' or
            userInput01 == 'CUSTOM' or userInput01 == 'custom' or userInput01 == 'Custom'):

            baseADPerLevel = [50, 60, 70, 80, 100]
            addedAD = [10, 100, 300, 400, 500]
            addedAP = [0, 5, 10, 20, 40]
            addedCDR = [0, 0.05, 0.10, 0.15, 0.4]

            w = 0
            #This is how the "Custom" fucntion is built.
            if (userInput01 == 'CUSTOM' or userInput01 == 'custom' or userInput01 == 'Custom'):
                while (w == 0):
                    print "\n"
                    print "P A R T  O N E"
                    print "Lets go step by step so that you can accurately input your numbers for AP, AD, and CDR.  Only input NUMBERS for everything (decimals are okay)"
                    raw_input("PRESS ENTER to continue.........\n")
                    print "Level 1, how much AD do you want your champ to have?"
                    AD1 = float(raw_input('Type your input here (Keep number between 0 and 1000): '))
                    while (AD1 > 1000 or AD1 < 0):
                        print "Your previous input had the incorrect bounds. Try again!"
                        AD1 = float(raw_input('Type your input here (Keep number between 0 and 1000): '))
                    print "\nLevel 5, how much AD do you want your champ to have?"
                    AD2 = float(raw_input('Type your input here (Keep number between 0 and 1000): '))
                    while (AD2 > 1000 or AD2 < 0):
                        print "Your previous input had the incorrect bounds. Try again!"
                        AD2 = float(raw_input('Type your input here (Keep number between 0 and 1000): '))
                    print "\nLevel 9, how much AD do you want your champ to have?"
                    AD3 = float(raw_input('Type your input here (Keep number between 0 and 1000): '))
                    while (AD3 > 1000 or AD3 < 0):
                        print "Your previous input had the incorrect bounds. Try again!"
                        AD3 = float(raw_input('Type your input here (Keep number between 0 and 1000): '))
                    print "\nLevel 13, how much AD do you want your champ to have?"
                    AD4 = float(raw_input('Type your input here (Keep number between 0 and 1000): '))
                    while (AD4 > 1000 or AD4 < 0):
                        print "Your previous input had the incorrect bounds. Try again!"
                        AD4 = float(raw_input('Type your input here (Keep number between 0 and 1000): '))
                    print "\nLevel 18, how much AD do you want your champ to have?"
                    AD5 = float(raw_input('Type your input here (Keep number between 0 and 1000): '))
                    while (AD5 > 1000 or AD5 < 0):
                        print "Your previous input had the incorrect bounds. Try again!"
                        AD5 = float(raw_input('Type your input here (Keep number between 0 and 1000): '))
                    print "\n"
                    addedAD = [AD1, AD2, AD3, AD4, AD5]

                    print "P A R T  T W 0"
                    print "Now you can input the amount of AP you want to give your champ!"
                    raw_input("PRESS ENTER to continue.........\n")

                    print "\n"
                    print "Level 1, how much AP do you want your champ to have?"
                    AP1 = float(raw_input('Type your input here (Keep number between 0 and 1500): '))
                    while (AP1 > 1500 or AP1 < 0):
                        print "Your previous input had the incorrect bounds. Try again!"
                        AP1 = float(raw_input('Type your input here (Keep number between 0 and 1500): '))
                    print "\nLevel 5, how much AP do you want your champ to have?"
                    AP2 = float(raw_input('Type your input here (Keep number between 0 and 1500): '))
                    while (AP2 > 1500 or AP2 < 0):
                        print "Your previous input had the incorrect bounds. Try again!"
                        AP2 = float(raw_input('Type your input here (Keep number between 0 and 1500): '))
                    print "\nLevel 9, how much AP do you want your champ to have?"
                    AP3 = float(raw_input('Type your input here (Keep number between 0 and 1500): '))
                    while (AP3 > 1500 or AP3 < 0):
                        print "Your previous input had the incorrect bounds. Try again!"
                        AP3 = float(raw_input('Type your input here (Keep number between 0 and 1500): '))
                    print "\nLevel 13, how much AP do you want your champ to have?"
                    AP4 = float(raw_input('Type your input here (Keep number between 0 and 1500): '))
                    while (AP4 > 1500 or AP4 < 0):
                        print "Your previous input had the incorrect bounds. Try again!"
                        AP4 = float(raw_input('Type your input here (Keep number between 0 and 1500): '))
                    print "\nLevel 18, how much AP do you want your champ to have?"
                    AP5 = float(raw_input('Type your input here (Keep number between 0 and 1500): '))
                    while (AP5 > 1500 or AP5 < 0):
                        print "Your previous input had the incorrect bounds. Try again!"
                        AP5 = float(raw_input('Type your input here (Keep number between 0 and 1500): '))
                    print "\n"
                    addedAP =  [AP1, AP2, AP3, AP4, AP5]

                    print "P A R T  T H R E E"
                    print "Time to plug in your numbeers for CoolDown Reduction (CDR)!"
                    print "IMPORTANT: Input CDR PERCENT as a DECIMAL! (Example: for 20% CDR type in 0.20)"
                    raw_input("PRESS ENTER to continue.........\n")

                    print "\nLevel 1, how much CDR do you want your champ to have?"
                    CDR1 = float(raw_input('Type your input here (Keep number between 0.00 and 0.40): '))
                    while (CDR1 > 0.4 or CDR1 < 0):
                        print "Your previous input had the incorrect bounds. Try again!"
                        CDR1 = float(raw_input('Type your input here (Keep number between 0.00 and 0.40): '))
                    print "\nLevel 5, how much CDR do you want your champ to have?"
                    CDR2 = float(raw_input('Type your input here (Keep number between 0.00 and 0.40): '))
                    while (CDR2 > 0.4 or CDR2 < 0):
                        print "Your previous input had the incorrect bounds. Try again!"
                        CDR2 = float(raw_input('Type your input here (Keep number between 0 and 0.40): '))
                    print "\nLevel 9, how much CDR do you want your champ to have?"
                    CDR3 = float(raw_input('Type your input here (Keep number between 0.00 and 0.40): '))
                    while (CDR3 > 0.4 or CDR3 < 0):
                        print "Your previous input had the incorrect bounds. Try again!"
                        CDR3 = float(raw_input('Type your input here (Keep number between 0 and 0.40): '))
                    print "\nLevel 13, how much CDR do you want your champ to have?"
                    CDR4 = float(raw_input('Type your input here (Keep number between 0.00 and 0.40): '))
                    while (CDR4 > 0.4 or CDR4 < 0):
                        print "Your previous input had the incorrect bounds. Try again!"
                        CDR4= float(raw_input('Type your input here (Keep number between 0 and 0.40): '))
                    print "\nLevel 18, how much CDR do you want your champ to have?"
                    CDR5 = float(raw_input('Type your input here (Keep number between 0.00 and 0.40): '))
                    while (CDR5 > 0.4 or CDR5 < 0):
                        print "Your previous input had the incorrect bounds. Try again!"
                        CDR5= float(raw_input('Type your input here (Keep number between 0 and 0.40): '))

                    addedCDR = [CDR1, CDR2, CDR3, CDR4, CDR5]
                    print "\n"
                    print "Here is what your input looks like when it is organized"

                    print "              AD", "         ","AP", "       ","CDR"
                    print "Level 1:     ","%.2f" %addedAD[0],  "     ", "%.2f" %addedAP[0],  "     ", "%.2f" %addedCDR[0]
                    print "Level 5:     ","%.2f" %addedAD[1],  "     ", "%.2f" %addedAP[1],  "     ", "%.2f" %addedCDR[1]
                    print "Level 9:     ","%.2f" %addedAD[2],  "     ", "%.2f" %addedAP[2],  "     ", "%.2f" %addedCDR[2]
                    print "Level 13:    ","%.2f" %addedAD[3],  "     ", "%.2f" %addedAP[3],  "     ", "%.2f" %addedCDR[3]
                    print "Level 18:    ","%.2f" %addedAD[4],  "     ", "%.2f" %addedAP[4],  "     ", "%.2f" %addedCDR[4]

                    print "Type in the word READY to move forward with the numbers above"
                    print "Type in the word AGAIN to input your numbers from the beginning"
                    userInput01 = (str)(raw_input('Type preferred option here: '))
                    userInput01 = userInput01.lower()

                    if (userInput01 == 'READY' or userInput01 == 'ready' or userInput01 == 'Ready'):
                        w = 1
                        break;
                    if (userInput01 == 'AGAIN' or userInput01 == 'again' or userInput01 == 'Again'):
                        w = 0
                        continue;
                    else:
                        print "Your input was incorrect! The program will now exit...\n"
                        sys.exit()
            #This is where I grab the most efficient spells and assign them accordingly.
            #I go through every single object in my list.
            for i in range (0, len(champIDList)):
                currentObject = championObjectList[i]
                print currentObject._returnChampName()
                currentObject._printValues()
                currentObject._clearEfficiencyLists()
    
                #I go through "R" values first and create a list for that champion efficiencies.
                for k in range (3, 6):
                    #Calculating the actual efficiencies is all done in my champion class. Check that out for more info.
                    rList = currentObject._calculateREfficiency((k-2), baseADPerLevel[k-1], addedAD[k-1], addedAP[k-1], addedCDR[k-1])
                #Here I am just assigning the winners.
                if rList[0] > winnerR[0]:
                    winnerR[0] = rList[0]
                    winnerRName[0] = currentObject._returnChampName()
                if rList[1] > winnerR[1]:
                    winnerR[1] = rList[1]
                    winnerRName[1] = currentObject._returnChampName()
                if rList[2] > winnerR[2]:
                    winnerR[2] = rList[2]
                    winnerRName[2] = currentObject._returnChampName()
                    
                #Now lets do Q, W, E, R
                for j in range (1, 6):
                    #print "The AP Ratio is ", addedAP
                    qList = currentObject._calculateQEfficiency(j, baseADPerLevel[j-1], addedAD[j-1], addedAP[j-1], addedCDR[j-1])
                    wList = currentObject._calculateWEfficiency(j, baseADPerLevel[j-1], addedAD[j-1], addedAP[j-1], addedCDR[j-1])
                    eList = currentObject._calculateEEfficiency(j, baseADPerLevel[j-1], addedAD[j-1], addedAP[j-1], addedCDR[j-1])
                    #print "Q List: ", qList
          
                if qList[0] > winnerQ[0]:
                    winnerQ[0] = qList[0]
                    winnerQName[0] = currentObject._returnChampName()
                if qList[1] > winnerQ[1]:
                    winnerQ[1] = qList[1]
                    winnerQName[1] = currentObject._returnChampName()
                if qList[2] > winnerQ[2]:
                    winnerQ[2] = qList[2]
                    winnerQName[2] = currentObject._returnChampName()
                if qList[3] > winnerQ[3]:
                    winnerQ[3] = qList[3]
                    winnerQName[3] = currentObject._returnChampName()
                if qList[4] > winnerQ[4]:
                    winnerQ[4] = qList[4]
                    winnerQName[4] = currentObject._returnChampName()
                
                if wList[0] > winnerW[0]:
                    winnerW[0] = wList[0]
                    winnerWName[0] = currentObject._returnChampName()
                if wList[1] > winnerW[1]:
                    winnerW[1] = wList[1]
                    winnerWName[1] = currentObject._returnChampName()
                if wList[2] > winnerW[2]:
                    winnerW[2] = wList[2]
                    winnerWName[2] = currentObject._returnChampName()
                if wList[3] > winnerW[3]:
                    winnerW[3] = wList[3]
                    winnerWName[3] = currentObject._returnChampName()
                if wList[4] > winnerW[4]:
                    winnerW[4] = wList[4]
                    winnerWName[4] = currentObject._returnChampName()

                if eList[0] > winnerE[0]:
                    winnerE[0] = eList[0]
                    winnerEName[0] = currentObject._returnChampName()
                if eList[1] > winnerE[1]:
                    winnerE[1] = eList[1]
                    winnerEName[1] = currentObject._returnChampName()
                if eList[2] > winnerE[2]:
                    winnerE[2] = eList[2]
                    winnerEName[2] = currentObject._returnChampName()
                if eList[3] > winnerE[3]:
                    winnerE[3] = eList[3]
                    winnerEName[3] = currentObject._returnChampName()
                if eList[4] > winnerE[4]:
                    winnerE[4] = eList[4]
                    winnerEName[4] = currentObject._returnChampName()

            _easyPrinter(winnerQ, winnerQName, winnerW, winnerWName, winnerE, winnerEName, winnerR, winnerRName)
            #I zero everything out just in case to avoid weird numbers.
            winnerQ = [0, 0, 0, 0, 0]
            winnerQName = [0, 0, 0, 0, 0]
            winnerW = [0, 0, 0, 0, 0]
            winnerWName = [0, 0, 0, 0, 0]
            winnerE = [0, 0, 0, 0, 0]
            winnerEName = [0, 0, 0, 0, 0]
            winnerR = [0, 0, 0, 0, 0]
            winnerRName = [0, 0, 0, 0, 0]
            
            print "\n"
            i = 0
        elif (userInput01 == 'LEAVE' or userInput01 == 'leave' or userInput01 == 'Leave'):
            print "Thanks for using RitoPlsNerf OP Skills Calculator"
            sys.exit()
        elif (userInput01 == 'GET' or userInput01 == 'get' or userInput01 == 'Get'):
            print "\n"
            print "Type in the name of the champion you want to retrieve the object of. Be sure to capitalize the correct letters and spell correctly\n"
            print "For champion names greater than one word, simply type in the first part of it (ex. to search Twisted Faith, simply type the word Twisted)\n"
            print "IMPORTANT: The values in the object are not necessarily the values used in the calculations. Some values are manually changed within the program\n"

            champInput = (str)(raw_input('Type champion name exactly how it looks: '))
            winnerChampObject = 0
            #This is a real simple function that grabs the champ name that correspond with the one the user eneters. It then spits out the data using
            #a function from the champion class.
            for p in range (0, len(championObjectList)):
                #print championObjectList[p]._returnChampName()
                if (champInput in championObjectList[p]._returnChampName()):
                    winnerChampObject = championObjectList[p]
                    print winnerChampObject._printValues()
                    break
            if (winnerChampObject == 0):
                print "\nCouldn't find that champion. Sure you spelled everything right? Taking you back to the menu now.\n"

        elif (userInput01 == 'SKILLS' or userInput01 == 'skills' or userInput01 == 'Skills'):
            print "\n"
            print "Type in the name of the champ you want to retrieve the skill efficiencies of. Be sure to capitalize the correct letters and spell correctly\n"
            print "For champion names greater than one word, simply type in the first part of it (ex. to search Twisted Faith, simply type the word Twisted)\n"

            champInput2 = (str)(raw_input('Type champion name exactly how it looks: '))
            #winner2ChampObject = 0
            print len(championObjectList)
            for p in range (0, len(championObjectList)):
                #print championObjectList[p]._returnChampName()
                if (champInput2 in championObjectList[p]._returnChampName()):
                    winner2ChampObject = championObjectList[p]
                    print winner2ChampObject._printEff()
                    break
            if (winner2ChampObject == 0):
                print "Couldn't find that champion. Sure you spelled everything right? Taking you back to the menu now."

        else:
            print "Your input was incorrect! The program will now exit...\n"
            sys.exit()

if __name__ == "__main__":
    main()
    
