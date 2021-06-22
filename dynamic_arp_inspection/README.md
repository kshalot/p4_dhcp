# Implementacja DHCP Snoopingu

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
mininet> h2 tcpdump -i eth0 arp -vvv &
```
 
Aby zapobiec niepotrzebnemu szumowi tcpdump pokaże informacje tylko o ruchu ARP.
 
4. Wyślij pakiety ARP Reply przy pomocy przygotowanych skryptów:
 
```sh
mininet> h1 ./send_arp.sh &
mininet> h3 ./send_arp.sh &
```
 
5. Zweryfikuj, że h2 otrzymał 2 odpowiedzi, z czego druga jest tą "złą".
 
Powinno to wyglądać następująco:
 
```
10:37:06.110567 ARP, Ethernet (len 6), IPv4 (len 4), Reply 10.0.0.1 is-at 08:00:00:00:01:11 (oui Unknown), length 28
10:37:16.688183 ARP, Ethernet (len 6), IPv4 (len 4), Reply 10.0.0.1 is-at 08:00:00:00:03:33 (oui Unknown), length 28
 
2 packets captured
2 packets received by filter
0 packets dropped by kernel
```
 
Po wykonaniu ćwiczenia ruch inny niż ARP powinien działać tak samo, natomiast w wyniku tcpdump powinien być widoczny tylko pakiet od h1.

## Przebieg laboratorium

1. W pliku `topo/s1-runtime.json` zdefiniuj tabelę przechowującą klucze MAC, IP. Zdefiniuj w niej wiersze odpowiadające domyślnym konfiugracją hostów w topologii.
2. Logika parsera uzględniająca ARP jest już napisana - przeanalizuj ją.
3. Uzupełnij logikę ingress - dodaj matchowanie po odpowiednim kluczu w tabeli stworzonej w punkcie 1. Sprawdź czy mamy do czynienia z ruchem ARP oraz dodatkowo operacją ARP Response - odfiltruj niezaufany ruch.
