valor= float(input("qual valor será pago na casa?"))
salario = float(input("qual o seu salario?"))
mes = int(input("quantos meses de pagamento"))


prest= valor / mes

if prest > ((salario/100)*30):
    print("emprestimo nao aprovado")
else:
    print("financiamento aprovado")