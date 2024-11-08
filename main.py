from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window


class QuadraticEquationSolver(App):
    def build(self):
        Window.clearcolor = (0.129, 0.576, 0.690, 1)

        self.equation_label = Label(text="Enter coefficients for quadratic equation (a, b, c):", color=(0, 0, 0, 1))
        self.a_input = TextInput(background_color=(0.427, 0.835, 0.933, 1), foreground_color=(0, 0, 0, 1))
        self.b_input = TextInput(background_color=(0.427, 0.835, 0.933, 1), foreground_color=(0, 0, 0, 1))
        self.c_input = TextInput(background_color=(0.427, 0.835, 0.933, 1), foreground_color=(0, 0, 0, 1))
        self.result_label = Label(color=(0, 0, 0, 1))
        self.solve_button = Button(text="Solve", background_color=(0.427, 0.835, 0.933, 1),
                                   color=(0, 0, 0, 1),
                                   on_press=self.validate_and_solve)

        layout = BoxLayout(orientation='vertical')
        layout.add_widget(self.equation_label)
        layout.add_widget(self.a_input)
        layout.add_widget(self.b_input)
        layout.add_widget(self.c_input)
        layout.add_widget(self.solve_button)
        layout.add_widget(self.result_label)

        return layout

    def is_unknown(self, input_text):
        return 'x' in input_text or 'y' in input_text

    def validate_and_solve(self, instance):
        a_text = self.a_input.text
        b_text = self.b_input.text
        c_text = self.c_input.text

        if self.is_unknown(a_text):
            a = self.solve_for_unknown(a_text, b_text, c_text)
            if a is None:
                self.result_label.text = "Error: Unable to solve for 'a'."
                return
        else:
            try:
                a = float(a_text)
            except ValueError:
                self.result_label.text = "Error: 'a' must be a number."
                return

        if self.is_unknown(b_text):
            b = self.solve_for_unknown(b_text, a_text, c_text)
            if b is None:
                self.result_label.text = "Error: Unable to solve for 'b'."
                return
        else:
            try:
                b = float(b_text)
            except ValueError:
                self.result_label.text = "Error: 'b' must be a number."
                return

        if self.is_unknown(c_text):
            c = self.solve_for_unknown(c_text, a_text, b_text)
            if c is None:
                self.result_label.text = "Error: Unable to solve for 'c'."
                return
        else:
            try:
                c = float(c_text)
            except ValueError:
                self.result_label.text = "Error: 'c' must be a number."
                return

        if a == 0:
            self.result_label.text = "Error: Value of 'a' cannot be 0."
            return

        delta = pow(b, 2) - 4 * a * c

        if delta > 0:
            x1 = round((-b + delta ** 0.5) / (2 * a), 3)
            x2 = round((-b - delta ** 0.5) / (2 * a), 3)
            self.result_label.text = f"Root 1: {x1}, Root 2: {x2}, Delta Result: {delta}"
        elif delta == 0:
            x = round(-b / (2 * a), 3)
            self.result_label.text = f"Double Root: {x}, Delta Result: {delta}"
        else:
            self.result_label.text = f"No Real Roots Exist!, Delta Result: {delta}"

    def solve_for_unknown(self, unknown, val1, val2):
        try:
            unknown_val = float(val1 if 'a' not in val1 else (val2 if 'a' not in val2 else None))
            known_val = float(val1 if unknown != val1 else val2)
            return eval(
                unknown.replace(unknown, str((eval(unknown.replace(unknown, str(known_val))) - unknown_val) / -1)))
        except ValueError:
            return None


if __name__ == '__main__':
    QuadraticEquationSolver().run()
