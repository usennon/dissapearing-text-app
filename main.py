import tkinter as tk
from textwrap import wrap

time = None


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Disappear')
        self.geometry('600x400')
        self.var = tk.StringVar()
        self.var.trace("w", self.show_message)
        self.entry = tk.Entry(self, textvariable=self.var, width=50)
        self.btn = tk.Button(self, text="Очистить",
                             command=lambda: self.clear())
        self.btn['state'] = 'disabled'
        self.label = tk.Label(self)
        self.timer = tk.Label(self)
        self.words = tk.Label(self)
        self.entry.pack()
        self.btn.pack()
        self.label.pack()
        self.timer.pack()
        self.words.pack()

    def show_message(self, *args):
        words = 0
        value = self.var.get()
        li = value.split(' ')
        for word in li:
            if len(word) > 1:
                words += 1
        self.words.config(text=f'There are {words} words.')


        width = self.label.winfo_width()

        if width > 400:
            char_width = width / len(value)
            wrapped_text = '\n'.join(wrap(value, int(400 / char_width)))
            self.label['text'] = wrapped_text
        else:
            self.label.config(text=value)

    def reset(self):
        self.entry['state'] = 'disabled'
        self.label.config(text='Well done')
        self.btn['state'] = 'active'

    def clear(self):
        self.var.set('')
        self.entry['state'] = 'normal'
        self.btn['state'] = 'disabled'


def timer(is_next, count):
    global time
    if is_next:
        try:
            app.after_cancel(time)
        except ValueError:
            pass
    app.timer.config(text=f'Time left: {count}')
    if count > 0:
        is_next = False
        time = app.after(1000, timer, is_next, count - 1)
    if count == 0:
        app.reset()


app = App()

app.bind_all('<KeyPress>', lambda x: timer(is_next=True, count=5))
app.mainloop()
