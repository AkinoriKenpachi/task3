import requests
try:
    # komunikacja z API
    communication = requests.get(
        f'https://api.nbp.pl/api/exchangerates/rates/c/USD/2024-02-15/?format=json')
    response = communication.json()
    exchange_rate = response['rates'][0]['bid']
    value_in_pln = 100 * exchange_rate

    print(value_in_pln)

except ValueError:
    print("[BŁĄD] Brak kursu walut dla danego dnia, proszę wprowadzić inną datę.")

