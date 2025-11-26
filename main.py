import customtkinter as ctk
from display import DisplayPanel
from logic import CalculatorLogic
from buttons import ButtonPanel

class CalculatorApp:
    def __init__(self):
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.root = ctk.CTk()
        self.root.title("Kalkulator Kelompok 1 Kelas F Pengenalan Pemrograman")
        self.root.geometry("360x500")
        self.root.resizable(False, False)
        self.root.bind("<Key>", self.handle_keypress)

        # DISPLAY
        self.display = DisplayPanel(self.root)

        # LOGIC
        self.logic = CalculatorLogic()
        self.logic.set_update_callback(self.display.set)

        # BUTTONS
        self.buttons = ButtonPanel(self.root, self.logic)
        for i in range(6):
            self.root.grid_rowconfigure(i, weight=1)

    def handle_keypress(self, event):
        key = event.char
                    #Angka dan titik
        if key.isdigit() or key == ".":
            self.logic.add_input(key)

                    #Operator umum
        elif key in "+-*/%":
            self.logic.add_input(key)

                    #Enter untuk =
        elif event.keysym in ("Return", "KP_Enter"):
            self.logic.operate("=")

                    #Backspace untuk hapus satu karakter
        elif event.keysym == "BackSpace":
            self.logic.expression = self.logic.expression[:-1]
            self.logic._update_display()

                    #Esc untuk Clear 
        elif event.keysym == "Escape":
            self.logic.clear_all()

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = CalculatorApp()
    app.run()
