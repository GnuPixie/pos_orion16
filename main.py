# main.py
import json
import os

import firebase_admin
from PySide6 import QtWidgets
from PySide6.QtCore import Qt, QLocale, QDateTime, QDate, QTime
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtWidgets import (
    QAbstractItemView,
    QMessageBox,
    QHeaderView,
    QDialog,
    QVBoxLayout,
    QLineEdit,
    QPushButton,
    QCompleter,
)
from PySide6.QtWidgets import QApplication
from PySide6.QtWidgets import QComboBox
from firebase_admin import credentials, firestore

from mainWindow import Ui_MainWindow

# Add this at the beginning of your code, before any Qt classes are imported
APPDATA_FOLDER = os.getenv("APPDATA")
SETTINGS_PATH = os.path.join(APPDATA_FOLDER, "StefanPOS", "settings.json")

FIELDS = {
    "korisnici": ["ime", "prezime", "telefon"],
    "vozila": [
        "pripada",
        "model",
        "vrsta",
        "sasija",
        "motor",
        "tablice",
        "godiste",
        "snaga",
        "kubikaza",
    ],
    "servisi": ["pripada", "detalji", "kilometraza", "cena", "datum", "vreme"],
}


class AddItemDialog(QDialog):
    def __init__(self, mode="korisnici", selected_user_id=None, parent=None):
        super().__init__(parent)
        self.mode = mode
        self.setWindowTitle(
            "Dodaj" + (" Korisnika" if mode == "korisnici" else " Vozilo")
        )
        layout = QVBoxLayout()
        self.fields = []
        if mode == "vozila":
            self.pripada_combo = QComboBox()
            self.pripada_combo.setEditable(True)
            layout.addWidget(self.pripada_combo)
            self.load_users(selected_user_id)
            self.fields = [
                ("model", "Model"),
                ("vrsta", "Vrsta"),
                ("sasija", "Šasija"),
                ("motor", "Motor"),
                ("tablice", "Tablice"),
                ("godiste", "Godište"),
                ("snaga", "Snaga"),
                ("kubikaza", "Kubikaža"),
            ]
        elif mode == "korisnici":
            self.fields = [
                ("ime", "Ime"),
                ("prezime", "Prezime"),
                ("telefon", "Telefon"),
            ]

        self.edits = {}
        for field_name, placeholder in self.fields:
            edit = QLineEdit()
            edit.setPlaceholderText(placeholder)
            layout.addWidget(edit)
            self.edits[field_name] = edit

        self.submit_button = QPushButton("Dodaj")
        self.submit_button.clicked.connect(self.accept)
        layout.addWidget(self.submit_button)

        self.setLayout(layout)

    def load_users(self, selected_user_id=None):
        # Fetch users from the database
        users_ref = self.parent().db.collection("korisnici").stream()
        user_names = []
        user_ids = {}
        for user in users_ref:
            user_data = user.to_dict()
            user_name = f"{user_data['ime']} {user_data['prezime']}"
            user_id = user.id
            user_names.append(user_name)
            user_ids[user_name] = user_id

        # Populate the combo box with user names
        self.pripada_combo.addItems(user_names)

        # Set up completer with user names
        self.completer = QCompleter(user_names)
        self.pripada_combo.setCompleter(self.completer)

        # Set selected user if provided
        if selected_user_id:
            selected_user_name = next(
                (name for name, id_ in user_ids.items() if id_ == selected_user_id),
                None,
            )
            if selected_user_name:
                self.pripada_combo.setCurrentText(selected_user_name)

        # Store user IDs for later retrieval
        self.user_ids = user_ids

    def data(self):
        data = {}
        if self.mode == "vozila":
            selected_user_name = self.pripada_combo.currentText()
            selected_user_id = self.user_ids.get(selected_user_name)
            data["pripada"] = selected_user_id
        for field_name, _ in self.fields:
            data[field_name] = self.edits[field_name].text()
        return data


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.load_settings()

        # Initialize tables
        self.init_table("korisnici", ["ID", "Ime", "Prezime", "Telefon"])
        self.init_table(
            "vozila",
            [
                "ID",
                "Pripada",
                "Model",
                "Vrsta",
                "Broj šasije",
                "Broj motora",
                "Tablice",
                "Godište",
                "Snaga",
                "Kubikaža",
            ],
        )
        self.init_table(
            "servisi",
            [
                "ID",
                "Pripada",
                "Detalji",
                "Kilometraža",
                "Cena",
                "Datum",
                "Vreme",
            ],
        )
        self.field_mapping = {
            "ID": "id",
            "Pripada": "pripada",
            "Ime": "ime",
            "Prezime": "prezime",
            "Telefon": "telefon",
            "Model": "model",
            "Vrsta": "vrsta",
            "Broj šasije": "sasija",
            "Broj motora": "motor",
            "Tablice": "tablice",
            "Godište": "godiste",
            "Snaga": "snaga",
            "Kubikaža": "kubikaza",
            "Datum ": "datum",
            "Vreme ": "vreme",
            "Detalji": "detalji",
            "Kilometraža": "kilometraza",
            "Cena": "cena",
        }

        # Connect buttons to methods
        self.ui.pushButton_dodajKorisnika.clicked.connect(
            lambda: self.add_item("korisnici")
        )
        self.ui.pushButton_izbrisiKorisnika.clicked.connect(
            lambda: self.delete_item("korisnici")
        )
        self.ui.pushButton_izbrisiKorisnika.setShortcut(Qt.Key_Backspace)
        self.ui.pushButton_izbrisiKorisnika.setShortcut(Qt.Key_Delete)

        self.ui.pushButton_dodajVozilo.clicked.connect(lambda: self.add_item("vozila"))
        self.ui.pushButton_izbrisiVozilo.clicked.connect(
            lambda: self.delete_item("vozila")
        )
        self.ui.pushButton_izbrisiVozilo.setShortcut(Qt.Key_Backspace)
        self.ui.pushButton_izbrisiVozilo.setShortcut(Qt.Key_Delete)

        self.ui.pushButton_dodaj.clicked.connect(self.add_servis)
        self.ui.pushButton_izmeni.clicked.connect(self.update_servis)
        self.ui.pushButton_izbrisi.clicked.connect(lambda: self.delete_item("servisi"))
        self.ui.pushButton_izbrisi.setShortcut(Qt.Key_Backspace)
        self.ui.pushButton_izbrisi.setShortcut(Qt.Key_Delete)

        self.ui.horizontalSlider_font.valueChanged.connect(
            lambda f: self.change_font_size(self.ui.horizontalSlider_font.value())
        )
        self.ui.lineEdit_pretraga.textChanged.connect(self.filter_korisnici)
        self.ui.tableView_servisi.selectionModel().selectionChanged.connect(
            self.load_servis_data
        )
        self.ui.tableView_vozila.selectionModel().selectionChanged.connect(
            self.filter_servisi_by_vozilo
        )

        self.clear_servis_data()

    def filter_servisi_by_vozilo(self, selected, deselected):
        if selected.indexes():
            # Get the selected vozilo_id
            row = selected.indexes()[0].row()
            vozilo_id = self.vozila_model.item(row, 0).text()

            # Retrieve corresponding data for the selected vehicle
            vozilo_ref = self.db.collection("vozila").document(vozilo_id)
            vozilo_data = vozilo_ref.get().to_dict()

            # Fill line edits with corresponding data
            self.ui.lineEdit_model.setText(vozilo_data.get("model", ""))
            self.ui.lineEdit_vrsta.setText(vozilo_data.get("vrsta", ""))
            self.ui.lineEdit_brojSasija.setText(vozilo_data.get("sasija", ""))
            self.ui.lineEdit_brojMotor.setText(vozilo_data.get("motor", ""))
            self.ui.lineEdit_tablice.setText(vozilo_data.get("tablice", ""))
            self.ui.lineEdit_godiste.setText(str(vozilo_data.get("godiste", "")))
            self.ui.lineEdit_snaga.setText(str(vozilo_data.get("snaga", "")))
            self.ui.lineEdit_kubikaza.setText(str(vozilo_data.get("kubikaza", "")))

            # Filter the servisi based on the selected vozilo_id
            servisi_model = self.servisi_model
            for row in range(servisi_model.rowCount()):
                item = servisi_model.item(
                    row, 1
                )  # Assuming pripada is in the second column
                if item and item.text() != vozilo_id:
                    self.ui.tableView_servisi.hideRow(row)
                else:
                    self.ui.tableView_servisi.showRow(row)
        else:
            # If no item is selected in tableView_vozila, show all items in tableView_servisi
            for row in range(self.ui.tableView_servisi.model().rowCount()):
                self.ui.tableView_servisi.showRow(row)

    def clear_servis_data(self):
        self.ui.lineEdit_detaljiServisa.clear()
        self.ui.lineEdit_kilometraza.clear()
        self.ui.lineEdit_cena.clear()
        self.ui.dateEdit_datum.setDate(QDate.currentDate())
        self.ui.timeEdit_vreme.setTime(QTime.currentTime())

    def load_servis_data(self, selected, deselected):
        if selected.indexes():
            row = selected.indexes()[0].row()
            model = self.servisi_model
            doc_id = model.item(row, 0).text()
            doc_ref = self.db.collection("servisi").document(doc_id)
            doc_data = doc_ref.get().to_dict()
            self.ui.lineEdit_detaljiServisa.setText(doc_data.get("detalji", ""))
            self.ui.lineEdit_kilometraza.setText(str(doc_data.get("kilometraza", "")))
            self.ui.lineEdit_cena.setText(str(doc_data.get("cena", "")))
            datum_vreme = doc_data.get("datum_vreme")
            if datum_vreme:
                datum, vreme = datum_vreme.split(" ")
                self.ui.dateEdit_datum.setDate(QDate.fromString(datum, "yyyy-MM-dd"))
                self.ui.timeEdit_vreme.setTime(QTime.fromString(vreme, "HH:mm:ss"))
        else:
            self.clear_servis_data()

    def filter_korisnici(self, text):
        search_text = self.ui.lineEdit_pretraga.text().lower()
        model = self.korisnici_model

        for row in range(model.rowCount()):
            match_found = any(
                search_text in model.item(row, col).text().lower()
                for col in range(model.columnCount())
                if model.item(row, col) is not None
            )

            if match_found:
                self.ui.tableView_korisnici.showRow(row)
            else:
                self.ui.tableView_korisnici.hideRow(row)

    def load_settings(self):
        # Load settings from settings.json
        if os.path.exists(SETTINGS_PATH):
            with open(SETTINGS_PATH, "r") as file:
                settings = json.load(file)
                font_size = settings.get("font_size", 12)
                cred_location = settings.get("cred_location", "")

                # Set font size
                self.change_font_size(font_size)
                self.ui.horizontalSlider_font.setValue(font_size)

                # Load Firebase Admin credentials
                if cred_location:
                    cred = credentials.Certificate(cred_location)
                    firebase_admin.initialize_app(cred)
                    self.db = firestore.client()
                else:
                    print("No cred_location found in settings.json")

    def change_font_size(self, font_size):
        app = QApplication.instance()
        font = app.font()
        font.setPointSize(font_size)
        app.setFont(font)
        self.update_settings({"font_size": font_size})

    def update_settings(self, new_settings):
        # Update settings.json with new settings
        if os.path.exists(SETTINGS_PATH):
            with open(SETTINGS_PATH, "r") as file:
                settings = json.load(file)
                settings.update(new_settings)

            with open(SETTINGS_PATH, "w") as file:
                json.dump(settings, file, indent=4)

    def add_item(self, item_type):
        selected_user_id = None
        selected_indexes = self.ui.tableView_korisnici.selectedIndexes()
        if selected_indexes and item_type == "vozila":
            row = selected_indexes[0].row()
            selected_user_id = self.korisnici_model.item(row, 0).text()
            print(selected_user_id, "selected")
        dialog = AddItemDialog(item_type, selected_user_id, self)
        if dialog.exec() == QDialog.Accepted:
            data = dialog.data()
            collection_ref = self.db.collection(item_type)
            collection_ref.add(data)

    def add_servis(self):
        selected_indexes = self.ui.tableView_vozila.selectedIndexes()
        if selected_indexes:
            row = selected_indexes[0].row()
            vozilo_id = self.vozila_model.item(row, 0).text()
            detalji = self.ui.lineEdit_detaljiServisa.toPlainText()
            kilometraza = self.ui.lineEdit_kilometraza.text()
            cena = self.ui.lineEdit_cena.text()
            datum = self.ui.dateEdit_datum.date().toString(Qt.ISODate)
            vreme = self.ui.timeEdit_vreme.time().toString("HH:mm:ss")

            data = {
                "pripada": vozilo_id,
                "detalji": detalji,
                "kilometraza": int(kilometraza) if kilometraza else 0,
                "cena": float(cena) if cena else 0.0,
                "datum": datum,  # Separate date
                "vreme": vreme,  # Separate time
            }

            collection_ref = self.db.collection("servisi")
            collection_ref.add(data)

            self.clear_servis_data()
        else:
            QMessageBox.warning(self, "Upozorenje", "Prvo odaberite vozilo.")

    def update_servis(self):
        selected_indexes = self.ui.tableView_servisi.selectedIndexes()
        if selected_indexes:
            row = selected_indexes[0].row()
            servis_id = self.servisi_model.item(row, 0).text()
            detalji = self.ui.lineEdit_detaljiServisa.toPlainText()
            kilometraza = self.ui.lineEdit_kilometraza.text()
            cena = self.ui.lineEdit_cena.text()
            datum = self.ui.dateEdit_datum.date().toString(Qt.ISODate)
            vreme = self.ui.timeEdit_vreme.time().toString("HH:mm:ss")

            data = {
                "detalji": detalji,
                "kilometraza": int(kilometraza) if kilometraza else 0,
                "cena": float(cena) if cena else 0.0,
                "datum": datum,  # Separate date
                "vreme": vreme,  # Separate time
            }

            ref = self.db.collection("servisi").document(servis_id)
            confirm = QMessageBox.question(
                self,
                "Potvrda",
                "Da li ste sigurni da želite da ažurirate ovaj servis?",
                QMessageBox.Yes | QMessageBox.No,
            )
            if confirm == QMessageBox.Yes:
                ref.update(data)
        else:
            QMessageBox.warning(self, "Upozorenje", "Prvo odaberite servis.")

    def delete_item(self, item_type):
        selected_indexes = getattr(self.ui, f"tableView_{item_type}").selectedIndexes()
        if selected_indexes:
            row = selected_indexes[0].row()
            item = getattr(self, f"{item_type}_model").item(row, 0)
            doc_id = item.text()
            confirm = QMessageBox.question(
                self,
                "Confirmation",
                "Are you sure you want to delete this item?",
                QMessageBox.Yes | QMessageBox.No,
            )
            if confirm == QMessageBox.Yes:
                self.remove_row(item_type, doc_id)
                self.remove_from_database(item_type, doc_id)

    def remove_from_database(self, item_type, doc_id):
        ref = self.db.collection(item_type).document(doc_id)
        ref.delete()

    def init_table(self, item_type, headers):
        # Set up model and headers for table
        model = QStandardItemModel()
        model.setHorizontalHeaderLabels(headers)
        table_view = getattr(self.ui, f"tableView_{item_type}")
        table_view.setModel(model)
        table_view.setEditTriggers(QAbstractItemView.DoubleClicked)

        # Fetch data from Firestore
        collection_ref = self.db.collection(item_type)
        listener = collection_ref.on_snapshot(
            lambda snapshot, changes, read_time: self.update_table(
                item_type, snapshot, changes, read_time
            )
        )

        # Connect dataChanged signal to update_database method
        model.dataChanged.connect(
            lambda index: self.update_in_database(item_type, index)
        )

        table_view.hideColumn(0)
        if item_type == "vozila" or item_type == "servisi":
            table_view.hideColumn(1)

        # Resize columns to stretch
        table_view.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        table_view.resizeColumnsToContents()

        # Store model and listener
        setattr(self, f"{item_type}_model", model)
        setattr(self, f"{item_type}_listener", listener)

    def update_table(self, item_type, snapshot, changes, read_time):
        model = getattr(self, f"{item_type}_model")
        for change in changes:
            if change.type.name == "ADDED":
                doc = change.document
                self.add_row(item_type, doc.id, doc.to_dict())
            elif change.type.name == "MODIFIED":
                doc = change.document
                self.update_row(item_type, doc.id, doc.to_dict())
            elif change.type.name == "REMOVED":
                self.remove_row(item_type, change.document.id)

    def add_row(self, item_type, doc_id, data):
        model = getattr(self, f"{item_type}_model")
        row = [QStandardItem(doc_id)]  # Insert document ID as the first item
        for field in FIELDS[item_type]:
            value = data.get(field, "")
            if item_type == "servisi" and field == "datum_vreme":
                datum, vreme = value.split(" ")
                value = QDateTime.fromString(
                    f"{datum} {vreme}", "yyyy-MM-dd HH:mm:ss"
                ).toString("dd.MM.yyyy. HH:mm")
            item = QStandardItem(str(value))
            item.setEditable(True)
            row.append(item)
        model.appendRow(row)

    def update_row(self, item_type, doc_id, data):
        model = getattr(self, f"{item_type}_model")
        for row in range(model.rowCount()):
            if model.item(row, 0).text() == doc_id:
                for col, field in enumerate(FIELDS[item_type]):
                    value = data.get(field, "")
                    if item_type == "servisi" and field == "datum_vreme":
                        datum, vreme = value.split(" ")
                        value = QDateTime.fromString(
                            f"{datum} {vreme}", "yyyy-MM-dd HH:mm:ss"
                        ).toString("dd.MM.yyyy. HH:mm")
                    model.item(row, col + 1).setText(str(value))

    def remove_row(self, item_type, doc_id):
        model = getattr(self, f"{item_type}_model")
        for row in range(model.rowCount()):
            if model.item(row, 0).text() == doc_id:
                model.removeRow(row)
                return

    def update_in_database(self, item_type, index):
        model = getattr(self, f"{item_type}_model")
        row = index.row()
        doc_id_item = model.item(row, 0)
        doc_id = doc_id_item.text()
        field_display_name = model.horizontalHeaderItem(index.column()).text()

        # Translate displayed name to database field name
        field_name = self.field_mapping.get(field_display_name, "").lower()
        if not field_name:
            return

        new_value = index.data(Qt.DisplayRole)

        # Retrieve previous value from the database
        doc_ref = self.db.collection(item_type).document(doc_id)
        doc = doc_ref.get()
        old_value = doc.to_dict().get(field_name)

        # Update the value in the database
        confirm = QMessageBox.question(
            self,
            "Potvrda",
            f"Da li želite da napravite izmenu?\nPrethodna vrednost: {old_value}\nNova vrednost: {new_value}",
            QMessageBox.Yes | QMessageBox.No,
        )
        if confirm == QMessageBox.Yes:
            doc_ref.update({field_name: new_value})


if __name__ == "__main__":
    # Set Serbian locale
    locale = QLocale(QLocale.Serbian, QLocale.Serbia)
    QLocale.setDefault(locale)
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
