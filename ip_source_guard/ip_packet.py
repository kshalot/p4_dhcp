import sys
import scapy.all

DEFAULT_INTERFACE = 'eth0'


class IpPacketSender:
    def __init__(self, dst_mac, src_mac, dst_addr, src_addr):
        self.dst_mac = dst_mac
        self.src_mac = src_mac
        self.dst_addr = dst_addr
        self.src_addr = src_addr
    
    def send_packet(self):
        print('Sending IP packet')
        scapy.all.sendp(self._packet(), iface=DEFAULT_INTERFACE)
        print('IP packet sent successfully')

    def _packet(self):
        return self._ethernet_packet() / self._ip_packet()

    def _ethernet_packet(self):
        return scapy.all.Ether(dst=self.dst_mac, src=self.src_mac, type=0x800)

    def _ip_packet(self):
        return scapy.all.IP(dst=self.dst_addr, src=self.src_addr)


if __name__ == '__main__':
    dst_mac = sys.argv[1]
    src_mac = sys.argv[2]
    dst_addr = sys.argv[3]
    src_addr = sys.argv[4]
    mock = IpPacketSender(dst_mac, src_mac, dst_addr, src_addr)

    mock.send_packet()


