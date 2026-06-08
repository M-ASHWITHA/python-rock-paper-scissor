print("Welcome to the quiz game!")
playing=input("Do you want to start? (y/n): ").lower()
score=0
questions=0

if playing=='n':
    print("Okay! Bye bye..")
    quit()

elif playing=='y':
    print("Let's start!")

    a1=input("What CPU stands for? ").lower()
    questions+=1
    if a1=="central processing unit":
        print("Correct!")
        score+=1
    else:
        print("Incorrect.")

    a2=input("What RAM stands for? ").lower()
    questions+=1
    if a2=="random access memory":
        print("Correct!")
        score+=1
    else:
        print("Incorrect.")

    a3=input("How much 1 byte equals? ").lower()
    questions+=1
    if a3 in ["8 bites", "eight bits", "8"]:
        print("Correct!")
        score+=1
    else:
        print("Incorrect.")

else:
    print("Please enter the valid choice.")

print(f"Your score: {score}/{questions}.")
print("Thank you for playing!")