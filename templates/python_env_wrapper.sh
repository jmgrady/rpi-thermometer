#! /usr/bin/env bash

cd {{ install_dir }}
source {{ virtual_env }}/bin/activate
$1
