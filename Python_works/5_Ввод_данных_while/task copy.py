
message = "сколько вам лет: "

while True:        
    age = input(message)              
    age = int(age)

    if age == 'q':
        age = str(age)
        break
    elif age < 3:                   
        print(f"Билет бесплатный")      
    elif age >= 3 and age < 12:        
        print(f"Билет стоит 10$")       
    else:                              
        print(f"Белет стоит 15$")      
        continue   

    
