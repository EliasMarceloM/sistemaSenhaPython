
#-------------cadastra a senha--------
f = open("senha.txt", "w")
senha = input("cadastre um senha:")
f.write(senha)
#-------------cadastra a senha--------
#-------------verifica se a senha está correta  --------
senha = input("digite a sua senha:")
f = open("senha.txt", "r")
texto = ""
for x in f:
 texto=texto+x 
if senha == texto:
 print("senha correta")
else : 
 print("senha errada")    

#-------------verifica se a senha está correta  --------
f.close()