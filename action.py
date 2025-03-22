import customtkinter
from tkinter import END
from spinbox import Spinbox
import json
import os

class ComparisonABC:
    def __init__(self, external_visualize):
        self.settings_path = "settings.json"
        self.external_visualize = external_visualize
        if os.path.exists(self.settings_path):
            with open(self.settings_path, "r") as f:
                self.a, self.b, self.c = json.load(f)
        else:
            self.a, self.b, self.c = 10, 50, 90
        self.logic()
    def visualize(self):
        self.external_visualize(self.a, self.b, self.c)
    def callback(self, a, b, c):
        self.a, self.b, self.c = a, b, c
        self.logic()
    def logic(self):
        if not(self.a <= self.b and self.b <= self.c):
            if self.a > self.b:
                if self.a > self.c:
                    self.a = self.c
                self.b = self.a
            if self.c < self.b:
                if self.a > self.c:
                    self.c = self.a
                self.b = self.c
        self.visualize()
    def __del__(self):
        with open(self.settings_path, "w") as f:
            json.dump((self.a, self.b, self.c), f)


class Action(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.grid_rowconfigure((0,1,2,3), weight=0)
        self.grid_rowconfigure(4, weight=1)
        self.grid_columnconfigure((1,2,3), weight=0)       
        self.grid_columnconfigure((0, 4), weight=1)

        self.label = customtkinter.CTkLabel(self, 
                                            text="A <= B <= C", 
                                            fg_color="transparent", 
                                            font=("Noto Sans Regular", 60))
        self.label.grid(row=0, column=1, padx=5, pady=5, sticky="nsew", columnspan=3)
        
        vcmd = (self.register(self.validate))

        self.entry_A = customtkinter.CTkEntry(self, validate='all', validatecommand=(vcmd, '%P'))
        self.entry_A.grid(row=1, column=1, padx=5, pady=5, sticky="nsew")
        self.entry_A.bind("<Leave>", self.getABC)

        self.entry_B = customtkinter.CTkEntry(self, placeholder_text="213")
        self.entry_B.grid(row=1, column=2, padx=5, pady=5, sticky="nsew")
        self.entry_B.bind("<Leave>", self.getABC)
        
        self.entry_C = customtkinter.CTkEntry(self, placeholder_text="313")
        self.entry_C.grid(row=1, column=3, padx=5, pady=5, sticky="nsew")
        self.entry_C.bind("<Leave>", self.getABC)

        self.spinbox_A = Spinbox(self, width=150, step_size=1)
        self.spinbox_A.grid(row=2, column=1, padx=5, pady=5, sticky="nsew")
        self.spinbox_A.bind("<Leave>", self.getABC)
        
        self.spinbox_B = Spinbox(self, width=150, step_size=1)
        self.spinbox_B.grid(row=2, column=2, padx=5, pady=5, sticky="nsew")
        self.spinbox_B.bind("<Leave>", self.getABC)

        self.spinbox_C = Spinbox(self, width=150, step_size=1)
        self.spinbox_C.grid(row=2, column=3, padx=5, pady=5, sticky="nsew")
        self.spinbox_C.bind("<Leave>", self.getABC)
        
        self.slider_A = customtkinter.CTkSlider(self, from_=0, to=100, number_of_steps=100)
        self.slider_A.grid(row=3, column=1, padx=5, pady=5, sticky="nsew")
        self.slider_A.bind("<Leave>", self.getABC)

        self.slider_B = customtkinter.CTkSlider(self, from_=0, to=100, number_of_steps=100)
        self.slider_B.grid(row=3, column=2, padx=5, pady=5, sticky="nsew")
        self.slider_B.bind("<Leave>", self.getABC)

        self.slider_C = customtkinter.CTkSlider(self, from_=0, to=100, number_of_steps=100)
        self.slider_C.grid(row=3, column=3, padx=5, pady=5, sticky="nsew")
        self.slider_C.bind("<Leave>", self.getABC)
        
        self.comp_abc = ComparisonABC(self.setABC)

    def setABC(self, a:int, b:int, c:int):
        self.entry_A.delete(0, END)
        self.entry_A.insert(0, str(a))
        self.entry_B.delete(0, END)
        self.entry_B.insert(0, str(b))
        self.entry_C.delete(0, END)
        self.entry_C.insert(0, str(c))

        self.spinbox_A.set(a)
        self.spinbox_B.set(b)
        self.spinbox_C.set(c)

        self.slider_A.set(a)
        self.slider_B.set(b)
        self.slider_C.set(c)

    def getABC(self, args):
        a = [int(self.entry_A.get()), self.spinbox_A.get(), int(self.slider_A.get())]
        print(a)
        a_uniq = list(set(filter(lambda x: a.count(x) == 1, a)))
        a = a_uniq[0] if len(a_uniq) > 0 else a[0]
        
        b = [int(self.entry_B.get()), self.spinbox_B.get(), int(self.slider_B.get())]
        print(b)
        b_uniq = list(set(filter(lambda x: b.count(x) == 1, b)))
        b = b_uniq[0] if len(b_uniq) > 0 else b[0]       

        c = [int(self.entry_C.get()), self.spinbox_C.get(), int(self.slider_C.get())]
        print(c)
        c_uniq = list(set(filter(lambda x: c.count(x) == 1, c)))
        c = c_uniq[0] if len(c_uniq) > 0 else c[0]

        self.comp_abc.callback(a, b, c)
        pass

    def validate(self, P):
        return str.isdigit(P) or P == ""

