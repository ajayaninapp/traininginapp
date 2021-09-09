import random
i=0
userchoice={}
pcchoice={}
rock_choice=0
paper_choice=1
scissor_choice=2
u_score=0
pc_score=0


def game_fun(c1,c2):
    
    if(c1==rock_choice):
        print('user:rock')
        if(c1==c2):
            print('pc:rock\n Tied')
        elif(c2==paper_choice):
            print('pc:paper\n PC wins')
        elif(c2== scissor_choice):
            print("pc:scissor\n USER wins")
        
    
    if(c1==scissor_choice):
        print('user:scissor\n')
        if(c1==c2):
            print('pc:Scissor\n Tied')
        elif(c2==paper_choice):
            print('pc:paper\n User wins')
        elif(c2== rock_choice):
            print("pc:Rock\n PC wins")

   
    if(c1==paper_choice):
        print('user:Paper\n')
        if(c1==c2):
            print('pc:Paper\n Tied')
        elif(c2==rock_choice):
            print('pc:Rock\n User wins')
        elif(c2== scissor_choice):
            print("pc:scissor\n PC wins")


            
    
        
        
 
choices=[0,1,2]
while i<10:
    choice=int(input("Enter the corresponding number as choice\nRocks -0\nPaper-1\nscissor-2\n"))

    userchoice[i+1]=choice
    i=i+1
    pcchoice[i]=random.choice(choices)
    
    if(choice==rock_choice):
       
        if(choice==pcchoice[i]):
            u_score=u_score+0
        elif(pcchoice[i]==paper_choice):
             pc_score=pc_score+1
        elif(pcchoice[i]== scissor_choice):
            u_score=u_score+1
        
    
    if(choice==scissor_choice):
       
        if(choice==pcchoice[i]):
            u_score=u_score+0
        elif(pcchoice[i]==paper_choice):
            u_score=u_score+1
        elif(pcchoice[i]== rock_choice):
            pc_score=pc_score+1

   
    if(choice==paper_choice):
       
        if(choice==pcchoice):
            u_score=u_score+0
        elif(pcchoice==rock_choice):
            u_score=u_score+1
        elif(pcchoice== scissor_choice):
             pc_score=pc_score+1


            

     
print("user point:",u_score)
print("pc_score:",pc_score)
while input("Do You Want To Continue? [y/n]") == "y":
    round=int(input("enter the round which information is needed"))
    game_fun(int(userchoice[round]),pcchoice[round])




