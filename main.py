import customtkinter
from action import Action

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("ООП, Лабораторная работа №3.2")
        self.geometry(f"{700}x{250}")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.action = Action(master=self)
        self.action.grid(row=0, column=0, padx=0, pady=0,sticky="nsew")
        
        self.protocol("WM_DELETE_WINDOW", self.on_close)
    def on_close(self):
        self.action.comp_abc.__del__()
        self.destroy()


if __name__ == "__main__":
    app = App()
    app.mainloop()

