from address import Address


class WorkAddress(Address):
    def __init__(self, first_name, last_name, city, street, house_no, company):
        super().__init__(first_name, last_name, city, street, house_no)
        self.company = company

    def get_full_address(self):
        return super().get_full_address() + ", " + self.company
