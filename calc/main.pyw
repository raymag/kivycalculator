from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class Calculator(BoxLayout):
    def solve(self, text): #Resolve as Operações
        try:
            s = str(eval(text))
        except:
            s = "Erro"
        return s
    def apagar(self, text): #Apaga o ultimo caractere do Campo de Operacoces
        try:
            s = text.replace(text[-1], '')
        except:
            s = ''
        return s
    
class App(App):
    def build(self):
        return Calculator()

App().run()
