import sys
from PyQt5 import (QtWidgets, QtCore, QtGui)
from PyQt5.QtWidgets import (QMessageBox, QFileDialog)
from Ui_NewKeyStoreDialog import Ui_Dialog_NewKeyStore


class Dialog_NewKeyStore(QtWidgets.QDialog, Ui_Dialog_NewKeyStore):

    def __init__(self, parent=None):
        super(Dialog_NewKeyStore, self).__init__(parent)
        self.setupUi(self)

        # buttonBox
        self.buttonBox.accepted.connect(self.on_buttonBox_accept)
        self.buttonBox.rejected.connect(self.reject)

        # button ...
        self.pushButton_OpenKeystore.clicked.connect(self.on_pushButton_OpenKeystore)

        # Member variables
        # keystore
        self.keyStorePath = ''
        self.storePass = ''
        self.storePassConfirm = ''
        # key
        self.alias = ''
        self.keyPass = ''
        self.keyPassConfirm = ''
        self.validity = 25
        # certificate
        self.dname = {}
        self.name = ''
        self.organizationalUnit = ''
        self.organization = ''
        self.locality = ''
        self.state = ''
        self.countryCode = ''

    def msgBox(self, msg):
        QMessageBox.information(self, "Error", msg)

    def on_buttonBox_accept(self):
        # keystore
        self.keyStorePath = self.lineEdit_KeyStorePath.text()
        self.storePass = self.lineEdit_StorePass.text()
        self.storePassConfirm = self.lineEdit_StorePassConfirm.text()
        # key
        self.alias = self.lineEdit_Alias.text()
        self.keyPass = self.lineEdit_KeyPass.text()
        self.keyPassConfirm = self.lineEdit_KeyPassConfirm.text()
        self.validity = self.spinBox_Validity.value()
        # certificate
        self.name = self.lineEdit_Name.text()
        self.organizationalUnit = self.lineEdit_OrganizationalUnit.text()
        self.organization = self.lineEdit_Organization.text()
        self.locality = self.lineEdit_Locality.text()
        self.state = self.lineEdit_State.text()
        self.countryCode = self.lineEdit_CountryCode.text()

        if self.keyStorePath == '':
            self.msgBox('specify key store path')
        elif self.storePass == '' or self.keyPass == '':
            self.msgBox('specify passwords')
        elif self.alias == '':
            self.msgBox('specify Alias')
        elif (self.name == '') and (self.organizationalUnit == '') and (self.organization == '') and (self.locality == '') and (
                self.state == '') and (self.countryCode == ''):
            self.msgBox('At least one Certificate issuer field is required to be non-empty')
        elif (self.storePass != self.storePassConfirm) or (self.keyPass != self.keyPassConfirm):
            self.msgBox('Passwords do not match')
        elif (len(self.storePass) < 6) or (len(self.keyPass) < 6):
            self.msgBox('Password must be at least 6 characters')
        else:
            # CN=1,OU=2,O=3,L=4,ST=5,C=6
            self.dname['CN'] = self.name
            self.dname['OU'] = self.organizationalUnit
            self.dname['O'] = self.organization
            self.dname['L'] = self.locality
            self.dname['ST'] = self.state
            self.dname['C'] = self.countryCode
            self.accept()

    def on_pushButton_OpenKeystore(self):
        fileName, _ = QFileDialog.getSaveFileName(self, "Save Key Store Path", "keystore.jks", "keystore(*.jks);;All Files (*.*)")
        if fileName:
            self.lineEdit_KeyStorePath.setText(fileName)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Dialog_NewKeyStore()
    window.show()
    sys.exit(app.exec_())
