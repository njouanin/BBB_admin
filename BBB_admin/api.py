import bottle
import os
import netifaces
import socket
import sys

system_app = bottle.Bottle(catchall=False)

@system_app.route('/uname')
def os_uname():
    uname = os.uname()
    info = {'sysname': uname.sysname, 'nodename': uname.nodename, 'release': uname.release, 'version':uname.version, 'machine': uname.machine}
    return info

@system_app.route('/network')
def net_interfaces():
    list_interfaces = []
    net_ifaces = netifaces.interfaces()
    for interface in net_ifaces:
        dict_interface = {'name': interface}
        addrs = netifaces.ifaddresses(interface)
        list_addresses = []
        try :
            addrs_ipv4 = addrs[socket.AF_INET]
            for addr in addrs_ipv4:
                d = {'protocol': 'ipv4'}
                d.update(addr)
                list_addresses.append(d)
        except Exception as e:
            pass
        try :
            addrs_ipv6 = addrs[socket.AF_INET6]
            for addr in addrs_ipv6:
                d = {'protocol': 'ipv6'}
                d.update(addr)
                list_addresses.append(d)
        except Exception as e:
            pass
        try :
            addrs_mac = addrs[socket.AF_LINK]
            for addr in addrs_mac:
                d = {'protocol': 'mac'}
                d.update(addr)
                list_addresses.append(d)
        except Exception as e:
            pass
        dict_interface['addresses'] = list_addresses
        list_interfaces.append(dict_interface)
    return {'interfaces': list_interfaces }