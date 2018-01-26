#/bin/bash

rm -rf ./roles/vpn/vars/main.yml
rm -rf inventory

# ingest vpn conf xml file
python xmltovars.py /Users/benjaminlaplane/Downloads/vpn-e04b7aca.xml
# change path to ssh key
ansible-playbook -i inventory vpn.yml --key-file "~/.ssh/outscale_demo.rsa"