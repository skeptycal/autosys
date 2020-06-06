#!/usr/bin/env python3
# !---------------------------------------------- Imports
if True:  # ! -- System Imports
    import platform
    import requests
    from subprocess import check_output
    import sys

if True:  # ! -- Specific System Imports
    # from base64 import b64decode, b64encode
    # from pathlib import Path
    # from typing import Dict, List
    # try:
    #     import ujson as json
    # except:
    #     import json
    pass
if True:  # ! -- Package Imports
    from autosys.utils import dbprint, read, NL


class DnsError(Exception):
    pass


def is_valid_ipv4_address(address):
    import socket

    try:
        socket.inet_pton(socket.AF_INET, address)
    except AttributeError:  # no inet_pton here, sorry
        try:
            socket.inet_aton(address)
        except socket.error:
            return False
        return address.count(".") == 3
    except socket.error:  # not a valid address
        return False

    return True


def get_unix_dns_ips():
    dns_ips = []
    # macOS /etc/resolv.conf is mapped from /var/run/resolv.conf
    # -rw-r--r-- 1 root daemon 484 Apr 14 07:10 resolv.conf
    with open("/etc/resolv.conf") as fp:
        for cnt, line in enumerate(fp):
            columns = line.split()
            if columns[0] == "nameserver":
                ip = columns[1:][0]
                if is_valid_ipv4_address(ip):
                    dns_ips.append(ip)
    return dns_ips


def get_windows_dns_ips():
    output = check_output(["ipconfig", "-all"])
    ipconfig_all_list = output.split("\n")

    dns_ips = []
    for i in range(0, len(ipconfig_all_list)):
        if "DNS Servers" in ipconfig_all_list[i]:
            # get the first dns server ip
            first_ip = ipconfig_all_list[i].split(":")[1].strip()
            if not is_valid_ipv4_address(first_ip):
                continue
            dns_ips.append(first_ip)
            # get all other dns server ips if they exist
            k = i + 1
            while (
                k < len(ipconfig_all_list) and ":" not in ipconfig_all_list[k]
            ):
                ip = ipconfig_all_list[k].strip()
                if is_valid_ipv4_address(ip):
                    dns_ips.append(ip)
                k += 1
            # at this point we're done
            break
    return dns_ips


def main():
    if platform.system() == "Windows":
        dns_ips = get_windows_dns_ips()
    elif platform.system() == "Darwin":
        dns_ips = get_unix_dns_ips()
    elif platform.system() == "Linux":
        dns_ips = get_unix_dns_ips()
    else:
        raise DnsError(f"unsupported platform: {platform.system()}")
    return dns_ips[0]  # return 1st dns entry


if __name__ == "__main__":
    main()
""" Tested with default macbookpro settings:

wifi 2g HughesNet ['192.168.0.1', '192.168.0.1']
wifi 5g HughesNet ['192.168.0.1', '192.168.0.1']

"""
