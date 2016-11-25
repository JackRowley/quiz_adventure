# Our quiz!
score=0
name = ""

def quiz():
    global score
    global name

    name = input("Enter your name: ")
    question1()
    question2()
    question3()
    question4()
    question5()
    question6()



    
def question1():
    global score
    global name

    print("Here is question 1,", name)

    
    print("Who is the best leader of a country")
    print("A. Donald trump")
    print("B. Vladimir Putin")
    print("C. Theresa May")
    print("D. Barrack Obama")
    print("E. Kim Jon Un")

def question2():
    global score
    global name

    print("Here is question 2,", name)

    answer = input("Answer: ")

    if answer.lower() == "d":
        score=score + 1000
        print("Correct")
    else:
        print("Wrong")
    print("Score:",score)



def question5():
    global score
    global name

    print("Here is question 5,", name)

    print("What country would you rather live in now?")
    print("A. America")
    print("B. Russia")
    print("C. U.K")
    print("D. Netherlands")
    print("E. North Korea")

    answer = input("Answer: ")

    if answer.lower() == "d":
        score=score + 1000
        print("You get paid to go to school")
    elif answer.lower() == "a":
        print("He already built the wall!")
    else:
        print("Whats wrong with you")
    print("Score:",score)

def question6():
    global score
    global name

    print("Here is question 6,", name)

    print("What is going to happen to the world?")
    print("A. No one can go any where because there is walls everywhere")
    print("B. The world gets nuked")
    print("C. No one knows")
    print("D. It will be saved")
    print("E. Kanye West becomes president")

    answer = input("Answer: ")

    if answer.lower() == "c":
        score=score + 1000
        print("We are doomed")
    else:
        print("Hopefully not")
    print("Score:",score)

def question6():
    global score
    global name

    print("Here is question 6,", name)
    print("When is this quiz going to end?")
    print("A. 5 more questions")
    print("B. 6 more questions")
    print("C. 7 more questions")
    print("D. 8 more questions")
    print("E. 9 more questions")

    answer = input("Answer: ")

    if answer.lower() == "a":
        score=score + 1000
        print("Correct")
    else:
        print("Wrong")
    print("Score:",score)


def question7():
    global score
    global name

    print("Here is question 7,", name)
    print("What year did WW2 start?")
    print("A.1942")
    print("B.1939")
    print("C.1937")
    print("D.1940")
    print("E.1941")

    answer = input("Answer: ")

    if answer.lower() == "b":
        score=score + 1000
        print("Correct")
    else:
        print("Wrong")
    print("Score:",score)


    
    
    



    



    
    




    
    



    
    





# Leave this at the bottom - it makes quiz run automatically when you
# run your code.
if __name__ == "__main__":
    quiz()
