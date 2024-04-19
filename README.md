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
   cd hw-services
   ./new-venv
   ```
   A reboot will probably be required when complete.

4. Synchronized the venv with the pinned drivers:

   ```console
   ./update-venv
   ```

   If `requirements.in` has been modified or to update the versions of the python dependencies, run `update-venv` with the `build` option. This will
    first update `requirements.txt` with the new module requirements.

## Setup Services

### Display IP

To setup the _Display IP_ service, run:

```console
ansible-playbook install-display-ip.yaml --limit <IP of RPi>, -K
```

### Temperature Logger

To setup the _Temperature Logger_ service, run:

```console
ansible-playbook install-temp-logger.yaml --limit <IP of RPi>, -K
```

### Notes

1. There must be a comma after the IP address of the Raspberry Pi so that Ansible does not interpret the IP address as a hostname.
