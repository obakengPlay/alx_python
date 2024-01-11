#Bonus_rate = 0.3

#user_input = input("What is your name ?")
#user_salary = float(input("What is your Salary ?"))



#def calculate_bonus (value):
   # bonus = value * Bonus_rate
    #return bonus 

#def greetings (name , salary):
   # print("Function called", end="\n")
   # print ("Hello {name}".format(name=name))
    #user_bonus = calculate_bonus(salary)
    #print("The bonus calculated on your salary {} is {}".fomrat(salary,user_bonus))
    
    #greetings(user_input,user_salary)
    
def greet_group(*people):
    for person in people:
        print("Howdy {}".format(person))
        
greet_group("Violet","Sakwa")
