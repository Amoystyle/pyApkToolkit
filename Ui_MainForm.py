# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Project\Python_Code\pyApkToolkit\MainForm.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowModality(QtCore.Qt.NonModal)
        Form.resize(450, 540)
        Form.setMinimumSize(QtCore.QSize(450, 540))
        Form.setMaximumSize(QtCore.QSize(450, 540))
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 449, 291))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        self.groupBox.setGeometry(QtCore.QRect(5, 5, 436, 136))
        self.groupBox.setObjectName("groupBox")
        self.lineEdit_DeApk = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_DeApk.setGeometry(QtCore.QRect(13, 17, 330, 20))
        self.lineEdit_DeApk.setMinimumSize(QtCore.QSize(330, 20))
        self.lineEdit_DeApk.setMaximumSize(QtCore.QSize(330, 20))
        self.lineEdit_DeApk.setDragEnabled(False)
        self.lineEdit_DeApk.setObjectName("lineEdit_DeApk")
        self.lineEdit_ReApk = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_ReApk.setGeometry(QtCore.QRect(13, 47, 330, 20))
        self.lineEdit_ReApk.setMinimumSize(QtCore.QSize(330, 20))
        self.lineEdit_ReApk.setMaximumSize(QtCore.QSize(330, 20))
        self.lineEdit_ReApk.setDragEnabled(False)
        self.lineEdit_ReApk.setObjectName("lineEdit_ReApk")
        self.lineEdit_OptzApk = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_OptzApk.setGeometry(QtCore.QRect(13, 77, 330, 20))
        self.lineEdit_OptzApk.setMinimumSize(QtCore.QSize(330, 20))
        self.lineEdit_OptzApk.setMaximumSize(QtCore.QSize(330, 20))
        self.lineEdit_OptzApk.setDragEnabled(False)
        self.lineEdit_OptzApk.setObjectName("lineEdit_OptzApk")
        self.lineEdit_SignApk = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_SignApk.setGeometry(QtCore.QRect(13, 107, 330, 20))
        self.lineEdit_SignApk.setMinimumSize(QtCore.QSize(330, 20))
        self.lineEdit_SignApk.setMaximumSize(QtCore.QSize(330, 20))
        self.lineEdit_SignApk.setDragEnabled(False)
        self.lineEdit_SignApk.setObjectName("lineEdit_SignApk")
        self.pushButton_DeApk = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_DeApk.setGeometry(QtCore.QRect(349, 16, 81, 23))
        self.pushButton_DeApk.setMinimumSize(QtCore.QSize(81, 23))
        self.pushButton_DeApk.setObjectName("pushButton_DeApk")
        self.pushButton_ReApk = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_ReApk.setGeometry(QtCore.QRect(349, 46, 81, 23))
        self.pushButton_ReApk.setMinimumSize(QtCore.QSize(81, 23))
        self.pushButton_ReApk.setObjectName("pushButton_ReApk")
        self.pushButton_OptzApk = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_OptzApk.setGeometry(QtCore.QRect(349, 76, 81, 23))
        self.pushButton_OptzApk.setMinimumSize(QtCore.QSize(81, 23))
        self.pushButton_OptzApk.setObjectName("pushButton_OptzApk")
        self.pushButton_SignApk = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_SignApk.setGeometry(QtCore.QRect(349, 106, 81, 23))
        self.pushButton_SignApk.setMinimumSize(QtCore.QSize(81, 23))
        self.pushButton_SignApk.setObjectName("pushButton_SignApk")
        self.pushButton_DeApk.raise_()
        self.pushButton_ReApk.raise_()
        self.pushButton_OptzApk.raise_()
        self.pushButton_SignApk.raise_()
        self.lineEdit_ReApk.raise_()
        self.lineEdit_OptzApk.raise_()
        self.lineEdit_SignApk.raise_()
        self.lineEdit_DeApk.raise_()
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_2.setGeometry(QtCore.QRect(5, 145, 436, 46))
        self.groupBox_2.setObjectName("groupBox_2")
        self.lineEdit_Framework = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_Framework.setGeometry(QtCore.QRect(11, 16, 330, 20))
        self.lineEdit_Framework.setMinimumSize(QtCore.QSize(330, 20))
        self.lineEdit_Framework.setMaximumSize(QtCore.QSize(330, 20))
        self.lineEdit_Framework.setDragEnabled(False)
        self.lineEdit_Framework.setObjectName("lineEdit_Framework")
        self.pushButton_InsFramework = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_InsFramework.setGeometry(QtCore.QRect(347, 16, 40, 20))
        self.pushButton_InsFramework.setMinimumSize(QtCore.QSize(40, 20))
        self.pushButton_InsFramework.setMaximumSize(QtCore.QSize(40, 20))
        self.pushButton_InsFramework.setObjectName("pushButton_InsFramework")
        self.pushButton_ViewFramework = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_ViewFramework.setGeometry(QtCore.QRect(390, 16, 40, 20))
        self.pushButton_ViewFramework.setMinimumSize(QtCore.QSize(40, 20))
        self.pushButton_ViewFramework.setMaximumSize(QtCore.QSize(40, 20))
        self.pushButton_ViewFramework.setObjectName("pushButton_ViewFramework")
        self.pushButton_InsFramework.raise_()
        self.pushButton_ViewFramework.raise_()
        self.lineEdit_Framework.raise_()
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_3.setGeometry(QtCore.QRect(5, 195, 436, 71))
        self.groupBox_3.setObjectName("groupBox_3")
        self.lineEdit_Apk2Jar = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_Apk2Jar.setGeometry(QtCore.QRect(11, 17, 330, 20))
        self.lineEdit_Apk2Jar.setMinimumSize(QtCore.QSize(330, 20))
        self.lineEdit_Apk2Jar.setMaximumSize(QtCore.QSize(330, 20))
        self.lineEdit_Apk2Jar.setDragEnabled(False)
        self.lineEdit_Apk2Jar.setObjectName("lineEdit_Apk2Jar")
        self.lineEdit_Dex2Jar = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_Dex2Jar.setGeometry(QtCore.QRect(11, 42, 330, 20))
        self.lineEdit_Dex2Jar.setMinimumSize(QtCore.QSize(330, 20))
        self.lineEdit_Dex2Jar.setMaximumSize(QtCore.QSize(330, 20))
        self.lineEdit_Dex2Jar.setFrame(True)
        self.lineEdit_Dex2Jar.setDragEnabled(False)
        self.lineEdit_Dex2Jar.setObjectName("lineEdit_Dex2Jar")
        self.pushButton_Apk2Jar = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_Apk2Jar.setGeometry(QtCore.QRect(347, 16, 81, 23))
        self.pushButton_Apk2Jar.setMinimumSize(QtCore.QSize(81, 23))
        self.pushButton_Apk2Jar.setObjectName("pushButton_Apk2Jar")
        self.pushButton_Dex2Jar = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_Dex2Jar.setGeometry(QtCore.QRect(347, 41, 81, 23))
        self.pushButton_Dex2Jar.setMinimumSize(QtCore.QSize(81, 23))
        self.pushButton_Dex2Jar.setObjectName("pushButton_Dex2Jar")
        self.pushButton_Apk2Jar.raise_()
        self.pushButton_Dex2Jar.raise_()
        self.lineEdit_Apk2Jar.raise_()
        self.lineEdit_Dex2Jar.raise_()
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.groupBox_6 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_6.setGeometry(QtCore.QRect(5, 5, 433, 188))
        self.groupBox_6.setMinimumSize(QtCore.QSize(433, 188))
        self.groupBox_6.setObjectName("groupBox_6")
        self.label = QtWidgets.QLabel(self.groupBox_6)
        self.label.setGeometry(QtCore.QRect(10, 20, 90, 12))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox_6)
        self.label_2.setGeometry(QtCore.QRect(11, 80, 114, 12))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox_6)
        self.label_3.setGeometry(QtCore.QRect(11, 108, 60, 12))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox_6)
        self.label_4.setGeometry(QtCore.QRect(11, 136, 78, 12))
        self.label_4.setObjectName("label_4")
        self.checkBox_Remember = QtWidgets.QCheckBox(self.groupBox_6)
        self.checkBox_Remember.setGeometry(QtCore.QRect(129, 156, 131, 16))
        self.checkBox_Remember.setObjectName("checkBox_Remember")
        self.pushButton_CreateKeyStore = QtWidgets.QPushButton(self.groupBox_6)
        self.pushButton_CreateKeyStore.setGeometry(QtCore.QRect(208, 44, 86, 23))
        self.pushButton_CreateKeyStore.setMinimumSize(QtCore.QSize(86, 23))
        self.pushButton_CreateKeyStore.setObjectName("pushButton_CreateKeyStore")
        self.pushButton_ChooseKeyStore = QtWidgets.QPushButton(self.groupBox_6)
        self.pushButton_ChooseKeyStore.setGeometry(QtCore.QRect(299, 44, 129, 23))
        self.pushButton_ChooseKeyStore.setMinimumSize(QtCore.QSize(129, 23))
        self.pushButton_ChooseKeyStore.setObjectName("pushButton_ChooseKeyStore")
        self.lineEdit_KeyStorePath = QtWidgets.QLineEdit(self.groupBox_6)
        self.lineEdit_KeyStorePath.setGeometry(QtCore.QRect(129, 16, 297, 20))
        self.lineEdit_KeyStorePath.setMinimumSize(QtCore.QSize(297, 20))
        self.lineEdit_KeyStorePath.setObjectName("lineEdit_KeyStorePath")
        self.lineEdit_StorePassword = QtWidgets.QLineEdit(self.groupBox_6)
        self.lineEdit_StorePassword.setGeometry(QtCore.QRect(129, 77, 297, 20))
        self.lineEdit_StorePassword.setMinimumSize(QtCore.QSize(297, 20))
        self.lineEdit_StorePassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_StorePassword.setObjectName("lineEdit_StorePassword")
        self.lineEdit_KeyAlias = QtWidgets.QLineEdit(self.groupBox_6)
        self.lineEdit_KeyAlias.setGeometry(QtCore.QRect(129, 103, 297, 20))
        self.lineEdit_KeyAlias.setMinimumSize(QtCore.QSize(297, 20))
        self.lineEdit_KeyAlias.setObjectName("lineEdit_KeyAlias")
        self.lineEdit_KeyPassword = QtWidgets.QLineEdit(self.groupBox_6)
        self.lineEdit_KeyPassword.setGeometry(QtCore.QRect(129, 129, 297, 20))
        self.lineEdit_KeyPassword.setMinimumSize(QtCore.QSize(297, 20))
        self.lineEdit_KeyPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_KeyPassword.setObjectName("lineEdit_KeyPassword")
        self.groupBox_7 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_7.setGeometry(QtCore.QRect(5, 200, 433, 56))
        self.groupBox_7.setMinimumSize(QtCore.QSize(433, 56))
        self.groupBox_7.setObjectName("groupBox_7")
        self.checkBox_V1Signature = QtWidgets.QCheckBox(self.groupBox_7)
        self.checkBox_V1Signature.setGeometry(QtCore.QRect(129, 20, 125, 16))
        self.checkBox_V1Signature.setObjectName("checkBox_V1Signature")
        self.checkBox_V2Signature = QtWidgets.QCheckBox(self.groupBox_7)
        self.checkBox_V2Signature.setGeometry(QtCore.QRect(259, 20, 145, 16))
        self.checkBox_V2Signature.setObjectName("checkBox_V2Signature")
        self.label_5 = QtWidgets.QLabel(self.groupBox_7)
        self.label_5.setGeometry(QtCore.QRect(10, 20, 114, 16))
        self.label_5.setObjectName("label_5")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_4.setGeometry(QtCore.QRect(5, 5, 436, 66))
        self.groupBox_4.setObjectName("groupBox_4")
        self.checkBox_ReAutoOptz = QtWidgets.QCheckBox(self.groupBox_4)
        self.checkBox_ReAutoOptz.setGeometry(QtCore.QRect(10, 20, 287, 16))
        self.checkBox_ReAutoOptz.setObjectName("checkBox_ReAutoOptz")
        self.checkBox_ReAutoSign = QtWidgets.QCheckBox(self.groupBox_4)
        self.checkBox_ReAutoSign.setGeometry(QtCore.QRect(10, 40, 287, 16))
        self.checkBox_ReAutoSign.setObjectName("checkBox_ReAutoSign")
        self.groupBox_5 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_5.setGeometry(QtCore.QRect(5, 75, 436, 46))
        self.groupBox_5.setObjectName("groupBox_5")
        self.checkBox_DeAutoFix = QtWidgets.QCheckBox(self.groupBox_5)
        self.checkBox_DeAutoFix.setGeometry(QtCore.QRect(10, 20, 359, 16))
        self.checkBox_DeAutoFix.setObjectName("checkBox_DeAutoFix")
        self.tabWidget.addTab(self.tab_3, "")
        self.label_Log = QtWidgets.QLabel(Form)
        self.label_Log.setGeometry(QtCore.QRect(10, 290, 54, 16))
        self.label_Log.setMinimumSize(QtCore.QSize(54, 12))
        self.label_Log.setMaximumSize(QtCore.QSize(40, 20))
        self.label_Log.setObjectName("label_Log")
        self.splitter = QtWidgets.QSplitter(Form)
        self.splitter.setGeometry(QtCore.QRect(272, 290, 175, 20))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.pushButton_ClearLog = QtWidgets.QPushButton(self.splitter)
        self.pushButton_ClearLog.setMinimumSize(QtCore.QSize(40, 20))
        self.pushButton_ClearLog.setMaximumSize(QtCore.QSize(40, 20))
        self.pushButton_ClearLog.setObjectName("pushButton_ClearLog")
        self.pushButton_ExportLog = QtWidgets.QPushButton(self.splitter)
        self.pushButton_ExportLog.setMinimumSize(QtCore.QSize(40, 20))
        self.pushButton_ExportLog.setMaximumSize(QtCore.QSize(40, 20))
        self.pushButton_ExportLog.setObjectName("pushButton_ExportLog")
        self.pushButton_About = QtWidgets.QPushButton(self.splitter)
        self.pushButton_About.setMinimumSize(QtCore.QSize(40, 20))
        self.pushButton_About.setMaximumSize(QtCore.QSize(40, 20))
        self.pushButton_About.setObjectName("pushButton_About")
        self.pushButton_CheckEvn = QtWidgets.QPushButton(self.splitter)
        self.pushButton_CheckEvn.setMinimumSize(QtCore.QSize(40, 20))
        self.pushButton_CheckEvn.setMaximumSize(QtCore.QSize(40, 20))
        self.pushButton_CheckEvn.setObjectName("pushButton_CheckEvn")
        self.plainTextEdit_Log = QtWidgets.QPlainTextEdit(Form)
        self.plainTextEdit_Log.setGeometry(QtCore.QRect(5, 310, 441, 226))
        self.plainTextEdit_Log.setAcceptDrops(False)
        self.plainTextEdit_Log.setLineWrapMode(QtWidgets.QPlainTextEdit.NoWrap)
        self.plainTextEdit_Log.setReadOnly(True)
        self.plainTextEdit_Log.setObjectName("plainTextEdit_Log")

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.tabWidget, self.lineEdit_DeApk)
        Form.setTabOrder(self.lineEdit_DeApk, self.pushButton_DeApk)
        Form.setTabOrder(self.pushButton_DeApk, self.lineEdit_ReApk)
        Form.setTabOrder(self.lineEdit_ReApk, self.pushButton_ReApk)
        Form.setTabOrder(self.pushButton_ReApk, self.lineEdit_OptzApk)
        Form.setTabOrder(self.lineEdit_OptzApk, self.pushButton_OptzApk)
        Form.setTabOrder(self.pushButton_OptzApk, self.lineEdit_SignApk)
        Form.setTabOrder(self.lineEdit_SignApk, self.pushButton_SignApk)
        Form.setTabOrder(self.pushButton_SignApk, self.lineEdit_Framework)
        Form.setTabOrder(self.lineEdit_Framework, self.pushButton_InsFramework)
        Form.setTabOrder(self.pushButton_InsFramework, self.pushButton_ViewFramework)
        Form.setTabOrder(self.pushButton_ViewFramework, self.lineEdit_Apk2Jar)
        Form.setTabOrder(self.lineEdit_Apk2Jar, self.pushButton_Apk2Jar)
        Form.setTabOrder(self.pushButton_Apk2Jar, self.lineEdit_Dex2Jar)
        Form.setTabOrder(self.lineEdit_Dex2Jar, self.pushButton_Dex2Jar)
        Form.setTabOrder(self.pushButton_Dex2Jar, self.pushButton_ClearLog)
        Form.setTabOrder(self.pushButton_ClearLog, self.pushButton_ExportLog)
        Form.setTabOrder(self.pushButton_ExportLog, self.pushButton_About)
        Form.setTabOrder(self.pushButton_About, self.pushButton_CheckEvn)
        Form.setTabOrder(self.pushButton_CheckEvn, self.plainTextEdit_Log)
        Form.setTabOrder(self.plainTextEdit_Log, self.lineEdit_KeyStorePath)
        Form.setTabOrder(self.lineEdit_KeyStorePath, self.pushButton_CreateKeyStore)
        Form.setTabOrder(self.pushButton_CreateKeyStore, self.pushButton_ChooseKeyStore)
        Form.setTabOrder(self.pushButton_ChooseKeyStore, self.lineEdit_StorePassword)
        Form.setTabOrder(self.lineEdit_StorePassword, self.lineEdit_KeyAlias)
        Form.setTabOrder(self.lineEdit_KeyAlias, self.lineEdit_KeyPassword)
        Form.setTabOrder(self.lineEdit_KeyPassword, self.checkBox_Remember)
        Form.setTabOrder(self.checkBox_Remember, self.checkBox_V1Signature)
        Form.setTabOrder(self.checkBox_V1Signature, self.checkBox_V2Signature)
        Form.setTabOrder(self.checkBox_V2Signature, self.checkBox_ReAutoOptz)
        Form.setTabOrder(self.checkBox_ReAutoOptz, self.checkBox_ReAutoSign)
        Form.setTabOrder(self.checkBox_ReAutoSign, self.checkBox_DeAutoFix)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "ApkToolkit - By Arno"))
        self.groupBox.setTitle(_translate("Form", ".apk工具"))
        self.lineEdit_DeApk.setToolTip(_translate("Form", "<h4><p>提示：<br>&nbsp;&nbsp;&nbsp;拖拽要反编译的.apk文件到此！<br><font color = \'red\'>注意：<br>&nbsp;&nbsp;&nbsp;路径中不能出现中文字符！</font></p></h4>"))
        self.lineEdit_ReApk.setToolTip(_translate("Form", "<h4><p>提示：<br>&nbsp;&nbsp;&nbsp;拖拽要重建文件夹到此！<br><font color = \'red\'>注意：<br>&nbsp;&nbsp;&nbsp;路径中不能出现中文字符！</font></p></h4>"))
        self.lineEdit_OptzApk.setToolTip(_translate("Form", "<h4><p>提示：<br>&nbsp;&nbsp;&nbsp;拖拽要优化的.apk文件到此！</p></h4>"))
        self.lineEdit_SignApk.setToolTip(_translate("Form", "<h4><p>提示：<br>&nbsp;&nbsp;&nbsp;拖拽要签名的.apk文件到此！</p></h4>"))
        self.pushButton_DeApk.setText(_translate("Form", "反编译.apk"))
        self.pushButton_ReApk.setText(_translate("Form", "重建.apk"))
        self.pushButton_OptzApk.setText(_translate("Form", "优化.apk"))
        self.pushButton_SignApk.setText(_translate("Form", "签名.apk"))
        self.groupBox_2.setTitle(_translate("Form", "framework-res.apk工具"))
        self.lineEdit_Framework.setToolTip(_translate("Form", "<h4><p>提示：<br>&nbsp;&nbsp;&nbsp;拖拽要安装的Framework-res.apk文件到此！</p></h4>"))
        self.pushButton_InsFramework.setText(_translate("Form", "安装"))
        self.pushButton_ViewFramework.setText(_translate("Form", "查看"))
        self.groupBox_3.setTitle(_translate("Form", ".jar工具"))
        self.lineEdit_Apk2Jar.setToolTip(_translate("Form", "<h4><p>提示：<br>&nbsp;&nbsp;&nbsp;拖拽要转换的.apk文件到此！</p></h4>"))
        self.lineEdit_Dex2Jar.setToolTip(_translate("Form", "<h4><p>提示：<br>&nbsp;&nbsp;&nbsp;拖拽要转换的.dex文件到此！</p></h4>"))
        self.pushButton_Apk2Jar.setText(_translate("Form", ".apk转.jar"))
        self.pushButton_Dex2Jar.setText(_translate("Form", ".dex转.jar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "工具"))
        self.groupBox_6.setTitle(_translate("Form", "Key store"))
        self.label.setText(_translate("Form", "Key store path:"))
        self.label_2.setText(_translate("Form", "Key store password:"))
        self.label_3.setText(_translate("Form", "Key alias:"))
        self.label_4.setText(_translate("Form", "Key password:"))
        self.checkBox_Remember.setText(_translate("Form", "Remember passwords"))
        self.pushButton_CreateKeyStore.setText(_translate("Form", "Create new..."))
        self.pushButton_ChooseKeyStore.setText(_translate("Form", "Choose existing..."))
        self.lineEdit_KeyStorePath.setToolTip(_translate("Form", "<html><head/><body><p align=\"justify\"><span style=\" font-weight:600;\">指定密钥库的名称</span><span style=\" font-weight:600; color:#ff0000;\">keystore.jks</span></p></body></html>"))
        self.lineEdit_StorePassword.setToolTip(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600;\">指定密钥库的密码(获取keystore信息所需的密码，默认：arno123)</span></p></body></html>"))
        self.lineEdit_KeyAlias.setToolTip(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600;\">指定别名(每个keystore都关联这一个独一无二的alias，这个alias通常不区分大小写)</span></p></body></html>"))
        self.lineEdit_KeyPassword.setToolTip(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600;\">指定别名条目的密码(私钥的密码，默认：arno123)</span></p></body></html>"))
        self.groupBox_7.setTitle(_translate("Form", "Signature"))
        self.checkBox_V1Signature.setText(_translate("Form", "V1(Jar Signature)"))
        self.checkBox_V2Signature.setText(_translate("Form", "V2(Full APK Signature)"))
        self.label_5.setText(_translate("Form", "Signature Versions:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "签名"))
        self.groupBox_4.setTitle(_translate("Form", "常规"))
        self.checkBox_ReAutoOptz.setText(_translate("Form", "重建.apk时，自动对重建后的.apk文件进行优化。"))
        self.checkBox_ReAutoSign.setText(_translate("Form", "优化.apk时，自动对优化后的.apk文件进行签名。"))
        self.groupBox_5.setTitle(_translate("Form", "修复"))
        self.checkBox_DeAutoFix.setText(_translate("Form", "反编译.apk时，自动修复.xml文件重出现的\'@*android:\'错误。"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Form", "选项"))
        self.label_Log.setText(_translate("Form", "日志 ："))
        self.pushButton_ClearLog.setText(_translate("Form", "清除"))
        self.pushButton_ExportLog.setText(_translate("Form", "导出"))
        self.pushButton_About.setText(_translate("Form", "关于"))
        self.pushButton_CheckEvn.setText(_translate("Form", "检测"))
        self.plainTextEdit_Log.setPlainText(_translate("Form", "提示：使用apksigner，只能在APK文件签名之前执行zipalign。\n"
"如果您使用apksigner对APK进行签名并对APK进行进一步更改，则其签名将失效。\n"
""))

