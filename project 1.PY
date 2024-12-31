import random

age=[10,20,30,40,50]
choice=random.choice(age)

print(choice)

import random

print('Welcome to Rock  Paper Scissor Game')
print('Rules: Rock beats Scissors,Scissors beats Paper,Paper beats Rock')

#LIST OF OPTION
options=['Rock, Paper,Scissor']
 
 user_choice=input('entter your choice (Rock/Paper/Scissor):')
computer_choice=random.choice(options)

if user_choice==computer_choice:
 print('Match ties')

elif user_choice=='Rock':
 if computer_choice=random.
