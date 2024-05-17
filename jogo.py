def menu_principal():
    escolhas = {
        "Gênero de Jogo": None,
        "Estilo de Jogo": None,
        "Jogo": None
    }

    generos = ["Ação", "Aventura", "RPG", "Esporte", "Simulação", "Outros"]
    estilos = ["Single-player", "Multiplayer", "Co-op", "Sandbox", "Outros"]
    jogos = ["The Witcher 3", "FIFA 21", "Minecraft", "Fortnite", "Cyberpunk 2077", "Outros"]

    while True:
        print("\nMenu Principal:")
        print("1. Escolha o seu gênero de Jogo")
        print("2. Estilo de jogo")
        print("3. Escolha o seu jogo")
        print("4. Mostrar suas escolhas")
        print("5. Sair")

        opcao = input("Digite o número da opção desejada: ")

        if opcao == "1":
            print("\nEscolha o seu gênero de Jogo:")
            for idx, genero in enumerate(generos, start=1):
                print(f"{idx}. {genero}")
            genero_escolha = input("Digite o número do gênero desejado ou 'Outros' para digitar o gênero: ")
            if genero_escolha.isdigit() and 1 <= int(genero_escolha) <= len(generos):
                if int(genero_escolha) == len(generos):
                    escolhas["Gênero de Jogo"] = input("Digite o gênero do jogo que você deseja: ")
                else:
                    escolhas["Gênero de Jogo"] = generos[int(genero_escolha) - 1]
            else:
                print("Opção inválida. Tente novamente.")
            input("Gênero escolhido. Pressione Enter para voltar ao menu principal.")

        elif opcao == "2":
            print("\nEscolha o seu estilo de jogo:")
            for idx, estilo in enumerate(estilos, start=1):
                print(f"{idx}. {estilo}")
            estilo_escolha = input("Digite o número do estilo desejado ou 'Outros' para digitar o estilo: ")
            if estilo_escolha.isdigit() and 1 <= int(estilo_escolha) <= len(estilos):
                if int(estilo_escolha) == len(estilos):
                    escolhas["Estilo de Jogo"] = input("Digite o estilo de jogo que você deseja: ")
                else:
                    escolhas["Estilo de Jogo"] = estilos[int(estilo_escolha) - 1]
            else:
                print("Opção inválida. Tente novamente.")
            input("Estilo escolhido. Pressione Enter para voltar ao menu principal.")

        elif opcao == "3":
            print("\nEscolha o seu jogo:")
            for idx, jogo in enumerate(jogos, start=1):
                print(f"{idx}. {jogo}")
            jogo_escolha = input("Digite o número do jogo desejado ou 'Outros' para digitar o jogo: ")
            if jogo_escolha.isdigit() and 1 <= int(jogo_escolha) <= len(jogos):
                if int(jogo_escolha) == len(jogos):
                    escolhas["Jogo"] = input("Digite o jogo que você deseja: ")
                else:
                    escolhas["Jogo"] = jogos[int(jogo_escolha) - 1]
            else:
                print("Opção inválida. Tente novamente.")
            input("Jogo escolhido. Pressione Enter para voltar ao menu principal.")

        elif opcao == "4":
            print("\nSuas escolhas:")
            for chave, valor in escolhas.items():
                print(f"{chave}: {valor}")
            input("Pressione Enter para voltar ao menu principal.")

        elif opcao == "5":
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu_principal()
