
#________________________________________________________
                                                              #########
from scapy.all import sniff, ARP, sr1, wrpcap, rdpcap, ifaces, IP, IPv6, conf, UDP
from scapy.packet import Raw
from scapy.layers.dns import DNS, DNSQR
from collections import defaultdict
from scapy.layers.inet import IP, TCP, ICMP
from scapy.layers.inet6 import IPv6, ICMPv6EchoRequest
import ipaddress
import threading
import psutil
import dpkt
import socket
import requests
import sys
import time
import datetime
import os
import platform

print("""Porfavor de contactar con Leonardo Alfredo A.S.
por el programa de python
---
Whatsapp: (+52) 229 235 1345
""")