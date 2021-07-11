# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitledzmSCSU.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
from PyQt5.QtCore import pyqtSlot
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from UI.settings_window import SettingsWindow


class Ui_SettingsDialog(QDialog):
    def setupUi(self, SettingsDialog):
        if not SettingsDialog.objectName():
            SettingsDialog.setObjectName(u"SettingsDialog")
        SettingsDialog.resize(650, 340)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SettingsDialog.sizePolicy().hasHeightForWidth())
        SettingsDialog.setSizePolicy(sizePolicy)
        SettingsDialog.setModal(True)
        self.horizontalLayout = QHBoxLayout(SettingsDialog)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.ClientFrame = QFrame(SettingsDialog)
        self.ClientFrame.setObjectName(u"ClientFrame")
        self.ClientFrame.setFrameShape(QFrame.StyledPanel)
        self.ClientFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.ClientFrame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.ClientFrame)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label_2 = QLabel(self.ClientFrame)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.client_combobox = QComboBox(self.ClientFrame)
        self.client_combobox.setObjectName(u"client_combobox")

        self.update_client_list()
        self.client_combobox.activated.connect(self.client_selection_changed)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.client_combobox)

        self.label_3 = QLabel(self.ClientFrame)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_3)

        self.clientNameLineEdit = QLineEdit(self.ClientFrame)
        self.clientNameLineEdit.setObjectName(u"clientNameLineEdit")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.clientNameLineEdit)

        self.label_4 = QLabel(self.ClientFrame)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_4)

        self.clientAddressLineIlineEdit = QLineEdit(self.ClientFrame)
        self.clientAddressLineIlineEdit.setObjectName(u"clientAddressLineIlineEdit")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.clientAddressLineIlineEdit)

        self.label_5 = QLabel(self.ClientFrame)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_5)

        self.clientAddressLineIIlineEdit = QLineEdit(self.ClientFrame)
        self.clientAddressLineIIlineEdit.setObjectName(u"clientAddressLineIIlineEdit")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.clientAddressLineIIlineEdit)

        self.label_6 = QLabel(self.ClientFrame)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_6)

        self.clientPostCodelineEdit = QLineEdit(self.ClientFrame)
        self.clientPostCodelineEdit.setObjectName(u"clientPostCodelineEdit")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.clientPostCodelineEdit)

        self.label_7 = QLabel(self.ClientFrame)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_7)

        self.clientPhoneNumberlineEdit = QLineEdit(self.ClientFrame)
        self.clientPhoneNumberlineEdit.setObjectName(u"clientPhoneNumberlineEdit")
        self.clientPhoneNumberlineEdit.setValidator(QRegExpValidator(QRegExp("^\+?[0-9]+$")))

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.clientPhoneNumberlineEdit)

        self.label_8 = QLabel(self.ClientFrame)
        self.label_8.setObjectName(u"label_8")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_8)

        self.clientQuantitylineEdit = QLineEdit(self.ClientFrame)
        self.clientQuantitylineEdit.setObjectName(u"clientQuantitylineEdit")
        self.clientQuantitylineEdit.setValidator(QDoubleValidator(0, 100, 2))

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.clientQuantitylineEdit)

        self.label_9 = QLabel(self.ClientFrame)
        self.label_9.setObjectName(u"label_9")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.label_9)

        self.clientPricelineEdit = QLineEdit(self.ClientFrame)
        self.clientPricelineEdit.setObjectName(u"clientPricelineEdit")
        self.clientPricelineEdit.setValidator(QDoubleValidator(0, 100, 2))

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.clientPricelineEdit)


        self.label_17 = QLabel(self.ClientFrame)
        self.label_17.setObjectName(u"label_17")

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.label_17)

        self.clientTermlineEdit = QLineEdit(self.ClientFrame)
        self.clientTermlineEdit.setObjectName(u"clientTermLimit")
        self.clientTermlineEdit.setValidator(QIntValidator(0, 100))

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.clientTermlineEdit)


        self.verticalLayout.addLayout(self.formLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.clientCreateButton = QPushButton(self.ClientFrame)
        self.clientCreateButton.setObjectName(u"clientCreateButton")
        self.clientCreateButton.pressed.connect(self.create_client)

        self.horizontalLayout_2.addWidget(self.clientCreateButton)

        self.clientSaveButton = QPushButton(self.ClientFrame)
        self.clientSaveButton.setObjectName(u"clientSaveButton")
        self.clientSaveButton.pressed.connect(self.update_client)
        self.clientSaveButton.hide()

        self.horizontalLayout_2.addWidget(self.clientSaveButton)

        self.clientDeleteButton = QPushButton(self.ClientFrame)
        self.clientDeleteButton.setObjectName(u"clientDeleteButton")
        self.clientDeleteButton.hide()
        self.clientDeleteButton.pressed.connect(self.delete_client)

        self.horizontalLayout_2.addWidget(self.clientDeleteButton)

        self.clientResetButton = QPushButton(self.ClientFrame)
        self.clientResetButton.setObjectName(u"clientResetButton")
        self.clientResetButton.pressed.connect(self.reset_client_button)

        self.horizontalLayout_2.addWidget(self.clientResetButton)



        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.ClientFrame)

        self.line = QFrame(SettingsDialog)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line)

        self.Team2CleanFrame = QFrame(SettingsDialog)
        self.Team2CleanFrame.setObjectName(u"Team2CleanFrame")
        self.Team2CleanFrame.setFrameShape(QFrame.StyledPanel)
        self.Team2CleanFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.Team2CleanFrame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_10 = QLabel(self.Team2CleanFrame)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font)
        self.label_10.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_10)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_11 = QLabel(self.Team2CleanFrame)
        self.label_11.setObjectName(u"label_11")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_11)

        self.t2cInvoiceNumberlineEdit = QLineEdit(self.Team2CleanFrame)
        self.t2cInvoiceNumberlineEdit.setObjectName(u"t2cInvoiceNumberlineEdit")
        self.t2cInvoiceNumberlineEdit.setValidator(QIntValidator(1, 99999999))

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.t2cInvoiceNumberlineEdit)

        self.label_12 = QLabel(self.Team2CleanFrame)
        self.label_12.setObjectName(u"label_12")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_12)

        self.t2cNamelineEdit = QLineEdit(self.Team2CleanFrame)
        self.t2cNamelineEdit.setObjectName(u"t2cNamelineEdit")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.t2cNamelineEdit)

        self.label_13 = QLabel(self.Team2CleanFrame)
        self.label_13.setObjectName(u"label_13")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_13)

        self.t2cAddressLineIlineEdit = QLineEdit(self.Team2CleanFrame)
        self.t2cAddressLineIlineEdit.setObjectName(u"t2cAddressLineIlineEdit")

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.t2cAddressLineIlineEdit)

        self.label_14 = QLabel(self.Team2CleanFrame)
        self.label_14.setObjectName(u"label_14")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.label_14)

        self.t2cLineAddressIIlineEdit = QLineEdit(self.Team2CleanFrame)
        self.t2cLineAddressIIlineEdit.setObjectName(u"t2cLineAddressIIlineEdit")

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.t2cLineAddressIIlineEdit)

        self.label_15 = QLabel(self.Team2CleanFrame)
        self.label_15.setObjectName(u"label_15")

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.label_15)

        self.t2cPostCode = QLineEdit(self.Team2CleanFrame)
        self.t2cPostCode.setObjectName(u"t2cPostCode")

        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.t2cPostCode)

        self.label_16 = QLabel(self.Team2CleanFrame)
        self.label_16.setObjectName(u"label_16")

        self.formLayout_2.setWidget(5, QFormLayout.LabelRole, self.label_16)

        self.t2cPhoneNumberlineEdit = QLineEdit(self.Team2CleanFrame)
        self.t2cPhoneNumberlineEdit.setObjectName(u"t2cPhoneNumberlineEdit")

        self.formLayout_2.setWidget(5, QFormLayout.FieldRole, self.t2cPhoneNumberlineEdit)


        self.verticalLayout_2.addLayout(self.formLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.t2cSaveButton = QPushButton(self.Team2CleanFrame)
        self.t2cSaveButton.setObjectName(u"t2cSaveButton")
        self.t2cSaveButton.pressed.connect(self.update_settings)

        self.horizontalLayout_3.addWidget(self.t2cSaveButton)

        self.t2cResetButton = QPushButton(self.Team2CleanFrame)
        self.t2cResetButton.setObjectName(u"t2cResetButton")
        self.t2cResetButton.pressed.connect(self.populate_settings)

        self.horizontalLayout_3.addWidget(self.t2cResetButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)


        self.horizontalLayout.addWidget(self.Team2CleanFrame)


        self.retranslateUi(SettingsDialog)

        QMetaObject.connectSlotsByName(SettingsDialog)
        self.populate_settings()

    # setupUi

    def retranslateUi(self, SettingsDialog):
        SettingsDialog.setWindowTitle(QCoreApplication.translate("SettingsDialog", u"Settings", None))
        self.label.setText(QCoreApplication.translate("SettingsDialog", u"Client", None))
        self.label_2.setText(QCoreApplication.translate("SettingsDialog", u"Client", None))
        self.label_3.setText(QCoreApplication.translate("SettingsDialog", u"Name:", None))
        self.label_4.setText(QCoreApplication.translate("SettingsDialog", u"Address Line I", None))
        self.label_5.setText(QCoreApplication.translate("SettingsDialog", u"Address Line II", None))
        self.label_6.setText(QCoreApplication.translate("SettingsDialog", u"Post Code", None))
        self.label_7.setText(QCoreApplication.translate("SettingsDialog", u"Phone Number", None))
        self.label_8.setText(QCoreApplication.translate("SettingsDialog", u"Quantity", None))
        self.label_9.setText(QCoreApplication.translate("SettingsDialog", u"Price / h", None))
        self.clientCreateButton.setText(QCoreApplication.translate("SettingsDialog", u"Create", None))
        self.clientSaveButton.setText(QCoreApplication.translate("SettingsDialog", u"Save", None))
        self.clientDeleteButton.setText(QCoreApplication.translate("SettingsDialog", u"Delete", None))
        self.clientResetButton.setText(QCoreApplication.translate("SettingsDialog", u"Reset", None))
        self.label_10.setText(QCoreApplication.translate("SettingsDialog", u"Team2Clean", None))
        self.label_11.setText(QCoreApplication.translate("SettingsDialog", u"Invoice Nr:", None))
        self.label_12.setText(QCoreApplication.translate("SettingsDialog", u"Name:", None))
        self.label_13.setText(QCoreApplication.translate("SettingsDialog", u"Address line I", None))
        self.label_14.setText(QCoreApplication.translate("SettingsDialog", u"Address Line II", None))
        self.label_15.setText(QCoreApplication.translate("SettingsDialog", u"Post Code", None))
        self.label_16.setText(QCoreApplication.translate("SettingsDialog", u"Phone Number", None))
        self.label_17.setText(QCoreApplication.translate("SettingsDialog", u"Term:"))
        self.t2cSaveButton.setText(QCoreApplication.translate("SettingsDialog", u"Save", None))
        self.t2cResetButton.setText(QCoreApplication.translate("SettingsDialog", u"Reset", None))
    # retranslateUi

    @pyqtSlot(int)
    def client_selection_changed(self, new_index):
        if new_index == 0:
            self.clientSaveButton.hide()
            self.clientDeleteButton.hide()
            self.clientCreateButton.show()
            self.reset_client_form()
        else:
            self.clientSaveButton.show()
            self.clientDeleteButton.show()
            self.clientCreateButton.hide()

            client_name = self.client_combobox.currentText()
            client = SettingsWindow.get_client(client_name)

            self.clientNameLineEdit.setText(client.name)
            self.clientAddressLineIlineEdit.setText(client.address_line_i)
            self.clientAddressLineIIlineEdit.setText(client.address_line_ii)

            self.clientPostCodelineEdit.setText(client.post_code)
            self.clientPhoneNumberlineEdit.setText(client.phone)
            self.clientQuantitylineEdit.setText(str(client.usual_quantity))
            self.clientPricelineEdit.setText(str(client.usual_price))
            self.clientTermlineEdit.setText(str(client.terms))

    @pyqtSlot()
    def reset_client_button(self):
        self.client_selection_changed(self.client_combobox.currentIndex())

    @pyqtSlot()
    def create_client(self):
        if not self.validate_client_form():
            return

        client_name = self.clientNameLineEdit.text().strip()
        clients = [c.name for c in self.settings_window.get_clients()]
        if client_name in clients:
            self.validate_popup("Client name already exists")
            return

        address_line_i = self.clientAddressLineIlineEdit.text().strip()
        address_line_ii = self.clientAddressLineIIlineEdit.text().strip()
        post_code = self.clientPostCodelineEdit.text().strip()
        phone_number = self.clientPhoneNumberlineEdit.text().strip()
        quantity = float(self.clientQuantitylineEdit.text().strip())
        price = float(self.clientPricelineEdit.text().strip())
        term = int(self.clientTermlineEdit.text().strip())
        self.settings_window.create_client(client_name, address_line_i, address_line_ii, post_code, phone_number,
                                           quantity, price, term)

        self.reset_client_form()

    @pyqtSlot()
    def update_client(self):
        if not self.validate_client_form():
            return

        client_name = self.client_combobox.currentText()
        new_client_name = self.clientNameLineEdit.text().strip()
        clients = [c.name for c in SettingsWindow.get_clients()]
        if new_client_name != client_name and new_client_name in clients:
            self.validate_popup("Client name already exists")
            return False

        address_line_i = self.clientAddressLineIlineEdit.text().strip()
        address_line_ii = self.clientAddressLineIIlineEdit.text().strip()
        post_code = self.clientPostCodelineEdit.text().strip()
        phone_number = self.clientPhoneNumberlineEdit.text().strip()
        quantity = float(self.clientQuantitylineEdit.text().strip())
        price = float(self.clientPricelineEdit.text().strip())
        term = int(self.clientTermlineEdit.text().strip())

        SettingsWindow.update_client(client_name, new_client_name, address_line_i, address_line_ii, post_code,
                                     phone_number, quantity, price, term)

        self.update_client_list()
        self.client_combobox.setCurrentText(new_client_name)
        msg = QMessageBox()
        msg.setText("Client Updated")
        msg.exec_()

    @pyqtSlot()
    def populate_settings(self):
        settings = SettingsWindow.get_settings()
        self.t2cInvoiceNumberlineEdit.setText(f"{settings.invoice_nr}")
        self.t2cNamelineEdit.setText(settings.name)
        self.t2cAddressLineIlineEdit.setText(settings.address_line_i)
        self.t2cLineAddressIIlineEdit.setText(settings.address_line_ii)
        self.t2cPostCode.setText(settings.post_code)
        self.t2cPhoneNumberlineEdit.setText(settings.phone)

    def update_settings(self):
        if not self.validate_t2c_form():
            return

        invoice_nr = int(self.t2cInvoiceNumberlineEdit.text())
        name = self.t2cNamelineEdit.text()
        address_line_i = self.t2cAddressLineIlineEdit.text()
        address_line_ii = self.t2cLineAddressIIlineEdit.text()
        post_code = self.t2cPostCode.text()
        phone_number = self.t2cPhoneNumberlineEdit.text()

        SettingsWindow.update_settings(invoice_nr, name, address_line_i, address_line_ii, post_code,
                                       phone_number)

        msg = QMessageBox()
        msg.setText("Settings Updated")
        msg.exec_()

    def validate_t2c_form(self):
        invoice_nr = self.t2cInvoiceNumberlineEdit.text()
        if len(invoice_nr) < 1:
            self.validate_popup("Invoice Nr line is empty")
            return False

        name = self.t2cNamelineEdit.text()
        if len(name) < 1:
            self.validate_popup("Name line is empty")
            return False

        address_line_i = self.t2cAddressLineIlineEdit.text()
        if len(address_line_i) < 1:
            self.validate_popup("Address line I is empty")
            return False

        address_line_ii = self.t2cLineAddressIIlineEdit.text()
        if len(address_line_ii) < 1:
            self.validate_popup("Address line II is empty")
            return False

        post_code = self.t2cPostCode.text()
        if len(post_code) < 1:
            self.validate_popup("Post code line is empty")
            return False

        phone_number = self.t2cPhoneNumberlineEdit.text()
        if len(phone_number) < 1:
            self.validate_popup("Phone number line is empty")
            return False

        return True

    def validate_client_form(self):
        client_name = self.clientNameLineEdit.text().strip()
        if len(client_name) < 1:
            self.validate_popup("Client Name field is empty")
            return False

        address_line_i = self.clientAddressLineIlineEdit.text().strip()
        if len(address_line_i) < 1:
            self.validate_popup("Client Address Line I is empty")
            return False

        address_line_ii = self.clientAddressLineIIlineEdit.text().strip()
        if len(address_line_ii) < 1:
            self.validate_popup("Client Address Line II is empty")
            return False

        post_code = self.clientPostCodelineEdit.text().strip()
        if len(post_code) < 1:
            self.validate_popup("Post code line is empty")
            return False

        phone_number = self.clientPhoneNumberlineEdit.text().strip()
        if len(phone_number) < 1:
            self.validate_popup("Phone number line is empty")
            return False

        quantity = self.clientQuantitylineEdit.text().strip()
        if len(quantity) < 1:
            self.validate_popup("Quantity line is empty")
            return False

        price = self.clientPricelineEdit.text().strip()
        if len(price) < 1:
            self.validate_popup("Price line is empty")
            return False

        term = self.clientTermlineEdit.text().strip()
        if len(term) < 1:
            self.validate_popup("Term line is empty")
            return False

        return True

    def reset_client_form(self):
        self.update_client_list()
        self.clientNameLineEdit.clear()
        self.clientAddressLineIlineEdit.clear()
        self.clientAddressLineIIlineEdit.clear()
        self.clientPostCodelineEdit.clear()
        self.clientPhoneNumberlineEdit.clear()
        self.clientQuantitylineEdit.clear()
        self.clientPricelineEdit.clear()
        self.clientTermlineEdit.clear()

    def update_client_list(self):
        self.client_combobox.clear()
        clients = [c.name for c in SettingsWindow.get_clients()]
        clients.insert(0, "Add new client")
        self.client_combobox.addItems(clients)

    def validate_popup(self, error_message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText(error_message)
        msg.setWindowTitle("Error")
        msg.exec_()

    def delete_client(self):
        client_name = self.client_combobox.currentText()
        choice = QMessageBox.question(self, "Delete", f"Are you sure you want to delete {client_name}?",
                                      QMessageBox.Yes | QMessageBox.No)
        if choice == QMessageBox.Yes:
            SettingsWindow.delete_client(client_name)
            self.reset_client_form()
