class Apartment(object):

    def __init__(self, url, location, rent):
        self._url = url
        self._location = location
        self._rent = rent

    @property
    def url(self):
        return self._url

    @property
    def location(self):
        return self._location

    @property
    def rent(self):
        return self._rent
