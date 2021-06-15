import random
N = ('Rock','Paper','Scissors')

num = random.choice(N)
choice = input('Rock Paper or Scissors or end? ')
while True:
    if choice == 'Rock' and num=="Rock":
        print("I got Rock too its a Tie")
        

    elif choice == 'Paper'and num=="Paper":
        print("I got Paper too its a Tie")
       
        
    elif choice == 'Scissors'and num=="Scissors":
        print("I got Scissors too its a Tie")
         

    elif choice == 'Scissors'and num=="Paper":
        print("Good Game You Win I got Paper")
       

    elif choice == 'Scissors'and num=="Rock":
        print("Good Game I won I got Rock")
         

    elif choice == 'Rock'and num=="Paper":
        print("Good Game I won I got Paper")
         

    elif choice == 'Rock'and num=="Scissors":
        print("Good Game You won I got Scissors")
        

    elif choice == 'Paper'and num=="Scissors":
        print("Good Game I won I got Scissors")
         
    break;

    if choice == "end":
        break;