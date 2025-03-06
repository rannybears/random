user_data = {}
user_roles = {}
secret_questions = {}
user_todos = {}

admin_username = "admin"
admin_password = "admin123"


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
                while True:
                    print("\n1. View your To-Do list")
                    print("2. Add a task to your To-Do list")
                    print("3. Delete a task from your To-Do list")
                    print("4. Logout")

                    user_choice = input("Please choose an action (1, 2, 3, or 4): ")

                    if user_choice == "1":
                        view_todo_list(user)
                    elif user_choice == "2":
                        add_task(user)
                    elif user_choice == "3":
                        delete_task(user)
                    elif user_choice == "4":
                        print("Logging out...")
                        break
                    else:
                        print("Invalid choice. Please try again.")
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
