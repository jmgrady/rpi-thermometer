# Raspberry Pi Service Collection

## Setup

### Python Virtual Environment

The services need to run in a virtual environment on the Raspberry Pi.

#### Create a Virtual Environment

1. Install the required packages from `apt`:

   ```console
   sudo apt install python3-venv python3-pip
   sudo apt install --upgrade python3-setuptools
   ```

2. Clone the repo from github:

   ```console
   git clone https://github.com/jmgrady/rpi-setup
   ```

3. Create the virtual environment and install CircuitPython:

   ```console
   cd rpi-thermometer
   ./new-venv
   ```

   A reboot will probably be required when complete.

4. Synchronize the venv with the pinned drivers:

   ```console
   ./update-venv
   ```

   If `requirements.in` has been modified or to update the versions of the python dependencies, run `update-venv` with the `build` option. This will
   first update `requirements.txt` with the new module requirements.

## Installation

To install the temperature logger and supporting software, run:

```console
ansible-playbook -i hosts.yml install.yaml --limit <IP of RPi>,
```

### Notes

1. There must be a comma after the IP address of the Raspberry Pi so that Ansible does not interpret the IP address as a hostname. Alternately, edit `hosts.yml` to include the hostname of the target.
2. You may want to create your own `hosts.yml` file or modify the existing file to list the devices you will manage.
3. If your Raspberry Pi requires a password for `sudo`, add the `-K` option to the command above.

## Updating the Application

The UI Layout was created using _QtCreator_. Use _QtCreator_ to update the basic forms and widgets in the UI. If changes are made to any of the `.ui` files, update the UI Python files as follows:

```console
cd <project_dir>
./generate_ui.sh
```

Now the project can be installed on a target system.
