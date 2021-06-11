'''
o sistema deve conseguir adicionar produtos no banco de dados e acessa-los pelo nome do produto ou pelo seu Id
-o sistema deve ter uma "interface" de terminal que dê acesso a marco a acessar e adicionar seus produtos,
deleta-los, ver a quantidade de cada um e que avise a ele quando faltar menos de 3 exemplares de algum produto
'''


class Marquito:
    def __init__(self):
        self.data = {}
        while True:
            self.tratamento()
            for nome, values in self.data.items():
                if values[1] <= 3:
                    print(f"O produto {nome} tem apenas {values} exemplares!")
                    print("-="*30)
            print("-=" * 30)
            querer = input("Oque você quer acessar?\nadicionar (1) // retirar (2) // deletar (3) // acessar (4) // armazem (5) // sair (6)\n---> ")
            print("-=" * 30)
            if querer == "1":
                self.add()
            elif querer == "2":
                self.sub()
            elif querer == "3":
                self.delete()
            elif querer == "4":
                self.acesso()
            elif querer == "5":
                self.quantity()
            elif querer == "6":
                break
            else:
                print("Erro, reiniciando...")

    def tratamento(self):
        abc = open("LittlePIP.txt", "r")
        dados = abc.read()
        dados2 = dados.split("\n")
        capsula = []
        try:
            for value in dados2:
                if len(capsula) != 3 and value != " " and value != "":
                    capsula.append(value)
                else:
                    if int(capsula[2]) > 0:
                        self.data[capsula[0]] = [capsula[1], int(capsula[2])]
                    capsula = []
        except IndexError:
            pass

    def acesso(self):
        qual = input("Nome ou id do produto ---> ")
        for nome, values in self.data.items():
            if qual == nome or qual == values[0]:
                print(f"{nome} ---> {values[1]}")

    def delete(self):
        qual = input("Nome ou id do produto para retirar ---> ")
        try:
            for nome, values in self.data.items():
                if qual == nome or qual == values[0]:
                    del self.data[nome]
                    self.atualizar()
                    print(f"{nome} foi deletado!")
        except IndexError:
            pass

    def atualizar(self):
        abc = open("LittlePIP.txt", "w+")
        for nome, values in self.data.items():
            abc.write(f"{nome}\n{values[0]}\n{values[1]}\n\n")
        abc.close()

    def add(self):
        qual = input("Nome do produto ---> ")
        idd = input("id do produto ---> ")
        quantidade = int(input("quantidade do produto ---> "))
        self.data[qual] = [idd, quantidade]
        self.atualizar()

    def sub(self):
        qual = input("Nome ou id do produto ---> ")
        try:
            for nome, values in self.data.items():
                if qual == nome or qual == values[0]:
                    print(f"O produto {nome} tem {values[1]} exemplares!")
                    quanto = int(input("Quanto sera retirado do produto? ---> "))
                    if values[1] <= quanto:
                        print(f"O produto {nome} será deletado!")
                        del self.data[nome]
                        break
                    else:
                        self.data[nome][1] -= quanto
                        break
        except IndexError:
            pass
        self.atualizar()
        print(f"Atualizado!")

    def quantity(self):
        for nome, values in self.data.items():
            print(f"{nome} ---> {values[1]}")


Marquito()

