# Raspberry Pi Thermometer

## Introduction

This project implements a thermometer to measure and log temperature. The initial implementation uses a graphical user interface on a display such as the Official Raspberry Pi 7" touchscreen. It measures temperature using an [Adafruit RTD Sensor Amplifier](https://www.adafruit.com/product/3328) to read a PT100 RTD.

## Custom Raspberry Pi Hat

This software uses a custom Raspberry Pi Hat to connect the temperature sensor to the Raspberry Pi. The schematic for the hat is documented using [KiCAD](https://www.kicad.org/); it is available for Linux, MacOS, and Windows. The KiCAD files are in a sub-folder named `Temperature Logger Hat`. Note that the circuit diagram is for an older RTD Sensor amplifier board; it has a different connector but uses the same amplifier chip.

## Installing the Environment

1. Clone the project repository from github:

   ```console
   git clone https://github.com/jmgrady/rpi-thermometer
   ```

2. Create a Python virtual environment

   1. Install the required packages from `apt`:

      ```console
      sudo apt install python3-venv python3-pip
      sudo apt install --upgrade python3-setuptools
      ```

   2. Create the virtual environment and install CircuitPython:

      ```console
      cd rpi-thermometer
      ```

      A reboot will probably be required when complete.

   3. Synchronize the venv with the pinned drivers:

      ```console
      ./update-venv
      ```

      If `requirements.in` has been modified or to update the versions of the python dependencies, run `update-venv` with the `build` option. This will
      first update `requirements.txt` with the new module requirements.

## Run The Software Locally

```console
cd rpi-thermometer
. venv/bin/activate
cd app
./main.py
```

## Install the Software on a Raspberry Pi

There are two ways to install the software on a Raspberry Pi. The first method is to clone the repo on the host machine and use ansible to install the software on the Raspberry Pi. This is preferred if you plan to extend the project. The second method is to clone the repo to the Raspberry Pi and use ansible to install the software on `localhost`.

### Installing from a Host Machine

1. edit `hosts.yml` to include your target system(s).

2. Run

```console
. venv/bin/activate
ansible-playbook -i hosts.yml install-env.yaml --limit <hostname_of_rpi>
ansible-playbook -i hosts.yml install.yaml --limit <hostname_of_rpi>
```

### Installing on `localhost`

1. `ssh` to your Raspberry Pi or from the console install the environment as described in [Installing the Environment](#installing-the-environment)

2. Run

```console
. venv/bin/activate
ansible-playbook -i hosts.yml install-env.yaml --limit localhost
ansible-playbook -i hosts.yml install.yaml --limit localhost
```

### Notes

1. If your Raspberry Pi requires a password for `sudo`, add the `-K` option to the command above.

## Updating the Application

The UI Layout was created using _QtCreator_. Use _QtCreator_ to update the basic forms and widgets in the UI. If changes are made to any of the `.ui` files, update the UI Python files as follows:

```console
cd <project_dir>
. venv/bin/activate
./generate_ui.sh
```

Now the project can be installed on a target system.
