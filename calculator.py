import sys

def soma(x,y):
    return x + y

def subtracao(x,y):
    return x - y

def multiplicacao(x,y):
    return x * y

def divisao(x,y):
    return x / y

ultimo_calculo = []
def historico():
    global ultimo_calculo
    if ultimo_calculo == []:
        print("Non-existant history to show. Try doing a math operation.")
    else:
        for i in ultimo_calculo:
            print(i)            

def verificar_operacao():
    operacoes_possiveis = ["+","-","*","/",".", "?"]
    while True:
        operacao = input("Choose the operation:\n+ for adding\n- for subtract\n* for multiply\n/ for divide\n. to end\n? for history\n")
        if operacao in operacoes_possiveis:
            return operacao
        else:
            print("Invalid operation, please try again.")

def main():
    Reset = "y"
    while Reset.lower() == "y":
        isEnd = False
        while not isEnd:
            verify = False
            while not verify:
                numero1 = input("\nType the first number: ")
                try:
                    numero1 = float(numero1)
                    verify = True
                except:
                    print("Try again, invalid number.")
            operacao = verificar_operacao()
            if operacao == "?":
                historico()
                operacao = verificar_operacao()
                if operacao == ".":
                    sys.exit()
            if operacao == ".":
                sys.exit()
            verify = False
            while not verify:
                numero2 = input("\nType the second number: ")
                try:
                    numero2 = float(numero2)
                    verify = True
                except:
                    print("Try again, invalid number.")
            resultado = None
            if operacao == "+":
                resultado = soma(numero1, numero2)
            elif operacao == "-":
                resultado = subtracao(numero1, numero2)
            elif operacao == "*":
                resultado = multiplicacao(numero1, numero2)
            else:
                resultado = divisao(numero1, numero2)
            
            print(f"\nThe result is {numero1} {operacao} {numero2} = {resultado}\n")
            
            ultimo_calculo.append(resultado)
            verify = False
            while not verify:
                try: 
                    Reset = input("\nWould you like to reset calculator? Type 'y' for yes or 'n' for no. If you may like, type '?' to check the history of given results.: \n")
                    if Reset == "n":
                        verify = True
                        sys.exit("Ending...")
                    elif Reset == "y":
                        main()
                    elif Reset == "?":
                        historico()
                    else:
                        print("Invalid digit, try again.")
                except Exception as e:
                    print("Something went wrong: ", e)
main()