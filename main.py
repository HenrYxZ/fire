import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, \
    QLineEdit, QLabel, QVBoxLayout, QWidget, QHBoxLayout


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Fire Calculator")

        layout = QVBoxLayout()

        monthly_row = QHBoxLayout()
        label_monthly = QLabel("Monthly contrib: ")
        self.input_monthly = QLineEdit("2000")
        monthly_row.addWidget(label_monthly)
        monthly_row.addWidget(self.input_monthly)

        rate_row = QHBoxLayout()
        label_rate = QLabel("Rate: ")
        self.input_rate = QLineEdit("4")
        rate_row.addWidget(label_rate)
        rate_row.addWidget(self.input_rate)

        years_row = QHBoxLayout()
        label_years = QLabel("Years: ")
        self.input_years = QLineEdit("25")
        years_row.addWidget(label_years)
        years_row.addWidget(self.input_years)

        self.button = QPushButton("Calculate")
        self.button.clicked.connect(self.calculate)

        self.label = QLabel(f"${0}")

        layout.addLayout(monthly_row)
        layout.addLayout(rate_row)
        layout.addLayout(years_row)
        layout.addWidget(self.button)
        layout.addWidget(self.label)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def calculate(self):

        monthly = int(self.input_monthly.text())
        annual = 12 * monthly
        rate = float(self.input_rate.text()) / 100
        years = int(self.input_years.text())
        final = 0
        for i in range(years):
            final += annual
            final *= (1 + rate)

        final_str = "{:,.0f}".format(final)
        self.label.setText(f"${final_str}")


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.calculate()
    window.show()

    app.exec()
