class Address:
    def __init__(self, first_name, last_name, city, street, house_no):
        self.person = Person(first_name, last_name)
        self.city = city
        self.street = street
        self.house_no = house_no

    def get_full_address(self):
        return "{} {}, {}, {} {}".format(self.first_name, self.last_name, self.city, self.street, self.house_no)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

    def __gt__(self, other):
        return self.get_full_address() > other.get_full_address()
