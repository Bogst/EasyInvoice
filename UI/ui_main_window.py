
from datetime import datetime
from calendar import month_abbr
from functools import partialmethod, partial

from PyQt5.QtCore import QSize, pyqtSlot, QDate
from PyQt5.QtGui import QIcon, QDoubleValidator
from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QComboBox, QLabel, QDateEdit, QLineEdit, \
    QFrame

from UI.main_window import MainWindow
from UI.ui_settings_window import Ui_SettingsDialog
from UI.ui_splash_screen import SplashScreen
from pathing import resource_path


class MainWindowUI(QWidget):
    def __init__(self):
        super().__init__()
        self.main_window = MainWindow()
        self.title = "Easy Invoice"
        self.splash_screen = SplashScreen(main_window=self)

        self.config_button = QPushButton()

        self.client_dropdown = QComboBox()
        self.month_dropdown = QComboBox()
        self.dates = []
        self.amounts_per_hour = []
        self.quantities = []
        self.gross_total = QLabel()

        self.new_date = QDateEdit()

        self.dates_layout = QVBoxLayout()
        self.month_selection_frame = QFrame()
        self.dates_frame = QFrame()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle(self.title)

        main_layout = QVBoxLayout()

        title_layout = QHBoxLayout()
        title_layout.addStretch()

        self.config_button.setIcon(QIcon(resource_path('./resources/img/settings_icon.png')))
        self.config_button.setIconSize(QSize(30, 30))
        self.config_button.pressed.connect(self.settings_window)

        title_layout.addWidget(self.config_button)

        main_layout.addItem(title_layout)

        lef_pane = QVBoxLayout()

        # Clients droplist
        client_box = QHBoxLayout()
        lef_pane.addItem(client_box)

        clients_label = QLabel()
        clients_label.setText("Choose client: ")
        client_box.addWidget(clients_label)

        self.update_clients_list()
        # self.client_dropdown.setEditable(True)
        self.client_dropdown.setCurrentText("")
        self.client_dropdown.textActivated.connect(self.client_selected)
        client_box.addWidget(self.client_dropdown)

        # Month selection droplist
        month_layout = QHBoxLayout()
        self.month_selection_frame.setLayout(month_layout)
        self.month_selection_frame.hide()
        month_label = QLabel()
        month_label.setText("For month")
        month_layout.addWidget(month_label)

        month_list = [month_abbr[i] for i in range(1, 13)]

        self.month_dropdown.addItems(month_list)
        current_month_index = (datetime.now().month + 12 - 2) % 12
        self.month_dropdown.setCurrentIndex(current_month_index)
        self.month_selected(self.month_dropdown.itemText(current_month_index))
        self.month_dropdown.textActivated.connect(self.month_selected)
        month_layout.addWidget(self.month_dropdown)

        lef_pane.addWidget(self.month_selection_frame)

        right_pane = QVBoxLayout()

        main_body_layout = QHBoxLayout()
        main_body_layout.addItem(lef_pane)

        main_body_layout.addStretch()
        main_body_layout.addItem(right_pane)

        main_layout.addItem(main_body_layout)

        # dates

        self.dates_frame.setLayout(self.dates_layout)
        self.dates_layout.setParent(self.dates_frame)
        self.dates_frame.hide()

        # New date picker
        new_date_picker_layout = QHBoxLayout()
        new_date_picker_layout.setParent(self.dates_layout)
        self.dates_layout.addItem(new_date_picker_layout)
        new_date_picker_lable = QLabel()
        new_date_picker_lable.setText("Add new date")
        new_date_picker_layout.addWidget(new_date_picker_lable)
        self.new_date.setCalendarPopup(True)
        self.new_date.setDate(QDate.currentDate())
        self.new_date.dateChanged.connect(self.add_new_date)
        new_date_picker_layout.addWidget(self.new_date)
        new_date_picker_layout.addStretch()

        self.gross_total.setText("Gross Total: ")
        self.gross_total.hide()
        new_date_picker_layout.addWidget(self.gross_total)

        main_layout.addWidget(self.dates_frame)

        main_layout.addStretch()

        print_box = QHBoxLayout()
        main_layout.addItem(print_box)
        print_box.setParent(main_layout)
        print_box.addStretch()

        print_buton = QPushButton()
        print_buton.setText('Print')
        print_box.addWidget(print_buton)

        self.setLayout(main_layout)

        self.splash_screen.show()

    @pyqtSlot(str)
    def client_selected(self, selected_text):
        self.month_selection_frame.show()
        self.dates_frame.show()
        self.main_window.set_selected_client(selected_text)

    @pyqtSlot(str)
    def month_selected(self, selected_month):
        month_name = datetime.strptime(selected_month, '%b').strftime("%B")
        self.main_window.set_selected_month(month_name)

    @pyqtSlot(QDate)
    def add_new_date(self, date):
        default_price, default_amount = self.main_window.get_client_defaults()
        layout = QHBoxLayout()
        frame = QFrame()
        frame.setLayout(layout)
        layout.setParent(frame)
        self.dates_layout.insertWidget(len(self.dates), frame)

        delete_button = QPushButton()
        delete_button.setIcon(QIcon(resource_path('./resources/img/delete_icon.png')))
        delete_button.pressed.connect(partial(self.delete_date, len(self.dates)))
        layout.addWidget(delete_button)
        delete_button.setParent(frame)

        date_edit = QDateEdit()
        date_edit.setDate(date)
        date_edit.setCalendarPopup(True)
        self.dates.append(date_edit)
        layout.addWidget(date_edit)
        date_edit.setParent(frame)

        amount_lable = QLabel()
        amount_lable.setText('amount / h')
        layout.addWidget(amount_lable)
        amount_lable.setParent(frame)

        amount_edit = QLineEdit()
        amount_edit.setText(f'{default_price}')
        amount_edit.setValidator(QDoubleValidator(0, 100, 2))
        self.amounts_per_hour.append(amount_edit)
        layout.addWidget(amount_edit)
        amount_edit.setParent(frame)

        quantity_label = QLabel()
        quantity_label.setText("quantity")
        layout.addWidget(quantity_label)
        quantity_label.setParent(frame)

        quantity_line_edit = QLineEdit()
        quantity_line_edit.setText(f'{default_amount}')
        quantity_line_edit.setValidator(QDoubleValidator(0, 100, 2))
        self.quantities.append(quantity_line_edit)
        layout.addWidget(quantity_line_edit)
        quantity_line_edit.setParent(frame)

        gross = QLabel()
        gross.setText(f"Gross: {float(amount_edit.text()) * float(quantity_line_edit.text()):.2f}")
        layout.addWidget(gross)
        gross.setParent(frame)

        amount_edit.textChanged.connect(partial(self.update_amount, gross, quantity_line_edit))
        quantity_line_edit.textChanged.connect(partial(self.update_quantity, gross, amount_edit))
        self.update_gross_total()

    def update_amount(self, gross, new_quantity, new_ammount ):
        if len(new_ammount) > 0:
            gross.setText(f"Gross: {float(new_ammount) * float(new_quantity.text()):.2f}")
        else:
            gross.setText("Gross: NaN")
        self.update_gross_total()

    def update_quantity(self, gross, new_ammount, new_quantity):
        if len(new_quantity) > 0:
            gross.setText(f"Gross: {float(new_ammount.text()) * float(new_quantity):.2f}")
        else:
            gross.setText("Gross: NaN")
        self.update_gross_total()

    def update_gross_total(self):
        running_sum = 0
        for new_quantity, new_amount in zip(self.quantities, self.amounts_per_hour):
            if len(new_quantity.text()) == 0 or len(new_amount.text()) == 0:
                self.gross_total.setText("Total Gross: NaN")
                return

            running_sum += (float(new_quantity.text()) * float(new_amount.text()))
        self.gross_total.setText(f"Total Gross: {running_sum}")
        self.gross_total.show()

    def delete_date(self, date_index):
        self.dates_layout.itemAt(date_index).widget().deleteLater()
        self.dates.pop(date_index)
        self.quantities.pop(date_index)
        self.amounts_per_hour.pop(date_index)
        self.update_gross_total()

    def update_clients_list(self):
        clients = MainWindow.get_clients()
        self.client_dropdown.clear()
        self.client_dropdown.addItems([c.name for c in clients])

    @pyqtSlot()
    def settings_window(self):
        settings_window = Ui_SettingsDialog()
        settings_window.setupUi(settings_window)
        settings_window.exec_()
        self.update_clients_list()