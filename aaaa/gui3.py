import tkinter as tk

class Gui():
    """docstring for Gui"""
    def __init__(self, root):
        super(Gui, self).__init__()
        self.root = root
        self.root.geometry('1000x1000')
        b  = tk.Button(root,text='提交',bg='yellow',command=lambda:self.func())
        b.pack(expand='yes')
    def func(self):
        self.top = tk.Toplevel(self.root)
        var=tk.StringVar()
        l=tk.Label(self.top,bg='yellow',width=20,text='empty')
        l.pack()
        def print_selection():
            l.config(text='you have selected '+var.get())
        r1=tk.Radiobutton(self.top,text='Option A',
                          variable=var,value='A',
                          command=print_selection)
        r1.pack()
        r2=tk.Radiobutton(self.top,text='Option B',
                          variable=var,value='B',
                          command=print_selection)
        r2.pack()
        r3=tk.Radiobutton(self.top,text='Option C',
                          variable=var,value='C',
                      command=print_selection)
        r3.pack()
    
if __name__ == '__main__':
    root=tk.Tk()
    gui = Gui(root)
    root.mainloop()