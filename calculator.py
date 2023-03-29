import tkinter as tk

LARGE_FONT = ('Arial', 40, 'bold')
SMALL_FONT = ('Arial', 16)
DIGIT_FONT = ('Arial', 24, 'bold')
DEFAULT_FONT = ('Arial', 20, 'bold')

LABEL_COLOR = '#25265E'
OFF_WHITE = '#F8FAFF'
LIGHT_GRAY = "#F5F5F5"
WHITE = "#FFFFFF"
LIGHT_BLUE = '#ADD8E6'

class Calculator:

    def __init__(self):

        self.root = tk.Tk()
        self.root.geometry("375x677")
        self.root.resizable(0, 0)
        self.root.title("Calculator")

        self.total_expression = ""
        self.current_expression = ""

        self.display_frame = self.create_display_frame()

        self.total_label = self.create_total_label()
        self.current_label = self.create_current_label()

        self.digits = {
            7:(1, 1), 8:(1, 2), 9:(1, 3),
            4:(2, 1), 5:(2, 2), 6:(2, 3),
            1:(3, 1), 2:(3, 2), 3:(3, 3),
            0:(4, 1), '.':(4, 2) 
        }

        self.operations = {'/':'\u00F7', '*':'\u00D7', '-':'-', '+':'+'}

        self.button_frame = self.create_button_frame()
        self.digit_buttons = self.create_digit_buttons()
        self.operation_buttons = self.create_operation_buttons()
        self.clear_button = self.create_clear_button()
        self.answer_button = self.create_answer_button()
        self.square_button = self.create_square_button()
        self.sqrt_button = self.create_sqrt_button()

        for x in range(1, 5):
            self.button_frame.rowconfigure(x, weight=1)
            self.button_frame.columnconfigure(x, weight=1) 

    def create_total_label(self):
        total_label = tk.Label(self.display_frame, text=self.total_expression, anchor=tk.E, bg=LIGHT_GRAY, fg=LABEL_COLOR, font=SMALL_FONT, padx=24)
        total_label.pack(expand=True, fill='both')

        return total_label

    def create_current_label(self):
        current_label = tk.Label(self.display_frame, text=self.current_expression, anchor=tk.E, bg=LIGHT_GRAY, fg=LABEL_COLOR, padx=24, font=LARGE_FONT)
        current_label.pack(expand=True, fill='both')

        return current_label

    def create_display_frame(self):
        frame = tk.Frame(self.root, height=221, bg=LIGHT_GRAY)
        frame.pack(expand=True, fill="both")
        return frame
    
    def create_digit_buttons(self):
        for digit, grid_value in self.digits.items():
            button = tk.Button(self.button_frame, text=str(digit), bg=WHITE, fg=LABEL_COLOR, font=DIGIT_FONT, borderwidth=0, command=lambda x=digit: self.add_to_expression(x))
            button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)

    def create_operation_buttons(self):
        i = 0
        for operator, symbol in self.operations.items():
            button = tk.Button(self.button_frame, text=symbol, bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT, borderwidth=0, command=lambda x=operator: self.append_operator(x))
            button.grid(row=i, column=4, sticky=tk.NSEW)
            i += 1

    def create_clear_button(self):
        button = tk.Button(self.button_frame, text='C', font=DEFAULT_FONT, bg=OFF_WHITE, fg=LABEL_COLOR, borderwidth=0, command=self.clear)
        button.grid(row=0, column=1, sticky=tk.NSEW)

    def create_answer_button(self):
        button = tk.Button(self.button_frame, text='=', font=DEFAULT_FONT, bg=LIGHT_BLUE, fg=LABEL_COLOR, borderwidth=0, command=self.apply_answer)
        button.grid(row=4, column=3, columnspan=2, sticky=tk.NSEW)

    def create_square_button(self):
        button = tk.Button(self.button_frame, text='x\u00b2', font=DEFAULT_FONT, bg=OFF_WHITE, fg=LABEL_COLOR, borderwidth=0, command=self.apply_square)
        button.grid(row=0, column=2, sticky=tk.NSEW)
    
    def create_sqrt_button(self):
        button = tk.Button(self.button_frame, text='\u221ax', font=DEFAULT_FONT, bg=OFF_WHITE, fg=LABEL_COLOR, borderwidth=0, command=self.apply_sqrt)
        button.grid(row=0, column=3, sticky=tk.NSEW)

    def add_to_expression(self, value):
        self.current_expression += str(value)
        self.update_current()
    
    def append_operator(self, operator):
        self.current_expression += operator
        self.total_expression = self.current_expression
        self.update_total()
        self.current_expression = ''
        self.update_current()

    def clear(self):
        self.total_expression = ''
        self.current_expression = ''
        self.update_total()
        self.update_current()

    def apply_answer(self):
        self.total_expression += self.current_expression
        self.update_total()
        self.current_expression = str(eval(self.total_expression))
        if self.current_expression.find('.'):
            self.current_expression = str(round(float(self.current_expression), 5))
            self.update_current()
        else:
            self.update_current
    
    def apply_square(self):
        self.current_expression = str(eval(f'{self.current_expression}**2'))
        self.update_current()
    
    def apply_sqrt(self):
        self.current_expression = str(eval(f'{self.current_expression}**0.5'))
        self.update_current()

    def update_total(self):
        self.total_label.config(text=self.total_expression)

    def update_current(self):
        self.current_label.config(text=self.current_expression[:11])
    
    def create_button_frame(self):
        frame = tk.Frame(self.root)
        frame.pack(expand=True, fill="both")
        return frame

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = Calculator()
    app.run()