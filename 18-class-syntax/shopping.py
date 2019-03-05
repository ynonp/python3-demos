class Invoice:
    vat = 0.17

    def __init__(self):
        self.foo = 10
        
    def print_item(self, name, price):
        print(f'{name}: {self._with_vat(price)}')

    def _with_vat(self, price):
        return price * (1 + self.vat)

i = Invoice()
j = Invoice()
k = Invoice()

Invoice.vat = 0.10

# print: 3510
i.print_item('iPhone', 3000)
i.print_item('Samsung', 3120)

j.print_item('demo', 1000)
