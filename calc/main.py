from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class Calculator(BoxLayout):
    def solve(self, text):
        try:
            s = str(eval(text))
        except:
            s = "Erro"
        return s

class App(App):
    def build(self):
        return Calculator()

App().run()
