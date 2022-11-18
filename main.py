import generator
from tkinter import *
import os


class GenerateAndSave:

    def __init__(self, master):

        self.button_to_save, self.button_to_delete = None, None
        self.password = ''
        self.var_1, self.var_2, self.var_3, self.var_4 = IntVar(), IntVar(), IntVar(), IntVar()
        self.number_of_elements = Entry(root, state='disabled')
        self.number = 8
        self.password_history = Text(master, width=30, height=15)
        self.require_number_of_elements = Checkbutton(master,
                                                      text="Number of Elements",
                                                      onvalue=1,
                                                      offvalue=0,
                                                      variable=self.var_1,
                                                      command=self.toggle)
        self.require_upper_and_lower = Checkbutton(master,
                                                   text="Upper Case and Lower Case",
                                                   onvalue=1,
                                                   offvalue=0,
                                                   variable=self.var_2)
        self.require_numbers = Checkbutton(master,
                                           text="Letters and Numbers",
                                           onvalue=1,
                                           offvalue=0,
                                           variable=self.var_3)
        self.require_special_signs = Checkbutton(master,
                                                 text="Special Signs",
                                                 onvalue=1,
                                                 offvalue=0,
                                                 variable=self.var_4)
        self.my_entry = Entry(root, font=("Helvetica", 20))
        self.button_to_generate = Button(master,
                                         text='Generate Password',
                                         command=self.generate,
                                         width=40,
                                         bg="#FFC773",
                                         activebackground="#DC9B3B",
                                         fg="white",
                                         activeforeground="white")

        self.button_to_check = Button(master,
                                      text='Check the history',
                                      command=self.check,
                                      width=35,
                                      bg="#FFC773",
                                      activebackground="#DC9B3B",
                                      fg="white",
                                      activeforeground="white")

        self.master = master
        self.master.title("Generate And Save")
        self.master.geometry("500x550")
        self.master.resizable(0, 0)

        self.packed()

        self.master.mainloop()

    def generate(self):
        try:
            self.button_to_save.pack_forget()
        except AttributeError:
            pass
        try:
            self.replace_number()
        except ValueError:
            self.number = 8
        try:
            your_password = generator.password_generator(self.number,
                                                         self.var_2.get(), self.var_3.get(), self.var_4.get())
        except ValueError:
            your_password = generator.password_generator(self.number,
                                                         self.var_2.get(), self.var_3.get(), self.var_4.get())

        self.password = your_password.password
        self.entry_configuration(self.password)
        self.button_to_save = Button(self.master,
                                     text='Save',
                                     command=lambda: self.save(self.password),
                                     width=20,
                                     bg="#2C2C2C",
                                     activebackground="#969696",
                                     fg="white",
                                     activeforeground="white")

        self.button_to_save.pack()
        your_password.reset()

    def toggle(self):
        if self.var_1.get() == 1:
            self.number_of_elements.config(state=NORMAL)
        if self.var_1.get() == 0:
            self.number_of_elements.config(state='disabled')

    def replace_number(self):
        self.number = int(self.number_of_elements.get())

    def packed(self):
        self.require_number_of_elements.pack()
        self.number_of_elements.pack()
        self.require_upper_and_lower.pack()
        self.require_numbers.pack()
        self.require_special_signs.pack()
        self.button_to_generate.pack()
        self.my_entry.pack()
        self.button_to_check.pack()

    def entry_configuration(self, password):
        self.my_entry.config(state=NORMAL)
        self.my_entry.delete(0, 'end')
        self.my_entry.insert(0, password)
        self.my_entry.config(state="readonly")

    def save(self, password):
        with open('passwords.txt', 'a') as file:
            if os.stat("passwords.txt").st_size == 0:
                file.write(password)
            else:
                file.write('\n' + password)
        self.check()

    def delete(self):
        file = open('passwords.txt', 'r')
        content = file.read()
        file.close()
        content = content.split('\n')
        new_content = '\n'.join(content[:-1])
        file = open('passwords.txt', 'w+')
        for i in range(len(new_content)):
            file.write(new_content[i])
        file.close()
        self.check()

    def check(self):
        try:
            self.button_to_delete.pack_forget()
        except AttributeError:
            pass
        if self.password_history.winfo_ismapped():
            self.password_history.pack_forget()
            return
        self.password_history.delete('1.0', END)
        with open('passwords.txt', "r") as file:
            file_text = file.read()
        self.password_history.insert(END, file_text)
        self.password_history.pack()
        self.button_to_delete = Button(self.master,
                                       text="Delete last entry",
                                       command=self.delete,
                                       width=20,
                                       bg="#2C2C2C",
                                       activebackground="#969696",
                                       fg="white",
                                       activeforeground="white")
        self.button_to_delete.pack()


if __name__ == "__main__":
    root = Tk()
    app = GenerateAndSave(root)
