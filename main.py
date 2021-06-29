#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python
bill=input("what is the bill:")
tip=input("what percent of tip do you want to pay 12 , 15 or 18:")
total_people=input("how many people pay:")
total_people_int=int(total_people)
int_of_bill=int(bill)
int_of_tip=int(tip)
percent_of_bill=int_of_bill*(int_of_tip/100)
Total_bill=int_of_bill+percent_of_bill
Final_bill=(round(Total_bill/total_people_int,2))
print("You should pay:",Final_bill)