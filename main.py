from Usuario import Usuario
from CuentaBancaria import CuentaBancaria

diego = Usuario("Diego","diego.asmat@example.com",[CuentaBancaria(5,100),CuentaBancaria(3)])

diego.hacer_deposito(0,400).hacer_deposito(1,200).hacer_retiro(0,200).transferir_dinero(diego,1,0,100).mostrar_balance_usuario()