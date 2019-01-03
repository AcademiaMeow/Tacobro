from models.model import model


class AdBoard(model):

    def __init__(self, position, width, height, price):
        self.position = position
        self.width = width
        self.height = height
        self.price = price
