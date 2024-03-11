# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'punMenioGkEng.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
)
from PySide6.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QAbstractItemView,
    QAbstractScrollArea,
    QApplication,
    QDateEdit,
    QFormLayout,
    QFrame,
    QGridLayout,
    QHBoxLayout,
    QHeaderView,
    QLabel,
    QLayout,
    QLineEdit,
    QMainWindow,
    QMenuBar,
    QPushButton,
    QSizePolicy,
    QSlider,
    QSplitter,
    QStatusBar,
    QTabWidget,
    QTableView,
    QTextEdit,
    QTimeEdit,
    QToolBar,
    QVBoxLayout,
    QWidget,
)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setLocale(QLocale(QLocale.Serbian, QLocale.Serbia))
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QTabWidget.Triangular)
        MainWindow.setUnifiedTitleAndToolBarOnMac(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        sizePolicy.setHeightForWidth(
            self.centralwidget.sizePolicy().hasHeightForWidth()
        )
        self.centralwidget.setSizePolicy(sizePolicy)
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_korisnici = QWidget()
        self.tab_korisnici.setObjectName("tab_korisnici")
        sizePolicy.setHeightForWidth(
            self.tab_korisnici.sizePolicy().hasHeightForWidth()
        )
        self.tab_korisnici.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(self.tab_korisnici)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_glavniMeni = QVBoxLayout()
        self.verticalLayout_glavniMeni.setObjectName("verticalLayout_glavniMeni")
        self.lineEdit_pretraga = QLineEdit(self.tab_korisnici)
        self.lineEdit_pretraga.setObjectName("lineEdit_pretraga")

        self.verticalLayout_glavniMeni.addWidget(self.lineEdit_pretraga)

        self.splitter = QSplitter(self.tab_korisnici)
        self.splitter.setObjectName("splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.verticalLayoutWidget = QWidget(self.splitter)
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_tabele = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_tabele.setObjectName("verticalLayout_tabele")
        self.verticalLayout_tabele.setContentsMargins(0, 0, 0, 0)
        self.label_korisnici = QLabel(self.verticalLayoutWidget)
        self.label_korisnici.setObjectName("label_korisnici")

        self.verticalLayout_tabele.addWidget(self.label_korisnici)

        self.tableView_korisnici = QTableView(self.verticalLayoutWidget)
        self.tableView_korisnici.setObjectName("tableView_korisnici")
        self.tableView_korisnici.setSizeAdjustPolicy(
            QAbstractScrollArea.AdjustToContents
        )
        self.tableView_korisnici.setDragEnabled(True)
        self.tableView_korisnici.setAlternatingRowColors(True)
        self.tableView_korisnici.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableView_korisnici.setGridStyle(Qt.NoPen)
        self.tableView_korisnici.setSortingEnabled(True)

        self.verticalLayout_tabele.addWidget(self.tableView_korisnici)

        self.horizontalLayout_korisnici = QHBoxLayout()
        self.horizontalLayout_korisnici.setObjectName("horizontalLayout_korisnici")
        self.pushButton_dodajKorisnika = QPushButton(self.verticalLayoutWidget)
        self.pushButton_dodajKorisnika.setObjectName("pushButton_dodajKorisnika")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(
            self.pushButton_dodajKorisnika.sizePolicy().hasHeightForWidth()
        )
        self.pushButton_dodajKorisnika.setSizePolicy(sizePolicy1)

        self.horizontalLayout_korisnici.addWidget(self.pushButton_dodajKorisnika)

        self.pushButton_izbrisiKorisnika = QPushButton(self.verticalLayoutWidget)
        self.pushButton_izbrisiKorisnika.setObjectName("pushButton_izbrisiKorisnika")
        sizePolicy1.setHeightForWidth(
            self.pushButton_izbrisiKorisnika.sizePolicy().hasHeightForWidth()
        )
        self.pushButton_izbrisiKorisnika.setSizePolicy(sizePolicy1)

        self.horizontalLayout_korisnici.addWidget(self.pushButton_izbrisiKorisnika)

        self.verticalLayout_tabele.addLayout(self.horizontalLayout_korisnici)

        self.splitter.addWidget(self.verticalLayoutWidget)
        self.verticalLayoutWidget_2 = QWidget(self.splitter)
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_vozila = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_vozila.setObjectName("verticalLayout_vozila")
        self.verticalLayout_vozila.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_vozila.setContentsMargins(0, 0, 0, 0)
        self.label_vozila = QLabel(self.verticalLayoutWidget_2)
        self.label_vozila.setObjectName("label_vozila")

        self.verticalLayout_vozila.addWidget(self.label_vozila)

        self.tableView_vozila = QTableView(self.verticalLayoutWidget_2)
        self.tableView_vozila.setObjectName("tableView_vozila")
        self.tableView_vozila.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableView_vozila.setDragEnabled(True)
        self.tableView_vozila.setAlternatingRowColors(True)
        self.tableView_vozila.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableView_vozila.setSortingEnabled(True)

        self.verticalLayout_vozila.addWidget(self.tableView_vozila)

        self.horizontalLayout_buttonsKorisnici = QHBoxLayout()
        self.horizontalLayout_buttonsKorisnici.setObjectName(
            "horizontalLayout_buttonsKorisnici"
        )
        self.pushButton_dodajVozilo = QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_dodajVozilo.setObjectName("pushButton_dodajVozilo")
        sizePolicy1.setHeightForWidth(
            self.pushButton_dodajVozilo.sizePolicy().hasHeightForWidth()
        )
        self.pushButton_dodajVozilo.setSizePolicy(sizePolicy1)

        self.horizontalLayout_buttonsKorisnici.addWidget(self.pushButton_dodajVozilo)

        self.pushButton_izbrisiVozilo = QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_izbrisiVozilo.setObjectName("pushButton_izbrisiVozilo")
        sizePolicy1.setHeightForWidth(
            self.pushButton_izbrisiVozilo.sizePolicy().hasHeightForWidth()
        )
        self.pushButton_izbrisiVozilo.setSizePolicy(sizePolicy1)

        self.horizontalLayout_buttonsKorisnici.addWidget(self.pushButton_izbrisiVozilo)

        self.verticalLayout_vozila.addLayout(self.horizontalLayout_buttonsKorisnici)

        self.splitter.addWidget(self.verticalLayoutWidget_2)

        self.verticalLayout_glavniMeni.addWidget(self.splitter)

        self.gridLayout.addLayout(self.verticalLayout_glavniMeni, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_korisnici, "")
        self.tab_podesavanja = QWidget()
        self.tab_podesavanja.setObjectName("tab_podesavanja")
        self.formLayout_2 = QFormLayout(self.tab_podesavanja)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_velicina = QLabel(self.tab_podesavanja)
        self.label_velicina.setObjectName("label_velicina")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_velicina)

        self.horizontalLayout_font = QHBoxLayout()
        self.horizontalLayout_font.setObjectName("horizontalLayout_font")
        self.label_velicinaFontaMin = QLabel(self.tab_podesavanja)
        self.label_velicinaFontaMin.setObjectName("label_velicinaFontaMin")

        self.horizontalLayout_font.addWidget(self.label_velicinaFontaMin)

        self.horizontalSlider_font = QSlider(self.tab_podesavanja)
        self.horizontalSlider_font.setObjectName("horizontalSlider_font")
        self.horizontalSlider_font.setMinimum(8)
        self.horizontalSlider_font.setMaximum(24)
        self.horizontalSlider_font.setPageStep(1)
        self.horizontalSlider_font.setValue(12)
        self.horizontalSlider_font.setOrientation(Qt.Horizontal)
        self.horizontalSlider_font.setTickPosition(QSlider.TicksBelow)

        self.horizontalLayout_font.addWidget(self.horizontalSlider_font)

        self.label_velicinaFontaMax = QLabel(self.tab_podesavanja)
        self.label_velicinaFontaMax.setObjectName("label_velicinaFontaMax")

        self.horizontalLayout_font.addWidget(self.label_velicinaFontaMax)

        self.formLayout_2.setLayout(
            1, QFormLayout.FieldRole, self.horizontalLayout_font
        )

        self.tabWidget.addTab(self.tab_podesavanja, "")
        self.tab_servis = QWidget()
        self.tab_servis.setObjectName("tab_servis")
        self.verticalLayout = QVBoxLayout(self.tab_servis)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_glavniServis = QVBoxLayout()
        self.verticalLayout_glavniServis.setObjectName("verticalLayout_glavniServis")
        self.gridLayout_servis = QGridLayout()
        self.gridLayout_servis.setObjectName("gridLayout_servis")
        self.label_model = QLabel(self.tab_servis)
        self.label_model.setObjectName("label_model")

        self.gridLayout_servis.addWidget(self.label_model, 0, 0, 1, 1)

        self.lineEdit_model = QLineEdit(self.tab_servis)
        self.lineEdit_model.setObjectName("lineEdit_model")

        self.gridLayout_servis.addWidget(self.lineEdit_model, 0, 1, 1, 1)

        self.label_vrsta = QLabel(self.tab_servis)
        self.label_vrsta.setObjectName("label_vrsta")

        self.gridLayout_servis.addWidget(self.label_vrsta, 1, 0, 1, 1)

        self.lineEdit_vrsta = QLineEdit(self.tab_servis)
        self.lineEdit_vrsta.setObjectName("lineEdit_vrsta")

        self.gridLayout_servis.addWidget(self.lineEdit_vrsta, 1, 1, 1, 1)

        self.label_brojSasija = QLabel(self.tab_servis)
        self.label_brojSasija.setObjectName("label_brojSasija")

        self.gridLayout_servis.addWidget(self.label_brojSasija, 0, 2, 1, 1)

        self.lineEdit_brojSasija = QLineEdit(self.tab_servis)
        self.lineEdit_brojSasija.setObjectName("lineEdit_brojSasija")

        self.gridLayout_servis.addWidget(self.lineEdit_brojSasija, 0, 3, 1, 1)

        self.label_brojMotor = QLabel(self.tab_servis)
        self.label_brojMotor.setObjectName("label_brojMotor")

        self.gridLayout_servis.addWidget(self.label_brojMotor, 1, 2, 1, 1)

        self.lineEdit_brojMotor = QLineEdit(self.tab_servis)
        self.lineEdit_brojMotor.setObjectName("lineEdit_brojMotor")

        self.gridLayout_servis.addWidget(self.lineEdit_brojMotor, 1, 3, 1, 1)

        self.label_tablice = QLabel(self.tab_servis)
        self.label_tablice.setObjectName("label_tablice")

        self.gridLayout_servis.addWidget(self.label_tablice, 0, 4, 1, 1)

        self.lineEdit_tablice = QLineEdit(self.tab_servis)
        self.lineEdit_tablice.setObjectName("lineEdit_tablice")

        self.gridLayout_servis.addWidget(self.lineEdit_tablice, 0, 5, 1, 1)

        self.label_godiste = QLabel(self.tab_servis)
        self.label_godiste.setObjectName("label_godiste")

        self.gridLayout_servis.addWidget(self.label_godiste, 1, 4, 1, 1)

        self.lineEdit_godiste = QLineEdit(self.tab_servis)
        self.lineEdit_godiste.setObjectName("lineEdit_godiste")

        self.gridLayout_servis.addWidget(self.lineEdit_godiste, 1, 5, 1, 1)

        self.label_snaga = QLabel(self.tab_servis)
        self.label_snaga.setObjectName("label_snaga")

        self.gridLayout_servis.addWidget(self.label_snaga, 0, 6, 1, 1)

        self.lineEdit_snaga = QLineEdit(self.tab_servis)
        self.lineEdit_snaga.setObjectName("lineEdit_snaga")

        self.gridLayout_servis.addWidget(self.lineEdit_snaga, 0, 7, 1, 1)

        self.label_kubikaza = QLabel(self.tab_servis)
        self.label_kubikaza.setObjectName("label_kubikaza")

        self.gridLayout_servis.addWidget(self.label_kubikaza, 1, 6, 1, 1)

        self.lineEdit_kubikaza = QLineEdit(self.tab_servis)
        self.lineEdit_kubikaza.setObjectName("lineEdit_kubikaza")

        self.gridLayout_servis.addWidget(self.lineEdit_kubikaza, 1, 7, 1, 1)

        self.verticalLayout_glavniServis.addLayout(self.gridLayout_servis)

        self.splitter_servis = QSplitter(self.tab_servis)
        self.splitter_servis.setObjectName("splitter_servis")
        self.splitter_servis.setOrientation(Qt.Horizontal)
        self.widget = QWidget(self.splitter_servis)
        self.widget.setObjectName("widget")
        self.verticalLayout_dodajServis = QVBoxLayout(self.widget)
        self.verticalLayout_dodajServis.setObjectName("verticalLayout_dodajServis")
        self.verticalLayout_dodajServis.setContentsMargins(0, 0, 0, 0)
        self.label_dodajServis = QLabel(self.widget)
        self.label_dodajServis.setObjectName("label_dodajServis")

        self.verticalLayout_dodajServis.addWidget(self.label_dodajServis)

        self.label_datum = QLabel(self.widget)
        self.label_datum.setObjectName("label_datum")

        self.verticalLayout_dodajServis.addWidget(self.label_datum)

        self.dateEdit_datum = QDateEdit(self.widget)
        self.dateEdit_datum.setObjectName("dateEdit_datum")
        self.dateEdit_datum.setCalendarPopup(True)

        self.verticalLayout_dodajServis.addWidget(self.dateEdit_datum)

        self.label_vreme = QLabel(self.widget)
        self.label_vreme.setObjectName("label_vreme")

        self.verticalLayout_dodajServis.addWidget(self.label_vreme)

        self.timeEdit_vreme = QTimeEdit(self.widget)
        self.timeEdit_vreme.setObjectName("timeEdit_vreme")

        self.verticalLayout_dodajServis.addWidget(self.timeEdit_vreme)

        self.label_detaljiServisa = QLabel(self.widget)
        self.label_detaljiServisa.setObjectName("label_detaljiServisa")

        self.verticalLayout_dodajServis.addWidget(self.label_detaljiServisa)

        self.lineEdit_detaljiServisa = QTextEdit(self.widget)
        self.lineEdit_detaljiServisa.setObjectName("lineEdit_detaljiServisa")

        self.verticalLayout_dodajServis.addWidget(self.lineEdit_detaljiServisa)

        self.label_kilometraza = QLabel(self.widget)
        self.label_kilometraza.setObjectName("label_kilometraza")

        self.verticalLayout_dodajServis.addWidget(self.label_kilometraza)

        self.lineEdit_kilometraza = QLineEdit(self.widget)
        self.lineEdit_kilometraza.setObjectName("lineEdit_kilometraza")

        self.verticalLayout_dodajServis.addWidget(self.lineEdit_kilometraza)

        self.label_cena = QLabel(self.widget)
        self.label_cena.setObjectName("label_cena")

        self.verticalLayout_dodajServis.addWidget(self.label_cena)

        self.lineEdit_cena = QLineEdit(self.widget)
        self.lineEdit_cena.setObjectName("lineEdit_cena")

        self.verticalLayout_dodajServis.addWidget(self.lineEdit_cena)

        self.pushButton_dodaj = QPushButton(self.widget)
        self.pushButton_dodaj.setObjectName("pushButton_dodaj")

        self.verticalLayout_dodajServis.addWidget(self.pushButton_dodaj)

        self.pushButton_izmeni = QPushButton(self.widget)
        self.pushButton_izmeni.setObjectName("pushButton_izmeni")

        self.verticalLayout_dodajServis.addWidget(self.pushButton_izmeni)

        self.splitter_servis.addWidget(self.widget)
        self.frame = QFrame(self.splitter_servis)
        self.frame.setObjectName("frame")
        self.verticalLayout_4 = QVBoxLayout(self.frame)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.tableView_servisi = QTableView(self.frame)
        self.tableView_servisi.setObjectName("tableView_servisi")

        self.verticalLayout_4.addWidget(self.tableView_servisi)

        self.pushButton_izbrisi = QPushButton(self.frame)
        self.pushButton_izbrisi.setObjectName("pushButton_izbrisi")

        self.verticalLayout_4.addWidget(self.pushButton_izbrisi)

        self.splitter_servis.addWidget(self.frame)

        self.verticalLayout_glavniServis.addWidget(self.splitter_servis)

        self.verticalLayout_glavniServis.setStretch(1, 1)

        self.verticalLayout.addLayout(self.verticalLayout_glavniServis)

        self.tabWidget.addTab(self.tab_servis, "")

        self.gridLayout_3.addWidget(self.tabWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName("menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "MainWindow", None)
        )
        self.label_korisnici.setText(
            QCoreApplication.translate("MainWindow", "Korisnici:", None)
        )
        self.pushButton_dodajKorisnika.setText(
            QCoreApplication.translate("MainWindow", "Dodaj korisnika", None)
        )
        self.pushButton_izbrisiKorisnika.setText(
            QCoreApplication.translate("MainWindow", "Izbri\u0161i korisnika", None)
        )
        self.label_vozila.setText(
            QCoreApplication.translate("MainWindow", "Vozila:", None)
        )
        self.pushButton_dodajVozilo.setText(
            QCoreApplication.translate("MainWindow", "Dodaj vozilo", None)
        )
        self.pushButton_izbrisiVozilo.setText(
            QCoreApplication.translate("MainWindow", "Izbri\u0161i vozilo", None)
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_korisnici),
            QCoreApplication.translate("MainWindow", "Korisnici", None),
        )
        self.label_velicina.setText(
            QCoreApplication.translate("MainWindow", "Veli\u010dina", None)
        )
        self.label_velicinaFontaMin.setText(
            QCoreApplication.translate("MainWindow", "8", None)
        )
        # if QT_CONFIG(tooltip)
        self.horizontalSlider_font.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                "Promena veli\u010dine fonta u opsegu datom brojevima",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.label_velicinaFontaMax.setText(
            QCoreApplication.translate("MainWindow", "24", None)
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_podesavanja),
            QCoreApplication.translate("MainWindow", "Pode\u0161avanja", None),
        )
        self.label_model.setText(
            QCoreApplication.translate("MainWindow", "Model", None)
        )
        self.label_vrsta.setText(
            QCoreApplication.translate("MainWindow", "Vrsta", None)
        )
        self.label_brojSasija.setText(
            QCoreApplication.translate("MainWindow", "Broj \u0161asija", None)
        )
        self.label_brojMotor.setText(
            QCoreApplication.translate("MainWindow", "Broj motor", None)
        )
        self.label_tablice.setText(
            QCoreApplication.translate("MainWindow", "Tablice", None)
        )
        self.label_godiste.setText(
            QCoreApplication.translate("MainWindow", "Godi\u0161te", None)
        )
        self.label_snaga.setText(
            QCoreApplication.translate("MainWindow", "Snaga", None)
        )
        self.label_kubikaza.setText(
            QCoreApplication.translate("MainWindow", "Kubika\u017ea", None)
        )
        self.label_dodajServis.setText(
            QCoreApplication.translate("MainWindow", "Dodaj servis:", None)
        )
        self.label_datum.setText(
            QCoreApplication.translate("MainWindow", "Datum:", None)
        )
        self.label_vreme.setText(
            QCoreApplication.translate("MainWindow", "Vreme:", None)
        )
        self.label_detaljiServisa.setText(
            QCoreApplication.translate("MainWindow", "Detalji servisa:", None)
        )
        self.label_kilometraza.setText(
            QCoreApplication.translate("MainWindow", "Kilometra\u017ea:", None)
        )
        self.label_cena.setText(QCoreApplication.translate("MainWindow", "Cena:", None))
        self.pushButton_dodaj.setText(
            QCoreApplication.translate("MainWindow", "Dodaj>", None)
        )
        self.pushButton_izmeni.setText(
            QCoreApplication.translate("MainWindow", "Izmeni>", None)
        )
        self.pushButton_izbrisi.setText(
            QCoreApplication.translate("MainWindow", "Izbri\u0161i", None)
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_servis),
            QCoreApplication.translate("MainWindow", "Servis", None),
        )
        self.toolBar.setWindowTitle(
            QCoreApplication.translate("MainWindow", "toolBar", None)
        )

    # retranslateUi
