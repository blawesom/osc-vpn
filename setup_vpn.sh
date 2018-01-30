#/bin/bash

# Use the following options: -x pathto/vpn.xml -k pathto/key.rsa

# Get arguments
xml=''
key=''

while getopts 'x:k:' flag; do
  case "${flag}" in
    x) xml="${OPTARG}" ;;
    k) key="${OPTARG}" ;;
    *) error "Unexpected option ${flag}" ;;
  esac
done

# Clean previous deployments
rm -rf ./roles/vpn/vars/main.yml
rm -rf inventory

# Generate vars file and play book
python xmltovars.py $xml
ansible-playbook -i inventory vpn.yml --key-file $key
