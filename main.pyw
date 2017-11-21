#:Kivy 1.9.1
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.core.text import LabelBase

LabelBase.register(name='Ubuntu',
                fn_regular='./fonts/UbuntuCondensed-Regular.ttf',
                fn_bold='./fonts/UbuntuCondensed-Regular.ttf')

class Calculator(BoxLayout):
    def fix(self, text): #Verifica a existencia de erros de escrita no TextInput
        operators = ['*', '+', '/', '.']
        repeated_operators = ['++', '//', '..', '--', '***']
        numbers = [str(n) for n in range(10)]
        if '0**0.5' in text: #Verifica se ha uso da raiz quadrada de 0
            text = text.replace('0**0.5', '0')
        if text == '': #Verifica se nenhum valor foi inserido
            text = '0'
        wrong = True
        while wrong == True: #Verifica a existencia de zeros a esquerda sem nenhum uso de sinal
            wrong = False
            try:
                if text[0] == '0' and text[1] != operators:
                    text = text[1:]
                    wrong = True
            except:
                pass
        wrong = True
        for number in numbers: #Verifica a inexistencia de numeros no TextInput
            if number in text:
                wrong = False
        if wrong == True:
            text = '0'
        wrong = True
        while wrong == True: #Verifica a existencia de operadores repetidos
            wrong = False
            for operator in repeated_operators:
                if operator in text:
                    wrong = True
                    text = text.replace(operator, (operator[:-1]))
        wrong = True
        while wrong == True: #Verifica a existencia de operadores sem termos suficientes
            wrong = False
            if text[0] in operators or ')' == text[0]:
                text = text[1:]
                print(text)
                wrong = True
            if text[-1] in operators or '-' in text[-1]:
                text = text[:-1]
                wrong = True
        return text
    def solve(self, text): #Resolve as Operacoes
        text = self.fix(text)
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
    title = "WiseCalc"
    def build(self):
        return Calculator()
if __name__ == '__main__':
    Window.clearcolor = [0.1, 0.1, 0.1, 1]
    App().run()
