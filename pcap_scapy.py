from scapy.all import *
from scapy.layers.dot11 import Dot11
from scapy.layers.inet import IP


# https://scapy.readthedocs.io/en/latest/installation.html#latest-release
# pip install --pre 'scapy[basic]'
# 패킷 캡처 함수
def packet_callback(packet: scapy.layers.l2.Ether):
    # print(packet.summary())
    # print(packet.__all__)
    # print(dir(packet))
    # print(packet.getlayer)
    print(packet.show())
    print(packet.show())
    # print(f'{packet.type} {packet.src} -> {packet.dst}')
    # print(f'{packet.type} {packet} -> {packet.dst}')
    # print(f'{packet.haslayer}')

    if packet.haslayer(Dot11) and packet.type == 0 and packet.subtype == 8:
        # do your stuff here
        print(packet.show())


ls(IP, verbose=True)

# 패킷 캡처 설정
sniff(
    prn=packet_callback,
    # filter="tcp",
    count=3
)

# def packet_handler(packet) :
#     print(packet)
#     # if packet has 802.11 layer, and type of packet is Data frame
#     if packet.haslayer(Dot11) and packet.type == 0 and packet.subtype == 8:
#             # do your stuff here
#             print(packet.show())
#
#
# sniff(prn=packet_handler)
