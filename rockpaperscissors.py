import random
list=['rock','paper','scissor']
comp=random.choice(list)

user=input("Enter do you want to be (rock,paper,scissor)?\n")
if (user!='rock' and user!='paper' and user!='scissor'):
    print("\nInvalid choice, choose one out of rock,paper,scissor")
    user=input("Enter do you want to be (rock,paper,scissor)?")

    
print(f'You are {user}')
print(f'The computer is {comp}')

userwins=0
compwins=0

if user==comp:
    print("It's a tie!")
elif (user=='scissor' and comp=='paper') or (user=='paper' and comp=='rock') or (user=='rock' and comp=='scissor'):
    print("You won!")
    userwins+=1
else:
    print("You lose!")
    compwins+=1

