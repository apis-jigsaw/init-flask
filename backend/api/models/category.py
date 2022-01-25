# from api.models.venue import Venue
import api.models as models
class Category:
    __table__ = 'categories'
    columns = ['id', 'name']
    def __init__(self, values):
        self.__dict__ = dict(zip(self.columns, values))

    def build_venue(self, values):
        self.venue = models.Venue(values)


