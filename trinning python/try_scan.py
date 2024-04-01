import netifaces as ni 
import socket 
import nmap
from os import name,system

def cl_sc():
    if name == "nt":
        system("cls")
    else:
        system("cls")

def get_valid_interfaces():
    get_faces = ni.interfaces()
    return get_faces

def get_ip(interface):
    ip = ni.ifaddresses(interface)[ni.AF_INET][0]['addr']
    return ip

def scan_ip(ip_address):
    scanner = nmap.PortScanner()
    scanner.scan(ip_address, arguments='-p1-65535')
    return scanner[ip_address]

def get_mask(interfaces):
    mask = ni.ifaddresses(interfaces)[ni.AF_INET][0]["mask"]
    return mask


# def get_gateways():
#         gwd = ni.get_gateways()
#         return list(gwd['default'].values())[0][0]

