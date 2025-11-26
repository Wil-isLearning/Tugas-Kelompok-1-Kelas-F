import customtkinter as ctk

class DisplayPanel:
    def __init__(self, parent):
        self.entry = ctk.CTkEntry(
            parent,
            font=("Segoe UI", 28),
            justify="right",
            height=70,
            corner_radius=12
        )
        self.entry.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=10, pady=10)
        self.set("0")

    def set(self, text):
        self.entry.delete(0, "end")
        self.entry.insert(0, text)

    def get(self):
        return self.entry.get()
