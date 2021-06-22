# Implementacja IP Source Guard

## Wstęp

## Opis skryptów

## Cel laboratorium

## Uruchomienie niekompletnego kodu
 
1. W konsoli wpisz aby uruchomić przykład:
 
```sh
$ make
```
 
2. Powinna być widoczna konsola minineta. Sprawdź, czy działa ping:
 
```sh
mininet> pingall
```
 
Wszystkie hosty powinny być w stanie się komunikować.
 
3. Uruchom tcpdump na `h2`:
 
```sh
mininet> h2 tcpdump -e -i eth0 ip -vvv &
```
 
Aby zapobiec niepotrzebnemu szumowi tcpdump pokaże informacje tylko o ruchu IP.
 
4. Wyślij pakiety IP przy pomocy przygotowanych skryptów:
 
```sh
mininet> h1 ./good_ip.sh &
mininet> h3 ./evil_ip.sh &
```
 
5. Zweryfikuj, że h2 otrzymał 2 pakiety, z czego drugi jest tym "złym".
 
Powinno to wyglądać następująco:
 
```
10:49:22.290725 08:00:00:00:01:11 (oui Unknown) > 08:00:00:00:02:22 (oui Unknown), ethertype IPv4 (0x0800), length 34: (tos 0x0, ttl 64, id 1, offset 0, flags [none], proto Options (0), length 20)
    10.0.0.1 > 10.0.0.2:  hopopt 0
10:49:22.341009 08:00:00:00:02:22 (oui Unknown) > 08:00:00:00:01:11 (oui Unknown), ethertype IPv4 (0x0800), length 62: (tos 0xc0, ttl 64, id 8195, offset 0, flags [none], proto ICMP (1), length 48)
    10.0.0.2 > 10.0.0.1: ICMP 10.0.0.2 protocol 0 unreachable, length 28
        (tos 0x0, ttl 64, id 1, offset 0, flags [none], proto Options (0), length 20)
    10.0.0.1 > 10.0.0.2:  hopopt 0
10:49:24.123653 08:00:00:00:03:33 (oui Unknown) > 08:00:00:00:02:22 (oui Unknown), ethertype IPv4 (0x0800), length 34: (tos 0x0, ttl 64, id 1, offset 0, flags [none], proto Options (0), length 20)
    10.0.0.1 > 10.0.0.2:  hopopt 0
10:49:24.173821 08:00:00:00:02:22 (oui Unknown) > 08:00:00:00:01:11 (oui Unknown), ethertype IPv4 (0x0800), length 62: (tos 0xc0, ttl 64, id 8647, offset 0, flags [none], proto ICMP (1), length 48)
    10.0.0.2 > 10.0.0.1: ICMP 10.0.0.2 protocol 0 unreachable, length 28
        (tos 0x0, ttl 64, id 1, offset 0, flags [none], proto Options (0), length 20)
    10.0.0.1 > 10.0.0.2:  hopopt 0
 
4 packets captured
4 packets received by filter
0 packets dropped by kernel
```
 
Widać 4 pakiety, ponieważ h2 odpowiedział na każdy wysyłając odpowiedni komunikat ICMP.
 
Po wykonaniu ćwiczenia ruch inny niż IP powinien działać tak samo, natomiast w wyniku tcpdump powinien być widoczny tylko pakiet od h1.
 
Po wykonaniu ćwiczenia pingall powinien dalej działać prawidłowo.

## Przebieg laboratorium
