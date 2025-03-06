import random

user_data = {}
user_roles = {}
secret_questions = {}
user_todos = {}

admin_username = "admin"
admin_password = "admin123"

# List of predefined fortunes for the "Fortune Cookie"
fortunes = [
    "Today is a good day to start something new!",
    "Success is on the horizon, keep moving forward.",
    "You will face challenges today, but you will overcome them.",
    "Luck is on your side, but you need to take action.",
    "A great opportunity is coming your way. Stay alert!",
    "Good things come to those who wait, but better things come to those who act.",
    "Today is the day to trust your instincts. Follow your gut!",
    "A surprise awaits you soon, so keep an open mind.",
    "You are capable of achieving great things. Don't doubt yourself.",
    "Things may seem difficult, but don't lose hope. Perseverance is key.",
    "Great things are coming to you. Your hard work will pay off soon.",
    "A friend will bring good news your way today.",
    "The answers you seek will come when you least expect them.",
    "Prepare for a challenge ahead, but stay strong and you will triumph.",
    "Unexpected wealth is in your near future. Stay ready!",
    "Opportunities are knocking on your door. Don't hesitate to open it.",
    "Your good fortune is the result of your efforts. Keep going!",
    "A new beginning is just around the corner. Embrace it with confidence.",
    "Be careful today, a small mistake could cost you dearly.",
    "Someone is hiding their true feelings about you. Be cautious.",
    "Expect delays today, but they will only make your victory sweeter.",
    "A small setback will soon lead to a big breakthrough. Stay patient.",
    "Don’t be afraid of change. It will bring you what you need.",
    "Someone may try to deceive you today. Stay vigilant.",
    "Fortune favors the brave, but it also tests them. Be prepared.",
    "Today may seem like a dull day, but small victories will come your way.",
    "Beware of overspending today. Your financial luck isn’t favorable.",
    "You might face a tough decision soon. Take your time to think it through.",
    "Things may not go as planned today. Embrace the unexpected.",
    "A big opportunity is on the horizon, but don’t rush into it.",
    "Your luck may take a turn today. Keep your head high.",
    "The universe is guiding you toward something greater. Trust the process.",
    "Someone close to you will offer help when you need it most.",
    "Take a deep breath, everything will fall into place soon.",
    "Beware of gossip today; not everything you hear is true.",
    "You might face some turbulence today, but calm will follow soon.",
    "This is a good time to step out of your comfort zone.",
    "A person from your past may come back into your life unexpectedly.",
    "A small but important decision will impact your future in a big way.",
    "Trust in your ability to overcome obstacles. You have the strength.",
    "The road to success is long, but every step you take brings you closer.",
    "A difficult person will test your patience today. Stay calm.",
    "A lucky break is coming your way. Don’t miss it when it arrives.",
    "Your current worries will soon dissipate. Everything will work out.",
    "Your ability to adapt will be your greatest strength in the coming days.",
    "Be cautious of making impulsive decisions today. Think things through.",
    "Your actions today will set the stage for your success tomorrow.",
    "An unexpected obstacle may appear, but you will have the strength to face it.",
    "A surprising change is coming, and it will challenge you in new ways.",
    "The stars align in your favor today. Embrace the good energy.",
    "Don't be afraid to take the first step toward your dreams today.",
    "A challenging situation will be resolved in your favor very soon.",
    "Someone may offer you advice today, but only you know what's best for you.",
    "Your intuition will guide you today. Trust it and you'll succeed.",
    "Not everything is as it seems today. Look deeper into matters before making decisions.",
    "Someone’s actions may disappoint you. Stay strong and don’t take it personally.",
    "Luck will be unpredictable today, so take things with a grain of salt.",
    "Don’t rely too heavily on others today. Trust your own judgment.",
    "The tide will turn soon, but patience is required to see the changes.",
    "While today may feel challenging, it is simply preparing you for something better."
]


def register():
    print("Registration")
    user = input("Please enter your desired username: ")

    if user in user_data:
        print("Username already taken. Please choose a different username.")
        return

    pw = input("Please enter your desired password: ")

    print("Select a secret question for account recovery:")
    print("1. What is your pet's name?")
    print("2. What is your mother's maiden name?")
    print("3. What is the name of your first school?")

    secret_question_choice = input("Please choose a question (1, 2, or 3): ")

    if secret_question_choice == "1":
        secret_question = "What is your pet's name?"
    elif secret_question_choice == "2":
        secret_question = "What is your mother's maiden name?"
    elif secret_question_choice == "3":
        secret_question = "What is the name of your first school?"
    else:
        print("Invalid choice, defaulting to 'What is your pet's name?'")
        secret_question = "What is your pet's name?"

    secret_answer = input(f"Please answer the secret question: {secret_question} ")

    user_data[user] = pw
    user_roles[user] = "user"  # Default role as "user"
    secret_questions[user] = (secret_question, secret_answer)
    user_todos[user] = []  # Initialize empty To-Do list for the user

    print(f"Registration successful! Welcome, {user}.")


def login():
    print("Login")
    user = input("Please enter your username: ")

    if user not in user_data:
        print("Username not found. Please register first.")
        return None

    pw = input("Please enter your password: ")

    if user_data[user] == pw:
        print(f"Login successful! Welcome back, {user}.")
        return user
    else:
        print("Incorrect password. Please try again.")
        return None


def forgot_password():
    print("Forgot Password")
    user = input("Please enter your username: ")

    if user not in user_data:
        print("Username not found. Please register first.")
        return

    print(f"Your secret question is: {secret_questions[user][0]}")
    answer = input("Please provide the answer to your secret question: ")

    if answer == secret_questions[user][1]:
        print("Answer correct. You can now reset your password.")
        new_pw = input(f"Please enter a new password for {user}: ")
        user_data[user] = new_pw
        print(f"Password for {user} has been successfully reset.")
    else:
        print("Incorrect answer. Password reset failed.")


def admin_view():
    print("Admin View - All Registered Users and Roles:")
    if user_data:
        for username, role in user_roles.items():
            print(f"Username: {username}, Role: {role}")
    else:
        print("No users registered yet.")


def remove_user():
    print("Remove User")
    user = input("Enter the username to remove: ")

    if user in user_data:
        del user_data[user]
        del user_roles[user]
        del secret_questions[user]
        del user_todos[user]  # Remove To-Do list if user is deleted
        print(f"User {user} has been removed.")
    else:
        print(f"User {user} not found.")


def assign_role():
    print("Assign Role")
    user = input("Enter the username to assign a role: ")

    if user in user_data:
        role = input("Enter the custom role to assign (it can be any name): ")

        user_roles[user] = role
        print(f"Role '{role}' has been assigned to {user}.")
    else:
        print(f"User {user} not found.")


def view_todo_list(user):
    print(f"\n{user}'s To-Do List:")
    if user_todos[user]:
        for idx, task in enumerate(user_todos[user], 1):
            print(f"{idx}. {task}")
    else:
        print("Your To-Do list is empty.")


def add_task(user):
    task = input("Enter a new task for your To-Do list: ")
    user_todos[user].append(task)
    print(f"Task '{task}' added to your To-Do list.")


def delete_task(user):
    view_todo_list(user)
    task_number = int(input("Enter the task number to delete: "))

    if 1 <= task_number <= len(user_todos[user]):
        deleted_task = user_todos[user].pop(task_number - 1)
        print(f"Task '{deleted_task}' has been deleted from your To-Do list.")
    else:
        print("Invalid task number.")


def fortune_cookie():
    try:
        if not fortunes:  # Check if the fortunes list is empty
            print("Oops! Something went wrong, no fortunes available.")
            return
        print("\nYour Fortune Cookie for today:")
        fortune = random.choice(fortunes)  # Select a random fortune from the list
        print(fortune)
    except Exception as e:
        print(f"An error occurred while fetching the fortune: {e}")


def user_dashboard(user):
    while True:
        print("\n1. View your To-Do list")
        print("2. Add a task to your To-Do list")
        print("3. Delete a task from your To-Do list")
        print("4. Fortune Cookie (Get your daily fortune)")
        print("5. Logout")

        user_choice = input("Please choose an action (1, 2, 3, 4, or 5): ")

        if user_choice == "1":
            print(f"\n{user}'s To-Do List:")
            if user_todos[user]:
                for idx, task in enumerate(user_todos[user], 1):
                    print(f"{idx}. {task}")
            else:
                print("Your To-Do list is empty.")
        elif user_choice == "2":
            task = input("Enter a new task for your To-Do list: ")
            user_todos[user].append(task)
            print(f"Task '{task}' added to your To-Do list.")
        elif user_choice == "3":
            print(f"\n{user}'s To-Do List:")
            if user_todos[user]:
                for idx, task in enumerate(user_todos[user], 1):
                    print(f"{idx}. {task}")
                task_number = int(input("Enter the task number to delete: "))
                if 1 <= task_number <= len(user_todos[user]):
                    deleted_task = user_todos[user].pop(task_number - 1)
                    print(f"Task '{deleted_task}' has been deleted from your To-Do list.")
                else:
                    print("Invalid task number.")
            else:
                print("Your To-Do list is empty.")
        elif user_choice == "4":
            fortune_cookie()
        elif user_choice == "5":
            print("Logging out...")
            break
        else:
            print("Invalid choice. Please try again.")


def main():
    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Forgot Password")
        print("4. Admin Login (View registered users, remove users, assign roles)")
        print("5. Exit")

        choice = input("Please choose an option (1, 2, 3, 4, or 5): ")

        if choice == "1":
            register()
        elif choice == "2":
            user = login()
            if user:
                user_dashboard(user)  # After login, go to the user dashboard
        elif choice == "3":
            forgot_password()
        elif choice == "4":
            print("Admin Login")
            admin_user = input("Please enter admin username: ")
            admin_pw = input("Please enter admin password: ")

            if admin_user == admin_username and admin_pw == admin_password:
                while True:
                    print("\nAdmin Actions:")
                    print("1. View all registered users and their roles")
                    print("2. Remove a user")
                    print("3. Assign role to a user")
                    print("4. Logout")

                    admin_choice = input("Please choose an admin action (1, 2, 3, or 4): ")

                    if admin_choice == "1":
                        admin_view()
                    elif admin_choice == "2":
                        remove_user()
                    elif admin_choice == "3":
                        assign_role()
                    elif admin_choice == "4":
                        print("Logging out of admin...")
                        break
                    else:
                        print("Invalid choice. Please try again.")
            else:
                print("Invalid admin credentials. Access denied.")
        elif choice == "5":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


main()
