from PySide6.QtWidgets import *
from PySide6.QtCore import QStringListModel

app = QApplication([])
model = QStringListModel([
    "An element", "Another element", "Yay! Another one."
])
view = QListView()
view.setModel(model)
view.show()
app.exec()