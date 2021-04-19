from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from string import punctuation, ascii_uppercase, ascii_lowercase, digits
from random import sample, shuffle, randint
import pyperclip

Builder.load_file("Password.kv")


class MyLayout(BoxLayout):
    def checkbox_click(self, parameters):
        numbers = digits
        symbols = punctuation
        capital = ascii_uppercase
        small = ascii_lowercase
        initial_password = ""
        if parameters == "easy":
            initial_password = sample(small, randint(2, 5)) + sample(capital, randint(3, 5))
        elif parameters == "normal":
            initial_password = sample(small, randint(2, 3)) + sample(capital, randint(2, 4)) + \
                               sample(numbers, randint(3, 5))
        elif parameters == "hard":
            initial_password = sample(small, randint(2, 3)) + sample(capital, randint(2, 3)) + \
                               sample(numbers, randint(3, 4)) + sample(symbols, randint(3, 5))
        shuffle(initial_password)
        global final_password
        final_password = "".join(initial_password)
        self.ids.password.text = f"Your Password: {final_password}"

    def copy(self):
        try:
            pyperclip.copy(final_password)
        except Exception as e:
            print(f"Error: {e}")


class PGApp(App):
    def build(self):
        Window.clearcolor = .5, .5, .5, 1
        Window.size = (350, 500)
        return MyLayout()


if __name__ == '__main__':
    PGApp().run()
