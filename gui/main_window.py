from PySide6.QtWidgets import *
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__();self.setWindowTitle('TradePilot v0.3.0');self.resize(1200,800);m=self.menuBar();[m.addMenu(x) for x in ['File','Broker','Strategies','Journal','Settings','Help']];c=QWidget();h=QHBoxLayout(c);nav=QListWidget();nav.addItems(['Dashboard','Strategies','Positions','Journal','Logs']);h.addWidget(nav);v=QVBoxLayout();
        [v.addWidget(QLabel(t)) for t in ['Broker: Not Connected','Paper Trading: Enabled','Buying Power: --','Today P/L: --']];log=QPlainTextEdit();log.setReadOnly(True);log.setPlainText('TradePilot Started\nSettings Loaded\nReady');v.addWidget(log);h.addLayout(v);self.setCentralWidget(c);self.setStatusBar(QStatusBar());self.statusBar().showMessage('Ready')