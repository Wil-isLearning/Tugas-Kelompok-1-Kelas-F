class CalculatorLogic:
    def __init__(self):
        self.expression = ""
        self.update_callback = None

    def set_update_callback(self, func):
        self.update_callback = func

    #DISPLAY FORMAT
    def _format_display(self, text):
        """Mengubah simbol internal ke simbol cantik."""
        return (
            text.replace("*", "×")
                .replace("/", "÷")
        )

    def _update_display(self, text=None):
        """Update display dengan format cantik."""
        if self.update_callback:
            raw_text = self.expression if text is None else text
            formatted = self._format_display(raw_text)
            self.update_callback(formatted)

    #LOGIC UTAMA
    def add_input(self, value):
        self.expression += str(value)
        self._update_display()

    def clear_all(self):
        self.expression = ""
        self._update_display()

    def operate(self, op):
        if op == "=":
            self.calculate()

    def calculate(self):
        if not self.expression:
            return

        try:
            result = eval(self.expression, {"__builtins__": None}, {})
            self.expression = str(result)
            self._update_display()
        except Exception:
            self.expression = ""
            self._update_display("Error")
