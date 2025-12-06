import tkinter as tk
import tkinter.messagebox as msg


class Todo(tk.Tk):
    def __init__(self, tasks=None):
        super().__init__()

        if not tasks:
            self.tasks = []
        else:
            self.tasks = tasks

        self.tasks_canvas = tk.Canvas(self)
        self.tasks_frame = tk.Frame(self.tasks_canvas)
        self.text_frame = tk.Frame(self)

        self.scrollbar = tk.Scrollbar(self.tasks_canvas, orient="vertical",
                                      command=self.tasks_canvas.yview)
        self.tasks_canvas.configure(yscrollcommand=self.scrollbar.set)

        # CHANGED: window title to lastname-ToDo
        self.title("Erkol-ToDo")
        self.geometry("300x400")

        # ADDED: File -> Exit menu
        menubar = tk.Menu(self)
        file_menu = tk.Menu(menubar, tearoff=0, bg="purple", fg="yellow")
        file_menu.add_command(label="Exit", command=self.destroy)
        menubar.add_cascade(label="File", menu=file_menu)
        self.config(menu=menubar)

        self.task_create = tk.Text(self.text_frame, height=3, bg="white", fg="black")
        self.tasks_canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.canvas_frame = self.tasks_canvas.create_window(
            (0, 0), window=self.tasks_frame, anchor="nw"
        )
        self.task_create.pack(side=tk.BOTTOM, fill=tk.X)
        self.text_frame.pack(side=tk.BOTTOM, fill=tk.X)
        self.task_create.focus_set()

        # ADDED: starter tasks
        starter_tasks = [
            "Set title to last name",
            "Change color to 2 complementary colors",
            "Right-click to delete task",
            "Read label for delete instructions",
            "Add Exit to program",
            "Add tasks while running",
            "Delete tasks while running"
        ]

        # CHANGED: alternating purple/yellow
        self.colour_schemes = [
            {"bg": "purple", "fg": "yellow"},
            {"bg": "yellow", "fg": "purple"}
        ]

        # create starter task labels
        for text in starter_tasks:
            label = tk.Label(self.tasks_frame, text=text, pady=10)
            self.set_task_colour(len(self.tasks), label)
            label.bind("<Button-3>", self.remove_task)
            label.pack(side=tk.TOP, fill=tk.X)
            self.tasks.append(label)

        # Added Instructions for deleting tasks with right click
        info = tk.Label(
            self.tasks_frame,
            text="----Right-click a task to delete it----",
            bg="#555555",   # gray background
            fg="white",     # white text
            pady=10
        )
        info.pack(side=tk.TOP, fill=tk.X)
        self.tasks.append(info)

        self.bind("<Return>", self.add_task)
        self.bind("<Configure>", self.on_frame_configure)
        self.bind_all("<MouseWheel>", self.mouse_scroll)
        self.bind_all("<Button-4>", self.mouse_scroll)
        self.bind_all("<Button-5>", self.mouse_scroll)
        self.tasks_canvas.bind("<Configure>", self.task_width)

    # CHANGED: newly added tasks also use right-click delete
    def add_task(self, event=None):
        task_text = self.task_create.get(1.0, tk.END).strip()
        if len(task_text) > 0:
            label = tk.Label(self.tasks_frame, text=task_text, pady=10)
            self.set_task_colour(len(self.tasks), label)
            label.bind("<Button-3>", self.remove_task)
            label.pack(side=tk.TOP, fill=tk.X)
            self.tasks.append(label)
        self.task_create.delete(1.0, tk.END)

    def remove_task(self, event):
        task = event.widget
        if msg.askyesno("Delete Task?", "Delete: " + task.cget("text") + "?"):
            self.tasks.remove(task)
            task.destroy()
            self.recolour_tasks()

    def recolour_tasks(self):
        for i, task in enumerate(self.tasks[:-1]):       # keep gray one last
            self.set_task_colour(i, task)

    def set_task_colour(self, index, task):
        _, scheme = divmod(index, 2)
        colors = self.colour_schemes[scheme]
        task.configure(bg=colors["bg"], fg=colors["fg"])

    def on_frame_configure(self, event=None):
        self.tasks_canvas.configure(scrollregion=self.tasks_canvas.bbox("all"))

    def task_width(self, event):
        self.tasks_canvas.itemconfig(self.canvas_frame, width=event.width)

    def mouse_scroll(self, event):
        if event.delta:
            self.tasks_canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
        else:
            move = 1 if event.num == 5 else -1
            self.tasks_canvas.yview_scroll(move, "units")


if __name__ == "__main__":
    todo = Todo()
    todo.mainloop()



