# Most-Efficient-Spells

*Note:  To actually view step by step instructions on how to run the program, please view the readMeFiles folder.* 

**Concepts Explored in Program**


Parsing JSONs using Python's built in parser, connecting to Riot API and learning to use their giant interface, grabbing data from Riot API from a URL and actually accessing it in the program, constructing objects on a huge scale


**Program Summary**


Whats up! This is a Python program that uses Riot API to grab static champion data and uses this data to figure out the most efficient Q, W, E, and R in the game based on levels and varying amounts of AP, AD, and CDR. It also takes into account every single champions AD and AP ratios.  Note: The AP, AD, and CDR numbers are *fully customizable* and are user inputted. 

**How Does it Work?**


The program is a little complicated.  So lemme layout how it works 


1. We connect to Riot API using a module called "requests" (find out more in the attached readMe folder).


2. Using specific fucntions from the API, I grab each champions Q, W, E, and R.  This means I get their skill specfic damage numbers, AD/AP ratios, and cooldown numbers. That's a lot of data! So it can take about 60 seconds to grab all of it. *Note*:  I only grab abilities that do damage, so things like Soraka's W (which is a heal) is ignored. 

3. I make each champion an object and put all the data I grab from the API into the object. I do this so that we have instant access to all this data. Imagine waiting 60 seconds for every single calculation. YUCK. 

4. At this point I have access to every single spell in the game that does damage.  I also have the spell's damage per level, cooldown per level, and AD/AP ratio per level.  Now the user will input varying amounts of AP, AD, and CDR.

5. Once the user inputs the proper numbers, the program will calculate efficieny based on damage per second. 


**Input**


![IMAGE MISSING](http://i.imgur.com/8ZCZqVM.png)

So what are all these numbers? So lets look at Level 1.  At Level 1 our make-beleive "champion" has 0 AD, 0 AP, 0 CDR. But as our "champion" buys items and gains level these numbers increase.  That is why at Level 5 it has 100 AD, 10 AP, and 5% CDR.

**Output**


![IMAGE MISSING](http://i.imgur.com/rezFA37.png)

Woah more numbers. So here we can see our final calculations. I output data based on the champions *level* and the specifc *skill* (Q/W/E/R). So at Level 1 Karthus has the most efficient Q in the game and does 40 Damage Per Second. But, at Level 2 Urgot has the most efficient Q at 92.63 Damage Per Second. This makes sense! As different champion gain levels and buy different items they become stronger than each other. 

In our input we have our fake "champion" lots of AD and CDR, but not much AP. So Urgot won out since he can just spam Q which has a low cooldown and scales with AD.  The program allows you to change these numbers all you want so you can obtain different results. 





