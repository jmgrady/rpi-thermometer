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
   cd rpi-setup
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
ansible-playbook install.yaml --limit <IP of RPi>,
```

### Notes

1. There must be a comma after the IP address of the Raspberry Pi so that Ansible does not interpret the IP address as a hostname. Alternately, edit `hosts.yml` to include the hostname of the target.
2. If your Raspberry Pi requires a password for `sudo`, add the `-K` option to the command above.
