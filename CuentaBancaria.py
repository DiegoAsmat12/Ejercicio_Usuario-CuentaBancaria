class CuentaBancaria:

    cuentasBancarias=[]

    def __init__(self,tasa_interes=5,balance=0):
        self.tasa_interes=tasa_interes
        self.balance=balance
        CuentaBancaria.cuentasBancarias.append(self)

    def deposito(self,amount):
        self.balance+=amount
        return self

    def retiro(self,amount):
        if(CuentaBancaria.puede_retirar(self.balance,amount)):
            self.balance-=amount
        else:
            print("No cuenta con los fondos suficientes para realizar este retiro.")
        return self

    def mostrar_info_cuenta(self):
        print(f"Tasa de interes: {self.tasa_interes}, Balance:{self.balance}")

    def obtener_balance(self):
        return self.balance

    def generar_interes(self):
        self.balance *=(100 +self.tasa_interes)/100
        return self

    @classmethod
    def imprime_instancias(cls):
        cls.cuentasBancarias
        for cuenta in cls.cuentasBancarias:
            cuenta.mostrar_info_cuenta()

    @staticmethod
    def puede_retirar(balance,amount):
        if(balance-amount<0): return False
        return True
