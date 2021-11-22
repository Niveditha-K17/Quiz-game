import time
import tkinter
from tkinter import *
import random
from PIL import Image
from PIL import ImageTk

##########################################################################################################################################

lit_quest_list = [ "Who is the author of 'To Kill a Mockingbird'?",
                  "Material feminism studies inequality in terms of-",
                  "Anita Desai's 'Where Shall We Go This Summer' has been compared to Virginia Woolf's-",
                  "How many sonnets did Shakespeare write in all?",
                  "Which is believed to be the first important revenge tragedy?",
                  "Which one of these books is not written by 'Haruki Murakami'?",
                  "In 1913 Tagore was awarded the Nobel Prize for literature for the English translation of?",
                  "To read critically means-",
                  "Which one is the world's longest novel?"]

lit_choice_list = [["Harper Lee","Virginia Woolf","George Orwell","Enid Blyton"],
                   ["Only Gender","Only Class","Both Class and Gender","Only Patriarchy"],
                   ["To The Lighthouse","The Voyage Out","The Waves","Night and Day"],
                   [152,153,154,155],
                   ["Gorboduc","Hamlet","The Spanish Tragedy","Tamburlaine"],
                   ["Kafka on the Shore","After Dark","1984","Men Without Women"],
                   ["The Gitanjali","Fruit Gathering","Lover’s Gift","None"],
                   ["Taking an opposing point of view to the ideas and opinions expressed",
                    "Skimming through the material because most of it is just padding",
                    "Evaluating what you read in terms of your own research questions",
                    "Being negative about something before you read it"],
                   ["A Suitable Boy","L'Astree","War and Peace",
                    "Remembrance of Things Past"]]

lit_ans_list = [0,2,0,2,2,2,0,2,3]
##########################################################################################################################################
sports_quest_list = ["Which captain led Indian cricket team to win in all 3 formats of cricket?",
                    "In which country was the first olympics held?",
                    "Who is the captain of Indian Football team",
                    "What is the national sport of India",
                    "Which team has most number of FIFA World cups",
                    "Which player has dunked most in NBA",
                    "Which wrestler has the most no. of golds in olympics",
                    "Who is currently Word No.1 in tennis",
                    "Which cricketer has scored the fastest 100 in IPL"]

sports_choice_list = [["Mahendra Singh Dhoni","Virat Kohli",
                       "Sourav Ganguly","Rahul Dravid"],
                      ["Hong Kong","Greece","Athens","Seoul"],
                      ["Sunil Chhetri","Gurpreet Singh",
                       "Abhisekh B","Rahul C"],
                      ["Kabaddi","Cricket","Hockey","Tennis"],
                      ["Brazil","Spain","Italy","Germany"],
                      ["Rudy","Michael Jordan","Duncan","Tom Harry"],
                      ["Yama Moto","Bruce Baumgarterner",
                       "Sushil Kumar","Kerelin"],
                      ["Novak Djokovic","Andy Murray",
                       "Leander Paes","Roger Federer"],
                      ["Chris Gayle","ABD","Virat Kohli","KL Rahul"]]
sports_ans_list= [0,2,0,2,0,0,1,0,0]
##########################################################################################################################################
civics_quest_list = ["What is the minimum age to be elected VP of India?",
                     "The term 'Union Cabinet' was introduced in the\n"
                    "Constitution of India in which year?",
                    "Which High Court has jurisdiction of Andaman and Nicobar?",
                    "The head of a Municipal Corporation is called...",
                    "The term 'laissez faire' refers to...",
                    "Which organization encourages international investment and trade?",
                    "What is the maximum claim amount in a District Consumer Court?",
                    "Which is the global agency for protecting consumer rights?",
                    "The mid-day meal scheme was first implemented in which state?"]
civics_choice_list = [["25","35","40","45"],
                      ["1949","1950","1979","1980"],
                    ["Bombay High Court","Madras High Court",
                     "karnataka High Court", "Calcutta High Court"],
                    ["Mayor","Chairman","Tehsildar","Registrar"],
                    ["'Fair price' control on essential commodities",
                     "Deregulation of private business",
                    "Breakdown of law and order",
                    "Socialism"],
                    ["IMF", "World Bank", "UNESCO", "WTO"],
                    ["Rs 1 lakh","Rs 1 crore", "20 lakhs", "2 crores"],
                    ["Consumers International","International Consumer Forum",
                     "UN Consumer Court", "International Consumer Commission"],
                    ["Tamil Nadu", "Andhra Pradesh","Punjab","Uttar Pradesh"]]
civics_ans_list = [1,2,3,0,1,3,2,0,0]

##########################################################################################################################################

hist_quest_list = ["Which university was founded by king Ramapala of Pala dynasty?",
                   "Which dynasty was ruling Magadha when Alexander invaded India?\n",
                   "The Sangam Literature tells us about which ancient Tamil kingdom?",
                   "Pushkalavati was the capital of which ancient kingdom?",
                   "Which Kushan emperor first introduced gold coinage in India?",
                   "Which river was called Vipasa in Vedic India?",
                   "Sarnath is associated with which aspect of Budddha's life?",
                   "Which of the following was used in the Mathura school of sculpture?",
                   "What was the name of judges in the Satavahana dynasty?"]
hist_choice_list = [["Somapuri","Vallabhi","Jagadal","Odantpuri"],
                    ["Shisunagas","Nandas","Mauryas","Kosalas"],
                    ["Chola","Chera","Pandya","All of the above"],
                    ["Gandhara","Kosala","Magadha","Kashi"],
                    ["Vima Kadphises","Vima Taktu","Vasishka","Kujula Kadphises"],
                    ["Ganga", "Jhelum", "Beas", "Indus"],
                    ["Birth","Residence", "First sermon", "Death"],
                    ["Red sandstone","Marble","Granite","Clay"],
                    ["Amatyas", "Rajukas","Bhoja","Gamika"]]
hist_ans_list = [2,1,3,0,0,2,2,0,1]

##########################################################################################################################################
nature_quest_list = [ "Pakistan developed the National conservation strategy in-",
                     "Recycling of one ton of paper can save-",
                     "Stilt roots are found in -",
                     "The age of a tree can be determined more or less accurately by-",
                     "Which of the following plants is referred to as a living fossil?",
                     "Birds are known to survive in virtually all known environments. To which class do they belong?",
                     "An example of a flightless, swimming bird is a",
                     "What is the largest group of insects?",
                     "Why do Crickets rub their wings together?"]
nature_choice_list = [["1990","1991","1993","1992"],
                      ["120 trees","130 trees","17 trees","18 trees"],
                      ["Banyan","Maize","Mango","China rose"],
                      ["finding the ratio of height to the width of the tree",
                       "counting the number of rings in the trunk",
                       "measuring the height of the tree",
                       "measuring the diameter of the trunk"],
                      ["Ephedra","Cycas","Ginkgo","Adiantum"],
                      ["Reptiles","Aves","Agnatha","Fliers"],
                      ["Gull","Quail","Penguin","Crane"],
                      ["Flies","Butterflies","Bees and wasps","Beetles"],
                      ["To help them fly","To keep themselves warm",
                       "To attract a male","To keep their predators away"]]


nature_ans_list = [3,2,1,1,2,1,2,3,2]

##########################################################################################################################################

entertain_quest_list = ["Who directed the movie '3 IDIOTS?' ",
                        "Which is the highest Grossing Film at present",
                        "Who is India's Richest Actor?",
                        "Who is the first Indian to win he prestigous Booker Prize",
                        "Which IMD Indian Web series is 1st on IMDb ",
                        "Which country will be the focus country of the 50th- edition of International Film Festival of India (IFFI)? ",
                        "Aishwarya Rai was crowned Miss World in which year? ",
                        "Who is known as father of Indian Cinema?",
                        "Which one is India's first television soap opera?"]
entertain_choice_list = [["Rajkumar Hirani","Anurag Kashyap",
                          "Karan Johar","Aditya Chopda"],
                         ["Infinity Wars","Avatar","Endgame","Titanic"],
                         ["Shah Rukh Khan","Amitabh Bacchan",
                          "Akshay Kumar","Me"],
                         ["Kushwant Singh","Ruskin Bond",
                          "Suchetha Dalal","Arunaduthi Roy"],
                         ["Scam 1992","Pataal Lok","SPECIAL OPS","Asur"],
                         ["Germany","Italy","Russia","Japan"],
                         ["1990","2000","1998","1994"],
                         ["Dadasaheb Torne","V Shantaram",
                          "Dada Saheb Palake","Satyajit Ray"],
                         ["Ramayan","Hum Log","Mahabharat","Buniyaad"]]
entertain_ans_list = [0,2,0,3,0,2,3,2,1]


##########################################################################################################################################
    

root = Tk()
root.title("NoBrainer")
root.geometry("800x600")
root.config(bg="light green")
root.resizable(0,0)

##########################################################################################################################################
img1 = Image.open("NoBrainer.png")
img1 = img1.resize((150,120), Image.ANTIALIAS)
img1 = ImageTk.PhotoImage(img1)

img2 = Image.open("unnamed.png")
img2 = img2.resize((150,90), Image.ANTIALIAS)
img2 = ImageTk.PhotoImage(img2)

photo= Image.open("Civics.png")
photo = photo.resize((100,75), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(photo)
photo1= Image.open("Nature.png")
photo1 = photo1.resize((100,75), Image.ANTIALIAS)
photo1 = ImageTk.PhotoImage(photo1)
photo2=Image.open('English.png')
photo2 = photo2.resize((100,75), Image.ANTIALIAS)
photo2 = ImageTk.PhotoImage(photo2)
photo3=Image.open('Sports.png')
photo3 = photo3.resize((100,75), Image.ANTIALIAS)
photo3 = ImageTk.PhotoImage(photo3)
photo4=Image.open("Mental_Ability.png")
photo4 = photo4.resize((100,75), Image.ANTIALIAS)
photo4 = ImageTk.PhotoImage(photo4)
photo5=Image.open("His.png")
photo5 = photo5.resize((100,75), Image.ANTIALIAS)
photo5 = ImageTk.PhotoImage(photo5)
####################################################################################################################################################

def gen(how_many):
    indexes= []
    while (len(indexes) < how_many):
        x = random.randint(0, how_many-1)
        if x not in indexes:
            indexes.append(x)
    return indexes

class SelectedTopic:
    def __init__(self, quest_list, choice_list, ans_list):
        self.quest_list     = quest_list
        self.choice_list    = choice_list
        self.ans_list       = ans_list
        self.user_ans_list  = []

def show_selected_quiz(selected_topic):

    b_1.destroy()
    b_2.destroy()
    b_3.destroy()
    b_4.destroy()
    b_5.destroy()
    b_6.destroy()

    selected_topic.indexes = gen(len(selected_topic.quest_list))
    
    choices = selected_topic.choice_list
    indexes = selected_topic.indexes
    ques = selected_topic.quest_list
    answers = selected_topic.ans_list

    def calc():
        nonlocal selected_topic
        answered_count = len(selected_topic.user_ans_list)
        
        user_ans = selected_topic.user_ans_list
        indexes = selected_topic.indexes
        ques = selected_topic.quest_list
        
        n = 0
        score = 0
        eoq = Label(root,text = 'END OF THE QUIZ',font = ('Consolas',23) , fg = '#056462',bg = "light green",width = 20)
        eoq.pack()
        eoq1 = Label(root,text = 'Correct answers are in Green and are Incorrect in Red', font =('Times',17),bg = "light green", fg = '#790ed1')
        eoq1.pack(pady =(8,8))
        
        for i_pos,i in enumerate(indexes):
            if (i_pos < answered_count) and (user_ans[i_pos] == answers[i]):
                score += 1
                lb1 = Label(root, text = ques[i] + ": " + 
                            choices[i][answers[i]],
                            justify = 'right',
                            bg="light green",
                            fg = '#056420',
                            font=(5))
                lb1.pack(pady=(7,5))
            else:
                lb2 = Label(root, text = ques[i] + ": " + 
                            choices[i][answers[i]],
                            justify = 'right',
                            bg="light green",
                            fg = 'red',
                            font=(5))
                lb2.pack(pady=(7,5))
        
        print(score)
        final = Label(root, text = "You've answered " + str(score) +" out of 9 questions correct", font = ("Consolas",18) ,width = 55,bg="light green",
        fg = 'blue')
        final.pack(pady=(12,8))
        quit_b = Button(root, text="PRESS TO QUIT", command=root.destroy, bg = 'yellow', fg= 'red',width=15,font=(8))
        quit_b.pack(pady=(10,5))

    def scoreboard():
        lbl_ques.destroy()
        r1.destroy()
        r2.destroy()
        r3.destroy()
        r4.destroy()
        time_l.destroy()
        timeleft_l.destroy()
        end.destroy()
        calc()

    
    t = 600
    def timer():
        nonlocal time_l,t
        if t>0:
            minute = t//60
            second = t%60
            t-=1
            time_l.config(text = str(minute) +":"+str(second)) 
            time_l.after(1000,timer)
        elif t==0:
            scoreboard()
        
    time_l = Label(
        root,
        text = "",
        bg = "yellow",
        fg= "black",
        width = "10",
        font = (10)
        )
    time_l.place(x=390,y=360)
    timer()

    timeleft_l = Label(
        root,
        text="Time Left:",
        bg="yellow",
        fg = "red",
        width="8",
        font = (10)
    )
    timeleft_l.place(x= 330,y=360)

    def selected():
        nonlocal radiovar
        nonlocal lbl_ques,r1,r2,r3,r4
        nonlocal time_l
        ques = selected_topic.quest_list
        choices = selected_topic.choice_list
        x = radiovar.get()
        user_ans = selected_topic.user_ans_list
        user_ans.append(x)
        radiovar.set(-1)
        q_no = len(selected_topic.user_ans_list)
        if q_no<9:
            lbl_ques['text']= ques[indexes[q_no]]
            r1['text']= choices[indexes[q_no]][0]
            r2['text']= choices[indexes[q_no]][1]
            r3['text']= choices[indexes[q_no]][2]
            r4['text']= choices[indexes[q_no]][3]
            q_no += 1
        
        elif q_no == 9:
          scoreboard()

    lbl_ques = Label(
        root,
        text = ques[indexes[0]],
        font = ("Times",17),
        wraplength = 350,
        bg = "light green",
        width = 500
        )    
    lbl_ques.pack(pady=(10,10))
    radiovar = IntVar()
    radiovar.set(-1)

    r1 = Radiobutton(
        root,
        text = choices[indexes[0]][0],
        font = ("Times",14),
        variable = radiovar,
        value = 0,
        bg = "light green",
        command = selected)
    r1.pack(pady=(10,10))
    r2 = Radiobutton(
        root,
        text = choices[indexes[0]][1],
        font = ("Times",14),
        variable = radiovar,
        value = 1,
        bg = "light green",
        command = selected)
    r2.pack(pady=(10,10))

    r3 = Radiobutton(
        root,
        text = choices[indexes[0]][2],
        font = ("Times",14),
        variable = radiovar,
        value = 2,
        bg = "light green",
        command = selected)
    r3.pack(pady=(10,10))
    r4 = Radiobutton(
        root,
        text = choices[indexes[0]][3],
        font = ("Times",14),
        variable = radiovar,
        bg = "light green",
        value = 3,
        command = selected)
    r4.pack(pady=(10,10))

    end = Button(
        root,
        text="END QUIZ",
        command = scoreboard,
        width=15,
        bg = "black",
        fg = "yellow"
    )
    end.place(x=650,y=300)
    


##########################################################################################################################################

def show_literature():
    
    selected_topic = SelectedTopic(lit_quest_list,
                                   lit_choice_list,
                                   lit_ans_list)
    
    show_selected_quiz(selected_topic)
#########################################################################################################################################
def show_sports():

    selected_topic = SelectedTopic(sports_quest_list,
                                   sports_choice_list,
                                   sports_ans_list)

    show_selected_quiz(selected_topic)
#########################################################################################################################################

def show_civics():
    selected_topic = SelectedTopic(civics_quest_list,
                                   civics_choice_list,
                                   civics_ans_list)
    
    show_selected_quiz(selected_topic)


#########################################################################################################################################

def show_history():
    selected_topic = SelectedTopic(hist_quest_list,
                                   hist_choice_list,
                                   hist_ans_list)
    
    show_selected_quiz(selected_topic)


#########################################################################################################################################

def show_nature():
    selected_topic = SelectedTopic(nature_quest_list,
                                   nature_choice_list,
                                   nature_ans_list)
    
    show_selected_quiz(selected_topic)

##########################################################################################################################################

def show_entertainment():
    selected_topic = SelectedTopic(entertain_quest_list,
                                   entertain_choice_list,
                                   entertain_ans_list)
    
    show_selected_quiz(selected_topic)

##########################################################################################################################################

def _menu():
    global b_1,b_2,b_3,b_4,b_5,b_6

    b_1 = Button(root,text='\nLiterature\n\t\t',width=100,height = 121, 
                 compound='top', fg='white', font=(5),
                 command=show_literature,image=photo2,bg="Blue",border=0)
    b_1.grid(row=0, column=0)
    b_2 = Button(root,text='\nNature\n',width=100,height = 121, 
                 compound='top', fg='white', font=(5),
                 command=show_nature,image=photo1,bg="Blue",border=0) 
    b_2.grid(row=0, column=1)
    b_3 = Button(root,text='\nCivics\n\t\t',width=100,height = 121, 
                 compound='top', fg='white', font=(5),
                 command=show_civics,image=photo,bg="Blue",border=0)
    b_3.grid(row=1, column=0)
    b_4 = Button(root,text='\nSports\n',width=100,height = 121, 
                 compound='top', fg='white', font=(5),
                 command=show_sports,image=photo3,bg="Blue",border=0)
    b_4.grid(row=1, column=1)
    b_5 = Button(root,text='\nEntertainment \n',width=100,height = 121,
                 compound='top', fg='white', font=(5),
                 command=show_entertainment,image=photo4,bg="Blue",border=0)
    b_5.grid(row=2, column=0)
    b_6 = Button(root,text='\nHistory\n\t\t',width=100,height = 121, 
                 compound='top', fg='white', font=(5),
                 command=show_history,image=photo5,bg="Blue",border=0)
    b_6.grid(row=2, column=1)
    
    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=1)
    root.rowconfigure(0, weight=1)
    root.rowconfigure(1, weight=1)
    root.rowconfigure(2, weight=1)

##########################################################################################################################################

def destroy1():
    Label_img.destroy()
    Label_text.destroy()
    name.destroy()
    lbl_instructions_1.destroy()
    lbl_instructions_t.destroy()
    lbl_instructions.destroy()
    start_bt.destroy()
    click.destroy()
    _menu()
##########################################################################################################################################

Label_img = Label(
    root,
    image= img1, 
    bg ="light green")
Label_img.pack()
Label_text = Label(
    root,
    text="Welcome!",
    bg ="light green",
    font= ("Calibri",24,"bold")
)
Label_text.pack()
name = Entry(root,width=80)
name.pack()
name.insert(0,"Enter your name")
user_name = name.get()
def my_click():
    global lbl_instructions_1,lbl_instructions_t,lbl_instructions
    global start_bt,name,click
    name.config(state = "disabled")
    click.config(state="disabled")
    lbl_instructions_1 = Label(
    root,
    text= "Hello "+name.get()+"!" + """  Click on the start button to choose your quiz topic
            once you've read the instructions.""",
    font = (12),
    bg = "light green",
    justify = "center"
    )
    lbl_instructions_1.pack(pady=(5,5))
    lbl_instructions_t = Label(
    root,
    text= "::INSTRUCTIONS::",
    font= ("Calibri",14,"bold"),
    fg = "#343dc2",
    bg = "light green",
    justify = "center"
    )
    lbl_instructions_t.pack(pady=(3,0))

    lbl_instructions =  Label(
        root,
        text="""
        1) The quiz contains six quiz topics.You can choose one of them.
        2)Each quiz contains 9 questions
        3)The quiz lasts for 10 mins, after which the quiz will end automatically.
        4)The questions will be of  MCQ type.
        5)You can select an option only once, after which the next ques will be displayed. 
        So, choose wisely.
        6)Your answers will be auto-saved as you enter them.
        7)You can click the End Quiz button at any point of the quiz to end the quiz.
        \t\tHave fun and Good Luck!""",
        font = ("Comic Sans",12),
        bg = "light green",
        foreground = "#d10d1a",
        justify = "left"
        )
    lbl_instructions.pack(pady=(0,3),padx=(130,0))

    start_bt = Button(
        root,
        image=img2,
        bg ="light green",
        relief = GROOVE,
        border = 0,
        command = destroy1
        )
    start_bt.pack(pady=(0,23))

click = Button(
    root,
    text="Click here",
    width = 10,
    relief = FLAT,
    border=0,
    bg= "Dark Blue",
    fg ="white",
    command = my_click,
    )
click.pack()


root.mainloop()

