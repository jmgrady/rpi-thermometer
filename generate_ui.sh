#! /usr/bin/env bash

# Generate UI code using 'pyside6-uic' and add typing annotations

# cd to directory with this script
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
cd ${SCRIPT_DIR}

# activate the Python virtual environment
. venv/bin/activate

# Generate the Python UI code
cd app/ui
ui_file=mainwindow.ui
py_file=ui_mainwindow.py
pyside6-uic $ui_file -o $py_file

for rc_file in *.qrc; do
    rc_name=${rc_file%.qrc}
    pyside6-rcc $rc_file -o ${rc_name}_rc.py
    sed -i "/^# WARNING!/a \# type: ignore" ${rc_name}_rc.py
    sed -i "/^# WARNING!/a \# flake8: noqa" ${rc_name}_rc.py
    sed -i "/^# WARNING!/a \# fmt: off" ${rc_name}_rc.py
    sed -i "/^# WARNING!/a \# isort: skip_file" ${rc_name}_rc.py
    sed -i "s/^import ${rc_name}_rc/import ui.${rc_name}_rc/" $py_file
    
done
               
# Add missing typing information
# Currently the only missing annotations are function arguments that are QMainWindow
# and a missing return type (None).
sed -i "s/MainWindow):/MainWindow: QMainWindow) -> None:/" $py_file
