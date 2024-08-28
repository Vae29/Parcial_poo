class Cuenta_Bancaria:
    def __init__(self,numero_cuenta,saldo):
        self.numero_cuenta=numero_cuenta
        self.saldo=saldo

mi_cuenta=Cuenta_Bancaria("123456","3.104,00")
print(type(mi_cuenta))
print(f"\nSu número de cuenta es: {mi_cuenta.numero_cuenta}\nSu saldo actual es: {mi_cuenta.saldo}\n")

cuenta_2=Cuenta_Bancaria("789103","10.500,00")
print("/////////////////////////////////////////")
print(type(cuenta_2))
print(f"\nSu número de cuenta es: {cuenta_2.numero_cuenta}\nSu saldo actual es: {cuenta_2.saldo}")
    
        