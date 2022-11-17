import generator
from tkinter import *
import os


class GenerateAndSave:

    def __init__(self, master):

        self.button_to_save = None
        self.var_1, self.var_2, self.var_3, self.var_4 = IntVar(), IntVar(), IntVar(), IntVar()
        self.min_number_of_elements, self.max_number_of_elements = Entry(root), Entry(root)
        self.minimum, self.maximum = 5, 10
        self.require_number_of_elements = Checkbutton(master,
                                                      text="Number Of Elements",
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
                                         width=20,
                                         bg="#FFC773",
                                         activebackground="#DC9B3B",
                                         fg="white",
                                         activeforeground="white")

        self.master = master
        self.master.title("Generate And Save")
        self.master.geometry("1250x650")

        self.packed()

        self.master.mainloop()

    def generate(self):
        try:
            self.button_to_save.pack_forget()
        except AttributeError:
            pass
        try:
            self.replace_min_and_max()
        except ValueError:
            self.minimum = 5
            self.maximum = 10
        try:
            your_password = generator.password_generator([self.minimum, self.maximum],
                                                         self.var_2.get(), self.var_3.get(), self.var_4.get())
        except ValueError:
            your_password = generator.password_generator([max(self.minimum, self.maximum),
                                                          max(self.minimum, self.maximum)],
                                                         self.var_2.get(), self.var_3.get(), self.var_4.get())
        self.my_entry.config(state=NORMAL)
        self.my_entry.delete(0, 'end')
        self.my_entry.insert(0, your_password.password)
        self.my_entry.config(state="readonly")
        self.button_to_save = Button(self.master,
                                     text='Save',
                                     command=self.save(your_password.password),
                                     width=20)
        self.button_to_save.pack()
        your_password.reset()

    def toggle(self):
        if self.var_1.get() == 1:
            self.min_number_of_elements.pack()
            self.max_number_of_elements.pack()
        if self.var_1.get() == 0:
            self.min_number_of_elements.pack_forget()
            self.max_number_of_elements.pack_forget()

    def replace_min_and_max(self):
        self.minimum = int(self.min_number_of_elements.get())
        self.maximum = int(self.max_number_of_elements.get())

    def packed(self):
        self.require_number_of_elements.pack()
        self.require_upper_and_lower.pack()
        self.require_numbers.pack()
        self.require_special_signs.pack()
        self.button_to_generate.pack(pady=100)
        self.my_entry.pack(padx=10, pady=0)

    @staticmethod
    def save(password):
        with open('passwords.txt', 'a') as file:
            if os.stat("passwords.txt").st_size == 0:
                file.write(password)
            else:
                file.write('\n' + password)


if __name__ == "__main__":
    root = Tk()
    app = GenerateAndSave(root)
