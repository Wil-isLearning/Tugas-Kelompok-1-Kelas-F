import customtkinter as ctk

class ButtonPanel:
    def __init__(self, parent, logic):
        self.logic = logic

        buttons = [
            ["7", "8", "9", "÷"],
            ["4", "5", "6", "x"],
            ["1", "2", "3", "-"],
            ["0", ".", "%", "+"],
        ]

        for i in range(4):
            parent.grid_columnconfigure(i, weight=1)

        #Tombol Clear
        ctk.CTkButton(
            parent, text="C",
            fg_color="#b30000", hover_color="#cc0000",
            font=("Segoe UI", 22),
            command=self.logic.clear_all
        ).grid(row=1, column=0, sticky="nsew", padx=5, pady=5)

        #Tombol √
        ctk.CTkButton(
            parent, text="√",
            fg_color="#0059b3", hover_color="#0073e6",
            font=("Segoe UI", 22),
            command=lambda: self.logic.add_input("**0.5")
        ).grid(row=1, column=1, sticky="nsew", padx=5, pady=5)

        #Tombol =
        ctk.CTkButton(
            parent, text="=",
            fg_color="#cc9900", hover_color="#e6b800",
            font=("Segoe UI", 22),
            command=self.logic.calculate
        ).grid(row=1, column=2, columnspan=2, sticky="nsew", padx=5, pady=5)

        #Tombol angka & operator lain
        for r, row in enumerate(buttons):
            for c, text in enumerate(row):
                ctk.CTkButton(
                    parent,
                    text=text,
                    font=("Segoe UI", 22),
                    fg_color="#2b2b2b" if text.isdigit() or text == "." else "#0047b2",
                    hover_color="#3a3a3a" if text.isdigit() else "#0066ff",
                    command=lambda t=text: self.logic.add_input(t)
                ).grid(row=r + 2, column=c, sticky="nsew", padx=5, pady=5)
