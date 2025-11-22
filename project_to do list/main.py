from todolist.toDoList import ToDo
from todolist.task import Task
from todolist.utils import want_to_continue

"""
This is a to do list which you can add,delete and save your
task, for adding first you enter what is needed and then 
you should save them otherwise they will not be saved to
your task list.
if you add something and what to delete it before save it
you can choose number 2 to delete it
you can see all your tasks
and also you can delete them by pressing number 5 and the
task's name.
"""

# modules will not start by their own they only start from main.py
if __name__ == "__main__":
    print("Hello, Let's Go To Work.")
    print('--------------------------')
    finish = False

    while not finish:
        print("1. Add a task\n2. Delete a task (before save it)\n3. Show my to do list\n"
              "4. Save my to do list\n5. Delete from CSV file")
        print('--------------------------')
        try:
            what_to_do = input("Choose What You Want To Do By"
                               " Entering The Number: ")
            what_to_do = int(what_to_do)
        except ValueError:
            print("Error: ValueError")
        except Exception as err:
            print(f"Error: {err}")
        my_instance = ToDo("instance")

        if what_to_do == 1:
            name = ""
            details = ""
            priority = ""
            while not name or not details or not priority:
                print('--------------------------')
                name = input("Enter the name of your task: ")
                details = input("Enter the details for your task: ")
                priority = input("Add how important this task is for you: ")
            print('--------------------------')
            new_task = Task(name, details, priority)
            my_instance.add_task(new_task.to_dict())  # an instance from task which is a dict
            finish = want_to_continue(finish)
            print('--------------------------')

        elif what_to_do == 2:
            name = input("Enter the name of task you want to delete: ")
            my_instance.delete_task(name)
            finish = want_to_continue(finish)
            print('--------------------------')

        elif what_to_do == 3:
            my_instance.show_to_do_list()
            print('--------------------------')
            finish = want_to_continue(finish)
            print('--------------------------')

        elif what_to_do == 4:
            my_instance.save_to_file()
            finish = want_to_continue(finish)
            print('--------------------------')

        elif what_to_do == 5:
            delete_name = input("Enter the name of task you want to delete "
                                "from your to do list: ")
            my_instance.delete_from_csv(delete_name)
            finish = want_to_continue(finish)
            print('--------------------------')





