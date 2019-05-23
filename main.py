#kivy.require("1.10.1")
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.config import Config


class CalculatorLayout(GridLayout):
    def calc(self, calculate):
        if calculate:
            try:
                self.display.text = str(eval(calculate))
            except ZeroDivisionError:
                self.display.text = "You can't devide by zero"
            except:
                self.display.text = "You did something wrong"


class CalculatorApp(App):
    def build(self):
        Config.set("graphics", "width", "430")
        Config.set("graphics", "height", "600")
        Config.set("graphics", "resizable", "0")
        return CalculatorLayout()


if __name__ == "__main__":
    CalculatorApp().run()


