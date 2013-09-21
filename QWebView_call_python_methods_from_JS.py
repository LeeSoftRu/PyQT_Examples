"""
This example shows how to call python methods from web page using JS
Tags: #QWebView #WebKit #PyQT4
"""
from PyQt4 import QtCore, QtGui
from PyQt4.QtWebKit import QWebView

class JsBridge(QtGui.QWidget):
    def __init__(self, parent=None):
        super(JsBridge, self).__init__(parent)

        self.ui = QWebView()
        self.ui.setHtml("""
            <input type="text" id="username" value="Vasya Pupkin"><br>
            <a onclick="bridge.someEvent()">Hello, Python!</a>
        """)
        self.ui.page().mainFrame().javaScriptWindowObjectCleared.connect(
            self.populateJavaScriptWindowObject)

    @QtCore.pyqtSlot()
    def someEvent(self):
        print('someEvent() called!')

        frame = self.ui.page().mainFrame()
        username = frame.findFirstElement('#username').evaluateJavaScript('this.value')
        QtGui.QMessageBox.about(self, "Aloha", "Hello, " + username + "!")

    def populateJavaScriptWindowObject(self):
        print("Bridge request handled")
        self.ui.page().mainFrame().addToJavaScriptWindowObject('bridge', self)

if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    form = JsBridge()
    form.ui.resize(250, 100)
    form.ui.show()
    sys.exit(app.exec_())
