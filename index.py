import customtkinter as ctk
from customtkinter import CTk

ctk.set_appearance_mode("System")  
ctk.set_default_color_theme("blue") 
tasks = []


def prin():
    task = task_input.get()
    row_index = len(tasks)
    if task:
        com = ctk.StringVar()
        task_la = ctk.CTkCheckBox(fram,text=task.title(),width=230,text_color="#ffa500",checkmark_color="#ffa500",variable=com,)        
        task_la.grid(row=row_index, column=0, padx=4, pady=5, sticky="w", columnspan=1)
        delete_button = ctk.CTkButton(
            fram,
            text="Delete",
            width=60,
            command=lambda: delete_task(task_la, delete_button)
            )
        delete_button.grid(row=row_index, column=1, padx=0, pady=0, sticky="e")
        task_input.delete(0,ctk.END)
        fram.grid_columnconfigure(0, weight=1)  
        fram.grid_columnconfigure(1, weight=0)
        tasks.append((task_la,delete_button))

def delete_task(checkbox, delete_button):
    checkbox.destroy()
    delete_button.destroy()
    tasks.remove((checkbox, delete_button))
    update_layout()

def update_layout():
    for idx, (checkbox, delete_button) in enumerate(tasks):
        checkbox.grid(row=idx, column=0, padx=10, pady=5, sticky="w", columnspan=1)
        delete_button.grid(row=idx, column=1, padx=0, pady=0, sticky="e")

app = ctk.CTk() 
app.geometry("250x350")  
app.resizable(False, False)
app.attributes("-topmost", True)
app.title("CustomTkinter Basic Template")
app.bind("<FocusIn>",lambda ev: app.attributes("-alpha",1))
app.bind("<FocusOut>",lambda ev: app.attributes("-alpha",0.6))  
app.title("TASK")
app.iconbitmap("app-icon-square.ico")
task_input = ctk.CTkEntry(master=app,width=230,height=30,placeholder_text="Enter Task")
task_input.bind("<Return>",lambda ev: prin())
task_input.pack(side="top",pady = 10)
fram = ctk.CTkScrollableFrame(app,width=230,height=320)
fram.pack(expand = False,pady = 10,padx =5)

app.mainloop()


