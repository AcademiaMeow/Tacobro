from models.model import model


class Ad():

    def __init__(self, ad, poster, URL, start_date, end_date, board):
        self.ad = ad
        self.poster = poster
        self.URL = URL
        self.start_date = start_date
        self.end_date = end_date
        self.board = board
