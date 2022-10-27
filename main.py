import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, \
    QLineEdit, QLabel, QWidget, QVBoxLayout, QFormLayout


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Fire Calculator")

        layout = QVBoxLayout()
        form_box = QFormLayout()

        label_monthly = QLabel("Monthly contrib: ")
        self.input_monthly = QLineEdit("2000")
        self.input_monthly.returnPressed.connect(self.calculate)
        form_box.addRow(label_monthly, self.input_monthly)

        label_rate = QLabel("Rate: ")
        self.input_rate = QLineEdit("5")
        self.input_rate.returnPressed.connect(self.calculate)
        form_box.addRow(label_rate, self.input_rate)

        label_years = QLabel("Years: ")
        self.input_years = QLineEdit("25")
        self.input_years.returnPressed.connect(self.calculate)
        form_box.addRow(label_years, self.input_years)

        self.button = QPushButton("Calculate")
        self.button.clicked.connect(self.calculate)
        form_box.addRow(self.button)

        self.total_label = QLabel(f"${0}")
        self.total_label.setStyleSheet("font-weight: bold")
        self.total_no_interest_label = QLabel(f"${0}")
        self.extra_label = QLabel(f"${0}")

        layout.addLayout(form_box)
        layout.addWidget(self.total_label)
        layout.addWidget(self.total_no_interest_label)
        layout.addWidget(self.extra_label)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def calculate(self):
        monthly = int(self.input_monthly.text())
        annual = 12 * monthly
        years = int(self.input_years.text())
        annual_rate = float(self.input_rate.text()) / 100

        # formula from https://www.wallstreetiswaiting.com/running-the-numbers-1/calculating-interest-recurring-payments/
        final = annual * ((1 + annual_rate) ** years - 1) / annual_rate
        self.total_label.setText("Total: ${:,.0f}".format(final))

        # Calculate total with no interest to compare
        total_no_interest = annual * years
        self.total_no_interest_label.setText(
            "Total without interest: ${:,.0f}".format(total_no_interest)
        )

        # Compound interest
        extra = final - total_no_interest
        self.extra_label.setText(
            "Obtained from interest: ${:,.0f}".format(extra)
        )


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.calculate()
    window.show()

    app.exec()
