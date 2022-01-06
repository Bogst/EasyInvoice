
from datetime import datetime
from calendar import month_abbr
from functools import partialmethod, partial

from PyQt5.QtCore import QSize, pyqtSlot, QDate, QDateTime
from PyQt5.QtGui import QIcon, QDoubleValidator, QIntValidator
from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QComboBox, QLabel, QDateEdit, QLineEdit, \
    QFrame, QFormLayout, QMessageBox, QFileDialog

from UI.main_window import MainWindow
from UI.settings_window import SettingsWindow
from UI.ui_settings_window import Ui_SettingsDialog
from UI.ui_splash_screen import SplashScreen
from database.entities.cleaning_session import CleaningSession
from database.entities.client import Client
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
        self.gross_frame = QFrame()
        self.invoice_nr_lineEdit = QLineEdit()
        self.tax_date_dateEdit = QDateEdit()
        self.terms_lineEdit = QLineEdit()
        self.due_by_label = QLabel()
        self.invoice_details_frame = QFrame()

        self.new_date = QDateEdit()

        self.dates_layout = QVBoxLayout()
        self.month_selection_frame = QFrame()
        self.dates_frame = QFrame()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle(self.title)
        self.resize(650, 450)

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
        self.client_dropdown.setEditable(True)
        self.client_dropdown.setCurrentText("")
        self.client_dropdown.textActivated.connect(self.client_selected)
        self.client_dropdown.setMinimumWidth(200)
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
        self.init_month_dropdown()
        self.month_dropdown.textActivated.connect(self.month_selected)
        month_layout.addWidget(self.month_dropdown)

        lef_pane.addWidget(self.month_selection_frame)

        month_layout.addStretch()

        right_pane = QVBoxLayout()
        invoice_details_layout = QFormLayout()


        self.invoice_details_frame.hide()
        self.invoice_details_frame.setLayout(invoice_details_layout)

        right_pane.addWidget(self.invoice_details_frame)
        invoice_details_layout.setParent(self.invoice_details_frame)

        invoice_nr_label = QLabel()
        invoice_nr_label.setText("Invoice Nr: ")

        self.invoice_nr_lineEdit.setValidator(QIntValidator(0,99999999))

        invoice_details_layout.addRow(invoice_nr_label, self.invoice_nr_lineEdit)

        tax_date_label = QLabel()
        tax_date_label.setText("Tax Date: ")

        self.tax_date_dateEdit.dateChanged.connect(self.recalculate_due_by)
        self.tax_date_dateEdit.setCalendarPopup(True)

        invoice_details_layout.addRow(tax_date_label, self.tax_date_dateEdit)

        terms_label = QLabel()
        terms_label.setText("Terms: ")

        self.terms_lineEdit.textChanged.connect(self.recalculate_due_by)
        self.terms_lineEdit.setValidator(QIntValidator(0,99999))
        invoice_details_layout.addRow(terms_label, self.terms_lineEdit)

        due_by_wording_label = QLabel()
        due_by_wording_label.setText("due by")

        invoice_details_layout.addRow(due_by_wording_label, self.due_by_label)

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
        self.new_date.setMinimumWidth(90)
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
        print_buton.pressed.connect(self.print)
        print_box.addWidget(print_buton)

        self.setLayout(main_layout)

        self.splash_screen.show()

    def init_month_dropdown(self):
        current_month_index = (datetime.now().month + 12 - 2) % 12
        self.month_dropdown.setCurrentIndex(current_month_index)
        self.month_selected(self.month_dropdown.itemText(current_month_index))

    @pyqtSlot(str)
    def client_selected(self, selected_text):
        self.reset_window()
        clients = [c.name for c in SettingsWindow.get_clients()]
        if selected_text not in clients:
            self.client_dropdown.clear()
            self.client_dropdown.addItems(clients)
            self.client_dropdown.setCurrentText("")
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Please select an actual client")
            msg.setWindowTitle("Error")
            msg.exec_()
            return
        self.month_selection_frame.show()
        self.dates_frame.show()
        self.main_window.set_selected_client(selected_text)
        self.client_dropdown.setCurrentText(selected_text)
        self.populate_invoice_settings()

    @pyqtSlot(str)
    def month_selected(self, selected_month):
        month_name = datetime.strptime(selected_month, '%b').strftime("%B")
        self.main_window.set_selected_month(month_name)

    @pyqtSlot(QDate)
    def add_new_date(self, date):
        default_amount, default_price = self.main_window.get_client_defaults()
        layout = QHBoxLayout()
        frame = QFrame()
        frame.setLayout(layout)
        layout.setParent(frame)
        self.dates_layout.insertWidget(len(self.dates), frame)

        delete_button = QPushButton()
        delete_button.setIcon(QIcon(resource_path('./resources/img/delete_icon.png')))
        delete_button.pressed.connect(partial(self.delete_date, len(self.dates)))
        delete_button.setMaximumWidth(30)
        layout.addWidget(delete_button)
        delete_button.setParent(frame)

        date_edit = QDateEdit()
        date_edit.setDate(date)
        date_edit.setCalendarPopup(True)
        date_edit.setMinimumWidth(90)
        self.dates.append(date_edit)
        layout.addWidget(date_edit)
        date_edit.setParent(frame)

        layout.addStretch()

        amount_lable = QLabel()
        amount_lable.setText('amount / h')
        layout.addWidget(amount_lable)
        amount_lable.setParent(frame)

        amount_edit = QLineEdit()
        amount_edit.setText(f'{default_price}')
        amount_edit.setValidator(QDoubleValidator(0, 100, 2))
        amount_edit.setMaximumWidth(40)
        self.amounts_per_hour.append(amount_edit)
        layout.addWidget(amount_edit)
        amount_edit.setParent(frame)

        layout.addStretch()

        quantity_label = QLabel()
        quantity_label.setText("quantity")
        layout.addWidget(quantity_label)
        quantity_label.setParent(frame)

        quantity_line_edit = QLineEdit()
        quantity_line_edit.setText(f'{default_amount}')
        quantity_line_edit.setValidator(QDoubleValidator(0, 100, 2))
        quantity_line_edit.setMaximumWidth(40)
        self.quantities.append(quantity_line_edit)
        layout.addWidget(quantity_line_edit)
        quantity_line_edit.setParent(frame)

        layout.addStretch()

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

    def populate_invoice_settings(self):
        settings = SettingsWindow.get_settings()
        client = SettingsWindow.get_client(self.client_dropdown.currentText())
        self.invoice_details_frame.show()
        self.invoice_nr_lineEdit.setText(f'{settings.invoice_nr}')
        current_date = QDate.currentDate()
        self.tax_date_dateEdit.setDate(current_date)
        self.terms_lineEdit.setText(f"{client.terms}")
        self.due_by_label.setText(current_date.addDays(client.terms).toString("dd/MM/yyyy"))

    @pyqtSlot()
    def recalculate_due_by(self):
        if len(self.terms_lineEdit.text()) < 1 or not self.terms_lineEdit.text().isnumeric():
            return

        self.due_by_label.setText(
            self.tax_date_dateEdit.date().addDays(int(self.terms_lineEdit.text())).toString("dd/MM/yyyy"))


    @pyqtSlot()
    def settings_window(self):
        settings_window = Ui_SettingsDialog()
        settings_window.setupUi(settings_window)
        settings_window.exec_()
        self.update_clients_list()
        self.reset_window()

    @pyqtSlot()
    def print(self):
        if len(self.dates) <1:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("No dates selcted")
            msg.setWindowTitle("Error")
            msg.exec_()
            return

        client = Client()
        orm_client = SettingsWindow.get_client(self.client_dropdown.currentText())
        client.name = orm_client.name
        client.address_line_i = orm_client.address_line_i
        client.address_line_ii = orm_client.address_line_ii
        client.post_code = orm_client.post_code
        client.phone = orm_client.phone

        orm_settings = SettingsWindow.get_settings()
        t2c = Client()
        t2c.name = orm_settings.name
        t2c.address_line_i = orm_settings.address_line_i
        t2c.address_line_ii = orm_settings.address_line_ii
        t2c.post_code = orm_settings.post_code
        t2c.phone = orm_settings.phone

        invoice_nr = int(self.invoice_nr_lineEdit.text())
        tax_date = self.tax_date_dateEdit.date().toString("dd-MMM-yyyy")
        terms = int(self.terms_lineEdit.text())
        month = datetime.strptime(self.month_dropdown.currentText(), '%b').strftime("%B")
        pay_by = QDate.fromString(self.due_by_label.text(), 'dd/MM/yyyy').toString("dd-MMM-yyyy")

        sessions = []
        for s in zip(self.dates, self.amounts_per_hour, self.quantities):
            ses = CleaningSession()
            ses.date = s[0].date().toString('dd/MM/yyyy')
            ses.price = float(s[1].text())
            ses.quantity = float(s[2].text())
            sessions.append(ses)

        sessions.sort(key=lambda x: datetime.strptime(x.date, "%d/%m/%Y"))

        path, _ = QFileDialog.getSaveFileName(self, 'Invoice Save', f"inv{invoice_nr}-{month}-{datetime.strptime(tax_date,'%d-%b-%Y').year}-"
        f"{client.name}.xlsx", "Excel Files (*.xlsx);;All Files (*)")

        if not path:
            return

        MainWindow.write_invoice(path, client, t2c, invoice_nr, tax_date, terms, month, pay_by, sessions)
        SettingsWindow.increment_invoice_nr(invoice_nr)
        self.reset_window()

    def reset_window(self):
        for s in self.dates:
            s.parent().deleteLater()
        self.dates = []
        self.amounts_per_hour = []
        self.quantities = []
        self.invoice_details_frame.hide()
        self.init_month_dropdown()
        self.month_selection_frame.hide()
        self.gross_total.hide()
        self.dates_frame.hide()
        self.client_dropdown.setCurrentText("")
