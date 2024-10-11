from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import sqlite3

# Database setup
def init_db():
    conn = sqlite3.connect('Liba.db')
    c = conn.cursor()

    # Create member table
    c.execute('''
        CREATE TABLE IF NOT EXISTS Members (
            id INTEGER PRIMARY KEY,
            first_name TEXT,
            last_name TEXT)
    ''')

    # Create book table
    c.execute('''
        CREATE TABLE IF NOT EXISTS Books (
            book_number INTEGER PRIMARY KEY,
            title TEXT,
            author TEXT,
            translator TEXT,
            summary TEXT)
    ''')

    # Create borrowing table
    c.execute('''
        CREATE TABLE IF NOT EXISTS Borrowings (
            id INTEGER PRIMARY KEY,
            member_id INTEGER,
            book_number INTEGER,
            FOREIGN KEY(member_id) REFERENCES Members(id),
            FOREIGN KEY(book_number) REFERENCES Books(book_number))
    ''')

    conn.commit()
    conn.close()


class Ui_Form(QtWidgets.QWidget):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1042, 683)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 1042, 683))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Background.jpg"))
        self.label.setObjectName("label")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(240, 30, 131, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(9)
        font.setBold(True)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_4.setStyleSheet("background-color:rgb(255, 255, 255);\n"
"border-radius:25px;\n"
"")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.display_books)
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(450, 30, 131, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(9)
        font.setBold(True)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setStyleSheet("background-color:rgb(255, 255, 255);\n"
"border-radius:25px;\n"
"")
        self.pushButton_3.clicked.connect(self.open_add_book_window)
        self.pushButton_6 = QtWidgets.QPushButton(Form)
        self.pushButton_6.setGeometry(QtCore.QRect(30, 30, 131, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(9)
        font.setBold(True)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.setStyleSheet("background-color:rgb(255, 255, 255);\n"
"border-radius:25px;\n"
"")
        self.pushButton_6.clicked.connect(self.borrow_book)
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(670, 30, 131, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(9)
        font.setBold(True)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setStyleSheet("background-color:rgb(255, 255, 255);\n"
"border-radius:25px;\n"
"")
        self.pushButton_2.clicked.connect(self.display_members)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(880, 30, 131, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(9)
        font.setBold(True)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("background-color:rgb(255, 255, 255);\n"
"border-radius:25px;\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.open_add_member_window)
        self.pushButton_7 = QtWidgets.QPushButton(Form)
        self.pushButton_7.setGeometry(QtCore.QRect(880, 590, 131, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.setStyleSheet("background-color:rgb(255, 255, 255);\n"
"border-radius:25px;\n"
"")
        self.pushButton_7.clicked.connect(self.exit_app)
        self.pushButton_8 = QtWidgets.QPushButton(Form)
        self.pushButton_8.setGeometry(QtCore.QRect(30, 130, 131, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(9)
        font.setBold(True)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_8.setStyleSheet("background-color:rgb(255, 255, 255);\n"
"border-radius:25px;\n"
"")
        self.pushButton_8.clicked.connect(self.show_borrowings)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 630, 341, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "School Library MS"))
        self.pushButton_4.setText(_translate("Form", "Display Books"))
        self.pushButton_3.setText(_translate("Form", "Add Book"))
        self.pushButton_6.setText(_translate("Form", "Borrow Book"))
        self.pushButton_2.setText(_translate("Form", "Display Members"))
        self.pushButton.setText(_translate("Form", "Add Member"))
        self.pushButton_7.setText(_translate("Form", "Exit"))
        self.pushButton_8.setText(_translate("Form", "Borrowed Books"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p><span style=\" color:#ffffff;\">Made by Mostafa Safarian 2023</span></p></body></html>"))


        init_db()

    def open_add_member_window(self):
        self.add_member_window = AddMemberWindow()
        self.add_member_window.show()

    def open_add_book_window(self):
        self.add_book_window = AddBookWindow()
        self.add_book_window.show()

    def display_members(self):
        conn = sqlite3.connect('Liba.db')
        c = conn.cursor()
        members = c.execute('SELECT * FROM Members').fetchall()
        conn.close()

        self.members_window = QtWidgets.QDialog(self)
        self.members_window.setWindowTitle("Library Members")
        self.members_window.setGeometry(100, 100, 400, 300)

        layout = QtWidgets.QVBoxLayout()
        self.members_table = QtWidgets.QTableWidget(len(members), 3)
        self.members_table.setHorizontalHeaderLabels(["ID", "First Name", "Last Name"])

        for row, member in enumerate(members):
            self.members_table.setItem(row, 0, QtWidgets.QTableWidgetItem(str(member[0])))
            self.members_table.setItem(row, 1, QtWidgets.QTableWidgetItem(member[1]))
            self.members_table.setItem(row, 2, QtWidgets.QTableWidgetItem(member[2]))

        layout.addWidget(self.members_table)

        delete_member_button = QtWidgets.QPushButton("Delete Selected Member")
        delete_member_button.clicked.connect(self.delete_member)
        layout.addWidget(delete_member_button)

        delete_all_members_button = QtWidgets.QPushButton("Delete All Members")
        delete_all_members_button.clicked.connect(self.delete_all_members)
        layout.addWidget(delete_all_members_button)

        self.members_window.setLayout(layout)
        self.members_window.exec_()

    def delete_member(self):
        selected_row = self.members_table.currentRow()
        if selected_row < 0:
            QtWidgets.QMessageBox.warning(self, "Selection Error", "Please select a member entry to delete.")
            return

        member_id = self.members_table.item(selected_row, 0).text()
        conn = sqlite3.connect('Liba.db')
        c = conn.cursor()
        c.execute('DELETE FROM Members WHERE id = ?', (member_id,))
        conn.commit()
        conn.close()
        self.members_table.removeRow(selected_row)
        QtWidgets.QMessageBox.information(self, "Success", "Member deleted successfully!")

    def delete_all_members(self):
        reply = QtWidgets.QMessageBox.question(
            self,
            'Delete All Members',
            "Are you sure you want to delete all members?",
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
            QtWidgets.QMessageBox.No)

        if reply == QtWidgets.QMessageBox.Yes:
            conn = sqlite3.connect('Liba.db')
            c = conn.cursor()
            c.execute('DELETE FROM Members')
            conn.commit()
            conn.close()

            QtWidgets.QMessageBox.information(self, "Success", "All members deleted successfully!")
            self.display_members()  # Refresh the member list

    def display_books(self):
        conn = sqlite3.connect('Liba.db')
        c = conn.cursor()
        books = c.execute('SELECT * FROM Books').fetchall()
        conn.close()

        self.books_window = QtWidgets.QDialog(self)
        self.books_window.setWindowTitle("Available Books")
        self.books_window.setGeometry(100, 100, 653, 400)

        layout = QtWidgets.QVBoxLayout()
        self.books_table = QtWidgets.QTableWidget(len(books), 5)
        self.books_table.setHorizontalHeaderLabels(["Book Number", "Title", "Author", "Translator", "Summary"])

        for row, book in enumerate(books):
            self.books_table.setItem(row, 0, QtWidgets.QTableWidgetItem(str(book[0])))
            self.books_table.setItem(row, 1, QtWidgets.QTableWidgetItem(book[1]))
            self.books_table.setItem(row, 2, QtWidgets.QTableWidgetItem(book[2]))
            self.books_table.setItem(row, 3, QtWidgets.QTableWidgetItem(book[3]))
            self.books_table.setItem(row, 4, QtWidgets.QTableWidgetItem(book[4]))

        layout.addWidget(self.books_table)

        delete_book_button = QtWidgets.QPushButton("Delete Selected Book")
        delete_book_button.clicked.connect(self.delete_book)
        layout.addWidget(delete_book_button)

        self.books_window.setLayout(layout)
        self.books_window.exec_()

    def delete_book(self):
        selected_row = self.books_table.currentRow()
        if selected_row < 0:
            QtWidgets.QMessageBox.warning(self, "Selection Error", "Please select a book entry to delete.")
            return

        book_number = self.books_table.item(selected_row, 0).text()
        conn = sqlite3.connect('Liba.db')
        c = conn.cursor()
        c.execute('DELETE FROM Books WHERE book_number = ?', (book_number,))
        conn.commit()
        conn.close()
        self.books_table.removeRow(selected_row)
        QtWidgets.QMessageBox.information(self, "Success", "Book deleted successfully!")

    def borrow_book(self):
        conn = sqlite3.connect('Liba.db')
        c = conn.cursor()
        members = c.execute('SELECT id, first_name, last_name FROM Members').fetchall()
        books = c.execute('SELECT book_number, title FROM Books').fetchall()
        conn.close()

        borrow_window = QtWidgets.QDialog(self)
        borrow_window.setWindowTitle("Borrow Book")
        borrow_window.setGeometry(100, 100, 350, 200)

        layout = QtWidgets.QVBoxLayout()

        self.member_combo = QtWidgets.QComboBox()
        self.member_combo.addItems([f"{m[1]} {m[2]} (ID: {m[0]})" for m in members])
        self.book_combo = QtWidgets.QComboBox()
        self.book_combo.addItems([f"{b[0]}: {b[1]}" for b in books])

        layout.addWidget(QtWidgets.QLabel("Select Member"))
        layout.addWidget(self.member_combo)
        layout.addWidget(QtWidgets.QLabel("Select Book"))
        layout.addWidget(self.book_combo)

        borrow_button = QtWidgets.QPushButton("Borrow Book")
        borrow_button.clicked.connect(self.process_borrow)
        layout.addWidget(borrow_button)

        borrow_window.setLayout(layout)
        borrow_window.exec_()

    def process_borrow(self):
        member_info = self.member_combo.currentText()
        book_info = self.book_combo.currentText()

        member_id = member_info.split(" (ID: ")[-1][:-1]
        book_number = book_info.split(": ")[0]

        conn = sqlite3.connect('Liba.db')
        c = conn.cursor()
        c.execute('INSERT INTO Borrowings (member_id, book_number) VALUES (?, ?)', (member_id, book_number))
        conn.commit()
        conn.close()

        QtWidgets.QMessageBox.information(self, "Success", "Book borrowed successfully!")

    def show_borrowings(self):
        conn = sqlite3.connect('Liba.db')
        c = conn.cursor()
        borrowings = c.execute('''
            SELECT Borrowings.id, Members.first_name, Members.last_name, Books.title 
            FROM Borrowings 
            JOIN Members ON Borrowings.member_id = Members.id 
            JOIN Books ON Borrowings.book_number = Books.book_number
        ''').fetchall()
        conn.close()

        self.borrowings_window = QtWidgets.QDialog(self)
        self.borrowings_window.setWindowTitle("Borrowed Books")
        self.borrowings_window.setGeometry(100, 100, 528, 300)

        layout = QtWidgets.QVBoxLayout()
        self.borrowings_table = QtWidgets.QTableWidget(len(borrowings), 4)
        self.borrowings_table.setHorizontalHeaderLabels(["ID", "First Name", "Last Name", "Book Title"])

        for row, borrow in enumerate(borrowings):
            self.borrowings_table.setItem(row, 0, QtWidgets.QTableWidgetItem(str(borrow[0])))
            self.borrowings_table.setItem(row, 1, QtWidgets.QTableWidgetItem(borrow[1]))
            self.borrowings_table.setItem(row, 2, QtWidgets.QTableWidgetItem(borrow[2]))
            self.borrowings_table.setItem(row, 3, QtWidgets.QTableWidgetItem(borrow[3]))

        layout.addWidget(self.borrowings_table)

        return_book_button = QtWidgets.QPushButton("Return Selected Book")
        return_book_button.clicked.connect(self.delete_borrowing)
        layout.addWidget(return_book_button)

        self.borrowings_window.setLayout(layout)
        self.borrowings_window.exec_()

    def delete_borrowing(self):
        selected_row = self.borrowings_table.currentRow()
        if selected_row < 0:
            QtWidgets.QMessageBox.warning(self, "Selection Error", "Please select a borrowing entry to return the book.")
            return

        borrowing_id = self.borrowings_table.item(selected_row, 0).text()
        conn = sqlite3.connect('Liba.db')
        c = conn.cursor()
        c.execute('DELETE FROM Borrowings WHERE id = ?', (borrowing_id,))
        conn.commit()
        conn.close()
        self.borrowings_table.removeRow(selected_row)
        QtWidgets.QMessageBox.information(self, "Success", "Book returned successfully!")

    def exit_app(self):
        QtWidgets.QApplication.quit()

# Separate window for adding members
class AddMemberWindow(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add Member")
        self.setGeometry(100, 100, 300, 200)

        layout = QtWidgets.QVBoxLayout()

        self.member_id_input = QtWidgets.QLineEdit()
        self.first_name_input = QtWidgets.QLineEdit()
        self.last_name_input = QtWidgets.QLineEdit()
        
        self.add_member_button = QtWidgets.QPushButton("Add Member")
        self.add_member_button.clicked.connect(self.add_member)

        layout.addWidget(QtWidgets.QLabel("Member ID"))
        layout.addWidget(self.member_id_input)
        layout.addWidget(QtWidgets.QLabel("First Name"))
        layout.addWidget(self.first_name_input)
        layout.addWidget(QtWidgets.QLabel("Last Name"))
        layout.addWidget(self.last_name_input)
        layout.addWidget(self.add_member_button)

        self.setLayout(layout)

    def add_member(self):
        conn = sqlite3.connect('Liba.db')
        c = conn.cursor()
        member_id = self.member_id_input.text()
        first_name = self.first_name_input.text()
        last_name = self.last_name_input.text()
        try:
            c.execute('INSERT INTO Members (id, first_name, last_name) VALUES (?, ?, ?)', 
                      (member_id, first_name, last_name))
            conn.commit()
            QtWidgets.QMessageBox.information(self, "Success", "Member added successfully!")
            self.close()
        except sqlite3.IntegrityError:
            QtWidgets.QMessageBox.warning(self, "Error", "Member ID must be unique.")
        finally:
            conn.close()

# Separate window for adding books
class AddBookWindow(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add Book")
        self.setGeometry(100, 100, 400, 300)

        layout = QtWidgets.QVBoxLayout()

        self.book_number_input = QtWidgets.QLineEdit()
        self.title_input = QtWidgets.QLineEdit()
        self.author_input = QtWidgets.QLineEdit()
        self.translator_input = QtWidgets.QLineEdit()
        self.summary_input = QtWidgets.QTextEdit()

        self.add_book_button = QtWidgets.QPushButton("Add Book")
        self.add_book_button.clicked.connect(self.add_book)

        layout.addWidget(QtWidgets.QLabel("Book Number"))
        layout.addWidget(self.book_number_input)
        layout.addWidget(QtWidgets.QLabel("Title"))
        layout.addWidget(self.title_input)
        layout.addWidget(QtWidgets.QLabel("Author"))
        layout.addWidget(self.author_input)
        layout.addWidget(QtWidgets.QLabel("Translator"))
        layout.addWidget(self.translator_input)
        layout.addWidget(QtWidgets.QLabel("Summary"))
        layout.addWidget(self.summary_input)
        layout.addWidget(self.add_book_button)

        self.setLayout(layout)

    def add_book(self):
        conn = sqlite3.connect('Liba.db')
        c = conn.cursor()
        book_number = self.book_number_input.text()
        title = self.title_input.text()
        author = self.author_input.text()
        translator = self.translator_input.text()
        summary = self.summary_input.toPlainText()
        try:
            c.execute('INSERT INTO Books (book_number, title, author, translator, summary) VALUES (?, ?, ?, ?, ?)', 
                      (book_number, title, author, translator, summary))
            conn.commit()
            QtWidgets.QMessageBox.information(self, "Success", "Book added successfully!")
            self.close()
        except sqlite3.IntegrityError:
            QtWidgets.QMessageBox.warning(self, "Error", "Book number must be unique.")
        finally:
            conn.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
