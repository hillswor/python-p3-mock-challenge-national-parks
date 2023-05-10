class Visitor:
    all = []

    def __init__(self, name):
        if isinstance(name, str) and len(name) > 0 and len(name) < 16:
            self._name = name
        else:
            raise Exception("Name must be a string between 1 - 15 characters.")
        Visitor.all.append(self)

    @property
    def name(self):
        return self._name

    def trips(self, new_trip=None):
        from classes.trip import Trip

        return [trip for trip in Trip.all if trip.visitor == self]

    def national_parks(self, new_national_park=None):
        return list(set([trip.national_park for trip in self.trips()]))
