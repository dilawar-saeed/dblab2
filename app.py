from PyQt6 import QtWidgets, uic
from PyQt6.QtCore import Qt
import sys

books = [
    ["0201144719 9780201144710", "An introduction to database systems",
        "Database", "Reference Book", "True"],
    ["0805301453 9780805301458", "Fundamentals of database systems",
        "Database", "Reference Book", "False"],
    ["1571690867 9781571690869", "Object oriented programming in Java",
        "OOP", "Text Book", "False"],
    ["1842652478 9781842652473", "Object oriented programming using C++",
        "OOP", "Text Book", "False"],
    ["0070522618 9780070522619", "Artificial intelligence", "AI", "Journal", "False"],
    ["0865760047 9780865760042", "The Handbook of artificial intelligence",
        "AI", "Journal", "False"],
]


class UI(QtWidgets.QMainWindow):
    def __init__(self):
        # Call the inherited classes __init__ method
        super(UI, self).__init__()
        # Load the .ui file
        uic.loadUi('Lab02.ui', self)

        self.filtered_books = books
        self.categories()

        self.booksTableWidget.setRowCount(len(books))

        for i in range(len(books)):
            for j in range(5):
                item = QtWidgets.QTableWidgetItem(books[i][j])
                # Make the items non-editable
                item.setFlags(Qt.ItemFlag.ItemIsEnabled |
                              Qt.ItemFlag.ItemIsSelectable)
                self.booksTableWidget.setItem(i, j, item)

        # Connect the search function with the search button.
        self.searchbutton.clicked.connect(self.search)
        # Connect the view function with the view button.
        self.viewbutton.clicked.connect(self.view)
        # Connect the delete function with the delete button.
        self.deletebutton.clicked.connect(self.delete)
        # Connect the close function with the close button.
        self.closebutton.clicked.connect(self.close_form)

    def categories(self):
        categories = ["Database", "OOP", "AI"]
        self.category_input.addItems(categories)

    def search(self):
        category = self.category_input.currentText()
        title = self.title_input.text()
        issued = self.issued_checkbox.isChecked()

        book_type = None
        if self.reference_input.isChecked():
            book_type = "Reference Book"
        elif self.textbook_input.isChecked():
            book_type = "Text Book"
        elif self.journal_input.isChecked():
            book_type = "Journal"

        self.filtered_books = []
        for book in books:
            if (not title or title.lower() in book[1].lower()) and \
                (not category or book[2] == category) and \
                (not book_type or book[3] == book_type) and \
                    (not issued or (issued and book[4] == "True")):
                self.filtered_books.append(book)

        self.refresh_table()

    def view(self):
        selected_row = self.booksTableWidget.currentRow()
        if selected_row >= 0:
            book_details = books[selected_row]
            self.view_book_window = ViewBook(book_details)
            self.view_book_window.show()

    def refresh_table(self):
        self.booksTableWidget.setRowCount(len(self.filtered_books))
        for i, book in enumerate(self.filtered_books):
            for j in range(5):
                item = QtWidgets.QTableWidgetItem(book[j])
                item.setFlags(Qt.ItemFlag.ItemIsEnabled |
                              Qt.ItemFlag.ItemIsSelectable)
                self.booksTableWidget.setItem(i, j, item)

    def delete(self):
        selected_row = self.booksTableWidget.currentRow()
        if selected_row >= 0:
            confirm = QtWidgets.QMessageBox.question(self, 'Confirm Deletion',
                                                     'Do you want to delete this book?',
                                                     QtWidgets.QMessageBox.StandardButton.Yes |
                                                     QtWidgets.QMessageBox.StandardButton.No)
            if confirm == QtWidgets.QMessageBox.StandardButton.Yes:
                del self.filtered_books[selected_row]
                self.refresh_table()

    def close_form(self):
        self.close()


class ViewBook(QtWidgets.QMainWindow):
    def __init__(self, book):
        super(ViewBook, self).__init__()
        uic.loadUi('ViewBook.ui', self)
        self.setWindowTitle("View Book")
        self.setGeometry(100, 100, 400, 300)

        self.viewisbn.setReadOnly(True)
        self.viewtitle.setReadOnly(True)
        self.viewcategory.setReadOnly(True)
        self.viewtypebox.setEnabled(False)
        self.viewissued.setEnabled(False)

        self.viewisbn.setText(book[0])
        self.viewtitle.setText(book[1])
        self.viewcategory.setText(book[2])

        if book[3] == "Reference Book":
            self.viewreference.setChecked(True)
        elif book[3] == "Text Book":
            self.viewtextbook.setChecked(True)
        else:
            self.viewjournal.setChecked(True)

        if book[4] == "True":
            self.viewissued.setChecked(True)


# Create an instance of QtWidgets.QApplication
app = QtWidgets.QApplication(sys.argv)
window = UI()  # Create an instance of our
window.show()
app.exec()  # Start the application
