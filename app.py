import csv
import array
# el programa deberá calcular el ganador de votos validos considerando que los siguientes datos son proporcionados:
# region,provincia,distrito,dni,candidato,esvalido
# Si hay un candidato con >50% de votos válidos retornar un array con un string con el nombre del ganador
# Si no hay un candidato que cumpla la condicion anterior, retornar un array con los dos candidatos que pasan a segunda vuelta
# Si ambos empatan con 50% de los votos se retorna el que apareció primero en el archivo
# el DNI debe ser valido (8 digitos)

        
class CalculaGanador:

    def leerdatos(self):
        data = []
        with open('0204.csv', 'r') as csvfile:
            next(csvfile)
            datareader = csv.reader(csvfile)
            for fila in datareader:
                data.append( fila)
        return data
    
    
            

    def calcularganador(self, data):
        votosxcandidato = {}
        cant=0
        for fila in data:
            if self.dni_valido(fila[3]):
                nombre_candidato=fila[4] #Renombre de variable: Se le asigna una variable para saber que referencia la fila 4 
                valido=fila[5] #Renombre de variable: Se le asigna una variable para saber que referencia la fila 5
                cant=cant+1
                if not nombre_candidato in votosxcandidato:
                    votosxcandidato[nombre_candidato] = [nombre_candidato, 0]
                if valido == '1':
                    votosxcandidato[nombre_candidato][1] = votosxcandidato[nombre_candidato][1] + 1
        self.mostrar_candidatosxvotos(votosxcandidato) #Extraccion de metodos
        return self.print_ordenado(votosxcandidato, cant) #Extraccion de metodos

    def mostrar_candidatosxvotos(self, votosxcandidato): #muestra cada candidato con sus respectivos votos
        for candidato in votosxcandidato:
            print('candidato: ' + candidato + ' votos validos: ' + str(votosxcandidato[candidato]))

    def print_ordenado(self, votosxcandidato, cant): #Muestra el primer candidato de la lista ordenada, el que tiene mas votos
        dev=[]
        cnt=0
        print('cant: ' + str(cant))
        ordenado = sorted(votosxcandidato.items(), key=lambda item:item[1][1], reverse=True)
        for candidato in ordenado:
            if(int(cant/2)<=candidato[1][1]):
                return [candidato]
            if(int(cant/2)>candidato[1][1]):
                dev=dev + [candidato]
                cnt=cnt+1
            if(cnt==2):
                return [dev]
        


    def dni_valido(self, dni):
        if len(dni) == 8:
            return True
        return False


def Prueba_uni1(): #2 candidatos con la misma cantidad de votos
    datatest = [
['Áncash', 'Asunción', 'Acochaca', '40810062', 'Eddie Hinesley', '1'],
['Áncash', 'Asunción', 'Acochaca', '86777322', 'Aundrea Grace', '1'],
['Áncash', 'Asunción', 'Acochaca', '23017965', 'Aundrea Grace', '1'],
['Áncash', 'Asunción', 'Acochaca', '57533597', 'Eddie Hinesley', '1']
]            
    print('Prueba unitaria 1: Empate de candidatos')
    c=CalculaGanador()
    print(c.calcularganador(datatest))

def Pruebauni2(): #Se ingresa un dni invalido
    datatest = [
['Áncash', 'Asunción', 'Acochaca', '40810062', 'Eddie Hinesley', '0'],
['Áncash', 'Asunción', 'Acochaca', '8677732', 'Aundrea Grace', '0'],
['Áncash', 'Asunción', 'Acochaca', '2301796', 'Aundrea Grace', '1'],
['Áncash', 'Asunción', 'Acochaca', '57533597', 'Eddie Hinesley', '1']

]            
    print('Prueba unitaria 2: Dni invalido')
    c=CalculaGanador()
    print(c.calcularganador(datatest))


def Pruebauni3(): #ningun candidato con votos mayor al 50%
    datatest = [
['Áncash', 'Asunción', 'Acochaca', '40810062', 'Eddie Hinesley', '1'],
['Áncash', 'Asunción', 'Acochaca', '86777322', 'Aundrea Grace', '1'],
['Áncash', 'Asunción', 'Acochaca', '23017965', 'Aundrea Grace', '1'],
['Áncash', 'Asunción', 'Acochaca', '40810062', 'Hinesley', '1'],
['Áncash', 'Asunción', 'Acochaca', '86777322', 'Grace', '1'],
['Áncash', 'Asunción', 'Acochaca', '57533597', 'Eddie Hinesley', '1']
]  
    print('Prueba unitaria 3: Ningun candidato con votos mayor al 50%')
    c=CalculaGanador()
    print(c.calcularganador(datatest))

""""
c = CalculaGanador()
print(c.calcularganador(c.leerdatos()))
datatest = [
['Áncash', 'Asunción', 'Acochaca', '40810062', 'Eddie Hinesley', '0'],
['Áncash', 'Asunción', 'Acochaca', '57533597', 'Eddie Hinesley', '1'],
['Áncash', 'Asunción', 'Acochaca', '86777322', 'Aundrea Grace', '1'],
['Áncash', 'Asunción', 'Acochaca', '23017965', 'Aundrea Grace', '1']
]
print(c.calcularganador(datatest))
exit()
"""

Prueba_uni1()
print()
Pruebauni2()
print()
Pruebauni3()
exit()