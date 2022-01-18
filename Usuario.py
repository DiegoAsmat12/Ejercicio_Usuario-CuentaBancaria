from CuentaBancaria import CuentaBancaria

class Usuario:
    def __init__(self,name="N/A",email="N/A",accounts=[]):
        self.name = name
        self.email = email
        self.accounts = accounts

    def hacer_deposito(self,account_position,amount):
        self.accounts[account_position].deposito(amount)
        return self

    def hacer_retiro(self,account_position,amount):
        self.accounts[account_position].retiro(amount)
        return self

    def mostrar_balance_usuario(self):
        for account in self.accounts:
            print("User: %s, Balance: %d"%(self.name,account.obtener_balance()))

    def transferir_dinero(self, other_user,account_position,other_user_account_position,amount):
        self.hacer_retiro(account_position,amount)
        other_user.hacer_deposito(other_user_account_position,amount)
        return self

