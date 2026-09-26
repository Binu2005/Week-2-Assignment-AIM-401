name = input("Enter your name: ")
total_spent = 0
for day in range(3):
    spent = float(input("Enter money spent today ($): "))
    total_spent = total_spent + spent
    if spent > 20:
        print("Over your $20 budget today!")
else:
    print("Great! Under budget today.")
print(f"Total money spent over 3 days: ${total_spent:.2f}")
if total_spent <= 60:
    print("Overall Result: You stayed under your $60 total budget!")
else:
    print("Overall Result: You went over your $60 total budget!")

