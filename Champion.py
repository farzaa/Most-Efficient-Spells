#Built by Farzain Majeed
#Riot QA 2015 Internship Test Program
#University of Central Florida

class Champion(object):

        #In this class I mainly comment things related to the "Q" skill, since W, E, R related methods are quite similar.
        #This class is quite long.  Its nothing really quite complicated, but rather its lengthy because it deals with many special cases for
        #champions that don't aren't easy to calculate for. It also includes things like hybrid ratio calculations, per second calculations, and
        #other random fixes for champion stats that were not parsed correctly from the JSON.

        #This is the object that we create for every champion.  It includes everything we need to know about a champion to calculate his or her DPS
        #This includes its name, ratios (and hybrid ratios), damage increase per level (if any), cooldowns, and more!
        #I do this so that we don't have to constantly grab from Riots Cloud.  That would be annoying and take lots of time. Time that could be used
        #to play League of Legends

        def __init__(self, championJSON):
            self.champName = championJSON['name']
            self.champID = championJSON['id']

            #initializing
            self.qDamagePerLevelList = []
            self.wDamagePerLevelList = []
            self.eDamagePerLevelList = []
            self.rDamagePerLevelList = []


            
            #I use try/except blocks quite of often in this program for one main reason
            #Not every champion has the same JSON. So in order to not look fro information that is out of bounds, I use
            #these try and except blocks to handle them accordingly.

            try:  
                self.qLabel = championJSON['spells'][0]['leveltip']['label'][0]
            except KeyError or IndexError:
                self.qLabel = 'NULL'
                print "Label for Q not found for ", self.ChampName

            #Most champions that do damage with an ability have the word "Damage" in their label.  If they don't, I manually add it later.
            if 'Damage' in self.qLabel:
                #Damage, CD, and Ratios were usually in the same place.  IF they weren't I would manually insert them later.

                #This retreives the damage the skill does (per level) as a string.  I parse this later.
                self.qDamage = self._checkDamage(0,1,championJSON)
                #Here I retreive the cool down per level of the skill as a list.  This is very convenient!
                self.qCoolDown = self._checkCoolDown(0,0,championJSON)
                #RatioType is the type of damage.  This program accounts for AD, BonusAD, and Magic Damage.
                #It doesn't account for percent health damage.
                self.qRatioType = self._checkRatioType(0,0,championJSON)
                #This is the actual ratio itself.
                self.qRatio = self._checkRatio(0,0,0,championJSON)
                #Initializing.
                self.qDamagePerLevelList = []
                #Damage actually comes in the form of a string.  This fucntion parses the string, and sticks the Damage Per Level into
                #an organized list.
                self._buildQDamageList()
                #Once again, I use these try and except blocks becasue I don't want my program crashing.
                #Here I am trying to get the hybrid ratio of the champion. Lets say I didn't have this try/except block.
                #Then if I try to look for something that isn't there, my program would crash.
                try:
                    self.qRatio.append(championJSON['spells'][0]['vars'][1]['coeff'][0])
                    self.qRatioType2 = championJSON['spells'][0]['vars'][1]['link']
                #If I run into any sort of error, I set my hybrid ratio type to NULL.
                except KeyError:
                    self.qRatioType2 = 'NULL'
                except IndexError:
                    self.qRatioType2 = 'NULL'
                except AttributeError:
                    self.qRatioType2 = 'NULL'
            #I have this here as a backup. Basically, if the skill doesn't have the word "Damage" in the label I set everything to NULL.
            #This is so that I don't have my program crash later on.
            else:
                self.qDamage = 'NULL'
                self.qCoolDown = 'NULL'
                self.qRatioType = 'NULL'
                self.qRatioType2 = 'NULL'
                self.qRatio = 'NULL'

            #I continue what I did for Q for the other three skills: W, E, and R.
            try:
                self.wLabel = championJSON['spells'][1]['leveltip']['label'][0]
            except KeyError or IndexError:
                self.wLabel = 'NULL'
                print "Label for W not found for ", self.ChampName
        
            if 'Damage' in self.qLabel:
                self.wDamage = self._checkDamage(1,1,championJSON)
                self.wCoolDown = self._checkCoolDown(1,0,championJSON)
                self.wRatioType = self._checkRatioType(1,0,championJSON)
                self.wRatio = self._checkRatio(1,0,0,championJSON)
                self.wDamagePerLevelList = []
                self._buildWDamageList()
                try:
                    self.wRatio.append(championJSON['spells'][1]['vars'][1]['coeff'][0])
                    self.wRatioType2 = championJSON['spells'][1]['vars'][1]['link']
                except KeyError:
                    self.wRatioType2 = 'NULL'
                except IndexError:
                    self.wRatioType2 = 'NULL'
                except AttributeError:
                    self.wRatioType2 = 'NULL'
            else:
                self.wDamage = 'NULL'
                self.wCoolDown = 'NULL'
                self.wRatioType = 'NULL'
                self.wRatioType2 = 'NULL'
                self.wRatio = 'NULL'
           
            try:
                self.eLabel = championJSON['spells'][2]['leveltip']['label'][0]
            except KeyError or IndexError:
                self.rLabel = 'NULL'
                print "Label for E not found for ", self.ChampName
            
            if 'Damage' in self.eLabel:
                self.eDamage = self._checkDamage(2,1,championJSON)
                self.eCoolDown = self._checkCoolDown(2,0,championJSON)
                self.eRatioType = self._checkRatioType(2,0,championJSON)
                self.eRatio = self._checkRatio(2,0,0,championJSON)
                self.eDamagePerLevelList = []
                self._buildEDamageList()
                try:
                    self.eRatio.append(championJSON['spells'][2]['vars'][1]['coeff'][0])
                    self.eRatioType2 = championJSON['spells'][2]['vars'][1]['link']
                except KeyError:
                    self.eRatioType2 = 'NULL'
                except IndexError:
                    self.eRatioType2 = 'NULL'
                except AttributeError:
                    self.eRatioType2 = 'NULL'
            else:
                self.eDamage = 'NULL'
                self.eCoolDown = 'NULL'
                self.eRatioType = 'NULL'
                self.eRatioType2 = 'NULL'
                self.eRatio = 'NULL'
 
            try:
                self.rLabel = championJSON['spells'][3]['leveltip']['label'][0]
            except KeyError or IndexError:
                self.rLabel = 'NULL'
                print "Label for R not found for ", self.ChampName
                
            if 'Damage' in self.rLabel:
                self.rDamage = self._checkDamage(3,1,championJSON)
                self.rCoolDown = self._checkCoolDown(3,0,championJSON)
                self.rRatioType = self._checkRatioType(3,0,championJSON)
                self.rRatio = self._checkRatio(3,0,0,championJSON)
                self.rDamagePerLevelList = []
                self._buildRDamageList()

                try:
                    self.rRatio.append(championJSON['spells'][3]['vars'][1]['coeff'][0])
                    self.rRatioType2 = championJSON['spells'][3]['vars'][1]['link']
                except KeyError:
                    self.rRatioType2 = 'NULL'
                except IndexError:
                    self.rRatioType2 = 'NULL'
                except AttributeError:
                    self.rRatioType2 = 'NULL'
                
            else:
                self.rDamage = 'NULL'
                self.rCoolDown = 'NULL'
                self.rRatioType = 'NULL'
                self.rRatioType2 = 'NULL'
                self.rRatio = 'NULL'
                
                
            #Check for a second, hybrid ratio.
           
            #self._buildQDamageList()
            #self._buildWDamageList()
         
            #Sometimes values for certain champions are wrong.
            self._specialCases(self.champName, championJSON)
            
            self.qEfficiency = []
            self.wEfficiency = []
            self.eEfficiency = []
            self.rEfficiency = []


            self.calculatedECoolDown  = 0
                 
        #We get the damage numbers as a string, that sucks.
        #Lets turn them into lists so they are easier to work with.
        def _buildQDamageList(self):
            #I dont want to build a list when the skill doesn't do damage!
            if self.qDamage == 'NULL':
                return
            qDamageLength = len(self.qDamage)
            letterCounter = 0
            qDamagePerLevel = ""
            #This is a very simply function that just converts the string to a list accordingly.
            #It also gets ride of those pesky slashes.
            for number in self.qDamage:
                letterCounter += 1

                if number == '/':
                    self.qDamagePerLevelList.append(float(qDamagePerLevel))
                    qDamagePerLevel = ""
                    continue

                if letterCounter == qDamageLength:
                    qDamagePerLevel = qDamagePerLevel + number
                    self.qDamagePerLevelList.append(float(qDamagePerLevel))
                    qDamagePerLevel = ""
                    break

                qDamagePerLevel = qDamagePerLevel + number

        def _buildWDamageList(self):
            if self.wDamage == 'NULL':
                return
            wDamageLength = len(self.wDamage)
            letterCounter = 0
            wDamagePerLevel = ""

            for number in self.wDamage:
                letterCounter += 1

                if number == '/':
                    self.wDamagePerLevelList.append(float(wDamagePerLevel))
                    wDamagePerLevel = ""
                    continue

                if letterCounter == wDamageLength:
                    wDamagePerLevel = wDamagePerLevel + number
                    self.wDamagePerLevelList.append(float(wDamagePerLevel))
                    wDamagePerLevel = ""
                    break

                wDamagePerLevel = wDamagePerLevel + number

        def _buildEDamageList(self):
            if self.eDamage == 'NULL':
                return
            eDamageLength = len(self.eDamage)
            letterCounter = 0
            eDamagePerLevel = ""

            for number in self.eDamage:
                letterCounter += 1

                if number == '/':
                    self.eDamagePerLevelList.append(float(eDamagePerLevel))
                    eDamagePerLevel = ""
                    continue

                if letterCounter == eDamageLength:
                    eDamagePerLevel = eDamagePerLevel + number
                    self.eDamagePerLevelList.append(float(eDamagePerLevel))
                    eDamagePerLevel = ""
                    break

                eDamagePerLevel = eDamagePerLevel + number
        def _buildRDamageList(self):
            if self.rDamage == 'NULL':
                return
            rDamageLength = len(self.rDamage)
            letterCounter = 0
            rDamagePerLevel = ""

            for number in self.rDamage:
                letterCounter += 1

                if number == '/':
                    self.rDamagePerLevelList.append(float(rDamagePerLevel))
                    rDamagePerLevel = ""
                    continue

                if letterCounter == rDamageLength:
                    rDamagePerLevel = rDamagePerLevel + number
                    self.rDamagePerLevelList.append(float(rDamagePerLevel))
                    rDamagePerLevel = ""
                    break

                rDamagePerLevel = rDamagePerLevel + number
        def _returnChampName(self):
            name = self.champName
            return name
        def _printObject(self):
            print self.champName
        #This is the fucntion that prints out efficiencies.
        def _printEff(self):
            print"\n"
            print "Raw Efficiency of Q (In order of levels 1, 5, 9, 13, 18)"
            print self.qEfficiency
            print"\n"
            print "Raw Efficiency of W (In order of levels 1, 5, 9, 13, 18)"
            print self.wEfficiency
            print"\n"
            print "Raw Efficiency of E (In order of levels 1, 5, 9, 13, 18)"
            print self.eEfficiency
            print"\n"
            print "Raw Efficiency of R (In order of levels 9, 13, 18)"
            print self.rEfficiency
            print"\n"
        #This is the function prints out a champs object values.
        def _printValues(self):
            print self.champName
            
            if 'Damage' in self.qLabel:
                print "Q"
                print "Damage of Q Per Level", self.qDamagePerLevelList
                print "CoolDown of Q Per Level ",self.qCoolDown
                print "Ratio Type of Q ", self.qRatioType
                print "Second Ratio Type of Q", self.qRatioType2
                print "Q Ratios (in order of types) ",self.qRatio
                print "\n"
            if 'Damage' in self.wLabel:
                print "W"
                print "Damage of W Per Level", self.wDamagePerLevelList
                print "CoolDown of W Per Level ",self.wCoolDown
                print "Ratio Type of W ", self.wRatioType
                print "Second Ratio Type of W", self.wRatioType2
                print "W Ratios (in order of types) ",self.wRatio
                print "\n"
            if 'Damage' in self.eLabel:
                print "E"
                print "Damage of E Per Level", self.eDamagePerLevelList
                print "CoolDown of E Per Level ",self.eCoolDown
                print "Ratio Type of E ", self.eRatioType
                print "Second Ratio Type of E", self.eRatioType2
                print "E Ratios (in order of types) ",self.eRatio
                print "\n"
            if 'Damage' in self.rLabel:
                print "R"
                print "Damage of R Per Level", self.rDamagePerLevelList
                print "CoolDown of R Per Level ",self.rCoolDown
                print "Ratio Type of R ", self.rRatioType
                print "Second Ratio Type of R", self.rRatioType2
                print "R Ratios (in order of types) ",self.rRatio
                print "\n"
        #The fucntion four fcuntions below are EXTREMELY important because they stop the program from crashing when it runes into
        #a part of the JSON that can't be parsed because it doesn't exist.
        def _checkDamage (self, a, b, championJSON):
            try:
                data = championJSON['spells'][a]['effectBurn'][b]
                return data
            except KeyError:
                #I set things to NULL when I can't find them in the JSON.
                return 'NULL'
            except IndexError:
                return 'NULL'
            
        def _checkCoolDown (self, a, b, championJSON):
            try:
                data = championJSON['spells'][a]['cooldown']
                return data
            except KeyError: 
                return 'NULL'
            except IndexError:
                return 'NULL'
            
        def _checkRatioType (self, a, b, championJSON):
            try:
                data = championJSON['spells'][a]['vars'][b]['link']
                return data
            except KeyError: 
                return 'NULL'
            except IndexError:
                return 'NULL'
            
        def _checkRatio(self, a, b, c, championJSON):
            try:
                data = championJSON['spells'][a]['vars'][b]['coeff']
                return data
            except KeyError: 
                return 'NULL'
            except IndexError:
                return 'NULL'
        #This is where we calculate efficinecy!
        def _calculateQEfficiency(self, level, baseAD, AD, AP, CDR):

            #If it doesn't do damage, it has no DPS and is instantly 0.
            if 'Damage' not in self.qLabel:
                return [0, 0, 0, 0, 0]
            #If it doesn't have some sort of ratio, then it doesn't do damage.
            if self.qRatioType == 'NULL':
                self.qEfficiency = [0, 0, 0, 0, 0]
                return self.qEfficiency
            #We calculate cooldown accordingly by going into the right place of our CoolDown List.
            #I do everything according to the level.
            calculatedQCoolDown = (self.qCoolDown[level-1])-(CDR*self.qCoolDown[level-1])
            calculatedQDamage = 0

            #The calculations differ according to what type of damage is done (ex. spell, AD, bonus AD)
            if 'spelldamage' in self.qRatioType:
                #print "AP being used in calculations is", AP
                calculatedQDamage = (self.qRatio[0]*AP) + self.qDamagePerLevelList[level-1]
            #Bonus attack damage is calculated with just the AD while attack damage is calculated with base AD as well.
            elif 'bonusattackdamage' in self.qRatioType:
                calculatedQDamage = (self.qRatio[0]*(AD)) + self.qDamagePerLevelList[level-1]
                #This is how I deal with champs with scaling ratios.
                try:
                    #print "Ratio", self.qRatio[level-1]
                    calculatedQDamage = (self.qRatio[level-1]*(AD)) + self.qDamagePerLevelList[level-1]
                    #print calculatedQDamage
                except KeyError:
                    pass
                except IndexError:
                    pass

            elif 'attackdamage' in self.qRatioType:
                #I give each champ a base AD value.
                calculatedQDamage = (self.qRatio[0]*(baseAD+AD)) + self.qDamagePerLevelList[level-1]
                #For champions with scaling ratios
                try:
                    #print "Ratio", self.qRatio[level-1]
                    calculatedQDamage = (self.qRatio[level-1]*(AD+baseAD)) + self.qDamagePerLevelList[level-1]
                    #print calculatedQDamage
                except KeyError:
                    pass
                except IndexError:
                    pass

            #If the champion has a hybrid ratio, I take that into account as well.  That's why I have this again.
            if 'spelldamage' in self.qRatioType2:
                calculatedQDamage = self.qRatio[1]*AP +calculatedQDamage
            elif 'bonusattackdamage' in self.qRatioType2:
                calculatedQDamage = self.qRatio[1]*AD +calculatedQDamage
            elif 'attackdamage' in self.qRatioType2:
                calculatedQDamage = self.qRatio[1]*(AD+baseAD)+calculatedQDamage

            newDamage = self._specialQCalculations(calculatedQDamage, self.champName, AD, AP)
            #I override Zed's Q cooldown since he uses energy!
            #By the rules of this program, he doesn't regain energy which means he can cast 6Q's before losing all his energy.
            if (self.champName == 'Zed'):
                calculatedQCoolDown = 10
            #Here I manually give champions who don't have a CD on their Q a 60 second CD. This is so that we don't divide by zero later on.
            #This does not affect the actual calculations at all.
            if (self.champName == 'Singed'):
                calculatedQCoolDown = 60
            #Rumble uses heat! The rule for heat is that we don't allow any regen. Lets adjust the CD to reflect this.
            #Rumnble can use 5 Q's in a minute before running out of energy with zero regen.
            if (self.champName == 'Rumble'):
                calculateQCoolDown = 12

            if (newDamage == 0):
                #print "CD", calculatedQCoolDown
                #print "DMG", calculatedQDamage
                calculatedQEfficiency = ((60.0/calculatedQCoolDown)*calculatedQDamage)/60
                self.qEfficiency.append(calculatedQEfficiency)
                return self.qEfficiency
            else:
                calculatedQEfficiency = ((60.0/calculatedQCoolDown)*newDamage)/60
                self.qEfficiency.append(calculatedQEfficiency)
                return self.qEfficiency
            '''
            print "Printing Q Stuff"
            print calculatedQCoolDown
            print calculatedQDamage
            print calculatedQEfficiency
            '''
        
        def _calculateWEfficiency(self, level, baseAD, AD, AP, CDR):
            #print "WHERE AM MAN", self.champName
            if 'Damage' not in self.wLabel:
                return [0, 0, 0, 0, 0]
            if self.wRatioType == 'NULL':
                self.wEfficiency = [0, 0, 0, 0, 0]
                return self.wEfficiency
            calculatedWCoolDown = (self.wCoolDown[level-1])-(CDR*self.wCoolDown[level-1])
            calculatedWDamage = 0

            if 'spelldamage' in self.wRatioType:
                calculatedWDamage = (self.wRatio[0]*AP) + self.wDamagePerLevelList[level-1]
            elif 'bonusattackdamage' in self.wRatioType:
                calculatedWDamage = (self.wRatio[0]*(AD)) + self.wDamagePerLevelList[level-1]
            elif 'attackdamage' in self.wRatioType:
                calculatedWDamage = (self.wRatio[0]*(baseAD+AD)) + self.wDamagePerLevelList[level-1]
                #For champions with scaling ratios
                try:
                    calculatedWDamage = (self.wRatio[level-1]*(AD+baseAD)) + self.wDamagePerLevelList[level-1]
                except KeyError:
                    pass
                except IndexError:
                    pass

            if 'spelldamage' in self.wRatioType2:
                calculatedWDamage = self.wRatio[1]*AP +calculatedWDamage
                #print calculatedWDamage
            elif 'bonusattackdamage' in self.wRatioType2:
                calculatedWDamage = self.wRatio[1]*AD +calculatedWDamage
            elif 'attackdamage' in self.wRatioType2:
                calculatedWDamage = self.wRatio[1]*(AD+baseAD)+calculatedWDamage
                
            newDamage = self._specialWCalculations(calculatedWDamage, self.champName, AD, AP)

            if (self.champName == 'Amumu'):
                calculatedECoolDown = 60

            if (newDamage == 0):
                calculatedWEfficiency = ((60.0/calculatedWCoolDown)*calculatedWDamage)/60
                self.wEfficiency.append(calculatedWEfficiency)
                return self.wEfficiency
            else:
                calculatedWEfficiency = ((60.0/calculatedWCoolDown)*newDamage)/60
                self.wEfficiency.append(calculatedWEfficiency)
                return self.wEfficiency

            '''    
            calculatedWEfficiency = ((60.0/calculatedWCoolDown)*calculatedWDamage)/60
            self.wEfficiency.append(calculatedWEfficiency)

            print "Printing W Stuff"
            print calculatedWCoolDown
            print calculatedWDamage
            print calculatedWEfficiency
            print "\n"
            '''


        def _calculateEEfficiency(self, level, baseAD, AD, AP, CDR):

            if 'Damage' not in self.eLabel:
                self.eEfficiency = [0, 0, 0, 0, 0]
                return [0, 0, 0, 0, 0]
            if self.eRatioType == 'NULL':
                self.eEfficiency = [0, 0, 0, 0, 0]
                return self.eEfficiency
            calculatedEDamage = 0
            calculatedECoolDown = (self.eCoolDown[level-1])-(CDR*self.eCoolDown[level-1])
            '''
            #I manually give Karthus E a 60 second CD to avoid dividing by zero below.
            #This has no affect on the actual calculations and stops the program from crashing later on.
            if (self.champName == 'Karthus'):
                calculatedECoolDown = 60
            #EnergyRegen is not accounted for. So We give Zed a 15 second cooldown.
            #15 Second because with 200 Energy /50 Cost = 4 Q's in a minute.
            if (self.champName == 'Zed'):
                calculatedECoolDown = 15
            '''
            if 'spelldamage' in self.eRatioType:
                calculatedEDamage = (self.eRatio[0]*AP) + self.eDamagePerLevelList[level-1]
            elif 'bonusattackdamage' in self.eRatioType:
                calculatedEDamage = (self.eRatio[0]*(AD)) + self.eDamagePerLevelList[level-1]
            elif 'attackdamage' in self.eRatioType:
                calculatedEDamage = (self.eRatio[0]*(baseAD+AD)) + self.eDamagePerLevelList[level-1]
                #print "1", calculatedEDamage
                try:
                    #print "WE ARE IN THE TRY!", self.eRatio[level-1]
                    calculatedEDamage = (self.eRatio[level-1]*(AD+baseAD)) + self.eDamagePerLevelList[level-1]
                    #print "THE TRY IS WORKING!", calculatedEDamage
                except KeyError:
                    pass
                except IndexError:
                    pass
            if 'spelldamage' in self.eRatioType2:
                calculatedEDamage = self.eRatio[1]*AP +calculatedEDamage
                #print "2", calculatedEDamage
            elif 'bonusattackdamage' in self.eRatioType2:
                calculatedEDamage = self.eRatio[1]*AD +calculatedEDamage
            elif 'attackdamage' in self.eRatioType2:
                calculatedEDamage = self.eRatio[1]*(AD+baseAD)+calculatedEDamage

            newDamage = self._specialECalculations(calculatedEDamage, self.champName, AD, AP, level)

            if (self.champName == 'Karthus'):
                calculatedECoolDown = 60
            if (self.champName == 'Zed'):
                calculatedECoolDown = 15
                #print "E.CD", calculatedECoolDown

            if (newDamage == 0):
                calculatedEEfficiency = ((60.0/calculatedECoolDown)*calculatedEDamage)/60
                self.eEfficiency.append(calculatedEEfficiency)
                return self.eEfficiency
            else:
                calculatedEEfficiency = ((60.0/calculatedECoolDown)*newDamage)/60
                self.eEfficiency.append(calculatedEEfficiency)
                return self.eEfficiency
                
            #elif 'persecondspelldmg'
            #elif 'persecondattackdmg
            '''       
            print "Printing E Stuff"
            print calculatedECoolDown
            print calculatedEDamage
            print calculatedEEfficiency
            print "\n"
            '''

        def _calculateREfficiency(self, level, baseAD, AD, AP, CDR):

            if 'Damage' not in self.rLabel:
                self.rEfficiency = [0, 0, 0]
                return [0, 0, 0]
            if self.rRatioType == 'NULL':
                self.rEfficiency = [0, 0, 0]
                return self.rEfficiency
            
            calculatedRCoolDown = (self.rCoolDown[level-1])-(CDR*self.rCoolDown[level-1])
            calculatedRDamage = 0
            
            #if 'spelldmgpersec' in self.rRatioType

            if 'spelldamage' in self.rRatioType:
                calculatedRDamage = (self.rRatio[0]*AP) + self.rDamagePerLevelList[level-1]
            elif 'bonusattackdamage' in self.rRatioType:
                calculatedRDamage = (self.rRatio[0]*(AD)) + self.rDamagePerLevelList[level-1]
                #print calculatedRDamage
            elif 'attackdamage' in self.rRatioType:
                calculatedRDamage = (self.rRatio[0]*(baseAD+AD)) + self.rDamagePerLevelList[level-1]

            if 'spelldamage' in self.rRatioType2:
                calculatedRDamage = self.rRatio[1]*AP +calculatedRDamage
            elif 'bonusattackdamage' in self.rRatioType2:
                calculatedRDamage = self.rRatio[1]*AD +calculatedRDamage
            elif 'attackdamage' in self.rRatioType2:
                calculatedRDamage = self.rRatio[1]*(AD+baseAD)+calculatedRDamage

            newDamage = self._specialRCalculations(calculatedRDamage, self.champName, AD, AP)
            if (self.champName == 'Anivia'):
                calculatedRCoolDown = 60
            if (self.champName == 'Swain'):
                calculatedRCoolDown = 60

            if (newDamage == 0):
                calculatedREfficiency = ((60.0/calculatedRCoolDown)*calculatedRDamage)/60
                self.rEfficiency.append(calculatedREfficiency)
                return self.rEfficiency
            else:
                calculatedREfficiency = ((60.0/calculatedRCoolDown)*newDamage)/60
                self.rEfficiency.append(calculatedREfficiency)
                #print "1", self.rEfficiency
                return self.rEfficiency
            '''
            print "Printing R Stuff"
            print calculatedRCoolDown
            print calculatedRDamage
            print calculatedREfficiency
            print "\n"
            '''
        def _clearEfficiencyLists(self):
            self.qEfficiency = []
            self.wEfficiency = []
            self.eEfficiency = []
            self.rEfficiency = []

        #This method is used do special damage calculations for any champion that may need it.
        #For example, Morgana W does damage per second, which needs to be taken into account.
        def _specialQCalculations(self, calculatedQDamage, champName, AD, AP):

            #Singed does continuous damage.
            if(champName == 'Singed'):
                return calculatedQDamage*60
            if(champName == 'Heimerdinger'):
                return calculatedQDamage*60
            #Rumble Q does per second damage!
            if (champName == 'Rumble'):
                return calculatedQDamage*6
            #Riven has 3 procs!
            if (champName == 'Riven'):
                return calculatedQDamage*3
            #Sivir had a weird Ratio in that she had scaling AD and a single AP.
            #The easiest way to fix this was to make a special case below.
            if (champName == 'Sivir'):
                return calculatedQDamage + (0.5*AP)
            if (champName == 'Skarner'):
                return calculatedQDamage + (0.3*AP)
            if (champName == 'Swain'):
                return calculatedQDamage*3
            return 0

        def _specialWCalculations(self, calculatedWDamage, champName, AD, AP):
            #Morgana does damage per half second damage!
            if(champName == 'Morgana'):
                return calculatedWDamage*10
            #Fixing a bug with TF Calculations
            if champName == 'Twisted Fate':
                return calculatedWDamage + AD
              #Fizz does per second damage.
            if champName == 'Fizz':
                #17 is the average of his second set of damage numbers.
                #I use the average b/c this program doesn't use two damage sets.
                return calculatedWDamage
            if champName == 'Jayce':
                #print calculatedWDamage
                return calculatedWDamage*4
            if champName == 'Corki':
                return calculatedWDamage*2
            if champName == 'Shyvanna':
                return calculatedWDamage*3
            #Per second damage on Heca W!
            if champName == 'Hecarim':
                return calculatedWDamage*4
            if champName == 'Shaco':
                return calculatedWDamage*5
            if champName == 'Amumu':
                return calculatedWDamage*60
            return 0

        def _specialECalculations(self, calculatedEDamage, champName, AD, AP, level):
            #Karthus does constant damage for 60 seconds.
            if(champName == 'Karthus'):
                return calculatedEDamage*60
            #Garen does per second damage
            if(champName == 'Garen'):
                #Garen E Lasts for 3 seconds!
                return calculatedEDamage*3
            if (champName == 'Swain'):
                return calculatedEDamage*4
            if (champName == 'Urgot'):
                return calculatedEDamage*5
            if (champName == 'Ziggs'):
                ziggsSecondnaryEDamage = [16, 26, 36, 46, 56]
                #Ziggs does less damage after his first mine is popped.
                return calculatedEDamage + ((level-1)*10)
            if (champName == 'Blitzcrank'):
                #Blitz E does his attack damage!
                return calculatedEDamage + AD
            return 0

        def _specialRCalculations(self, calculatedRDamage, champName, AD, AP):
            if (champName == 'Viktor'):
                #Viktor R does per half second damage for 7 seconds.
                return calculatedRDamage + ((45 + (0.10*AP))*14)
            #Anivia does constant damage for 60 seconds.
            if (champName == 'Anivia'):
                return calculatedRDamage*60
            #Rumble R does per second damage!
            if (champName == 'Rumble'):
                return calculatedRDamage*5
            #Kat R does dmg per second!
            if (champName == 'Katarina'):
                return calculatedRDamage*10
            #Udyr R does per second dmg.
            if (champName == 'Udyr'):
                return calculatedRDamage*5
            if (champName == 'Teemo'):
                return calculatedRDamage*5
            if (champName == 'Swain'):
                return calculatedRDamage*60
            if (champName == 'Fiddlesticks'):
                return calculatedRDamage*5
            if (champName == 'Rammus'):
                return calculatedRDamage*8
            if (champName == 'Wukong'):
                return calculatedRDamage*4
            return 0

        #The following 700 lines or so is me manually adjusting certain values for certain champions.
        #This is for champs who were not built correctly after their JSON was parsed.
        #There isn't much I could say here other than it took a while LOL.
        #But for most champions the JSON was parsed perfectly.
        def _specialCases(self, champName, championJSON):
                 
            if champName == 'Aatrox':
                self.rDamage = '200/300/400'
                self.rDamagePerLevelList = []
                self._buildRDamageList()
                return
            if champName == 'Cassiopeia':
                self.eRatioType = 'spelldamage'
                self.eRatio = [0.55]
                return
            if champName == 'Lux':
                self.qDamage = '60/110/160/210/260'
                self.qDamagePerLevelList = []
                self._buildQDamageList()
                self.eDamage = '60/105/150/195/240'
                self.eDamagePerLevelList = []
                self._buildEDamageList()
                self.rDamage = '300/400/500'
                self.rDamagePerLevelList = []
                self._buildRDamageList()
                return
            #COME BACK TO THIS
            if champName == 'Garen':
                self.qRatio = [0.40]
                self.eRatioType = 'attackdamage'
                self.eRatio = [0.36]
                self.rRatioType = 'attackdamage'
                self.rRatio = [0.00]
                return
            if champName == 'Maokai':
                self.rDamage = '100/150/200'
                self.rDamagePerLevelList = []
                self._buildRDamageList()
                return
            if champName == 'Heimerdinger':
                #Heim R is an upgrade to his OTHER abilities. Therefore it doesn't count.
                self.rRatioType = 'NULL'
                self.rRatioType2 = 'NULL'

                self.qRatioType = 'spelldamage'
                self.qRatioType2 = 'NULL'
                self.qRatio = [0.15]

                #Heim turrets last as long as they are up! So they have no cooldown.
                self.qCoolDown = [60, 60, 60, 60, 60]

                return
            if champName == 'Lulu':
                self.eLabel = 'Damage'
                self.eDamage = '80/110/140/170/200'
                self.eDamagePerLevelList = []
                self._buildEDamageList()
                self.eCoolDown = [10, 10, 10, 10, 10]
                self.eRatioType = 'spelldamage'
                self.eRatio = [0.4]
                self.wRatio = [1.0]
                self.wRatioType = 'attackdamage'
                return
            if champName == 'Vayne':
                self.qDamage = '1/1/1/1/1'
                self.qDamagePerLevelList = []
                self._buildQDamageList()
                return
            if champName == 'Udyr':
                self.rLabel = 'Damage'
                self.rDamage = '15/25/35/45/55'
                self.rDamagePerLevelList = []
                self._buildRDamageList()
                self.rCoolDown = [6, 6, 6, 6, 6]
                self.rRatio = [0.25]
                self.rRatioType = 'spelldamage'
                return
            if champName == 'Leona':
                self.qDamage = '50/70/100/130/160'
                self.qDamagePerLevelList = []
                self._buildQDamageList()
                self.wLabel = 'Damage'
                self.wDamage = '60/110/160/210/260'
                self.wDamagePerLevelList = []
                self._buildWDamageList()
                self.wCoolDown = [14, 14, 14, 14, 14]
                self.wRatioType = 'spelldamage'
                self.wRatio = [0.4]
                self.rDamage = '150/250/350'
                self.rDamagePerLevelList = []
                self._buildRDamageList()
                return
            if champName == 'Riven':
                self.eRatioType = 'NULL'
                return
            if champName == 'Caitlyn':
                self.qLabel = 'Damage'
                self.qDamage = '25/70/115/160/205'
                self.qDamagePerLevelList = []
                self._buildQDamageList()
                self.qRatioType = 'attackdamage'
                self.qRatio = [1.6]

                self.wLabel = 'NULL'
                self.wRatioType = 'spelldamage'
                self.wDamage = '80/130/180/230/280'
                self.wDamagePerLevelList = []
                self._buildWDamageList()

                self.rLabel = 'Damage'
                self.rDamage = '250/475/700'
                self.rDamagePerLevelList = []
                self._buildRDamageList()

                self.eLabel = 'Damage'
                self.eDamage = '70/110/150/190/230'
                self.eDamagePerLevelList = []
                self._buildEDamageList()

                return
            if champName == 'Nidalee':
                self.qRatioType2 = 'NULL'
                self.qRatio.remove(1.2)
                self.wDamage = '10/20/30/40/50'
                self.wDamagePerLevelList = []
                self._buildWDamageList()
                self.wCoolDown = [13, 12, 11, 10, 9]
                self.wRatio = [0.05]
                return
            if champName == 'Kennen':
                self.eDamage = '65/95/125/155/185'
                self.eDamagePerLevelList = []
                self._buildEDamageList()
                self.eCoolDown = [14, 12, 10, 8, 6]
                self.eRatio = [0.55]
                self.eRatioType = 'spelldamage'
                return
            if champName == 'Gnar':
                self.qRatioType2 = 'NULL'
                self.qRatio.remove(1.2)
                self.wRatioType = 'spelldamage'
                self.wRatioType2 = 'NULL'
                self.eRatioType = 'NULL'
                self.eRatio = [0.06]
                return
            if champName == 'Vi':
                self.wRatioType = 'NULL'
                self.eCoolDown = [14, 12.5, 11, 9.5, 8]
                self.qRatioType2 = 'NULL'
                self.qRatio.remove(1.4)
                self.eRatio[0] = 0.15
                return
            if champName == 'Elise':
                self.rRatioType = 'NULL'
                self.wDamage = '75/125/175/225/275'
                self.wDamagePerLevelList = []
                self._buildWDamageList()
                return
            if champName == 'Nunu':
                self.qRatioType = 'NULL'
                return
            if champName == 'Twisted Fate':
                #I manually add TF's AD (on W) in later in the calculations.
                #I remove the E! Its AA based. So we take it out.
                self.eRatioType = 'NULL'
                self.eRatioType2 = 'NULL'
                self.wRatioType = 'spelldamage'
                self.wRatioType2 = 'NULL'
                self.wRatio.remove(1.0)
                return
            if champName == 'Jax':
                self.rRatioType = 'NULL'
                self.eLabel ='Damage'
                self.eDamage = '50/75/100/125/150'
                self.eDamagePerLevelList = []
                self._buildEDamageList()
                self.eCoolDown = [16, 14, 12, 10, 8]
                self.eRatioType = 'bonusattackdamage'
                self.eRatio = [0.5]
                return
            if champName == 'Shyvana':
                #We can't figure out her CD without knowing fury! Better to just remove it.
                self.rRatioType = 'NULL'
                #Q does dmg, based on AD
                self.qDamage = '1/1/1/1/1'
                self.qDamagePerLevelList = []
                self._buildQDamageList()
                return
            if champName == 'Kalista':
                self.wLabel = 'Nothing'
                self.eRatioType = 'NULL'
                self.qLabel = 'Damage'
                self.qDamage = '10/70/130/190/250'
                self.qDamagePerLevelList = []
                self._buildQDamageList()
                self._buildQDamageList()
                self.qCoolDown = [8, 8, 8, 8, 8]
                self.qRatioType = 'attackdamage'
                self.qRatio = [1.0]
                return
            if champName == 'Dr. Mundo':
                self.qRatioType = 'targetmaxhealth'
                self.qRatio = [0.21]
                self.eRatioType = 'mymaxhealth'
                self.eRatio = [0.05]
                return
            if champName == 'Tahm Kench':
                self.qDamage = '80/125/170/215/260'
                self.qDamagePerLevelList = []
                self._buildQDamageList()
                return
            if champName == 'Ezreal':
                self.qRatioType2 = 'attackdamage'
                self.qRatio.append(1.10)
                self.eRatioType2 = 'bonusattackdamage'
                self.wRatioType2 = 'NULL'
                self.eRatio[0] = 0.75
                self.eRatio.append(0.50)
            if champName == 'Ashe':
                self.wLabel = 'Damage'
                self.wDamage = '20/35/50/65/80'
                self.wDamagePerLevelList = []
                self._buildWDamageList()
                self.wCoolDown = [12, 10, 8, 6, 4]
                self.wRatioType = 'attackdamage'
                self.wRatio = [1.0]
                return
            if champName == 'Annie':
                self.eRatioType = 'NULL'
                self.rRatio.remove(0.2)
                self.rRatioType2 = 'NULL'
                return
            if champName == 'Poppy':
                self.eDamage = '50/70/90/110/130'
                self.eDamagePerLevelList = []
                self._buildEDamageList()
                self.qDamage = '40/70/100/130/160'
                self.qDamagePerLevelList = []
                self._buildQDamageList()
                self.rDamage = '200/300/400'
                self.rDamagePerLevelList = []
                self._buildRDamageList()

            if champName == 'Lee Sin':
                self.wRatioType = 'NULL'
                return
            if champName == 'VoliBear':
                self.wRatioType = 'NULL'
                return
            if champName == 'Syndra':
                self.wCoolDown = [12, 11, 10, 9, 8]
                self.rRatioType2 = 'NULL'
                self.rRatio.remove(0.2)
                return
            if champName == 'Azir':
                self.qCoolDown = [10, 9, 8, 7, 6]
                self.eCoolDown = [19, 18, 17, 16, 15]
                self.eDamage = '60/90/120/150/180'
                self.eDamagePerLevelList = []
                self._buildEDamageList()
                return
            if champName == 'Rumble':
                self.qRatio = [0.167]
                self.wRatioType = 'NULL'
                self.eCoolDown = [5.0, 5.0, 5.0, 5.0, 5.0]
                self.qDamage = '12.5/22.5/32.5/42.5/52.5'
                self.qDamagePerLevelList = []
                self._buildQDamageList()
                return
            if champName == 'Zed':
                #Have energy so that once there is no more. The champion is done.
                self.rRatioType = 'NULL'
                self.wRatioType = 'NULL'
                self.wRatioType2 = 'NULL'
                return
            if champName == 'Diana':
                self.wRatioType2 = 'NULL'
                self.wRatio.remove(0.3)
                self.wDamage = '66/102/138/174/210'
                self.wDamagePerLevelList = []
                self._buildWDamageList()
                self.rDamage = '100/160/220'
                self.rDamagePerLevelList = []
                self._buildRDamageList()
                return
            #Sadly I had to make Rek Sai from scratch. Her JSON was simply to odd to parse through.
            if 'Rek' in champName:
                self.qRatioType = 'spelldamage'
                self.qRatioType2 = 'NULL'
                self.qDamage = '60/90/120/150/180'
                self.qDamagePerLevelList = []
                self._buildQDamageList()
                self.qRatio.remove(0.2)

                self.wDamage = '40/80/120/160/200'
                self.wDamagePerLevelList = []
                self._buildWDamageList()
                self.wRatioType = 'bonusattackdamage'

                #Reksai E doesn't do dmg, tho it does have a ratio which does do dmg.
                self.eDamage = '1/1/1/1/1'
                self.eDamagePerLevelList = []
                self._buildEDamageList()
                self.eRatioType = 'attackdamage'
                self.eRatio = [0.8, 0.9, 0.1, 1.1, 1.2]
                return
            if champName == 'Quinn':
                self.eDamage = '40/70/100/130/160'
                self.eDamagePerLevelList = []
                self._buildEDamageList()
                #Rats! I have to build Quinn's R by hand!
                self.rLabel = 'Damage'
                self.rDamage = '100/150/200'
                self.rDamagePerLevelList = []
                self._buildRDamageList()
                self.rCoolDown = [140, 110, 80]
                self.rRatioType = 'bonusattackdamage'
                self.rRatio = [0.5]
                return
            if champName == 'Akali':
                #I need to manually adjust Akali's skills because she uses energy.
                #We are not working with unlimited energy!
                self.eCoolDown = [10, 9, 8, 7, 6]
                #This accounts for the R stacks.
                self.rCoolDown = [10, 10, 10]
                return
            #Hecarim was returned rather broken after parsing his JSON! I patched him up.
            if champName == 'Hecarim':
                self.wLabel = 'NULL'
                self.eDamage = '40/75/110/145/180'
                self.eDamagePerLevelList = []
                self._buildEDamageList()
                self.qDamage = '40/63.3/86.7/110/133.3'
                self.qDamagePerLevelList = []
                self._buildQDamageList()
                #Had to manually create Hecarim's W
                self.wLabel = 'Damage'
                self.wDamage = '20/30/40/50/60'
                self.wDamagePerLevelList = []
                self._buildWDamageList()
                self.wCoolDown = [22, 21, 20, 19, 18]
                self.wRatioType = 'spelldamage'
                self.wRatio = [0.2]
                self.eRatioType2 = 'NULL'
                self.eRatio.remove(1.0)
                return
            if champName == 'Lucian':
                #Attack speed based so not included.
                self.rLabel = 'NULL'
                return
            if champName == 'Skarner':
                #Skarner Q damages comes strictly from his ratios
                self.qDamage = '1/1/1/1/1'
                self.qDamagePerLevelList = []
                self._buildQDamageList()
                #W doesn't do dmg.
                self.qRatio = [0.33, 0.36, 0.39, 0.42, 0.45]
                #I calculate Skarners Q AP ratio damages later!!!
                self.qRatioType = 'attackdamage'
                self.qRatioType2 = 'NULL'
                self.wRatioType = 'NULL'
                self.wRatioType2 = 'NULL'
                self.rDamage = '20/60/100'
                self.rDamagePerLevelList = []
                self._buildRDamageList()
                return
            if champName == 'Rengar':
                self.qLabel = 'Damage'
                self.qDamage = '30/60/90/120/150'
                self.qDamagePerLevelList = []
                self._buildQDamageList()
                self.qCoolDown = [6, 5.5, 5, 4.5, 4]
                self.qRatioType = 'attackdamage'
                self.qRatio = [0.0, 0.05, 0.10, 0.15, 0.20]

                self.wLabel = 'Damage'
                self.wDamage = '50/80/110/140/170'
                self.wDamagePerLevelList = []
                self._buildWDamageList()
                self.wCoolDown = [12, 12, 12, 12, 12]
                self.wRatioType = 'spelldamage'
                self.wRatio = [0.8]

                self.eCoolDown = [10, 10, 10, 10, 10]
                return
            if champName == 'Malphite':
                self.eRatioType = 'spelldamage'
                self.eRatio = [0.2]
                self.eRatioType2 = 'NULL'
                self.rDamage = '200/300/400'
                self.rDamagePerLevelList = []
                self._buildRDamageList()
                self.eDamage = '60/100/140/180/220'
                self.eDamagePerLevelList = []
                self._buildEDamageList()
                return
            if champName == 'Yasuo':
                self.eCoolDown = [10, 9, 8, 7, 6]
                self.rCoolDown = [80, 55, 30]
                return
            if champName == 'Irelia':
                self.eRatioType2 = 'NULL'
                self.eRatio = [0.5]
            if champName == 'Xerath':
                self.rDamage = '190/245/300'
                self.rDamagePerLevelList = []
                self._buildRDamageList()
                self.wCoolDown = [14, 13, 12, 11, 10]
                self.wRatio = [0.60]
                return
            if champName == 'Teemo':
                self.eLabel = 'NULL'
                self.rLabel = 'Damage'
                self.rDamage = '50/81.25/112.5'
                self.rDamagePerLevelList = []
                self._buildRDamageList()
                self.rCoolDown = [22, 20, 18, 16, 14]
                self.rRatioType = 'spelldamage'
                self.rRatio = [.125]
                return
            if champName == 'Draven':
                self.qLabel = 'NULL'
                return
            if champName == 'Corki':
                self.eRatioType = 'NULL'
                #make CD recharge time.
                self.rCoolDown = [12,10,8]
                self.rRatio[0] = 0.3
                self.rRatio.remove(0.3)
                self.eDamage = '10/16/22/28/34'
                self.eDamagePerLevelList = []
                self._buildEDamageList()
                self.eRatioType = 'bonusattackdamage'
                self.eRatio = [1.6]
                self.qDamage = '80/130/180/230/280'
                self.qDamagePerLevelList = []
                self._buildQDamageList()
                self.qRatioType = 'bonusattackdamage'
                self.qRatioType2 = 'spelldamage'
                self.qRatio = [0.5, 0.5]
                self.wDamage = '30/45/60/75/90'
                self.wDamagePerLevelList = []
                self.wRatioType2 = 'NULL'
                self._buildWDamageList()
                self.wRatio = [0.20]
                return
            if champName == 'Fiddlesticks':
                self.eDamage = '65/85/105/125/145'
                self.eDamagePerLevelList = []
                self._buildEDamageList()
                return
            if 'Gath' in champName:
                self.eLabel = 'NULL'
                self.rLabel = 'Damage'
                self.rDamage = '300/475/650'
                self.rDamagePerLevelList = []
                self._buildRDamageList()
                self.rCoolDown = [80, 80, 80, 80, 80]
                self.rRatio = [0.7]
                self.rRatioType = 'spelldamage'
                return
            if champName == 'Kindred':
                self.qRatioType = 'attackdamage'
                self.qRatio = [0.2]
                self.wRatioType = 'attackdamage'
                self.wRatio = [0.4]
                self.eRatioType = 'attackdamage'
                self.eRatio = [0.2]
                
            if champName == 'Ekko':
                self.rRatio = [1.3]
                self.eRatioType2 = 'NULL'
                self.eRatio = [0.2]
                self.rRatioType2 = 'NULL'
            if 'Kog' in champName:
                self.rCoolDown = [2, 1.5, 1]
                return
            if champName == 'LeBlanc':
                self.rLabel = 'NULL'
                self.qRatioType2 = 'NULL'
                del self.qRatio[1]
                return
            if champName == 'Nocturne':
                self.rDamage = '150/250/350'
                self.rDamagePerLevelList = []
                self._buildRDamageList()
                return
            if champName == 'Master Yi':
                self.wRatioType = 'NULL'
                self.eRatioType = 'NULL'
                self.rRatioType = 'NULL'
                self.qRatioType2 = 'NULL'
                self.qRatio.remove(0.6)
                return
            if champName == 'Zyra':
                self.qRatioType2  = 'NULL'
                self.qRatio.remove(0.2)
                self.eRatioType2  = 'NULL'
                self.eRatio.remove(0.2)
                self.rDamage = '180/265/350'
                self.rDamagePerLevelList = []
                self._buildRDamageList()
                return
            if 'Vel' in champName:
                self.wCoolDown = [19, 18, 17, 16, 15]
                return
            if champName == 'Renekton':
                self.wRatio.remove(2.25)
                self.wRatioType2 = 'NULL'
                self.qRatioType2 = 'NULL'
                del self.qRatio[1]
                self.eRatioType2 = 'NULL'
                self.eRatio.remove(1.35)
                return
            if champName == 'Miss Fortune':
                return
            if champName == 'Katarina':
                self.wRatioType = 'bonusattackdamage'
                self.wRatio[1] = 0.25
                self.eRatioType2 = 'NULL'
                #KATARINA HAS A HYBRID R!
                self.rRatio[0] = 0.375
                self.rRatio[1] = 0.25
                return
            if champName == 'Blitzcrank':
                self.rDamage = '250/375/500'
                self.rDamagePerLevelList = []
                self._buildRDamageList()
                self.rRatioType2 = 'NULL'
                self.rRatio.remove(0.20)
                self.eLabel = 'Damage'
                self.eDamage = '1/1/1/1/1'
                self.eDamagePerLevelList = []
                self._buildEDamageList()
                self.eCoolDown = [9, 8, 7, 6, 5]
                self.eRatioType = 'attackdamage'
                self.eRatio = [0.0]
                return
            if 'Kha' in champName:
                self.qRatio.remove(1.56)
                self.qRatioType2 = 'NULL'
                self.wRatio.remove(0.5)
                self.wRatioType2 = 'NULL'
                return
            if champName == 'Tryndamere':
                self.qRatioType = 'NULL'
                self.qRatioType2 = 'NULL'
                return
            if champName == 'Gragas':
                self.wDamage = '20/50/80/110/140'
                self.wDamagePerLevelList = []
                self._buildWDamageList()
                return
            if champName == 'Ryze':
                self.eRatioType2 = 'NULL'
                self.eRatio.remove(0.1)
                return
            if champName == 'Sion':
                self.rRatio.remove(0.8)
                self.rRatioType2 ='NULL'
                self.qRatio.remove(1.8)
                self.qRatioType2 = 'NULL'
                return
            if champName == 'Nautilus':
                self.qRatio.remove(0.5)
                self.qRatioType2 = 'NULL'
                return
            if champName == 'Karma':
                self.eLabel = 'NULL'
                return
            if champName == 'Viktor':
                self.qRatio.remove(0.5)
                self.qRatioType2 = 'NULL'
                self.rRatioType2 = 'NULL'
                self.rRatio.remove(0.2)
                self.rDamage = '150/250/350'
                self.rDamagePerLevelList = []
                self._buildRDamageList()
                return
            if(champName == 'Morgana'):
                self.wRatio.remove(0.33)
                self.wRatio.remove(0.22)
                self.wRatio = [0.11]
                self.wRatioType2 = 'NULL'
                return
            if(champName == 'Anivia'):
                #We have unlimited mana. So we give Anivia R a 60 second CD
                #This is equivalent to no cooldown in my calculations
                self.rCoolDown = [60, 60, 60]
                return
            if champName == 'Kassadin':
                self.rCoolDown = [6, 4, 2]
                self.qRatioType2 = 'NULL'
                self.qRatio.remove(0.3)
                self.wRatioType2 = 'NULL'
                self.wRatio.remove (0.1)
                self.wDamage = '40/65/90/115/140'
                self.wDamagePerLevelList = []
                self._buildWDamageList()
                return
            if (champName == 'Lissandra'):
                #Liss heal does not count as damage.
                self.rRatio.remove(0.3)
                self.rRatioType2 = 'NULL'
                return
            if champName == 'Mordekaiser':
                #Morde Q is AA based
                self.qLabel = 'NULL'
                #Morde W is ally based
                self.wLabel = 'NULL'
                self.eDamage = '35/65/95/125/155'
                self.eDamagePerLevelList = []
                self._buildEDamageList()
                return
            if champName == 'Sona':
                self.qDamage = '40/80/120/160/200'
                self.qDamagePerLevelList = []
                self._buildQDamageList()
                self.qRatioType2 = 'NULL'
                self.qRatio.remove(0.2)
                return
            if champName == 'Alistar':
                self.eLabel = 'Damage'
                self.eDamage = '55/110/165/220/275'
                self.eDamagePerLevelList = []
                self._buildEDamageList()
                self.eCoolDown = [14, 13, 12, 11, 10]
                self.eRatioType = 'spelldamage'
                self.eRatio = [0.7]
                return
            if champName == 'Darius':
                self.qDamage = '20/35/50/65/80'
                self.qDamagePerLevelList = []
                self._buildQDamageList()
                #We take the avergae of his ratios. Darius is one of few champs thats have this scaling ratio.
                self.qRatio = [0.5, .55, .6, .65, .7]
                return
            if champName == 'Varus':
                self.wRatioType2 = 'NULL'
                self.wRatio.remove(0.02)
                return
            if champName == 'Galio':
                self.rRatioType2 = 'NULL'
                self.rRatio.remove(1.08)
                return
            if champName == 'Graves':
                self.wDamage = '60/110/160/210/260'
                self.wDamagePerLevelList = []
                self._buildWDamageList()
                self.rRatioType2 = 'NULL'
                #self.rRatio.remove(1.2)

                self.qLabel = 'Damage'
                self.qDamage = '60/80/100/120/140'
                self.qDamagePerLevelList = []
                self._buildQDamageList()
                self.qCoolDown = [14, 13, 12, 11, 10]
                self.qRatioType = 'bonusattackdamage'
                self.qRatio = [0.75]

                self.rLabel = 'Damage'
                self.rDamage = '250/400/550'
                self.rDamagePerLevelList = []
                self._buildRDamageList()
                self.rCoolDown = [100, 90, 80]
                self.rRatioType = 'bonusattackdamage'
                self.rRatio = [1.5]
                return
            if champName == 'Kayle':
                self.rRatioType2 = 'NULL'
                #AA Based
                self.eRatioType = 'NULL'
                self.eRatioType2 = 'NULL'
                return
            if champName == 'Sejuani':
                self.qDamage = '60/90/120/150/180'
                self.qDamagePerLevelList = []
                self._buildQDamageList()
                self.eDamage = '40/70/100/130/160'
                self.eDamagePerLevelList = []
                self._buildEDamageList()
                self.eRatio = [0.6]
                return
            if champName == 'Vladamir':
                self.rRatioType2 = 'NULL'
                self.rRatio.remove(0.25)
                self.wDamage = '120/170/220/170/320'
                self.wDamagePerLevelList = []
                self._buildWDamageList()
                return
            if champName == 'Zac':
                #I calculate the damage for 4 bounces all at once here.
                self.rDamage = '560/840/1120'
                self.rDamagePerLevelList = []
                self._buildRDamageList()
                return
            if champName == 'Tristana':
                self.wLabel = 'Damage'
                self.wDamage = '80/105/130/155/180'
                self.wDamagePerLevelList = []
                self._buildWDamageList()
                self.wCoolDown = [22, 20, 18, 16, 14]
                self.wRatioType = 'spelldamage'
                self.wRatio = [0.5]
                self.eDamage = '60/70/80/90/100'
                self.eDamagePerLevelList = []
                self._buildEDamageList()
                self.eRatioType = 'bonusattackdamage'
                self.eRatioType2 = 'spelldamage'
                #I took the average of her ratios in this special case.
                self.eRatio[0] = 0.8
                self.eRatio[1] = 0.5
                return
            if champName == 'Warwick':
                self.rRatio[0] = 0.4
                return
            if champName == 'Nasus':
                self.qRatio[0] = 0
                self.qRatio[1] = 0
                self.eDamagePerLevelList = []
                self._buildEDamageList()
                self.eRatio.remove(0.12)
                self.eRatioType2 = 'NULL'
                return
            if champName == 'Swain':
                self.eLabel = 'Damage'
                self.eDamage = '20/30/45/57/70'
                self.eDamagePerLevelList = []
                self._buildEDamageList()
                self.eCoolDown = [10, 10, 10, 10, 10]
                self.eRatioType = 'spelldamage'
                self.eRatio = [0.23]
                return
            if champName == 'Talon':
                self.qDamage = '30/60/90/120/150'
                self.qDamagePerLevelList = []
                self._buildQDamageList()
                self.qRatio.remove(1.2)
                self.qRatioType2 = 'NULL'
                self.rDamage = '120/170/220'
                self.rDamagePerLevelList = []
                self._buildRDamageList()
                return
            if champName == 'Janna':
                self.qRatioType2 = 'NULL'
                self.qRatio.remove(0.1)
                self.wLabel = 'Damage'
                self.wDamage = '60/115/170/225/280'
                self.wDamagePerLevelList = []
                self._buildWDamageList()
                self.wCoolDown = [12, 12, 12, 12, 12]
                self.wRatioType = 'spelldamage'
                self.wRatioType2 = 'NULL'
                self.wRatio = [0.5]
                return
            if champName == 'Fiora':
                self.qRatio = [0.55, 0.70, 0.85, 1.0, 1.15]
                self.wCoolDown = [19, 18, 17, 16, 15]
                self.wRatioType = 'spelldamage'
                self.wRatio = [1.0]
                return
            if champName == 'Jinx':
                self.rRatio.remove(1.0)
                self.rRatioType2 = 'NULL'
                self.wLabel = 'Damage'
                self.wDamage = '10/60/110/160/210'
                self.wDamagePerLevelList = []
                self._buildWDamageList()
                self.wCoolDown = [10, 9, 8, 7, 6]
                self.wRatioType = 'attackdamage'
                self.wRatio = [1.4]
                return
            if champName == 'Yorick':
                self.qRatioType = 'NULL'
                self.wDamage = '60/95/130/165/200'
                self.wDamagePerLevelList = []
                self._buildWDamageList()
                return
            if champName == 'Urgot':
                self.wRatioType = 'NULL'
                self.eDamage = '15/26/37/48/59'
                self.eDamagePerLevelList = []
                self._buildEDamageList()
                self.eRatio = [0.12]
                return
            if champName == 'Wukong':
                self.qRatio = [0.10]
                self.rRatio = [1.1]
                return
            if champName == 'Shen':
                self.eLabel = 'Damage'
                self.eDamage = '50/85/120/155/190'
                self.eDamagePerLevelList = []
                self._buildEDamageList()
                self.eCoolDown = [16, 14, 12, 10, 18]
                self.eRatioType = 'spelldamage'
                self.eRatio = [0.5]
                self.qRatioType2 = 'NULL'
                self.qRatio.remove(6.0)
                self.wLabel = "NULL"
                return
            if champName == 'Braum':
                self.qRatioType = 'spelldamage'
                self.qRatio = [0.00]
                return
            if champName == 'Twitch':
                #All of Twitch's skills are AA based.
                self.eLabel = 'NULL'
                self.rLabel = 'NULL'
                return
            if champName == 'Taric':
                self.eLabel = 'Damage'
                self.eDamage = '40/70/100/130/160'
                self.eDamagePerLevelList = []
                self._buildEDamageList()
                self.eCoolDown = [18, 17, 16, 15, 14]
                self.eRatioType = 'spelldamage'
                self.eRatio = [0.2]
                return
            if champName == 'Amumu':
                self.eDamage = '75/100/125/150/175'
                self.eDamagePerLevelList = []
                self._buildEDamageList()
                #Amumu W has no cooldown if you keep it onnall time! So I adjust his CD to 60.
                self.wDamage = '8/12/16/20/24'
                self.wDamagePerLevelList = []
                self._buildWDamageList()
                self.wCoolDown = [60, 60, 60, 60, 60]
                return
            if champName == 'Gangplank':
                self.rLabel = 'Damage'
                self.rDamage = '600/840/1080'
                self.rDamagePerLevelList = []
                self._buildRDamageList()
                self.rCoolDown = [140, 130, 120]
                self.rRatioType = 'attackdamage'
                self.rRatio = [1.2]
                return
            if champName == 'Trundle':
                self.qRatio = [0, 0.05, .1, .15, .2]
                return
            if champName == 'Nami':
                self.wLabel = 'Damage'
                self.wDamage = '70/110/150/190/230'
                self.wDamagePerLevelList = []
                self._buildWDamageList()
                self.wCoolDown = [10, 10, 10, 10, 10]
                self.wRatioType2 = 'NULL'
                self.wRatio = [0.5]
                self.eRatioType = 'NULL'
                self.eRatioType2 = 'NULL'
                self.eRatio = []
                return
            if champName == 'Jarvan IV':
                self.qRatio = [1.2]
                self.eDamage = '60/105/150/195/240'
                self.eDamagePerLevelList = []
                self._buildEDamageList()
                return
            if champName == 'Jayce':
                self.wRatio =[0.25]
                return


            return