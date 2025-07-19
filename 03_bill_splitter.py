def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("❌ Please enter a valid number. ")

grp_size = int(input("Enter the number of people in your group: "))

names = []

for i in range(grp_size):
    name = input(f"Enter the name of person #{i+1}: ").strip()
    names.append(name)
    
total_bill = get_float("Enter the bill amount in number only")

share = round(total_bill / grp_size, 2)

print("\n" + "*" * 40)
print(f"Total bill: {total_bill}")
print(f"Each person owes {share}")

for name in names:
    print(f"{name} owes {share} rupees")