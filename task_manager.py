import json


class TaskManager:
    def __init__(self):
        self.tasks = []


    def add_task(self, description: str):
        if any(task["description"] == description for task in self.tasks):
            raise ValueError(f"Задача с описанием {description} уже существует")
        task = {"description": description, "completed": False}
        self.tasks.append(task)


    def complete_task(self, index: int):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["completed"] = True
        else:
            raise IndexError(f"Некорректный индекс: {index}")


    def remove_task(self, index: int):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
        else:
            raise IndexError(f"Некорректный индекс: {index}")


    def save_to_json(self, filename: str):
        with open(filename, "w") as file:
            json.dump(self.tasks, file)


    def load_from_json(self, filename: str):
        with open(filename, "r") as file:
            self.tasks = json.load(file)