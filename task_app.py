import tkinter as tk
from tkinter import END

class TaskManager:
    def __init__(self):
        self.tasks = []  

    def add_task(self, task):
        if task:
            self.tasks.append(task)

    def get_tasks(self):
        return self.tasks


class TaskApp:
    def __init__(self, root, manager):
        self.manager = manager
        self.root = root
        self.root.title("Tareas")

      
        self.entry = tk.Entry(self.root, width=40)
        self.entry.pack(pady=5)

        
        self.add_button = tk.Button(self.root, text="Agregar tarea", command=self.add_task)
        self.add_button.pack(pady=5)

        
        self.listbox = tk.Listbox(self.root, width=50)
        self.listbox.pack(pady=5)

    def add_task(self):
        task = self.entry.get()
        self.manager.add_task(task)
        self.entry.delete(0, END)
        self.update_list()

    def update_list(self):
        self.listbox.delete(0, END)
        for t in self.manager.get_tasks():
            self.listbox.insert(END, t)


if __name__ == "__main__":
    root = tk.Tk()
    manager = TaskManager()
    app = TaskApp(root, manager)
    root.mainloop()
