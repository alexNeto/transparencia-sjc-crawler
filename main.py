from appman import AppMan


appman = AppMan()

appman.atualiza_raspagem()
while(True):
    print("Cargos da camara de São José dos Campos")
    print(appman.menu())
    escolha = int(input("Deseja ver as médias de qual cargo? "))
    if escolha == -1:
        break
    appman.plota(escolha)


