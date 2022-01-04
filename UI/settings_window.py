from database.session import get_session
from database.entities.ORM.ClientORM import ClientORM
from database.entities.ORM.SettingsORM import SettingsORM


class SettingsWindow:
    def __init__(self):
        pass

    @staticmethod
    def get_clients():
        return get_session().query(ClientORM).all()

    @staticmethod
    def create_client(name:str, addrLineI:str, addrLineII:str, postCode:str, phone:str, quantity:float, price:float,
                      term:int):
        client = ClientORM()
        client.name = name
        client.address_line_i = addrLineI
        client.address_line_ii = addrLineII
        client.post_code = postCode
        client.phone = phone
        client.usual_quantity = quantity
        client.usual_price = price
        client.terms = term

        session = get_session()
        session.add(client)
        session.commit()

    @staticmethod
    def get_client(name:str):
        return get_session().query(ClientORM).filter(ClientORM.name == name).first()

    @staticmethod
    def delete_client(name:str):
        session = get_session()
        client = session.query(ClientORM).filter(ClientORM.name==name).first()
        session.delete(client)
        session.commit()

    @staticmethod
    def update_client(client_name, new_client_name, address_line_i, address_line_ii, post_code,
                                     phone_number, quantity, price, term):
        session = get_session()
        client = session.query(ClientORM).filter(ClientORM.name==client_name).first()
        client.name = new_client_name
        client.address_line_i = address_line_i
        client.address_line_ii = address_line_ii
        client.post_code = post_code
        client.phone = phone_number
        client.usual_quantity = quantity
        client.usual_price = price
        client.terms = term
        session.commit()

    @staticmethod
    def create_init_settings():
        session = get_session()
        settings = SettingsORM()
        settings.invoice_nr = 1
        settings.name = "Team2Clean 98"
        settings.address_line_i = "18 Guelph's Lane"
        settings.address_line_ii = "Thaxted, Dunmow"
        settings.post_code = "CM6 2PT"
        settings.phone = "07551305564"
        session.add(settings)
        session.commit()

    @staticmethod
    def get_settings():
        settings = get_session().query(SettingsORM).first()
        if settings is None:
            SettingsWindow.create_init_settings()
        settings = get_session().query(SettingsORM).first()
        return settings

    @staticmethod
    def update_settings(invoice_nr, name, address_line_i, address_line_ii, post_code,
                                       phone_number):
        session = get_session()
        settings = session.query(SettingsORM).first()
        settings.invoice_nr = invoice_nr
        settings.name = name
        settings.address_line_i = address_line_i
        settings.address_line_ii = address_line_ii
        settings.post_code = post_code
        settings.phone = phone_number
        session.commit()

    @staticmethod
    def increment_invoice_nr(new_invoice_nr):
        session = get_session()
        settings = session.query(SettingsORM).first()
        if new_invoice_nr + 1 > settings.invoice_nr:
            settings.invoice_nr = new_invoice_nr+1
        session.commit()

    @staticmethod
    def update_all_prices(amount):
        session = get_session()
        clients = session.query(ClientORM).all()
        for client in clients:
            client.usual_price = float(client.usual_price) + amount
        session.commit()
