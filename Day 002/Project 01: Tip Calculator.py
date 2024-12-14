print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? R"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

#My Solution
bill_with_tip = (bill * (1 + tip / 100))
pay_per_person = round(bill_with_tip / people, 2)

print(f"Each person should pay R{pay_per_person}")

#Alternative
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)

print(f"Each person should pay: ${final_amount}")
