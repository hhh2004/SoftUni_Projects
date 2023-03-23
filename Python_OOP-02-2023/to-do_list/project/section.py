from project.task import Task


class Section:
    def __init__(self, name: str):
        self.name = name
        self.tasks = []

    def add_task(self, new_task: Task):
        if new_task not in self.tasks:
            self.tasks.append(new_task)
            return f"Task {new_task.details()} is added to the section"
        else:
            return f"Task is already in the section {self.name}"

    def complete_task(self, task_name: str):
        for task in self.tasks:
            if task_name == task.name:
                task.completed = True
                return f"Completed task {task_name}"
        else:
            return f"Could not find task with the name {task_name}"

    def clean_section(self):
        tasks = len(self.tasks)
        self.tasks.clear()
        return f"Cleared {tasks} tasks."

    def view_section(self):
        output = [f"Section {self.name}:"]
        for task in self.tasks:
            output.append(task.details())
        output = '\n'.join(output)
        return output
