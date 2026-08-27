# create a program capable of displaying question to the user like KBC.
# use list data type to store the questions and their ansers.
# display the final amount the pwesion is taking home after playing the game


questions =[
    {
        "Question": "What is the capital of India?",
        "Options": ["Mumbai", "New Delhi", "Kolkata", "chennai"],
        "Answer": "New Delhi",
        "Prize": 10000
    },
    {  
        "Question": "Which planet is known as red planet?",
        "Options": ["Venus", "Jupiter", "Mars", "Mercury"],
        "Answer": "Mars",
        "Prize": 20000
    },
    {
        "Question": "How many days are there in a leap year?",
        "Options": [365, 366, 364, 367],
        "Answer": 366,
        "Prize": 30000
    },
    {
        "Question": "Which language is primarily used to create the structure of a web page?",
        "Options": ["Python","HTML","SQL","C++"],
        "Answer": "HTML",
        "Prize": 40000
    },
    {
        "Question": "Which is the largest ocean in the world?",
        "Options": ["Atlantic ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
        "Answer": "Pacific Ocean",
        "Prize": 50000
    },
    {
        "Question": "Which Data Structure follows the LIFO principal?",
        "Options": ["Queue", "Array", "Staclk", "Linked List"],
        "Answer": "Stack",
        "Prize": 60000
    },
    {
        "Question": "Which of these is not a Python data type?",
        "Options": ["List", "Tuple", "Dictionary", "character"],
        "Answer": "Character",
        "Prize": 70000
    },
    {
        "Question": "Which SQL clause is used to filter groups after using GROUP BY?",
        "Options": ["WHERE", "ORDER BY", "HAVING", "FILTER"],
        "Answer": "HAVING",
        "prize": 80000
    },
    {
        "Question": "What is the boiling point of water at sea level?",
        "Options": ["50°C", "75°C", "100°C", "150°C"],
        "Answer": "100°C",
        "Prize": 90000
    },
    {
        "Question": "Which data structure follows FIFO?",
        "Options": ["Queue", "Tree", "Stack", "Graph"],
        "Answer": "Queue",
        "Prize": 100000        
    }
]
print("WELCOME TO KBC (Kon Banega Crorepati)")
print("Before start the game, there are some rules which you have to follow...")
print("1.The game will contain 10 questions.\n2.Each question will have 4 options: A, B, C, and D.\n3.The player must select one option for each question.\n4.Each correct answer increases the player's prize money.\n5.If the player gives a wrong answer, the game ends.\n6.The final prize depends on the highest level reached.\n7.Once an answer is submitted, it cannot be changed.")
inp = input("Can we start the Game (Yes or No)!!..? : ").upper()
if inp == "YES":
   print("GAME START!!...")
prize = 0
for question in questions:
    print(question["Question"]) 
    print("A.",question["Options"][0])   
    print("B.",question["Options"][1])
    print("C.",question["Options"][2])
    print("D.",question["Options"][3])
    answer = input("Enter your answer (A/B/VC/D): ").upper()
    if answer == "A":
        selected_answer = question["Options"][0]
    elif answer == "B":
        selected_answer = question["Options"][1]
    elif answer == "C":
        selected_answer = question["Options"][2]
    elif answer == "D":
        selected_answer = question["Options"][3]
    if selected_answer == question["Answer"]:
        prize = question["Prize"]
        print("correct Answer!")
        print("You won ₹",prize)
    else:
        print("Wrong Answer")
        break