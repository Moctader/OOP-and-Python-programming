class Order:
    def __init__(self, customer, items) -> None:
        self.customer=customer
        self.items=items
        totall=0
        for item in items:
            totall+=item.price
        self.bill=totall