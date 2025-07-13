import datetime

name = input("What's your name? ").strip()
age = input("How old are you? ").strip()
city = input("Which city do u live in? ").strip()
profession = input("What's your profession? ").strip()
hobby = input("What's your favourite hobby? ").strip()

intro_message = (
    f"Hello! my name is {name}, I'm {age} years old, I live in {city}\n"
    f"I work as a {profession} and I absolutely enjoy {hobby} in my free time\n"
    f"Nice to meet you!\n"                
    )

current_date = datetime.date.today().isoformat()
intro_message += f"Logged on: {current_date}"

border = "*" * 100
final_output = f"{border}\n{intro_message}\n{border}"

print(final_output)