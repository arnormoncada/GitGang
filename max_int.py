num_int = int(input("Input a number: "))    # Do not change this line
max_int = num_int

while num_int > 0:
    num_int = int(input("Input a number: "))
    if num_int > max_int:
        max_int=num_int
    
print("The maximum is", max_int)    # Do not change this line

#1. setja inn input
#2. búa til max breytu
#3. búa til loopu sem gengur á meðan inputið er stærra en 0
#4. copy paste input þangað inn
#5. nesta if setningu sem ræður því hvort næsta input er stærra en það seinasta og gefa þvi það gildi ef svo er.
#6. prenta stærsta gildið