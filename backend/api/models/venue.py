# from api.models.category import Category
import api.models as models
class Venue():
    __table__ = 'venues'
    columns = ['id', 'foursquare_id', 'name', 'price',
            'rating', 'likes', 'menu_url']

    def __init__(self, values):
        self.__dict__ = dict(zip(self.columns, values))

    def build_category(self, values):
        category = models.Category(values)


