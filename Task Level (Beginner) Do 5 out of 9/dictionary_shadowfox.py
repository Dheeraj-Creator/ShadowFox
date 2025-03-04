#list of friends and name lengths
friends=["Aditya","Rohit","Neha","Sanjay","Priya"]
name_lengths = [(friend, len(friend)) for friend in friends]
print("friends and their name lengths:",name_lengths)

#trip expenses tracking
your_expenses={
    "hotel":1200,
    "food":800,
    "transportation":500,
    "attractions":300,
    "miscellaneous":200
}

partner_expenses={
    "hotel":1000,
    "food":900,
    "transportation":600,
    "attractions":400,
    "miscellaneous":150
}

your_total=sum(your_expenses.values())
partner_total=sum(partner_expenses.values())

print(f"your total expenses:{your_total}")
print(f"your partner's total expenses:{partner_total}")

if your_total > partner_total:
    print("you spent more than your partner")
elif your_total < partner_total:
    print("your partner spent more than you")
else:
    print("both spent the same amount")

#find the expense category with the largest difference
max_diff_category=max(your_expenses.keys(),key=lambda category: abs(your_expenses[category] - partner_expenses[category]))
max_diff=abs(your_expenses[max_diff_category] - partner_expenses[max_diff_category])

print(f"the biggest difference is in {max_diff_category}, with a difference of {max_diff}")
