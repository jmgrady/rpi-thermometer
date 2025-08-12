#! /usr/bin/env bash

cd {{ rpi_services_dir }}
source {{ virtual_env }}/bin/activate
$1
