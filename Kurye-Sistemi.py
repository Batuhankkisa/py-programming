import tkinter as tk

class App():
    def __init__(self, parent):
        self.parent = parent
        self.chosen_item = None
        self.initUI()

    def initUI(self):
        frame = tk.Frame(self.parent)
        frame.pack(fill=tk.BOTH, expand=True)

        self.canvas = tk.Canvas(frame, bg = "white")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.canvas_items = []

        for i in range(1,6):
            x = i*50
            item_handle = self.canvas.create_oval(x, x, x+10, x+10, fill='red')
            self.canvas_items.append(item_handle)
        
        self.canvas.bind("<ButtonPress-3>", self.rightClick)
        self.canvas.bind("<ButtonPress-1>", self.leftClick)

    def leftClick(self, event):
        if self.chosen_item is not None:
            self.canvas.itemconfig(self.chosen_item, fill="red")
        self.chosen_item = self.canvas.find_closest(event.x, event.y)
        self.canvas.itemconfig(self.chosen_item, fill="blue")
        
    def rightClick(self, event):
        if self.chosen_item is not None:
            eski_pozisyonlar = self.canvas.coords(self.chosen_item)
            self.canvas.move(self.chosen_item, event.x-eski_pozisyonlar[0], event.y-eski_pozisyonlar[1])
            self.canvas.itemconfig(self.chosen_item, fill="green")
            self.chosen_item = None


root = tk.Tk()
root.geometry('500x500')
app = App(root)
root.mainloop()
