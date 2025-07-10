# Raspberry Pi Service Collection

## Setup

1. Install _Ansible_ - either as an application or as a Python module in a virtual environment.

2. Clone the repo from github:

   ```console
   git clone https://github.com/jmgrady/rpi-setup
   ```

3. Install the Python services on the Raspberry Pi

   ```console
   cd rpi-setup
   ansible-playbook -i hosts.yml playbook.yaml --limit <rpi_hostname>
   ```

   where `<rpi_hostname>` it the hostname of the Raspberry Pi where the services will be installed. The hostname must be listed in the `hosts.yml` file. A different `hosts.yml` file can be used if needed.

   It will probably be necessary to reboot the Raspberry Pi when complete.

## Using the Services

There are two services that are created:

- temperature-logger

  Measures temperature from a P100 RTD over the SPI interface and displays it on an LCD display

- display-ip-addr

  Displays the Raspberry Pi's IP address on the LCD display

They are not `enabled` so they do not start when the Raspberry Pi boots up.

See the man page for `systemctl` for information on how to start/stop services.
