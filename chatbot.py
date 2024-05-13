import pymongo

client=pymongo.MongoClient("mongodb://localhost:27017")
print(client)
db = client["database"]
col = db["faculty info"]
 
x = col.find()
 
for data in x:
    print(data)
from tkinter import *
root = Tk()
def send():
    send = "You:"+ e.get()
    text.insert(END,"\n" + send)
    if(e.get()=='hi'):
        text.insert(END, "\n" + "Bot: hello, Please enter the faculty name ")
    elif(e.get()=='hello'):
        text.insert(END, "\n" + "Bot: hi, Please enter the faculty name") 
    elif (e.get() == 'Dr Shrddha sagar'):
        text.insert(END, "\n" + "Bot: Dr. shrddha sagar  \n cabin number:- c-350 \n contact number:- 9650433534 \n email id:- shrddha.sagar@galgotiasuniversity.edu.in ")
    elif (e.get() == 'Dr Ajay sikandar'):
        text.insert(END, "\n" + "Bot: Dr Ajay Sikandar \n cabin number:- c-011 \n contact number:- 7840098564 \n email id:- ajay.sikandar@galgotiasuniversity.edu.in")
    elif (e.get() == 'Ms Greeshma G.S'):
        text.insert(END, "\n" + "Bot:Ms Greeshma G.S \n cabin number:- c-Cubical Room 3rd floor \n contact number:- 9645455738 \n email id:- greeshma.gs@galgotiasuniversity.edu.in")
    elif (e.get() == 'Ms Ruchi Sharma'):
        text.insert(END, "\n" + "Bot:Ms Ruchi Sharma \n cabin number:- c-Cubical Room 4th floor \n contact number:- 8130180258 \n email id:- ruchi.sharma@galgotiasuniversity.edu.in")
    elif (e.get() == 'Dr. Arvind dagur'):
        text.insert(END, "\n" + "Bot:Dr. Arvind dagur\n cabin number:- c-Cubical Room 3rd floor \n contact number:- 9811333406 \n email id:- arvind.dagur@galgotiasuniversity.edu.in")
    elif (e.get() == 'Dr. Arvind dagur'):
        text.insert(END, "\n" + "Bot:Dr. Arvind dagur\n cabin number:- c-Cubical Room 3rd floor \n contact number:- 9811333406 \n email id:- arvind.dagur@galgotiasuniversity.edu.in")
    elif (e.get() == "ok"):
        text.insert(END, "\n" + "Bot: Hope it helps you!!")
    else:
        text.insert(END, "\n" + "Bot: Sorry I didnt get it.")
text = Text(root,bg='black', fg='white')
text.grid(row=0,column=0,columnspan=2)
e = Entry(root,width=80)
send = Button(root,text='Send',bg='red', fg='white', width=20,command=send).grid(row=1,column=1)
e.grid(row=1,column=0)
root.title('HELPY')
root.mainloop()
