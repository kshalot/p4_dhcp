# Implementacja DHCP Snoopingu

## Wstęp

DHCP Snooping jest metodą filtracji pewnych typów ruchu DHCP na podstanie konfiguracji przełącznika. Pozwala na zwalczenie ataków typu man-in-the-middle. Prosty schemat takiego ataku to:

1. Atakujący podłącza sie do sieci i udając serwer DHCP nasłuchuje na przychodzące wiadomości broadcast od klientów chcących zdobyć adres IP
2. Klient wysyła zapytanie z prośbą o przydzielenie adresu IP
3. Atakujący odsyła mu lease ze spreparowaną konfiguracją (np. z adresem bramy domyślnej ustawionym na adres atakującego)
4. Klient odbiera lease i zaczyna go używać

DHCP Snooping polega na rozróżnieniu pomiędzy portami zaufanymi i niezaufanymi:
- na port niezaufany mogą przyjść jedynie wiadomości typu DHCP Request i DHCP Discover (port kliencki). Pozostałe typy DHCP (Offer i ACK) są odrzucane. Nie da się więc wysłać odpowiedzi z konfiguracją na zapytanie klienta.
- port zaufany przyjmuje dowolne wiadomości DHCP

Więcej szczegółów znajduje się w materiałach:
- https://www.computernetworkingnotes.com/ccna-study-guide/how-dhcp-snooping-works-explained.html
- https://www.computernetworkingnotes.com/ccna-study-guide/configure-dhcp-snooping-on-cisco-switches.html

## Opis skryptów

W ramach laboratorium udostępnione są dwa skrypty:

- good_dhcp.sh - zaufane źródło ramek DHCP
- evil_dhcp.sh - niezaufane źródło ramek DHCP

Działają na prostej zasadzie - po uruchomieniu wysyłają spreparowany pakiet DHCP Offer. Skrypty są parametryzowane poprzez:
- timeout
- docelowy adres MAC
- docelowy adres IP (będący "ofertą" serwera dla klienta)

Wszystkie parametry są juz uzupełnione i przygotowane na potrzeby laboratorium.

## Cel laboratorium

Celem laboratorium jest symulacja mechanizmu DHCP Snooping poprzez odflitrowanie ruchu DHCP pochodzącego z niezaufanego źródła - przychodzącego na port, na którym wiemy, że nie znajduje się serwer DHCP.

## Uruchomienie niekompletnego kodu
 
1. W konsoli wpisz aby uruchomić przykład:
 
```sh
$ make
```
 
2. Powinna być widoczna konsola minineta. Sprawdź, czy działa ping:
 
```sh
mininet> pingall
```
 
Wszystkie hosty powinny być w stanie się komunikować
 
3. Uruchom tcpdump na `h2`:
 
```sh
mininet> h2 tcpdump  -i eth0 udp port 67 and port 68 -vvv &
```
 
Aby zapobiec niepotrzebnemu szumowi tcpdump pokaże informacje tylko o ruchu DHCP.
 
4. Wyślij pakiety DHCP offer przy pomocy przygotowanych skryptów:
 
```sh
mininet> h1 ./good_dhcp.sh &
mininet> h3 ./evil_dhcp.sh &
```
 
5. Zweryfikuj, że h2 otrzymał 2 oferty, z czego pierwsza jest tą "złą".
 
Powinno to wyglądać następująco:
 
```
10:08:21.053284 IP (tos 0x0, ttl 64, id 1, offset 0, flags [none], proto UDP (17), length 272)
    10.0.0.3.bootps > 10.6.6.6.bootpc: [udp sum ok] BOOTP/DHCP, Request from 30:38:3a:30:30:3a (oui Unknown), length 244, Flags [none] (0x0000)
          Client-Ethernet-Address 30:38:3a:30:30:3a (oui Unknown)
          Vendor-rfc1048 Extensions
            Magic Cookie 0x63825363
            DHCP-Message Option 53, length 1: Offer
            END Option 255, length 0
10:08:25.139686 IP (tos 0x0, ttl 64, id 1, offset 0, flags [none], proto UDP (17), length 272)
    10.0.0.1.bootps > 10.0.0.22.bootpc: [udp sum ok] BOOTP/DHCP, Request from 30:38:3a:30:30:3a (oui Unknown), length 244, Flags [none] (0x0000)
          Client-Ethernet-Address 30:38:3a:30:30:3a (oui Unknown)
          Vendor-rfc1048 Extensions
            Magic Cookie 0x63825363
            DHCP-Message Option 53, length 1: Offer
            END Option 255, length 0
 
2 packets captured
2 packets received by filter
0 packets dropped by kernel
 
```
 
Po wykonaniu ćwiczenia ruch inny niż DHCP powinien działać tak samo, natomiast w wyniku tcpdump powinien być widoczny tylko pakiet od h1.

## Przebieg laboratorium

1. W pliku `topo/s1-runtime.json` zdefiniuj tabelę przechowującą zaufane porty DHCP (zaufany serwer DHCP znajduje się na porcie 1)
2. Uzupełnij logikę parsera w pliku `dhcp_snooping.p4` - powinien on rozpoznawać Ethernet, IPv4 oraz UDP.
3. Uzupełnij logikę ingress - sprawdź czy komunikacja odbywa się za pomocą protokołu DHCP (porty 67 i 68). Następnie zweryfikuj, czy ingress port zwarty jest w tabeli zaufanych portów.
4. Uzupełnij logikę deparsera - poskładaj pakiet UDP ponownie do całości.

