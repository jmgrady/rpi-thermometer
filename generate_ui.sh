#! /usr/bin/env bash

# Generate UI code using 'pyside6-uic' and add typing annotations

# cd to directory with this script
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
cd ${SCRIPT_DIR}

# activate the Python virtual environment
. venv/bin/activate

# Generate the Python UI code
cd app/ui
py_file=ui_mainwindow.py
dlg_file=ui_settingsdialog.py
prog_file=ui_saveprogressdialog.py
pyside6-uic mainwindow.ui -o $py_file
pyside6-uic settings_dialog.ui -o $dlg_file
pyside6-uic saveprogressdialog.ui -o $prog_file

for rc_file in *.qrc; do
    rc_name=${rc_file%.qrc}
    pyside6-rcc $rc_file -o ${rc_name}_rc.py
    sed -i "/^# WARNING!/a \# type: ignore" ${rc_name}_rc.py
    sed -i "/^# WARNING!/a \# flake8: noqa" ${rc_name}_rc.py
    sed -i "/^# WARNING!/a \# fmt: off" ${rc_name}_rc.py
    sed -i "/^# WARNING!/a \# isort: skip_file" ${rc_name}_rc.py
    for src_file in $py_file $dlg_file ; do
        sed -i "s/^import ${rc_name}_rc/import ui.${rc_name}_rc/" $src_file
    done
done
               
# Add missing typing information
# Currently the only missing annotations are function arguments that are QMainWindow
# and a missing return type (None).
sed -i "s/MainWindow):/MainWindow: QMainWindow) -> None:/" $py_file
sed -i "s/SettingsDialog):/SettingsDialog: QDialog) -> None:/" $dlg_file
sed -i "s/SaveProgressDialog):/SaveProgressDialog: QDialog) -> None:/" $prog_file
