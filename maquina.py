print("              Maquina dispensadora")
class Product:
    def __init__(self, _name, _price):
        self.name = _name
        self.price = _price

    def __repr__(self):
        return "{0} : {1}".format(self.name, self.price)


products = {
    1: Product("Papas sin marca", 0.50),
    2: Product("Galletas", 0.45),
    3: Product("Agua", 1.35),
    4: Product("Oreo", 0.65),
    5: Product("Ruffles", 0.25),
    6: Product("Pringles", 2.35),
    7: Product("Doritos", 0.25),
    8: Product("Sanduche", 1.65),
    9: Product("Manzana",45),
    10: Product("Yogurt toni", 0.50),
    11: Product("m&m's", 1.20),
    12: Product("Coca cola", 0.35),
    13: Product("Pepsi", 0.50),
    14: Product("V220", 0.65) ,
    15: Product("Monster",3.25)
    
}

coins = {
    "1": 10,
    "50": 5,
    "25": 10,
    "10": 10,
    "5": 5
}

# coin_translator = {
#     "5": 5,
#     "10": 10,
#     "25": 25,
#     "50": 50,
#     "1": 100
# }


class Machine:

    def __init__(self, coins, products):
        self.coins = coins
        self.products = products
        self.coin_translator = coin_translator = {
            "5": 5,
            "10": 10,
            "25": 25,
            "50": 50,
            "1": 100
        }

    def display_products(self):
        for key, value in self.products.items():
            print("{0}. {1}".format(key, value))

    def calculate_return(self, price, payed):
        returned = payed-price
        returned_coins = []
        for coin, coin_ammount in self.coins.items():
            coin_value = self.coin_translator[coin]
            if returned < coin_value:
                continue
            elif returned == coin_value and coin_ammount > 0:
                returned_coins.append(coin)
                self.coins[coin] = self.coins[coin]-1
                return returned_coins
            elif coin_ammount > 0:
                while returned > 0 and coin_ammount > 0:
                    returned -= coin_value
                    if returned < 0:
                        returned += coin_value
                        break
                    self.coins[coin] = self.coins[coin]-1
                    returned_coins.append(coin)
                if returned == 0:
                    return returned_coins

        print("Maquina no tiene cambio disponible")
        return []


if __name__ == "__main__":

    machine = Machine(coins, products)
    while True:
        machine.display_products()
        option = input("-> Elija un producto, q para salir: ")
        if option == "q":
            break
        if option.isdigit():
            option = int(option)
        else:
            break
        if option not in machine.products:
            print("Producto no existe")
        else:
            print("Producto elegido: {0} : {1}".format(
                machine.products[option].name, machine.products[option].price))
            payment = input("Ingrese su pago separado por comas -> ")
            payment = payment.split(",")
            for coin in payment:
                if coin not in machine.coins:
                    print("No se ha ingresado un pago valido")
                    pass
                machine.coins[coin] = machine.coins[coin]+1
            ammount = sum([machine.coin_translator[x] for x in payment])
            product_price = machine.products[option].price*100
            if ammount == product_price:
                input("Muchas gracias por su compra ... ")
            elif ammount > product_price:
                change = machine.calculate_return(product_price, ammount)
                input("Su cambio en monedas es: {0}, total: {1}".format(
                    ",".join(change), sum([machine.coin_translator[x] for x in change])/100))