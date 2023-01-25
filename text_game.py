(""""
__________          __  .__                      ________                       
\______   \___.__._/  |_|  |__   ____   ____    /  _____/_____    _____   ____  
 |     ___<   |  |\   __\  |  \ /  _ \ /    \  /   \  ___\__  \  /     \_/ __ \ 
 |    |    \___  | |  | |   Y  (  <_> )   |  \ \    \_\  \/ __ \|  Y Y  \  ___/ 
 |____|    / ____| |__| |___|  /\____/|___|  /  \______  (____  /__|_|  /\___  >
           \/                \/            \/          \/     \/      \/     \/ 
""")
#--------------
def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("---------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess =    input("Enter (A, B, C, or D):  ") 
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1



    display_score(correct_guesses, guesses)    
#--------------
def check_answer(answer, guess):
    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!") 
        return 0   
#--------------

def display_score(correct_guesses, guesses):
    print("-----------------")
    print("RESULTS")
    print("-----------------")

    print("Answer: ", end="")
    for i in questions:
        print(questions.get(i), end="")
    print()   

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end="")
    print()  

    score = int((correct_guesses/len(questions))*100)
    print("YOUR SCORE IS: "+ str(score)+ "%" )
#--------------
    
def play_again():
    response = input("Do you want to play again? (yes or no): ")
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False    
#--------------

questions = {
 "Who created Python?: ": "A",
 "What year was Apple founded?: ": "B",
 "Which car did Elon Musk make?: ": "C",
 "Is the Earth round?: ": "A"
}

options = [["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerburg"],
          ["A. 1989", "B. 1976", "C. 2000", "D. 2016"],
          ["A. Porsche", "B. Audi", "C. Tesla", "D. BMW"],
          ["A. True","B. False", "C. sometimes", "D. What's Earth?"]]

new_game()

while play_again():
    new_game()
    
print("Byeeee!")