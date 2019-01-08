import sys
import os
import shutil
import re
import subprocess
import platform
import time
import json
from PyQt5 import (QtWidgets, QtCore, QtGui)
from PyQt5.QtWidgets import (QMessageBox, QFileDialog)
from Ui_MainForm import Ui_Form
from pyNewKeyStore import Dialog_NewKeyStore


def sh(command):
    p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output = p.communicate()[0]
    # p.terminate()
    sysstr = platform.system()
    if (sysstr == 'Windows'):
        return output.decode('cp936').encode('utf-8').decode('utf-8')
    else:
        return output.decode('utf-8')


class ShellThread(QtCore.QThread):
    signal_shell = QtCore.pyqtSignal(int, str)  # 决定信号接受的参数类型
    signal_stdout = QtCore.pyqtSignal(str)

    def __init__(self, item, command):
        super(ShellThread, self).__init__()
        self.command = command
        self.item = item

    def __del__(self):
        self.wait()

    def run(self):
        p = subprocess.Popen(self.command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        while p.poll() is None:
            line = p.stdout.readline().strip()
            if line:
                if (platform.system() == 'Windows'):
                    self.signal_stdout.emit(line.decode('cp936').encode('utf-8').decode('utf-8') + "\r\n")
                else:
                    self.signal_stdout.emit(line.decode('utf-8'))

        # return result
        self.signal_shell.emit(p.returncode, self.item)
        # p.terminate()


class ExtLineEdit():

    def __init__(self, lineEdit):
        self.lineEdit = lineEdit
        self.lineEdit.setAcceptDrops(True)
        self.lineEdit.dragEnterEvent = self.dragEnterEvent
        self.lineEdit.dropEvent = self.dropEvent

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event):
        data = event.mimeData()
        urls = data.urls()
        if (urls and urls[0].scheme() == 'file'):
            # for some reason, this doubles up the intro slash
            filepath = str(urls[0].path())[1:]
            self.lineEdit.setText(filepath)


class MyWindow(QtWidgets.QMainWindow, Ui_Form):

    def __init__(self):
        super(MyWindow, self).__init__()
        self.setupUi(self)

        # ============================== tab ==============================
        ExtLineEdit(self.lineEdit_DeApk)
        ExtLineEdit(self.lineEdit_ReApk)
        ExtLineEdit(self.lineEdit_OptzApk)
        ExtLineEdit(self.lineEdit_SignApk)
        ExtLineEdit(self.lineEdit_Framework)
        ExtLineEdit(self.lineEdit_Apk2Jar)
        ExtLineEdit(self.lineEdit_Dex2Jar)

        # button clicked
        self.pushButton_DeApk.clicked.connect(self.on_pushButton_DeApk)
        self.pushButton_ReApk.clicked.connect(self.on_pushButton_ReApk)
        self.pushButton_OptzApk.clicked.connect(self.on_pushButton_OptzApk)
        self.pushButton_SignApk.clicked.connect(self.on_pushButton_SignApk)
        self.pushButton_InsFramework.clicked.connect(self.on_pushButton_InsFramework)
        self.pushButton_ViewFramework.clicked.connect(self.on_pushButton_ViewFramework)
        self.pushButton_Apk2Jar.clicked.connect(self.on_pushButton_Apk2Jar)
        self.pushButton_Dex2Jar.clicked.connect(self.on_pushButton_Dex2Jar)

        # 暂不开放资源美化
        self.pushButton_InsFramework.setDisabled(True)
        self.pushButton_ViewFramework.setDisabled(True)

        # button clicked
        self.pushButton_ClearLog.clicked.connect(self.on_pushButton_ClearLog)
        self.pushButton_CheckEvn.clicked.connect(self.on_pushButton_CheckEvn)
        self.pushButton_About.clicked.connect(self.on_pushButton_About)
        self.pushButton_ExportLog.clicked.connect(self.on_pushButton_ExportLog)

        # ============================== tab_2 ==============================
        self.pushButton_CreateKeyStore.clicked.connect(self.on_pushButton_CreateKeyStore)
        self.pushButton_ChooseKeyStore.clicked.connect(self.on_pushButton_ChooseKeyStore)
        self.checkBox_Remember.clicked.connect(self.on_checkBox_Remember)
        self.checkBox_V1Signature.setChecked(True)
        self.checkBox_V2Signature.setChecked(True)

        # ============================== tab_3 ==============================
        self.checkBox_ReAutoOptz.setChecked(True)
        self.checkBox_ReAutoSign.setChecked(True)
        self.checkBox_DeAutoFix.setChecked(True)

        # path
        self.exeDirPath = str(os.path.dirname(__file__)).replace("\\", "/")
        self.binToolPath = self.exeDirPath + '/bin/'
        self.apktool = 'apktool-cli.jar'
        self.dex2jar = 'd2j-dex2jar.bat'
        self.aapt = 'aapt.exe'
        self.zipalign = 'zipalign.exe'
        self.apksigner = 'apksigner.jar'

        # config
        self.settingsPath = self.exeDirPath + '/settings.json'
        if os.path.isfile(self.settingsPath):
            with open(self.settingsPath, 'r') as f:
                dict_settings = json.load(f)
                assert isinstance(dict_settings, dict)
                if dict_settings['RememberPassword']:
                    self.lineEdit_KeyStorePath.setText(dict_settings['KeyStorePath'])
                    self.lineEdit_StorePassword.setText(dict_settings['StorePassword'])
                    self.lineEdit_KeyAlias.setText(dict_settings['KeyAlias'])
                    self.lineEdit_KeyPassword.setText(dict_settings['KeyPassword'])
                    self.checkBox_Remember.setChecked(True)

    def shellThread(self, itme, command):
        self.addLog('命令: {}\r\n'.format(command))
        self.thread = ShellThread(itme, command)
        self.thread.signal_stdout.connect(self.addLog)  # 增强型错误信息
        self.thread.signal_shell.connect(self.ShellThreadInfo)
        self.thread.start()

    def ShellThreadInfo(self, returncode, item):
        tm = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        if returncode == 0:
            # success
            if "DeApk" == item:
                self.addLog("[{}] 反编译.apk成功！\r\n".format(tm))
            elif "ReApk" == item:
                self.addLog("[{}] 重建.apk成功！\r\n".format(tm))
                if self.checkBox_ReAutoOptz.isChecked():
                    self.on_pushButton_OptzApk()

            elif "OptzApk" == item:
                self.addLog("[{}] 优化.apk成功！\r\n".format(tm))
                if self.checkBox_ReAutoSign.isChecked():
                    self.on_pushButton_SignApk()

            elif "SignApk" == item:
                self.addLog("[{}] 签名.apk成功！\r\n".format(tm))
            elif "InsFramework" == item:
                pass
            elif "ViewFramework" == item:
                pass
            elif "Apk2Jar" == item:
                self.addLog("[{}] .apk转.jar成功！\r\n".format(tm))
                pass
            elif "Dex2Jar" == item:
                self.addLog("[{}] .dex转.jar成功！\r\n".format(tm))
                pass
            elif "CreateKeyStore" == item:
                self.addLog("[{}] 创建签名.jks成功！\r\n".format(tm))
            else:
                pass
        else:
            # error
            if "DeApk" == item:
                self.addLog("[{}] 反编译.apk失败！\r\n".format(tm))
            elif "ReApk" == item:
                self.addLog("[{}] 重建.apk失败！\r\n".format(tm))
            elif "OptzApk" == item:
                self.addLog("[{}] 优化.apk失败！\r\n".format(tm))
            elif "SignApk" == item:
                self.addLog("[{}] 签名.apk失败！\r\n".format(tm))
            elif "InsFramework" == item:
                self.addLog("[{}] 安装Framework-res失败！\r\n".format(tm))
            elif "Apk2Jar" == item:
                self.addLog("[{}] .apk转.jar失败！\r\n".format(tm))
            elif "Dex2Jar" == item:
                self.addLog("[{}] .dex转.jar失败！\r\n".format(tm))
            elif "CreateKeyStore" == item:
                self.addLog("[{}] 创建签名.jks失败！\r\n".format(tm))
            else:
                pass

    def bestPathAppend(self, path, step):
        subPath, extension = os.path.splitext(path)
        apk = os.path.basename(path)

        p = re.compile(r"(?<=\.\()(.+?)(?=\).apk$)")
        result = re.findall(p, apk)
        setup = ''
        if result:
            setup = result[0] + step
            subPath = subPath.rstrip('.({})'.format(setup))
        else:
            setup = step
            subPath = subPath.rstrip('.()')

        return '{}.({}){}'.format(subPath, setup, extension)

    # ============================== tab ==============================
    def addLog(self, msg):
        self.plainTextEdit_Log.moveCursor(QtGui.QTextCursor.End)
        self.plainTextEdit_Log.insertPlainText(msg)
        self.plainTextEdit_Log.moveCursor(QtGui.QTextCursor.End)

    def msgBox(self, msg):
        QMessageBox.information(self, "警告", msg)

    def aboutBox(self):
        title = "关于"
        msg = "程序：pyApkToolkit 1.0.0\r\n"\
              "作者：Arno\r\n"\
              "Copyright (c) 2018 - 2019, Arno.\r\n"\
              "All Rights Reserved."
        QMessageBox.information(self, title, msg)

    def checkJavaEvn(self):
        output = sh('java.exe -version')
        if not (output.find('version') >= 0):
            self.msgBox("    当前机器上无法检测到JDK 1.8的存在！\r\n" "请先安装JDK 1.8开发环境，再进行使用ApkToolkit！")

            self.addLog("警告：当前机器上无法检测到JDK 1.8的存在！\r\n"
                        "..请先安装JDK 1.8开发环境，再进行使用ApkToolkit！\r\n"
                        "..下载地址：http://www.oracle.com/technetwork/java/javase/downloads/index.html\r\n")
            return False

        if os.environ['JAVA_HOME'] == '':
            self.addLog("警告：请在环境变量中设置JAVA_HOME和PATH，例如：\r\n" "  JAVA_HOME=C:\\Program Files\\Java\\jre1.8.0_162\r\n" "  PATH=%PATH%;%JAVA_HOME%\\bin;\r\n")
            return False

        return True

    def checkFileExists(self, toolpath):
        if os.path.isfile(self.binToolPath + toolpath):
            self.addLog("加载{}: {}\r\n".format(toolpath.split('/')[-1], self.binToolPath + toolpath))
        else:
            self.addLog("加载{}: 无法检测到，请确认文件是否存在！\r\n".format(toolpath.split('/')[-1]))

    def on_pushButton_ClearLog(self):
        self.plainTextEdit_Log.clear()

    def on_pushButton_CheckEvn(self):
        # ==============================插件检测=============================
        # 加载aapt.exe：H:\Android\ApkTools\ApkToolkit\bin\aapt.exe
        # 加载apktool-cli.jar：H:\Android\ApkTools\ApkToolkit\bin\apktool-cli.jar
        # 加载dex2jar.bat：H:\Android\ApkTools\ApkToolkit\bin\dex2jar\dex2jar.bat
        # 加载jarsigner.exe：%JAVA_HOME%\bin\jarsigner.exe
        # ====================================================================
        self.addLog("==============================插件检测=============================\r\n")

        self.checkFileExists(self.aapt)
        self.checkFileExists(self.apktool)
        self.checkFileExists('dex2jar/' + self.dex2jar)

        output = sh('jarsigner.exe -help')
        if output.find('verify') >= 0:
            self.addLog("加载jarsigner.exe：%JAVA_HOME%\\bin\\jarsigner.exe\r\n")
        else:
            self.addLog("jarsigner.exe：无法检测到，请在环境变量中设置JAVA_HOME和PATH，例如：\r\n"
                        "  JAVA_HOME=C:\\Program Files\\Java\\jdk1.7.0_60\r\n"
                        "  PATH=%PATH%;%JAVA_HOME%\\bin;\r\n")

        # ============================版本检测================================
        # Java版本：1.8.0_162
        # Aapt版本：0.2-4913185
        # Apktool版本：2.3.4
        # Dex2Jar版本：reader-2.1-SNAPSHOT, translator-2.1-SNAPSHOT, ir-2.1-SNAPSHOT
        # ===================================================================
        self.addLog("==============================版本检测=============================\r\n")

        # java
        output = sh('java.exe -version')
        if output.find('version') >= 0:
            self.addLog("Java版本：{}\r\n".format(output.split('"')[1]))
        else:
            self.addLog("Java版本：未知\r\n")

        # aapt
        output = sh(self.binToolPath + self.aapt + ' v')
        if output.find('Tool,') >= 0:
            self.addLog("aapt版本：{}\r\n".format(output.split('v')[-1].strip('\r\n')))
        else:
            self.addLog("aapt版本：未知\r\n")

        # apktool
        output = sh("java -jar \"" + self.binToolPath + self.apktool + "\"")
        if output.find('usage: apktool') >= 0:
            p = re.compile(r"v([0-9]*?\.[0-9]*?\.[0-9]?)")
            result = re.findall(p, output)
            if result and len(result) > 2:
                self.addLog("apktool版本：{}\r\n".format(result[0]))
                self.addLog("smali版本: {}\r\n".format(result[1]))
                self.addLog("baksmali版本：{}\r\n".format(result[2]))
        else:
            self.addLog("apktool版本：未知\r\n")

        # dex2jar
        output = sh(self.binToolPath + 'dex2jar/' + self.dex2jar)
        if output.find('version: ') >= 0:
            self.addLog("dex2jar版本：{}\r\n".format(output.split('version: ')[-1].strip('\r\n')))
        else:
            self.addLog("dex2jar版本：未知\r\n")

        self.addLog("===================================================================\r\n")

    def on_pushButton_ExportLog(self):
        fileName, _ = QFileDialog.getSaveFileName(self, "导出日志文件", "Log.txt", "Log (*.txt)")
        if fileName:
            f = open(fileName, 'w')
            f.write(self.plainTextEdit_Log.toPlainText())
            f.close()

    def on_pushButton_About(self):
        self.aboutBox()

    # 反编译.apk
    def on_pushButton_DeApk(self):
        # self.lineEdit_DeApk.setText('H:/Android/test/app-release1.apk')
        path = self.lineEdit_DeApk.text()
        output, extension = os.path.splitext(path)
        apk = os.path.basename(path)
        '''
        out = sh("java.exe -jar {} d -f {} -o {}".format(self.binToolPath + self.apktool, path, output))
        self.addLog(out)
        return
        '''
        if os.path.isfile(path) and extension == '.apk':
            # [15:50:51] 反编译文件：app-release1.apk，请稍后...
            tm = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            self.addLog("[{}] 反编译文件: {}, 请稍后...\r\n".format(tm, apk))

            # 检测到目录：H:\Android\test\app-release1已存在，删除此目录！
            if os.path.isdir(output):
                self.addLog("检测到目录: {} 已存在, 删除此目录！\r\n".format(output))
                shutil.rmtree(output)

            self.shellThread("DeApk", "java.exe -jar {} d -f \"{}\" -o \"{}\"".format(self.binToolPath + self.apktool, path, output))

    # 重建.apk
    def on_pushButton_ReApk(self):
        # self.lineEdit_ReApk.setText('H:/Android/test/app-release1')
        path = self.lineEdit_ReApk.text()

        if os.path.isdir(path):
            outPath = self.bestPathAppend(path, 'R') + '.apk'
            self.shellThread("ReApk", "java.exe -jar {} b -f \"{}\" -o \"{}\"".format(self.binToolPath + self.apktool, path, outPath))

            if self.checkBox_ReAutoOptz.isChecked():
                self.lineEdit_OptzApk.setText(outPath)

    # 优化.apk
    def on_pushButton_OptzApk(self):
        # This must always be 4 (which provides 32-bit alignment) or else it effectively does nothing.
        # self.lineEdit_OptzApk.setText('H:/Android/test/app-release.(S).apk')

        path = self.lineEdit_OptzApk.text()
        if os.path.isfile(path):
            outPath = self.bestPathAppend(path, 'O')
            self.shellThread("OptzApk", "{} -f -v 4 \"{}\" \"{}\"".format(self.binToolPath + self.zipalign, path, outPath))

            if self.checkBox_ReAutoSign.isChecked():
                self.lineEdit_SignApk.setText(outPath)

    # 签名.apk
    def on_pushButton_SignApk(self):
        # java -jar apksigner.jar sign              // 执行签名操作
        # --ks H:\Android\arno.jks                  // jks签名证书路径
        # --ks-pass pass:amoy2018                   // keystore密码
        # --ks-key-alias arno                       // 生成jks时指定的alias
        # --key-pass pass:amoy2018                  // 签署者的密码，即生成jks时指定alias对应的密码
        # --v1-signing-enabled true/false           // 勾选v1签名
        # --v2-signing-enabled true/false           // 勾选v2签名
        # --in H:\Android\test\app-release.apk      // 输入路径
        # --out H:\Android\test\app-release.S.apk   // 输出路径
        # self.lineEdit_SignApk.setText('H:/Android/test/app-release.(S).apk')

        path = self.lineEdit_SignApk.text()
        if os.path.isfile(path):
            outPath = self.bestPathAppend(path, 'S')

            keyStorePath = self.lineEdit_KeyStorePath.text()
            storePassword = self.lineEdit_StorePassword.text()
            keyAlias = self.lineEdit_KeyAlias.text()
            keyPassword = self.lineEdit_KeyPassword.text()
            v1 = self.checkBox_V1Signature.isChecked()
            v2 = self.checkBox_V2Signature.isChecked()
            self.shellThread(
                "SignApk", "java -jar {} sign --ks {} --ks-pass pass:{} --ks-key-alias {} --key-pass pass:{} \
                --v1-signing-enabled {} --v2-signing-enabled {} --in \"{}\" --out \"{}\"".format(self.binToolPath + self.apksigner, keyStorePath, storePassword,
                                                                                                 keyAlias, keyPassword,
                                                                                                 str(v1).lower(),
                                                                                                 str(v2).lower(), path, outPath))

    def on_pushButton_InsFramework(self):
        pass

    def on_pushButton_ViewFramework(self):
        pass

    def on_pushButton_Apk2Jar(self):
        # self.lineEdit_Dex2Jar.setText('H:/Android/test/app-release.apk')
        path = self.lineEdit_Apk2Jar.text()
        output, extension = os.path.splitext(path)
        apk = os.path.basename(path)

        if os.path.isfile(path) and extension == '.apk':
            # [15:50:51] 转换文件：classes.dex，请稍后...
            tm = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            self.addLog("[{}] 转换文件: {}, 请稍后...\r\n".format(tm, apk))

            # 检测到目录：H:\Android\test\app-release-dex2jar.jar已存在，删除此目录！
            output += '-dex2jar.jar'
            if os.path.isfile(output):
                self.addLog("检测到文件: {} 已存在, 删除此目录！\r\n".format(output))
                os.remove(output)

            self.shellThread("Apk2Jar", "{} \"{}\" -o \"{}\"".format(self.binToolPath + 'dex2jar/' + self.dex2jar, path, output))

    def on_pushButton_Dex2Jar(self):
        # self.lineEdit_Dex2Jar.setText('H:/Android/test/classes.dex')
        path = self.lineEdit_Dex2Jar.text()
        output, extension = os.path.splitext(path)
        apk = os.path.basename(path)

        if os.path.isfile(path) and extension == '.dex':
            # [15:50:51] 转换文件：classes.dex，请稍后...
            tm = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            self.addLog("[{}] 转换文件: {}, 请稍后...\r\n".format(tm, apk))

            # 检测到目录：H:\Android\test\classes-dex2jar.jar已存在，删除此目录！
            output += '-dex2jar.jar'
            if os.path.isfile(output):
                self.addLog("检测到文件: {} 已存在, 删除此目录！\r\n".format(output))
                os.remove(output)

            self.shellThread("Dex2Jar", "{} \"{}\" -o \"{}\"".format(self.binToolPath + 'dex2jar/' + self.dex2jar, path, output))

    # ============================== tab_2 ==============================
    def on_pushButton_CreateKeyStore(self):
        # keytool.exe -genkey                   // 执行证书操作
        # -alias arno                           // 产生别名,每个keystore都关联这一个独一无二的alias，这个alias通常不区分大小写
        # -keyalg RSA                           // 指定密钥的算法
        # -dname CN=1,OU=2,O=3,L=4,ST=5,C=6     // 指定证书拥有者信息
        # -validity 9125                        // 指定创建的证书有效期多少天
        # -keypass amoy2018                     // 指定别名条目的密码(私钥的密码)
        # -keystore H:\Android\arno123.jks      // 指定密钥库的名称
        # -storepass amoy2018                   // 指定密钥库的密码(获取keystore信息所需的密码)
        dlg = Dialog_NewKeyStore(self)
        result = dlg.exec_()
        if result == QtWidgets.QDialog.Accepted:
            dname = ''
            for k, v in dlg.dname.items():
                if v:
                    dname += '{}={},'.format(k, v)

            dname = dname.rstrip(',')
            self.shellThread(
                "CreateKeyStore", "keytool.exe -genkey -alias {} -keyalg RSA -dname {} -validity {} -keypass {} -keystore \"{}\" -storepass {}".format(
                    dlg.alias, dname, str(dlg.validity * 365), dlg.keyPass, dlg.keyStorePath, dlg.storePass))

    def on_pushButton_ChooseKeyStore(self):
        fileName, _ = QFileDialog.getOpenFileName(self, "search Key Store Path", "keystore.jks", "keystore(*.jks);;All Files (*.*)")
        if fileName:
            self.lineEdit_KeyStorePath.setText(fileName)

    def on_checkBox_Remember(self):  # 有待增强
        dict_settings = {}
        if self.checkBox_Remember.isChecked():
            dict_settings['KeyStorePath'] = self.lineEdit_KeyStorePath.text()
            dict_settings['StorePassword'] = self.lineEdit_StorePassword.text()
            dict_settings['KeyAlias'] = self.lineEdit_KeyAlias.text()
            dict_settings['KeyPassword'] = self.lineEdit_KeyPassword.text()
            dict_settings['RememberPassword'] = True
        else:
            dict_settings['KeyStorePath'] = ''
            dict_settings['StorePassword'] = ''
            dict_settings['KeyAlias'] = ''
            dict_settings['KeyPassword'] = ''
            dict_settings['RememberPassword'] = False
        with open(self.settingsPath, 'w') as dump_f:
            json.dump(dict_settings, dump_f, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.checkJavaEvn()
    window.show()
    sys.exit(app.exec_())
