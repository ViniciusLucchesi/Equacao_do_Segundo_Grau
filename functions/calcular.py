from math import sqrt


class SegundoGrau:
    def __init__(self, valor_a, valor_b, valor_c):
        self.a = valor_a
        self.b = valor_b
        self.c = valor_c
        self.resultado = list()

    @property
    def valor_a(self):
        return self.a
    
    @property
    def valor_b(self):
        return self.b
    
    @property
    def valor_c(self):
        return self.c
    
    def calcular_delta(self):
        return (self.b**2) - (4 * self.a * self.c)

    def calcular_raizes(self):
        delta = self.calcular_delta()

        # Se não houver raiz
        if delta < 0:
            return self.resultado
        
        # Se houver uma raízes
        x = ((self.b * -1) + sqrt(delta)) / (2*self.a)
        self.resultado.append(round(x, 2))

        # Se houver mais de uma raiz
        if delta > 0:
            x2 = ((self.b * -1) - sqrt(delta)) / (2*self.a)
            self.resultado.append(round(x2, 2))
        
        return self.resultado
    
    def __str__(self):
        return f"A: {self.a}\nB: {self.b}\nC: {self.c}\nDelta: {self.calcular_delta}\nResult: {self.calcular_raizes}"



if __name__ == '__main__':
    conta = SegundoGrau(2, 0, -18)
    print(conta)