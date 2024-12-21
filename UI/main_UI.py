import customtkinter as ctk

from src.main import calculate_expression

class App(ctk.CTk):
    width = 400
    height = 350

    def __init__(self):
        super().__init__()
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")
        self.title("Omega Calculator")
        self.geometry(f"{self.width}x{self.height}")
        self.resizable(False, False)
        self.grid_rowconfigure(3, weight=1)
        

        self.exercise_text = ctk.CTkTextbox(self, width=350, height=50)
        self.exercise_text.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        self.clicked = False
        

        numbers_frame = ctk.CTkFrame(self, width=350, height=230)
        numbers_frame.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")
        numbers_frame.grid_propagate(False)
        # Define numbers and operators
        numbers = [
            '7', '8', '9', '+', 'C',
            '4', '5', '6', '-', '!',
            '1', '2', '3', '*', '&',
            '0', '.', '~', '/', '@',
            '^', '%', '$', '#', '=',
             
        ]

        row = 0
        col = 0
        for number in numbers:
            button = ctk.CTkButton(numbers_frame, text=number, width=59, height=35,
             command=lambda x=number: self.add_number(x))
            button.grid(row=row, column=col, padx=5, pady=5)
            col += 1
            if col > 4:
                col = 0
                row += 1

    def add_number(self, number):
        if number == '=':
            self.clicked = True

            self.calculate()
        elif number == 'C':
            self.exercise_text.delete("1.0", "end")
        else:
            if self.clicked:
                self.exercise_text.delete("1.0", "end")
                self.clicked = False
            current = self.exercise_text.get("1.0", "end-1c")
            self.exercise_text.delete("1.0", "end")
            self.exercise_text.insert("1.0", current + number)

    def calculate(self):
        exercise = self.exercise_text.get("1.0", "end-1c")
        try:
            result = calculate_expression(exercise)
        except Exception as e:
            result = f"Error: {e}"
        self.exercise_text.delete("1.0", "end")
        self.exercise_text.insert("1.0", str(result))













