import tkinter
import tkinter as tk
import mysql.connector
mycon=mysql.connector.connect(host="localhost",user="root",passwd="***",database="crime_management_system")
mycursor=mycon.cursor()
file=open("crime.txt","a")
text=print("\n *************************FBI**************************\n*********************CRIME MANAGEMENT***********************\n We see that when a group or society is formed, the people make some rules and laws, for the people and to the people. The purpose of these rules and laws are to ensure a  peaceful life to all in that society. Whenever any law is violated by anyone, we say that crime is committed and who break that law is called criminal. To have a peaceful life, we need a well-organized law enforcement system.\nThis management system is a database project which helps you in keeping the records of the crime happening around an area.\nThe benefits of the system:\n• To keep record of the criminals\n• To  record  improvement, decline the  rules  and regulation activities of the Country.\n• To  keep  record  of  criminals  details  for  future investigation\n• To keep record of criminals' crime activities\n• Reduce manual and redundant records keeping\n• Facilitate interaction and sharing of information among police  departments,  districts,  state/headquarters  and other police agencies.\nmenu\n1 = INSERT RECORD\n2 = DISPLAY RECORDS\n3 = SEARCH FOR RECORD BY AN INFO \n4 = AWARENESS")
file.write("\n")
file.close()
file=open("crime.txt","r")
display=file.read()
print(display)
file.close()


from tkinter import *
from tkinter.ttk import *


# importing only those functions
# which are needed
# importing only those functions
# which are needed
from tkinter import * 
from tkinter.ttk import *
  
# creating tkinter window
master= Tk()
  
# Adding widgets to the root window
Label(master, text = 'crime management system', font =(
  'Verdana', 15)).pack(side = TOP, pady = 10)
  
# Creating a photoimage object to use image
photo = PhotoImage(file = r"C:\Users\user\Pictures\Saved Pictures\crime.png")
  
# here, image option is used to
# set image on button
Button(master, text = 'Click Me !', image = photo).pack(side = TOP)
  
mainloop()
from tkinter.filedialog import askopenfilename
# here, image option is used to
# set image on button
# label text

import tkinter

root = tkinter.Tk()
root.geometry("300x300")
root.title("enter code")

entry = tkinter.Entry(root)
entry.pack()
print(entry.get())
def on_button():
    while True:
        if entry.get() == "6201" or entry.get() == "6201": #corrected
            slabel = tkinter.Label(root, text="access granted\n click cancel when asked 'your program is still running? do you want to kill it?'")
            slabel.pack()
            root.mainloop()
        else:
            tlabel = tkinter.Label(root, text="access denied")
            tlabel.pack()
            root.denied()
            exit()
        break
    

button = tkinter.Button(root, text="Enter", command=on_button)
button.pack()

root.mainloop()



def mainloop():

    print("Welcome")

def choice():
    while True:
        X=int(input("enter your choice:"))
        if X==1:
            print("you have chosen to insert records: You can enter the details of a criminal to store the data for further reference. Please ensure that you enter all the details in single/double quotes:)")
            name=str(input("name:"))
            alias=str(input("alias:"))
            age=str(input("age:"))
            sex=str(input("sex:"))
            height=str(input("height in cm:"))
            eyecolour=str(input("eye color:"))
            haircolour=str(input("hair color:"))
            scarsandmarks=str(input("scars and marks:"))
            city=str(input("city:"))
            nationality=str(input("nationality:"))
            chargeanddescription=str(input("charge an description:"))
            arrestingofficer=str(input("arresting officer:"))
            crimetechnique=str(input("crime technique:"))
            query="INSERT INTO crime_records(NAME,ALIAS,AGE,SEX,HEIGHT,EYECOLOUR,HAIRCOLOUR,SCARSANDMARKS,CITY,NATIONALITY,CHARGEANDDESCRIPTION,ARRESTINGOFFICER,CRIMETECHNIQUE)VALUES("+name+","+alias+","+age+","+sex+","+height+","+eyecolour+","+haircolour+","+scarsandmarks+","+city+","+nationality+","+chargeanddescription+","+arrestingofficer+","+crimetechnique+")"
            mycursor.execute(query)
            print("inserted successfully")
        elif X==2:
            display()
        elif X==3:
            search()
        elif X==4:
            intro()
        else:
            print("OUT OF BOUNDS, TRY AGAIN!")
            break
def exits():
    while True:
        print("YOU HAVE EXITED")
        print("THANK YOU FOR VISITING US :)")
        break
    
def insrt():
    print("you have chosen to insert records: You can enter the details of a criminal to store the data for further reference. Please ensure that you enter all the details in single/double quotes:)")
    name=str(input("name:"))
    alias=str(input("alias:"))
    age=str(input("age:"))
    sex=str(input("sex:"))
    height=str(input("height in cm:"))
    eyecolour=str(input("eye color:"))
    haircolour=str(input("hair color:"))
    scarsandmarks=str(input("scars and marks:"))
    city=str(input("city:"))
    nationality=str(input("nationality:"))
    chargeanddescription=str(input("charge an description:"))
    arrestingofficer=str(input("arresting officer:"))
    crimetechnique=str(input("crime technique:"))
    query="INSERT INTO crime_records(NAME,ALIAS,AGE,SEX,HEIGHT,EYECOLOUR,HAIRCOLOUR,SCARSANDMARKS,CITY,NATIONALITY,CHARGEANDDESCRIPTION,ARRESTINGOFFICER,CRIMETECHNIQUE)VALUES("+name+","+alias+","+age+","+sex+","+height+","+eyecolour+","+haircolour+","+scarsandmarks+","+city+","+nationality+","+chargeanddescription+","+arrestingofficer+","+crimetechnique+")"
    mycursor.execute(query)
    print("inserted successfully")
    x=input("would you like to continue?(y/n)")
    if x in "Yy":
        choice()
    if x in "Nn":
        exits()
        exit()  
    

def display():
    while True:
        print("you have chosen to display the records: By continuing you can see all the criminals and their details")
        query1="SELECT * FROM crime_records;"
        mycursor.execute(query1)
        rows = mycursor.fetchall()
        for row in rows:
            print(row)
        mycon.commit()
        x=input("would you like to continue?(y/n)")
        if x in "Yy":
            choice()
        if x in "Nn":
            exits()
            exit()  

def search():
    print("you have chosen to search for a record by an info: You can browse for a criminal, crime or their details by entering a specific info. Note: you won't be getting the info if the data does not exist in our system")
    x=str(input("enter data:"))
    mycursor.execute("SELECT * FROM crime_records WHERE name="+x+" OR alias="+x+" OR age="+x+" OR sex="+x+" OR height="+x+" OR sex="+x+" OR height="+x+" OR eyecolour="+x+" OR haircolour="+x+" OR scarsandmarks="+x+" OR nationality="+x+" OR chargeanddescription="+x+" OR arrestingofficer="+x+" OR crimetechnique="+x+";")
    rows1 = mycursor.fetchall()
    for row in rows1:
        if True:
            print(row)
            mycon.commit()
            break
    else:
        print("data does not exist")
    x=input("would you like to continue?(y/n)")
    if x in "Yy":
        choice()
    if x in "Nn":
        exits()
        exit()  

def intro():
    try:
        print('please choose one from the below options:\n1. few necessary self defence moves you may need \n2. how to handle hostage situations \n3. Awareness on human trafficking \n4. How to act during gun shots.\n5. cyber crimes')
        n=int(input("enter your choice:"))
        if n==1:
            root = Tk()
            T = Text(root, height=350, width=350)
            T.pack()
            T.insert(END, 'Carry protection. Whether pepper spray, a personal safety alarm, or a lipstick taser, self-defense tools can help you feel more at ease.\nnote>>>Focus on your attacker’s vulnerable places: eyes, nose, throat, and groin. Aim all of the moves below at one or several of these areas to have maximum impact.Don’t aim for the chest, as that tends to be ineffective. Aiming for the knees requires a specific kick that can be too risky for the average person.\n1. Hammer strike\nUsing your car keys is one of the easiest ways to defend yourself. Don’t use your fingernails, because you’re more at risk to injure your hands.\nInstead, if you feel unsafe while walking at night, have your keys stick out from one side of your fist for hammer strikes.\n2. Heel palm strike\nThis move can cause damage to the nose or throat. To execute, get in front of your attacker as much as is possible.\nTo perform:\n•With your dominant hand, flex your wrist.\n•Aim for either the attacker’s nose, jabbing upward from the nostrils, or underneath the attacker’s chin, jabbing upward at the throat.\n•Make sure to recoil your strike. Pulling your arm back quickly will help thrust the attacker’s head up and back.\n•This will cause your attacker to stagger backward, allowing you to escape their grasp.\n•Alternative: An open palm to the ears can be very disorienting.\n3. Groin kick\nIf someone is coming at you from the front, a groin kick may deliver enough force to paralyze your attacker, making your escape possible.\nTo perform:\n• Stabilize yourself as best you can.\n• Lift your dominant leg off the ground and begin to drive your knee upward.\n• Extend your dominant leg, drive hips forward, slightly lean back, and kick forcefully, making contact between your lower shin or ball of your foot and the attacker’s groin area.\nAlternative: If your attacker is too close, thrust your knee toward the groin. Make sure you’re stabilized and not at risk of falling over.\n4. Elbow strike\nIf your attacker is in close range and you’re unable to get enough momentum to throw a strong punch or kick, use your elbows.\nTo perform:\n• If you can, stabilize yourself with a strong core and legs to ensure a powerful blow.\n• Bend your arm at the elbow, shift your weight forward, and strike your elbow into your attacker’s neck, jawline, chin, or temple. These are all effective targets.\n• This may cause your attacker to loosen their grip, allowing you to run.\n5. Escape from a ‘bear hug attack’\nFor cases where the attacker is coming from behind, you’ll want to use this move. Focus on getting low and creating space to free yourself.\nTo perform:\n• Bend forward from the waist. This shifts your weight forward, making it more difficult for your attacker to pick you up. It also gives you a better angle to throw elbows from side to side to the attacker’s face.\n• Turn into the attacker with one of your elbows and continue counterattacking.\n• This should give you space to turn fully, using another move to injure the face or strike the groin. With the space these moves have created, you may be able to escape and run away.')
            root.mainloop()
        if n==2:
            root = Tk()
            T = Text(root, height=350, width=350)
            T.pack()
            T.insert(END,'HOW TO ACT IN HOSTAGE SITUATION\n•Remain calm, be polite, and cooperate with your captors.\n•DO NOT attempt escape unless there is an extremely good chance of survival. It is safer to be submissive and obey your captors.\n•Speak normally. DO NOT complain, avoid being belligerent, and comply with all orders and instructions.\n•DO NOT draw attention to yourself with sudden body movements, statements, comments, or hostile looks.\n•Observe the captors and try to memorize their physical traits, voice patterns, clothing, or other details that can help provide a description later.\n•Avoid getting into political or ideological discussions with your captors.\n•Try to establish a relationship with your captors and get to know them. Captors are less likely to harm you if they respect you.\n•If forced to present terrorist demands to authorities, either in writing or on tape, state clearly that the demands are from your captors. Avoid making a plea on your own behalf.\n•Try to stay low to the ground or behind cover from windows or doors, if possible.')
            root.mainloop()
        if n==3:
            root = Tk()
            T = Text(root, height=300, width=300)
            T.pack()
            T.insert(END,'WHAT TO DO \n•Fundraising\nHolding a fundraiser and donating the money raised to one of the countless organizations that help to fight human trafficking not only gives money to the cause but also brings awareness to the issue. Most organizations working to fight human trafficking are nonprofit organizations that rely on donations. Holding fundraisers helps maintain these nonprofits.\n•Volunteer\nVolunteering time and effort to an anti-trafficking organization is a great way to contribute to the fight against human trafficking. In addition to helping the organization itself, the more volunteers there are, the greater the outreach can be. For example, Unseen is a nonprofit organization that helps victims of human trafficking by providing specialist care to help them along the road to recovery. There are several volunteer roles with Unseen, ranging in levels of time commitment.\n•Be aware of the signs of human trafficking\nBeing educated on signs that could indicate someone is a victim of human trafficking increases the likelihood of reporting and could give a voice to victims who do not feel comfortable speaking out for themselves. Signs that someone is a victim of human trafficking come in several categories. Poor work and living conditions, poor mental health and lack of control are some of the main areas to look for.\n•Advocate\nMeeting with or reaching out to local, state and federal representatives informs them that their constituents are passionate about fighting human trafficking, and brings the issue to their attention. This increases the likelihood that they will do something about it. \n•Hold events to raise awareness\nRaising awareness for human trafficking can also get more people involved and interested in joining the fight. It can create a chain reaction, leading to more people lobbying, fundraising and educating themselves. Regardless of what the event is, they are efficient ways to raise awareness for a cause and gain new followers.\n•Boycott products and companies that permit human trafficking\nMany goods produced around the world are products of victims of human trafficking. Being conscientious about the products consumed and the companies supported is an easy way to contribute to the fight against human trafficking. An easy way to find out what products contribute to a “slavery footprint,” is the Department of Labor’s List of Goods Produced by Child Labor or Forced Labor.\n•Help survivors\nDonate clothes and other goods to shelters for victims of human trafficking. Also, encourage businesses to give jobs to survivors, helping them get back on their feet and get a fresh start. If applicable, offering legal advice to survivors allows them an opportunity to not only move forward but to gain justice. Helping survivors and contributing to their recovery stops the cycle of trauma in its tracks and ensures it won’t repeat itself.\n•Stay informed\nThere are many anti-trafficking nonprofits with blogs and updates that people can subscribe to, keeping them in the loop of any new information or solutions to human trafficking. For example, the nonprofit organization Polaris Project offers updates via email for anyone who chooses to subscribe.\n•Report suspicions \nIt is important to know the resources available. When traveling abroad, it is beneficial to look up the emergency phone number of the given country, to enable quick reports should a trafficking victim be spotted.\n•Help combat the demand\nThe main factor that keeps human trafficking such a big issue is the constant demand for cheap labor and exploitation. Traffickers often turn to websites such as Craigslist and Backpage to target vulnerable potential victims. Enforcing stricter validity checks on websites like these and offering jobs through more reliable online platforms is attacking the problem at its root, and stopping human trafficking before it even begins.')
            root.mainloop()
        if n==4:
            root = Tk()
            T = Text(root, height=350, width=350)
            T.pack()
            T.insert(END,'THINGS TO DO \nRUN: \n•If there is considerable distance between you and the gunfire/armed person, quickly move away from the sound of the gunfire/armed person. If the gunfire/armed person is in your building and it is safe to do so, run out of the building and move far away until you are in a secure place to hide.\n•Leave your belongings behind.\n•Keep your hands visible to law enforcement.\n•Take others with you, but do not stay behind because others will not go.\n•Call 100 when it is safe to do so. Do not assume that someone else has reported the incident. The information that you are able to provide law enforcement may be critical, e.g. number of shooters, physical description and identification, number and type(s) of weapons, and location of the shooter.\nHIDE: \n•If the shooter is in close proximity and you cannot evacuate safely, hide in an area out of the armed person’s view.\n•Choose a hiding place with thicker walls and fewer windows, if possible.\n•Lock doors and barricade with furniture, if possible.\n•Turn off lights\n•Silence phones and turn off other electronics.\n•Close windows, shades and blinds, and avoid being seen from outside the room, if possible.\n•If you are outdoors and cannot RUN safely, find a place to hide that will provide protection from gunfire such as a brick wall, large trees or buildings.\n•Remain in place until you receive an “all clear” signal.\nFIGHT: \n•As a last resort, fight. If you cannot evacuate or hide safely and only when your life is in imminent danger, take action.\n•Attempt to incapacitate or disrupt the actions of the shooter.\n•Act with physical aggression toward the shooter.\n•Use items in your area such as fire extinguishers or chairs.\n•Throw items at the shooter if possible.\n•Call 100 when it is safe to do so.')
            root.mainloop()
        if n==5:
            root = Tk()
            T = Text(root, height=350, width=350)
            T.pack()
            T.insert(END,'Despite our best efforts, our increasingly digital lives may put us in harm’s way. The fact remains that the bad guys continue to find new uses for ever-expanding—but easily accessible—online technologies to steal, harass, and commit all sorts of crime. If cybercrime happens to you, you need to know what to do and to respond quickly. Cybercrime in all its many forms (e.g., online identity theft, financial fraud, stalking, bullying, hacking, e-mail spoofing, information piracy and forgery, intellectual property crime, and more) can, at best, wreak havoc in victims’ lives through major inconvenience and annoyance. At worst, cybercrime can lead to financial ruin and potentially threaten a victim’s reputation and personal safety.\nWHO TO CONTACT:\n•Local law enforcement\n•IC3: refer www.ic3.gov/default.aspx.\n•Federal Trade Commission: refer www.ftccomplaintassistant.gov/FTC_Wizard.aspx?Lang=en.\n•Your Local Victim Service Provider: ovc.ncjrs.gov/findvictimservices/search.asp\nCOLLECT AND KEEP EVIDENCE\nIt’s important to keep any evidence you may have related\nto your complaint. Evidence may include the following:\n•Canceled checks\n•Certified or other mail receipts\n•Chatroom or newsgroup text\n•Credit card receipts\n•Envelopes (if you received items via FedEx, UPS, or U.S. Mail)\n•Facsimiles\n•Log files, if available, with date, time and time zone\n•Messages from Facebook, Twitter or other social networking sites\n•Money order receipts\n•Pamphlets or brochures\n•Phone bills\n•Printed or preferably electronic copies of emails(if printed, include full email header information)\n•Printed or preferably electronic copies of web pages\n•Wire receipts\n>>note: •Disconnect and Detach: In case of an ongoing attack on your computer or IT infrastructure, your first step should be to disconnect the device from the Internet as this is the most effective way to prevent further loss of data\nIn case of cyber bullying or cyber stalking, one should simply step away from the screen before proceeding to initiate legal action.\nIn the event of a successful phishing attack where you are conned into revealing private and confidential information, you should immediately initiate steps like:\n•Freeze your bank accounts and credit cards\n•Alter your Internet and mobile banking passwords\nIN CASE OF IDENTITY THEFT:\n•Make sure you change your passwords for all online accounts. Make it long, strong and unique, with a mix of upper and lowercase letters, numbers and symbols.\n•Inform your Contacts\n•Theft of your virtual identity can be misused by the cyber criminals to steal information and data from all your online contacts. Use social media to spread word about the incident. This simple step will minimise risk of your identity being misused to commit further crimes, and will ensure better awareness about cyber crime amongst your friends and relatives.\n•Close any unauthorized or compromised credit or charge accounts. Inform the companies that someone may beusing your identity, and find out if there have been any unauthorized transactions.\n•Think about what other personal information may be at risk. You may need to contact other agencies depending on the type of theft.\n•File a report with your local law enforcement agency. You will need to provide a copy of the law enforcement report to your banks, creditors, other businesses, credit bureaus, etc.\n•If your personal information has been stolen through a corporate data breach, you will likely be contacted by the business or agency whose data was compromised with additional instructions, as appropriate.\n•If stolen money or identity is involved, contact one of the three credit bureaus to report the crime (Equifax at 1-800-525-6285, Experian at 1-888-397-3742, or TransUnion at 1-800-680-7289). Request that the credit bureau place a fraud alert on your credit report to prevent any further fraudulent activity from occurring. As soon as one of the bureaus issues a fraud alert, the other two bureaus are automatically notified.\nIN CASES OF SOCIAL SECURITY FRAUD:\n•If you believe someone is using your social security number for employment purposes or to fraudulently receive Social Security benefits, contact the Social Security Administration’s fraud hotline at 1-800-269-0271. Request a copy of your social security statement to verify its accuracy.For additional resources, visit the Social Security Administration at oig.ssa.gov/report-fraud-waste-or-abuse.\nIN CASES ONLINE STALKING:\n•In cases where the offender is known, send the stalker a clear written warning saying the contact is unwanted and asking that the perpetrator cease sending communications of any kind.\n•Save copies of all communication from the stalker (e.g.,emails, threatening messages, messages via social media) and document each contact, including dates, times and additional circumstances, when appropriate.\n•File a complaint with the stalker’s Internet Service Provider (ISP) and yours. Many ISPs offer tools that filter or block communications from specific individuals.\n•Own your online presence. Set security and privacy settings on social networks and other services to your comfort level of sharing.\n•Consider changing your email address and ISP; use encryption software or privacy protection programs on your computer and mobile devices. (Consult with law enforcement before changing your email account.)')
            root.mainloop()
    except EOFError:
        print("error")
    x=input("would you like to continue?(y/n)")
    if x in "Yy":
        choice()
    if x in "Nn":
        exits()
        exit()  

def denied():
    print("sorry! you were denied")
        
mainloop()       
while True:
    x=input("would you like to continue?(y/n)")
    if x in "Yy":
        choice()
    if x in "Nn":
        break

print("YOU HAVE EXITED")
print("THANK YOU FOR VISITING US :)")


def denied():
    print("sorry! you were denied")

