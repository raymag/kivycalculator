#:Kivy 1.9.1
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.core.text import LabelBase

class Calculator(BoxLayout):
    def solve(self, text): #Resolve as Operacoes
        try:
            s = str(eval(text))
        except:
            s = "Erro"
        return s
    def apagar(self, text): #Apaga o ultimo caractere do Campo de Operacoces
        try:
            s = text[:-1]
        except:
            s = ''
        return s

class App(App):
    title = "Calculadora-Kivy"
    def build(self):
        return Calculator()
if __name__ == '__main__':
    Window.clearcolor = [0.1, 0.1, 0.1, 1]
    App().run()
#<Teclado@GridLayout>
