class Politician:

    def __init__(self, first, last, party, years_in_office, crook):
        self.first = first
        self.last = last
        self.party = party
        self.years_in_office = years_in_office
        self.crook = crook
    
    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{}.{}'.format(self.first, self.last)

    def _repr_(self):
        return "Employee('{}', '{}', '{}', {}, {})".format(self.first, self.last, self.party, self.years_in_office, self.crook)