# coding: utf-8
import requests

class Rate:
    def __init__(self, format='value', diff=False):
        self.format = format
        self.diff = diff
    
    def exchange_rates(self):
        """
        Возвращает ответ сервиса с информацией о валютах в виде:
        
        {
            'AMD': {
                'CharCode': 'AMD',
                'ID': 'R01060',
                'Name': 'Армянских драмов',
                'Nominal': 100,
                'NumCode': '051',
                'Previous': 14.103,
                'Value': 14.0879
                },
            ...
        }
        """
        r = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
        return r.json()['Valute']
    
    
    def max_value_daily(self):
        """
        Возвращает наименование валюты Name с максимальным значение курса:
        отношение текущего значения Value к номиналу Nominal
        """
        response = self.exchange_rates()
        max_value = 0
        result = ''
        for key, response_item in response.items():
            current_rate = (response_item['Value'] / response_item['Nominal'])
            if current_rate > max_value:
                max_value = current_rate
                result = response_item['Name']
        return result
    
    def make_format(self, currency):
        """
        Возвращает информацию о валюте currency в двух вариантах:
        - полная информация о валюте при self.format = 'full':
        Rate('full').make_format('EUR')
        {
            'CharCode': 'EUR',
            'ID': 'R01239',
            'Name': 'Евро',
            'Nominal': 1,
            'NumCode': '978',
            'Previous': 79.6765,
            'Value': 79.4966
        }
        
        Rate('value').make_format('EUR')
        79.4966
        """
        response = self.exchange_rates()
        
        if currency in response:
            if self.format == 'full':
                return response[currency]
            
            if self.format == 'value':
                result = response[currency]['Value']
                if self.diff == True:
                    result -= response[currency]['Previous']
                return f'{result:.4f}'
        
        return 'Error'
    
    def eur(self):
        """
        Возвращает курс евро на сегодня в формате self.format
        Если diff = True, то возвращает разность c прошлым значением
        """
        return self.make_format('EUR')
    
    def usd(self):
        """
        Возвращает курс доллара на сегодня в формате self.format
        Если diff = True, то возвращает разность c прошлым значением
        """
        return self.make_format('USD')

    def AZN(self):
        """
        Возвращает курс азербайджанского маната на сегодня в формате self.format
        Если diff = True, то возвращает разность c прошлым значением
        """
        return self.make_format('AZN')