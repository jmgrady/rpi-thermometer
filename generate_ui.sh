#! /usr/bin/env bash

# Generate UI code using 'pyside6-uic' and add typing annotations

# cd to directory with this script
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
cd ${SCRIPT_DIR}

# activate the Python virtual environment
. venv/bin/activate

# Generate the Python UI code
cd app/ui
ui_file=form.ui
py_file=ui_mainwindow.py
pyside6-uic $ui_file -o $py_file

# Add missing typing information
# Currently the only missing annotations are function arguments that are QMainWindow
# and a missing return type (None).
sed -i "s/MainWindow):/MainWindow: QMainWindow) -> None:/" $py_file
