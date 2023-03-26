from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QLineEdit,
    QLabel, QVBoxLayout, QCheckBox, QGroupBox,
    QMessageBox, QMainWindow, QFileDialog, QListWidget, QRadioButton
)
from PyQt5.QtCore import QEventLoop
from PyQt5.QtGui import QFont
import os
import sys


def creation_list():
    # Create the main window
    display = QMainWindow()
    display.setWindowTitle('List Creation')
    display.setFont(QFont('Courier', 12))
    display.resize(300, 300)

    # Create the widgets
    label = QLabel('NAME THE LIST')
    name_file = QLineEdit()
    name_file.setPlaceholderText('ENTER THE NAME OF THE LIST')
    label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
    button = QPushButton('Create')

    # Open a new list
    def open_new_list(name_file):
        # Create the main window
        display = QMainWindow()
        display.setWindowTitle(f'To-Do List: {name_file.text()}')
        display.setFont(QFont('Courier', 13))
        display.resize(300, 300)

        # Create the widgets
        label = QLabel(f'TO-DO LIST: {name_file.text()}')
        name_task = QLineEdit()
        name_task.setPlaceholderText('ENTER A NEW TASK')
        label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        button = QPushButton('Create Task')
        delete_button = QPushButton('Delete Task')
        checkbox_group = QGroupBox('Tasks')
        checkbox_layout = QVBoxLayout()
        save_button = QPushButton('Save List')
        checkbox_group.setLayout(checkbox_layout)

        # Add the delete button functionality
        def delete_recent_task():
            for i in reversed(range(checkbox_layout.count())):
                widget = checkbox_layout.itemAt(i).widget()
                if isinstance(widget, QCheckBox) and widget.isChecked():
                    widget.setParent(None)
                    widget.deleteLater()

        # Save the list to a file
        def save_list():
            file_name = f'{name_file.text()}.txt'
            # Write the list contents to the selected file
            if file_name:
                with open(file_name, 'w') as file:
                    for i in range(checkbox_layout.count()):
                        item = checkbox_layout.itemAt(i).widget()
                        file.write(f'{i + 1}: {item.text()}\n')
                path = os.path.abspath(file_name)  # get absolute path of file
                QMessageBox.information(None, 'Success', f'List saved in the path: {path}')
                QMessageBox.information(None, 'Success', 'Re-Run the program to see the changes')
                display.exec_(sys.argv)

        save_button.clicked.connect(save_list)
        delete_button.clicked.connect(delete_recent_task)

        # Create a new task
        def create_task():
            task_name = name_task.text()
            if task_name:
                task_checkbox = QCheckBox(task_name)
                checkbox_layout.addWidget(task_checkbox)
                name_task.clear()
            else:
                QMessageBox.warning(display, 'Warning', 'Please enter a task name')

        # Connect the "Add Task" button and the QLineEdit returnPressed signal to the create_task function
        button.clicked.connect(create_task)
        name_task.returnPressed.connect(create_task)

        # Create the layout and add widgets
        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(name_task)
        layout.addWidget(button)
        layout.addWidget(delete_button)
        layout.addWidget(checkbox_group)
        layout.addWidget(save_button)
        layout.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        display.setLayout(layout)

        # Create a central widget, set the layout, and set it to the main window
        central_widget = QWidget()
        central_widget.setLayout(layout)
        display.setCentralWidget(central_widget)

        # Show the window
        display.show()

        # Start an event loop to keep the window open
        loop = QEventLoop()
        while display.isVisible():
            loop.processEvents()

        # Clean up the event loop
        loop.deleteLater()

    def create_list():
        if name_file.text() == '':
            QMessageBox.warning(display, 'Warning', 'Please enter a list name')
        else:
            QMessageBox.information(display, 'Success', 'list created')
            display.close()
            open_new_list(name_file)

    button.clicked.connect(create_list)

    # Create the layout and add widgets
    layout = QVBoxLayout()
    layout.addWidget(label)
    layout.addWidget(name_file)
    layout.addWidget(button)

    layout.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
    display.setLayout(layout)

    # Create a central widget, set the layout, and set it to the main window
    central_widget = QWidget()
    central_widget.setLayout(layout)
    display.setCentralWidget(central_widget)

    # Show the window
    display.show()

    # Start an event loop to keep the window open
    loop = QEventLoop()
    while display.isVisible():
        loop.processEvents()

    # Clean up the event loop
    loop.deleteLater()

    # Create the layout and add widgets
    layout = QVBoxLayout()
    layout.addWidget(label)
    layout.addWidget(button)

    layout.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
    display.setLayout(layout)

    # Create a central widget, set the layout, and set it to the main window
    central_widget = QWidget()
    central_widget.setLayout(layout)
    display.setCentralWidget(central_widget)

    # Show the window
    display.show()

    # Start an event loop to keep the window open
    loop = QEventLoop()
    while display.isVisible():
        loop.processEvents()

    # Clean up the event loop
    loop.deleteLater()


def opening():
    for label in my_files:
        if label.isChecked():
            os.system(f'notepad.exe {label.text()}')
            break


# Initialize the application
app = QApplication([])
display = QWidget()
display.resize(300, 300)
display.setWindowTitle('To-Do List: To-Do List: Made by @SteliosMisk #2023')

# Making the program
title = QLabel('To-Do List: Made by @SteliosMisk #2023')
create_file = QPushButton('Create New List')
open_file = QPushButton('Open List')

group_box = QGroupBox("MY SAVED LISTS")
group_box_layout = QVBoxLayout()
group_box.setLayout(group_box_layout)
listdirs = os.path.dirname(os.path.abspath(__file__))
file_names = os.listdir(listdirs)

my_files = []
for file_name in file_names:
    if os.path.splitext(file_name)[1] == '.txt':
        label = QRadioButton(os.path.basename(file_name))
        group_box_layout.addWidget(label)
        label.setFont(QFont('Courier', 12))
        my_files.append(label)

create_file.clicked.connect(creation_list)
open_file.clicked.connect(opening)

layout = QVBoxLayout()
layout.addWidget(title)
layout.addWidget(create_file)
layout.addWidget(open_file)
layout.addWidget(group_box)

layout.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
display.setLayout(layout)

# Events
display.show()
app.exec_()
