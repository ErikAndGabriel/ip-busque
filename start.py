import os 
from ipbusca import BuscarIp, SalvarDados
from colorama import init, Fore

init()

def clear():
    os.system('clear')

banner = f"""
 {Fore.BLUE} ___       ____                      
 |_ _|_ __ | __ ) _   _ ___  ___ __ _ 
  | || '_ \|  _ \| | | / __|/ __/ _` |
{Fore.RED}  | || |_) | |_) | |_| \__ \ (_| (_| |
 |___| .__/|____/ \__,_|___/\___\__,_|
     |_|                         """

def menu():
    while True:
        try:
            print(banner)
            print(f"\n{Fore.YELLOW}[1]{Fore.RESET} buscar ip")
            print(f"{Fore.YELLOW}[2]{Fore.RESET} buscar e salvar ip")
            print(f"{Fore.YELLOW}[0]{Fore.RESET} sair")
            escolha = int(input("\nescolha: "))
            if escolha == 1:
                ip = input("seu ip: ")
                usuario = BuscarIp(ip)
                print(usuario.buscar())
                input("precione [ENTER]")
                clear()
                continue
            elif escolha == 2:
                ip = input("seu ip: ")
                arquivo = input("nome do arquivo: ")
                usuario = SalvarDados(ip, arquivo)
                print(usuario.buscar())
                usuario.salvar()
                input("precione [ENTER]")
                clear()
                continue
            elif escolha == 0:
                exit()
            else:
                input("escolha invalida, precione [ENTER]")
                clear()
                continue
        except ValueError:
            input("somente numeros, precione [ENTER]")
            clear()
            continue 


if __name__ == "__main__":
    clear()
    menu()
