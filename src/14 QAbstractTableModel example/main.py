from PySide6.QtWidgets import *
from PySide6.QtCore import *

headers = ["Scientist name", "Birthdate", "Contribution"]
rows = [("Newton", "1643-01-04", "Classical mechanics"),
        ("Einstein", "1879-03-14", "Relativity"),
        ("Darwin", "1809-02-12", "Evolution")]

class TableModel(QAbstractTableModel):
    def rowCount(self, parent):
        return len(rows)
    def columnCount(self, parent):
        return len(headers)
    def data(self, index, role):
        if role != Qt.ItemDataRole.DisplayRole:
            return QVariantAnimation()
        return rows[index.row()][index.column()]
    def headerData(self, section, orientation, role):
        if role != Qt.ItemDataRole.DisplayRole or orientation != Qt.Orientation.Horizontal:
            return QVariantAnimation()
        return headers[section]

app = QApplication([])
model = TableModel()
view = QTableView()
view.setModel(model)
view.show()
app.exec()