#! /usr/bin/env python
#  -*- coding: utf-8 -*-
# Script by blawesom

### OBJECT
# Transform xml file to var file

import sys
from lxml import etree

xml_file = sys.argv[1]

tree = etree.parse(xml_file)
psk = tree.xpath("/vpn_connection/ipsec_tunnel/ike/pre_shared_key")[0].text
cgw_public_ip = tree.xpath("/vpn_connection/ipsec_tunnel/customer_gateway/tunnel_outside_address/ip_address")[0].text
inside_tunnel_cgw_ip = tree.xpath("/vpn_connection/ipsec_tunnel/customer_gateway/tunnel_inside_address/ip_address")[0].text
vgw_public_ip = tree.xpath("/vpn_connection/ipsec_tunnel/vpn_gateway/tunnel_outside_address/ip_address")[0].text
inside_tunnel_vgw_ip = tree.xpath("/vpn_connection/ipsec_tunnel/vpn_gateway/tunnel_inside_address/ip_address")[0].text

# write vars

with open('roles/vpn/vars/main.yml','w') as var_file:
    var_file.write('---\n')
    var_file.write('  psk: {}\n'.format(psk))
    var_file.write('  cgw_public_ip: {}\n'.format(cgw_public_ip))
    var_file.write('  inside_tunnel_cgw_ip: {}\n'.format(inside_tunnel_cgw_ip))
    var_file.write('  vgw_public_ip: {}\n'.format(vgw_public_ip))
    var_file.write('  inside_tunnel_vgw_ip: {}\n'.format(inside_tunnel_vgw_ip))

# write inventory
with open('inventory','w') as inventory:
    inventory.write('[vpn_appliance]\n')
    inventory.write('{}'.format(cgw_public_ip))