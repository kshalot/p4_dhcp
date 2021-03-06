import sys
import time
import scapy.all

DEFAULT_INTERFACE = 'eth0'


class DHCPOfferSender:
    def __init__(self, destination_mac, destination_address):
        self.destination_mac = destination_mac
        self.source_mac = scapy.all.get_if_hwaddr(DEFAULT_INTERFACE)
        self.destination_address = destination_address
        self.source_address = scapy.all.get_if_addr(DEFAULT_INTERFACE)

        print(self.source_mac)
    
    def send_dhcp_offer(self):
        print('Sending DHCP Offer')
        scapy.all.sendp(self._packet(), iface=DEFAULT_INTERFACE)
        print('DHCP Offer sent successfully')

    def _packet(self):
        return self._ethernet_packet() / self._ip_packet() / self._udp_packet() / self._bootp_packet() / self._dhcp_packet()

    def _ethernet_packet(self):
        return scapy.all.Ether(dst=self.destination_mac, src=self.source_mac, type=0x800)

    def _ip_packet(self):
        return scapy.all.IP(dst=self.destination_address, src=self.source_address)

    def _udp_packet(self):
        return scapy.all.UDP(sport=67, dport=68)

    def _bootp_packet(self):
        print(self.source_mac)
        return scapy.all.BOOTP(chaddr=self.source_mac)

    def _dhcp_packet(self):
        return scapy.all.DHCP(options=[("message-type", "offer"), "end"])


if __name__ == '__main__':
    request_delay_in_seconds = int(sys.argv[1])
    destination_mac = sys.argv[2]
    destination_address = sys.argv[3]
    mock = DHCPOfferSender(destination_mac, destination_address)

    time.sleep(request_delay_in_seconds)
    mock.send_dhcp_offer()
