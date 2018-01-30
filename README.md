B. L. Awesome (2018)
Licence: DTFWYW

Quick project to setup a CentOS 7 machine as an IPSEC appliance
Setup and connect to an Outscale configured VPN Gateway:
Help here: https://wiki.outscale.net/display/DOCU/VPN+Connections

Works with python 2.7.10
Virtualenv is recommanded (requirements provided in the repo)

HOW TO:
- Run setup_vpn.sh from directory with the following arguments: ./setup_vpn.sh -x pathto/xml -k pathto/rsakey

TODO:
- Extensive testing of such deployment
- Better and more flexible handling of paths
- Ansible recommends using become_user: root instead of sudo: True (does not work)