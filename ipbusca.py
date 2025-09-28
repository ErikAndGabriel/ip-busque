import requests 
import json 

class BuscarIp:
    def __init__(self, ip):
        self.ip = ip 
        self.dados = None 

    def buscar(self):
        url = f"https://ipinfo.io/{self.ip}/json"
        resposta = requests.get(url)
        if resposta.status_code == 200:
            dados = resposta.json()
            print("=" * 50)
            print(f"ip: {dados['ip']}")
            print(f"hostname: {dados['hostname']}")
            print(f"city: {dados['city']}")
            print(f"region: {dados['region']}")
            print(f"country: {dados['country']}")
            print(f"loc: {dados['loc']}")
            print(f"org: {dados['org']}")
            print(f"postal: {dados['postal']}")
            print(f"timezone: {dados['timezone']}")
            print(f"readme: {dados['readme']}")
            print(f"anycast: {dados['anycast']}")
            print("=" * 50)
            self.dados = dados

class SalvarDados(BuscarIp):
    def __init__(self, ip, arquivo):
        super().__init__(ip)
        self.arquivo = arquivo
    def salvar(self):
        try:
            with open(f"{self.arquivo}", "w") as arq:
                json.dump(self.dados, arq, indent=4)
                print("arquivo criado com secesso")
        except FileExistsError:
            print("esse arquivo ja existe!")
        except exceptions as e:
            print(f"erro {e}")

pessoa1 = SalvarDados("8.8.8.8", "coisado.json")
pessoa1.buscar()
pessoa1.salvar()
