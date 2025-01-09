def gerar_prompts():
    print("Bem-vindo ao gerador de prompts do StackSpot!")
    
    # Solicita ao usuário o número de prompts que deseja criar
    try:
        numero_prompts = int(input("Digite o número de prompts que deseja criar por dia: "))
        if numero_prompts <= 0:
            print("Por favor, insira um número maior que zero.")
            return
    except ValueError:
        print("Por favor, insira um número válido.")
        return

    # Gera os prompts
    prompts = []
    for i in range(1, numero_prompts + 1):
        prompt = input(f"Digite o texto para o prompt {i}: ")
        prompts.append(prompt)

    # Exibe os prompts gerados
    print("\nPrompts gerados:")
    for i, prompt in enumerate(prompts, start=1):
        print(f"{i}. {prompt}")

    print("\nObrigado por usar o gerador de prompts do StackSpot!")

# Executa a função
if __name__ == "__main__":
    gerar_prompts()