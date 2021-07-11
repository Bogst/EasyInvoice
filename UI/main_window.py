from database.session import get_session
from database.entities.ORM.ClientORM import ClientORM


class MainWindow:
    def __init__(self):
        self.selected_client = None
        self.selected_month = None

    @staticmethod
    def get_clients():
        return get_session().query(ClientORM).all()

    def set_selected_client(self, name:str):
        self.selected_client = get_session().query(ClientORM).filter(ClientORM.name == name).first()
        print(f"Selected client: {self.selected_client}")

    def set_selected_month(self, month_name: str):
        self.selected_month = month_name
        print(f"Selected month: {month_name}")

    def get_client_defaults(self):
        return self.selected_client.usual_quantity, self.selected_client.usual_price

