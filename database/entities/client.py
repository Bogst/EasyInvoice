
class Client:
    name = ""
    address_line_i = ""
    address_line_ii = ""
    post_code = ""
    phone = ""
    terms = 0

    def __repr__(self):
        return f"<Client>(name={self.name})"
