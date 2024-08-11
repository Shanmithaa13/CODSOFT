import tkinter
import tkinter.messagebox
import pickle

base = tkinter.Tk()
base.title("To Do List ")

def add():
    task = entry_task.get()
    if task !="":
        listbox_task.insert(tkinter.END, task)
        entry_task.delete(0, tkinter.END)
    else:
        tkinter.messagebox.showwarning(title= "WARNING", message=" ENTER A TASK")

def delete():
    try:
        task_index = listbox_task.curselection()[0]
        listbox_task.delete(task_index)
    except:
        tkinter.messagebox.showwarning(title="WARNING", message="SELECT A TASK")

def load():
    try:
        tasks = pickle.load(open("tasks.dat","rb"))
        listbox_task.delete(0,tkinter.END)
        for t in tasks:
            listbox_task.insert(tkinter.END, t)
    except:
        tkinter.messagebox.showwarning(title="WARNING", message="CANNOT FIND A TASK")
   

def save():
    try:
        tasks = listbox_task.get(0, listbox_task.size())
        pickle.dump(tasks, open("tasks.dat","wb"))
    except:
         tkinter.messagebox.showwarning(title="WARNING", message="CANNOT SAVE A TASK")


frame_task = tkinter.Frame(base)
frame_task.pack()
    
listbox_task = tkinter.Listbox(frame_task, height=10,width=50)
listbox_task.pack(side = tkinter.LEFT)

scrollbar_task = tkinter.Scrollbar(frame_task)
scrollbar_task.pack(side = tkinter.RIGHT,fill = tkinter.Y)

listbox_task.config(yscrollcommand=scrollbar_task.set)
scrollbar_task.config(command = listbox_task.yview)


entry_task = tkinter.Entry(base,width=50)
entry_task.pack()

button_add_task = tkinter.Button(base, text="ADD YOUR TASK",width=48,command=add)
button_add_task.pack()


button_delete_task = tkinter.Button(base, text="DELETE YOUR TASK",width=48,command=delete)
button_delete_task.pack()

button_load_task = tkinter.Button(base, text="LOAD YOUR TASK",width=48,command=load)
button_load_task.pack()

button_save_task = tkinter.Button(base, text="SAVE YOUR TASK",width=48,command=save)
button_save_task.pack()

base.mainloop()