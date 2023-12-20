undefined = "undefined"
errors = [{"errors": "No information with this request"}, {"errors": "No information about keys"},
          {"errors": "Something went wrong with server of parsing sites"}]
maxItems = 5


class CurrencyRates:
    def __init__(self):
        pass

    def get_rates(self, currency):
        if currency == "USD":
            return {"EUR": 0.9}
        elif currency == "EUR":
            return {"USD": 1.10}
