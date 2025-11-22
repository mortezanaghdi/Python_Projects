# modules will not start by their own they only start from main.py
if __name__ != "__main__":

    class Task:
        def __init__(self, name, details, priority):
            self.name = name
            self.details = details
            self.priority = priority

        def __str__(self):
            return (f"Task: {self.name}\nDetails: {self.details}"
                    f"\nPriority: {self.priority}")

        def to_dict(self):
            """
            here we can get a dict instead of and object of Task
            """
            return {
                "name": self.name,
                "details": self.details,
                "priority": self.priority
            }
else:
    print("This is a module, you can add it to your project.")