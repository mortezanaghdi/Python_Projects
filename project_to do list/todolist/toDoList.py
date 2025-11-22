import csv
import json

# modules will not start by their own they only start from main.py
if __name__ != "__main__":

    class ToDo:
        def __init__(self, name):
            self.name = name

        to_do_list = []

        def add_task(self, name):
            self.name = name
            self.to_do_list.append(self.name)
            print(f"{self.name["name"]} added to your to do list\n"
                  f"Before leaving save it.")

        def delete_task(self, name):
            self.name = name
            found = False
            for task in self.to_do_list:  # everything we add to to_do_list is a dict
                if task["name"] == name:
                    self.to_do_list.remove(task)
                    print(f"{self.name} is deleted from your to do list")
                    found = True
                    break
            if not found:
                print(f"can't find {self.name} in the to do list")

        def show_to_do_list(self):
            print("Here is your to do list:")
            with open("to_do_list.csv", mode="r", newline="") as file:
                csv_reader = csv.reader(file)
                for index, data in enumerate(csv_reader, start=1):  # use enumerate to use
                    # index before them for every line
                    task_dict = json.loads(data[0])  # get the data with json for
                    # it is easier to use them later for sth like delete
                    print(f"{index}. Task: {task_dict["name"]} |"
                            f" Details: {task_dict["details"]} |"
                            f" Priority: {task_dict["priority"]}")

        def save_to_file(self):
            with open("to_do_list.csv", mode="a", newline="") as file:
                csv_writer = csv.writer(file)
                for task in self.to_do_list:
                    json_str = json.dumps(task)  # send data in a json form
                    csv_writer.writerow([json_str])
                print("Your to do list is saved.")

        def delete_from_csv(self, name):
            """
            here I make a list of everything we have except 'name' and then rewrite csv file
            with the new list again.
            """
            self.name = name
            new_data = []
            with open("to_do_list.csv", mode="r", newline="") as file:
                csv_reader = csv.reader(file)
                for item in csv_reader:
                    json_dict = json.loads(item[0])  # 0 means the first column, and we have only one column
                    if json_dict["name"] != self.name:
                        new_data.append(json_dict)

            with open("to_do_list.csv", mode="w", newline="") as file:
                csv_writer = csv.writer(file)
                for task in new_data:
                    json_str = json.dumps(task)
                    csv_writer.writerow([json_str])
            print(f"{self.name} is deleted from CSV file")

else:
    print("This is a module, you can add it to your project.")

