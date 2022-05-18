"""
Made by: Rajdristant Ghose
Date: 18 May, 2022
"""
import tkinter

DEFAULT_FONT_STYLE = ("Arial", 15, "bold")
SMALL_FONT_STYLE = ("Arial", 10, "bold")
LARGE_FONT_STYLE = ("Arial", 24, "bold")

SCREEN_SIZE = "360x500"
LIGHT_GRAY = "#F5F5F5"
GRAY = "#EBEBEB"
WHITE = "#FFFFFF"
PRUSSIAN_BLUE = "#003153"
BLUE = "#c5e3ed"
LIGHT_BLUE = "#e9f1f5"

class Calculator:
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.geometry(SCREEN_SIZE)
        self.window.resizable(False, False)
        self.window.title("Calculator")

        self.equation = ""
        self.current_equation = []

        self._symbols_to_equation = {
            'ln('    : 'math.log(',
            'sin('   : 'math.sin(',
            'cos('   : 'math.cos(',
            'tan('   : 'math.tan(',
            'log10(' : 'math.log10(',
            '\u03C0' : 'math.pi',
            '\u00B2' : '**2',
            '\u221A(': 'math.sqrt(',
            '\u00D7' : '*'
        }

        self.buttons = {
            'ln'   : [(0, 0), lambda : self._append_equation(f"ln(")],   'sin'    : [(0, 1), lambda : self._append_equation(f"sin(")],  'cos'     : [(0, 2), lambda : self._append_equation(f"cos(")],    'tan'    : [(0, 3), lambda : self._append_equation(f"tan(")],
            'log10': [(1, 0), lambda : self._append_equation(f"log10(")],'('      : [(1, 1), lambda : self._append_equation('(')],      ')'       : [(1, 2), lambda : self._append_equation(')')],        '\u03C0' : [(1, 3), lambda : self._append_equation(f"\u03C0")],
            'C'    : [(2, 0), lambda : self._append_equation()],         'x\u00B2': [(2, 1), lambda : self._append_equation(f"\u00B2")],'\u221Ax' : [(2, 2), lambda : self._append_equation(f"\u221A(")],'DEL'    : [(2, 3), lambda : self._append_equation(pop=True)],
            '7'    : [(3, 0), lambda : self._append_equation("7")],      '8'      : [(3, 1), lambda : self._append_equation("8")],      '9'       : [(3, 2), lambda : self._append_equation("9")],       '\u00F7' : [(3, 3), lambda : self._append_equation("/")],
            '4'    : [(4, 0), lambda : self._append_equation("4")],      '5'      : [(4, 1), lambda : self._append_equation("5")],      '6'       : [(4, 2), lambda : self._append_equation("6")],       '\u00D7' : [(4, 3), lambda : self._append_equation('\u00D7')],
            '1'    : [(5, 0), lambda : self._append_equation("1")],      '2'      : [(5, 1), lambda : self._append_equation("2")],      '3'       : [(5, 2), lambda : self._append_equation("3")],       '\u2212' : [(5, 3), lambda : self._append_equation('-')],
            '.'    : [(6, 0), lambda : self._append_equation(".")],      '0'      : [(6, 1), lambda : self._append_equation("0")],      '='       : [(6, 2), lambda : self._equate()],                   '+'      : [(6, 3), lambda : self._append_equation('+')],
        }

        self.display_frame = self._create_frame(height=100, color=LIGHT_GRAY)
        self.button_frame = self._create_frame()

        self._initiate_buttons()
        self.current_equation_label, self.total_equation_label = self._initiate_display()

    def _create_frame(self, color=None, height=None):
        frame = tkinter.Frame(self.window, height=height, bg=color)
        frame.pack(expand=True, fill="both")
        return frame

    def _initiate_display(self):

        total_equation_label=tkinter.Label(self.display_frame,text=self.equation,anchor=tkinter.E,
                                             bg=LIGHT_GRAY,
                                             fg=PRUSSIAN_BLUE,padx=24,font=SMALL_FONT_STYLE)
        total_equation_label.pack(expand=True,fill="both")

        current_equation_label= tkinter.Label(self.display_frame,text=''.join(self.current_equation),anchor=tkinter.E,bg=LIGHT_GRAY,
                                  fg=PRUSSIAN_BLUE,padx=24,font=LARGE_FONT_STYLE)
        current_equation_label.pack(expand=True, fill="both")


        return current_equation_label, total_equation_label

    def _initiate_buttons(self):
        for button, value in self.buttons.items():
            bg = None
            try:
                int(button)
            except ValueError:      # not a number
                if button == "=":
                    bg = BLUE
                elif button != '.':  # an operator
                    bg = LIGHT_BLUE

            button = tkinter.Button(self.button_frame, text=button, font=DEFAULT_FONT_STYLE if value[0][0] not in (0, 1) else SMALL_FONT_STYLE, borderwidth=0, fg=PRUSSIAN_BLUE, bg=bg, command=value[1])
            button.grid(row=value[0][0], column=value[0][1], sticky=tkinter.NSEW)

            self.button_frame.columnconfigure(value[0][1], weight=1)
            self.button_frame.rowconfigure(value[0][0], weight=1)

    def _equate(self):
        if self.current_equation[0] in ('/', '\u00D7', '-', '+'):
            equation=self.equation
        else:
            equation = ""

        for val in self.current_equation:
            if val in self._symbols_to_equation.keys():
                equation += self._symbols_to_equation[val]
            else:
                equation += val

        self.current_equation.clear()
        self.current_equation_label.config(text=''.join(self.current_equation))

        try:
            self.equation= str(eval(equation))
        except SyntaxError:
            self.current_equation = "ERROR"
            self.current_equation_label.config(text=''.join(self.current_equation))
            self.current_equation = []

        self.total_equation_label.config(text=self.equation)


    def _append_equation(self, val=None, pop=False):
        if pop is False:
            if val is None:
                self.current_equation.clear()
                self.equation=""
                self.total_equation_label.config(text=self.equation)
            else:
                self.current_equation.append(val)
        else :
            self.current_equation.pop(-1)

        self.current_equation_label.config(text=''.join(self.current_equation))

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    calc = Calculator()
    calc.run()
