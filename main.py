import random

score=0


list=["Virat Kohli","Priyanka Chopra","Shraddha Kapoor","Narendra Modi","Alia Bhatt","Katrina Kaif","Deepika","Neha Kakkar","Urvashi Rautela","Jacqueline Fernandez"]
global first_choice,second_choice,first_index,second_index
first_choice=(random.choice(list))
second_choice=(random.choice(list))
first_index=list.index(first_choice)
second_index=list.index(second_choice)

print("------------The game is to find who has more followers between both------------")
again='y'

while(again!='n'):
    first_choice=(random.choice(list))
    second_choice=(random.choice(list))
    first_index=list.index(first_choice)
    second_index=list.index(second_choice)

    print(f"A:   The first name is {first_choice}")
    print("-----------------V|S-----------------")
    print(f"B:   The second name is {second_choice}\n")
    user_guess=input("Guess who is the winner?Between 'A' and 'B' : ")

    if user_guess=='A':
        
        if first_index < second_index:
            score+=1
            print(f"Your score is {score}")
            print("Nice Job")
        else:
            print("You loose!!")
            
    elif user_guess=='B':
        if first_index > second_index:
            score+=1
            print(f"Your score is {score}")
            print("Nice Job")
            
        else:
            print("You loose!!")

    again=input("\n\nDo you want to continue? 'y' or 'n' : ")

