try:
    import requests
except Exception as e:
    print(f"Lib not installed: %s" % e)

class ConsultZip:
    def __init__(self):
        self.base_url = 'https://viacep.com.br/ws/'

    @staticmethod
    def search_zip(zip):
        if ConsultZip.validate_zip(zip):
            url = f'https://viacep.com.br/ws/{zip}/json/'
            response = requests.get(url)
            data = response.json()
            if "erro" in data:
                print('zip code not found')
                return None, None
            else:
                localidade = data['localidade']
                logradouro = data['logradouro']
                return localidade, logradouro
        else:
            print("Incorrect Zip")
            return None, None

    @staticmethod
    def validate_zip(zip):
        if len(zip) == 8 or len(zip) == 9:
            return True
        else:
            return False