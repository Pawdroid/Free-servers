# Instrukcje konfiguracji klientów

Najpierw wybierz klienta, a następnie sprawdź obsługiwany format wejściowy. Linki GitHub i Cloudflare w tym projekcie udostępniają dla każdego języka tę samą zwykłą subskrypcję węzłów URI/Base64. Nie są to gotowe profile Clash/Mihomo YAML ani natywne profile sing-box JSON.

Prywatne adresy subskrypcji i dane uwierzytelniające przechowuj na własnym urządzeniu. Nie wysyłaj ich do publicznych serwisów konwersji. Jeśli potrzebujesz innego formatu, uzyskaj zgodny profil od dostawcy lub przygotuj go lokalnie na podstawie oficjalnej dokumentacji konfiguracji docelowego klienta.

[v2rayN](#v2rayn)
[Clash Verge Rev](#clash-verge-rev)
[Hiddify](#hiddify)
[Clash Party](#clash-party)
[FlClash](#flclash)
[Karing](#karing)
[Throne](#throne)
[Surge Mac](#surge)
[Quantumult X](#quantumult-x)
[sing-box for Apple platforms](#sing-box)
[v2rayNG](#v2rayng)
[Clash Meta for Android](#clash-meta-android)
[Surfboard](#surfboard)
[NekoBox for Android](#nekobox-android)
[Shadowrocket](#shadowrocket)
[Stash](#stash)
[Loon](#loon)
[Egern](#egern)
[Streisand](#streisand)
[Potatso](#potatso)
[OpenClash](#openclash)
[PassWall2 / PassWall](#passwall)
[Nikki](#nikki)
[HomeProxy](#homeproxy)

<a id="v2rayn"></a>

## v2rayN

**Format importu:** URI / Base64

### Szybka konfiguracja

1. Dodaj obsługiwany adres URL węzła lub zwykłą subskrypcję URI/Base64 w sekcji subskrypcji lub profili klienta. Odśwież subskrypcję i sprawdź, czy pojawiły się oczekiwane węzły.
2. Jeśli profil pozwala na wybór, wybierz węzeł lub grupę proxy, a następnie włącz tryb proxy/VPN opisany w dokumentacji klienta. Przyznaj systemowe uprawnienie VPN wyłącznie zainstalowanej oficjalnej aplikacji. Po połączeniu sprawdź rzeczywisty dostęp.
3. Jeśli aktualizacja się nie powiedzie, sprawdź adres URL, sieć i błąd HTTP. W razie błędu parsowania sprawdź format i wersję silnika. Jeśli import działa, ale połączenie nie, odśwież subskrypcję, wypróbuj inny obsługiwany węzeł i sprawdź dziennik błędów klienta. Udana aktualizacja lub test opóźnienia nie gwarantują dostępności ani bezpieczeństwa.

Sprawdź obsługiwane protokoły i zainstalowaną wersję silnika. Import węzłów nie gwarantuje przeniesienia wszystkich reguł, ustawień DNS ani pól zaawansowanych.

[Oficjalna instrukcja [中文]](https://github.com/2dust/v2rayN/wiki/Description-of-some-ui)


<a id="clash-verge-rev"></a>

## Clash Verge Rev

**Format importu:** Clash / Mihomo YAML

### Szybka konfiguracja

1. Uzyskaj kompletny profil YAML zgodny z Clash/Mihomo. Zaimportuj go jako profil lokalny lub zdalny, zaktualizuj i wybierz. Zwykła subskrypcja podana powyżej nie jest kompletnym profilem YAML.
2. Jeśli profil pozwala na wybór, wybierz węzeł lub grupę proxy, a następnie włącz tryb proxy/VPN opisany w dokumentacji klienta. Przyznaj systemowe uprawnienie VPN wyłącznie zainstalowanej oficjalnej aplikacji. Po połączeniu sprawdź rzeczywisty dostęp.
3. Jeśli aktualizacja się nie powiedzie, sprawdź adres URL, sieć i błąd HTTP. W razie błędu parsowania sprawdź format i wersję silnika. Jeśli import działa, ale połączenie nie, odśwież subskrypcję, wypróbuj inny obsługiwany węzeł i sprawdź dziennik błędów klienta. Udana aktualizacja lub test opóźnienia nie gwarantują dostępności ani bezpieczeństwa.

Sprawdź obsługiwane protokoły i zainstalowaną wersję silnika. Import węzłów nie gwarantuje przeniesienia wszystkich reguł, ustawień DNS ani pól zaawansowanych.

[Oficjalna instrukcja [中文]](https://www.clashverge.dev/guide/quickstart.html)


<a id="hiddify"></a>

## Hiddify

**Format importu:** URI / Base64 · Clash YAML · sing-box JSON

Ten klient odczytuje kilka formatów, ale do subskrypcji tego projektu użyj zwykłego importu URI/Base64. Natywne profile JSON i YAML nadal mają własne wymagania.

### Szybka konfiguracja

1. Dodaj obsługiwany adres URL węzła lub zwykłą subskrypcję URI/Base64 w sekcji subskrypcji lub profili klienta. Odśwież subskrypcję i sprawdź, czy pojawiły się oczekiwane węzły.
2. Jeśli profil pozwala na wybór, wybierz węzeł lub grupę proxy, a następnie włącz tryb proxy/VPN opisany w dokumentacji klienta. Przyznaj systemowe uprawnienie VPN wyłącznie zainstalowanej oficjalnej aplikacji. Po połączeniu sprawdź rzeczywisty dostęp.
3. Jeśli aktualizacja się nie powiedzie, sprawdź adres URL, sieć i błąd HTTP. W razie błędu parsowania sprawdź format i wersję silnika. Jeśli import działa, ale połączenie nie, odśwież subskrypcję, wypróbuj inny obsługiwany węzeł i sprawdź dziennik błędów klienta. Udana aktualizacja lub test opóźnienia nie gwarantują dostępności ani bezpieczeństwa.

Sprawdź obsługiwane protokoły i zainstalowaną wersję silnika. Import węzłów nie gwarantuje przeniesienia wszystkich reguł, ustawień DNS ani pól zaawansowanych.

[Oficjalna instrukcja [English]](https://hiddify.com/app/How-to-use-Hiddify-app/)


<a id="clash-party"></a>

## Clash Party

**Format importu:** Clash / Mihomo YAML

### Szybka konfiguracja

1. Uzyskaj kompletny profil YAML zgodny z Clash/Mihomo. Zaimportuj go jako profil lokalny lub zdalny, zaktualizuj i wybierz. Zwykła subskrypcja podana powyżej nie jest kompletnym profilem YAML.
2. Jeśli profil pozwala na wybór, wybierz węzeł lub grupę proxy, a następnie włącz tryb proxy/VPN opisany w dokumentacji klienta. Przyznaj systemowe uprawnienie VPN wyłącznie zainstalowanej oficjalnej aplikacji. Po połączeniu sprawdź rzeczywisty dostęp.
3. Jeśli aktualizacja się nie powiedzie, sprawdź adres URL, sieć i błąd HTTP. W razie błędu parsowania sprawdź format i wersję silnika. Jeśli import działa, ale połączenie nie, odśwież subskrypcję, wypróbuj inny obsługiwany węzeł i sprawdź dziennik błędów klienta. Udana aktualizacja lub test opóźnienia nie gwarantują dostępności ani bezpieczeństwa.

Sprawdź obsługiwane protokoły i zainstalowaną wersję silnika. Import węzłów nie gwarantuje przeniesienia wszystkich reguł, ustawień DNS ani pól zaawansowanych.

[Oficjalna instrukcja [中文]](https://clashparty.org/docs/handson)


<a id="flclash"></a>

## FlClash

**Format importu:** Clash / Mihomo YAML

Oficjalne instrukcje użytkownika są ograniczone. Skorzystaj z krótkich kroków konfiguracji i zweryfikowanej oficjalnej dokumentacji formatu poniżej.

### Szybka konfiguracja

1. Uzyskaj kompletny profil YAML zgodny z Clash/Mihomo. Zaimportuj go jako profil lokalny lub zdalny, zaktualizuj i wybierz. Zwykła subskrypcja podana powyżej nie jest kompletnym profilem YAML.
2. Jeśli profil pozwala na wybór, wybierz węzeł lub grupę proxy, a następnie włącz tryb proxy/VPN opisany w dokumentacji klienta. Przyznaj systemowe uprawnienie VPN wyłącznie zainstalowanej oficjalnej aplikacji. Po połączeniu sprawdź rzeczywisty dostęp.
3. Jeśli aktualizacja się nie powiedzie, sprawdź adres URL, sieć i błąd HTTP. W razie błędu parsowania sprawdź format i wersję silnika. Jeśli import działa, ale połączenie nie, odśwież subskrypcję, wypróbuj inny obsługiwany węzeł i sprawdź dziennik błędów klienta. Udana aktualizacja lub test opóźnienia nie gwarantują dostępności ani bezpieczeństwa.

Sprawdź obsługiwane protokoły i zainstalowaną wersję silnika. Import węzłów nie gwarantuje przeniesienia wszystkich reguł, ustawień DNS ani pól zaawansowanych.

Ta krótka instrukcja opisuje zweryfikowany format wejściowy i podstawowy przebieg konfiguracji. Podlinkowana dokumentacja techniczna nie jest instrukcją krok po kroku dla użytkownika; nazwy elementów interfejsu mogą się różnić między wersjami.

- [Dokumentacja techniczna [English]](https://github.com/chen08209/FlClash#usage)

<a id="karing"></a>

## Karing

**Format importu:** URI / Base64 · Clash YAML · sing-box JSON

Ten klient odczytuje kilka formatów, ale do subskrypcji tego projektu użyj zwykłego importu URI/Base64. Natywne profile JSON i YAML nadal mają własne wymagania.

### Szybka konfiguracja

1. Dodaj obsługiwany adres URL węzła lub zwykłą subskrypcję URI/Base64 w sekcji subskrypcji lub profili klienta. Odśwież subskrypcję i sprawdź, czy pojawiły się oczekiwane węzły.
2. Jeśli profil pozwala na wybór, wybierz węzeł lub grupę proxy, a następnie włącz tryb proxy/VPN opisany w dokumentacji klienta. Przyznaj systemowe uprawnienie VPN wyłącznie zainstalowanej oficjalnej aplikacji. Po połączeniu sprawdź rzeczywisty dostęp.
3. Jeśli aktualizacja się nie powiedzie, sprawdź adres URL, sieć i błąd HTTP. W razie błędu parsowania sprawdź format i wersję silnika. Jeśli import działa, ale połączenie nie, odśwież subskrypcję, wypróbuj inny obsługiwany węzeł i sprawdź dziennik błędów klienta. Udana aktualizacja lub test opóźnienia nie gwarantują dostępności ani bezpieczeństwa.

Sprawdź obsługiwane protokoły i zainstalowaną wersję silnika. Import węzłów nie gwarantuje przeniesienia wszystkich reguł, ustawień DNS ani pól zaawansowanych.

[Oficjalna instrukcja [English]](https://karing.app/en/quickstart)


<a id="throne"></a>

## Throne

**Format importu:** URI / Base64 · sing-box JSON · Clash YAML proxies

Import subskrypcji wyodrębnia obsługiwane węzły. Nie zakładaj, że reguły i inne ustawienia oryginalnego profilu zostaną zachowane.

### Szybka konfiguracja

1. Dodaj obsługiwany adres URL węzła lub zwykłą subskrypcję URI/Base64 w sekcji subskrypcji lub profili klienta. Odśwież subskrypcję i sprawdź, czy pojawiły się oczekiwane węzły.
2. Jeśli profil pozwala na wybór, wybierz węzeł lub grupę proxy, a następnie włącz tryb proxy/VPN opisany w dokumentacji klienta. Przyznaj systemowe uprawnienie VPN wyłącznie zainstalowanej oficjalnej aplikacji. Po połączeniu sprawdź rzeczywisty dostęp.
3. Jeśli aktualizacja się nie powiedzie, sprawdź adres URL, sieć i błąd HTTP. W razie błędu parsowania sprawdź format i wersję silnika. Jeśli import działa, ale połączenie nie, odśwież subskrypcję, wypróbuj inny obsługiwany węzeł i sprawdź dziennik błędów klienta. Udana aktualizacja lub test opóźnienia nie gwarantują dostępności ani bezpieczeństwa.

Sprawdź obsługiwane protokoły i zainstalowaną wersję silnika. Import węzłów nie gwarantuje przeniesienia wszystkich reguł, ustawień DNS ani pól zaawansowanych.

[Oficjalna instrukcja [English]](https://throneproj.github.io/get_started/configuration/)


<a id="surge"></a>

## Surge Mac

**Format importu:** Surge INI / Managed Profile

Użyj konfiguracji Surge lub adresu URL konfiguracji zarządzanej. Nie traktuj ogólnej subskrypcji V2Ray jako kompletnej konfiguracji Surge.

### Szybka konfiguracja

1. Uzyskaj kompletny profil w podanym wyżej formacie. Zaimportuj obsługiwany przez klienta plik lokalny lub adres URL profilu zdalnego, zaktualizuj profil i wybierz go. Nie zakładaj, że zwykłe subskrypcje węzłów i konfiguracje innych aplikacji są zamienne.
2. Jeśli profil pozwala na wybór, wybierz węzeł lub grupę proxy, a następnie włącz tryb proxy/VPN opisany w dokumentacji klienta. Przyznaj systemowe uprawnienie VPN wyłącznie zainstalowanej oficjalnej aplikacji. Po połączeniu sprawdź rzeczywisty dostęp.
3. Jeśli aktualizacja się nie powiedzie, sprawdź adres URL, sieć i błąd HTTP. W razie błędu parsowania sprawdź format i wersję silnika. Jeśli import działa, ale połączenie nie, odśwież subskrypcję, wypróbuj inny obsługiwany węzeł i sprawdź dziennik błędów klienta. Udana aktualizacja lub test opóźnienia nie gwarantują dostępności ani bezpieczeństwa.

Sprawdź obsługiwane protokoły i zainstalowaną wersję silnika. Import węzłów nie gwarantuje przeniesienia wszystkich reguł, ustawień DNS ani pól zaawansowanych.

[Oficjalna instrukcja [English]](https://manual.nssurge.com/getting-started/quick-start.html)


<a id="quantumult-x"></a>

## Quantumult X

**Format importu:** Quantumult X / server_remote

Quantumult X używa własnej konfiguracji i zdalnych zasobów serwerów. Kompletna konfiguracja i zasób węzłów to różne dane wejściowe.

Oficjalne instrukcje użytkownika są ograniczone. Skorzystaj z krótkich kroków konfiguracji i zweryfikowanej oficjalnej dokumentacji formatu poniżej.

### Szybka konfiguracja

1. Uzyskaj kompletny profil w podanym wyżej formacie. Zaimportuj obsługiwany przez klienta plik lokalny lub adres URL profilu zdalnego, zaktualizuj profil i wybierz go. Nie zakładaj, że zwykłe subskrypcje węzłów i konfiguracje innych aplikacji są zamienne.
2. Jeśli profil pozwala na wybór, wybierz węzeł lub grupę proxy, a następnie włącz tryb proxy/VPN opisany w dokumentacji klienta. Przyznaj systemowe uprawnienie VPN wyłącznie zainstalowanej oficjalnej aplikacji. Po połączeniu sprawdź rzeczywisty dostęp.
3. Jeśli aktualizacja się nie powiedzie, sprawdź adres URL, sieć i błąd HTTP. W razie błędu parsowania sprawdź format i wersję silnika. Jeśli import działa, ale połączenie nie, odśwież subskrypcję, wypróbuj inny obsługiwany węzeł i sprawdź dziennik błędów klienta. Udana aktualizacja lub test opóźnienia nie gwarantują dostępności ani bezpieczeństwa.

Sprawdź obsługiwane protokoły i zainstalowaną wersję silnika. Import węzłów nie gwarantuje przeniesienia wszystkich reguł, ustawień DNS ani pól zaawansowanych.

Ta krótka instrukcja opisuje zweryfikowany format wejściowy i podstawowy przebieg konfiguracji. Podlinkowana dokumentacja techniczna nie jest instrukcją krok po kroku dla użytkownika; nazwy elementów interfejsu mogą się różnić między wersjami.

- [Dokumentacja techniczna [中文 / English]](https://github.com/crossutility/Quantumult-X/blob/master/sample.conf)

<a id="sing-box"></a>

## sing-box for Apple platforms

**Format importu:** sing-box JSON

### Szybka konfiguracja

1. Uzyskaj kompletny profil sing-box JSON zgodny z wersją silnika klienta. Dodaj go jako profil lokalny lub zdalny i zaktualizuj. Lista adresów URL węzłów ani plik YAML dla Clash nie mogą służyć jako natywny sing-box JSON.
2. Jeśli profil pozwala na wybór, wybierz węzeł lub grupę proxy, a następnie włącz tryb proxy/VPN opisany w dokumentacji klienta. Przyznaj systemowe uprawnienie VPN wyłącznie zainstalowanej oficjalnej aplikacji. Po połączeniu sprawdź rzeczywisty dostęp.
3. Jeśli aktualizacja się nie powiedzie, sprawdź adres URL, sieć i błąd HTTP. W razie błędu parsowania sprawdź format i wersję silnika. Jeśli import działa, ale połączenie nie, odśwież subskrypcję, wypróbuj inny obsługiwany węzeł i sprawdź dziennik błędów klienta. Udana aktualizacja lub test opóźnienia nie gwarantują dostępności ani bezpieczeństwa.

Sprawdź obsługiwane protokoły i zainstalowaną wersję silnika. Import węzłów nie gwarantuje przeniesienia wszystkich reguł, ustawień DNS ani pól zaawansowanych.

[Oficjalna instrukcja [English]](https://sing-box.sagernet.org/clients/general/)


<a id="v2rayng"></a>

## v2rayNG

**Format importu:** URI / Base64

Oficjalne instrukcje użytkownika są ograniczone. Skorzystaj z krótkich kroków konfiguracji i zweryfikowanej oficjalnej dokumentacji formatu poniżej.

### Szybka konfiguracja

1. Dodaj obsługiwany adres URL węzła lub zwykłą subskrypcję URI/Base64 w sekcji subskrypcji lub profili klienta. Odśwież subskrypcję i sprawdź, czy pojawiły się oczekiwane węzły.
2. Jeśli profil pozwala na wybór, wybierz węzeł lub grupę proxy, a następnie włącz tryb proxy/VPN opisany w dokumentacji klienta. Przyznaj systemowe uprawnienie VPN wyłącznie zainstalowanej oficjalnej aplikacji. Po połączeniu sprawdź rzeczywisty dostęp.
3. Jeśli aktualizacja się nie powiedzie, sprawdź adres URL, sieć i błąd HTTP. W razie błędu parsowania sprawdź format i wersję silnika. Jeśli import działa, ale połączenie nie, odśwież subskrypcję, wypróbuj inny obsługiwany węzeł i sprawdź dziennik błędów klienta. Udana aktualizacja lub test opóźnienia nie gwarantują dostępności ani bezpieczeństwa.

Sprawdź obsługiwane protokoły i zainstalowaną wersję silnika. Import węzłów nie gwarantuje przeniesienia wszystkich reguł, ustawień DNS ani pól zaawansowanych.

Ta krótka instrukcja opisuje zweryfikowany format wejściowy i podstawowy przebieg konfiguracji. Podlinkowana dokumentacja techniczna nie jest instrukcją krok po kroku dla użytkownika; nazwy elementów interfejsu mogą się różnić między wersjami.

- [Dokumentacja techniczna [English]](https://github.com/2dust/v2rayNG/wiki/Mode)

<a id="clash-meta-android"></a>

## Clash Meta for Android

**Format importu:** Clash / Mihomo YAML

Oficjalne instrukcje użytkownika są ograniczone. Skorzystaj z krótkich kroków konfiguracji i zweryfikowanej oficjalnej dokumentacji formatu poniżej.

### Szybka konfiguracja

1. Uzyskaj kompletny profil YAML zgodny z Clash/Mihomo. Zaimportuj go jako profil lokalny lub zdalny, zaktualizuj i wybierz. Zwykła subskrypcja podana powyżej nie jest kompletnym profilem YAML.
2. Jeśli profil pozwala na wybór, wybierz węzeł lub grupę proxy, a następnie włącz tryb proxy/VPN opisany w dokumentacji klienta. Przyznaj systemowe uprawnienie VPN wyłącznie zainstalowanej oficjalnej aplikacji. Po połączeniu sprawdź rzeczywisty dostęp.
3. Jeśli aktualizacja się nie powiedzie, sprawdź adres URL, sieć i błąd HTTP. W razie błędu parsowania sprawdź format i wersję silnika. Jeśli import działa, ale połączenie nie, odśwież subskrypcję, wypróbuj inny obsługiwany węzeł i sprawdź dziennik błędów klienta. Udana aktualizacja lub test opóźnienia nie gwarantują dostępności ani bezpieczeństwa.

Sprawdź obsługiwane protokoły i zainstalowaną wersję silnika. Import węzłów nie gwarantuje przeniesienia wszystkich reguł, ustawień DNS ani pól zaawansowanych.

Ta krótka instrukcja opisuje zweryfikowany format wejściowy i podstawowy przebieg konfiguracji. Podlinkowana dokumentacja techniczna nie jest instrukcją krok po kroku dla użytkownika; nazwy elementów interfejsu mogą się różnić między wersjami.

- [Dokumentacja techniczna [English]](https://wiki.metacubex.one/en/handbook/syntax/)
- [Dokumentacja techniczna [English]](https://github.com/MetaCubeX/ClashMetaForAndroid#automation)

<a id="surfboard"></a>

## Surfboard

**Format importu:** Surfboard / Surge profile

Użyj konfiguracji Surge lub adresu URL konfiguracji zarządzanej. Nie traktuj ogólnej subskrypcji V2Ray jako kompletnej konfiguracji Surge.

Oficjalne instrukcje użytkownika są ograniczone. Skorzystaj z krótkich kroków konfiguracji i zweryfikowanej oficjalnej dokumentacji formatu poniżej.

### Szybka konfiguracja

1. Uzyskaj kompletny profil w podanym wyżej formacie. Zaimportuj obsługiwany przez klienta plik lokalny lub adres URL profilu zdalnego, zaktualizuj profil i wybierz go. Nie zakładaj, że zwykłe subskrypcje węzłów i konfiguracje innych aplikacji są zamienne.
2. Jeśli profil pozwala na wybór, wybierz węzeł lub grupę proxy, a następnie włącz tryb proxy/VPN opisany w dokumentacji klienta. Przyznaj systemowe uprawnienie VPN wyłącznie zainstalowanej oficjalnej aplikacji. Po połączeniu sprawdź rzeczywisty dostęp.
3. Jeśli aktualizacja się nie powiedzie, sprawdź adres URL, sieć i błąd HTTP. W razie błędu parsowania sprawdź format i wersję silnika. Jeśli import działa, ale połączenie nie, odśwież subskrypcję, wypróbuj inny obsługiwany węzeł i sprawdź dziennik błędów klienta. Udana aktualizacja lub test opóźnienia nie gwarantują dostępności ani bezpieczeństwa.

Sprawdź obsługiwane protokoły i zainstalowaną wersję silnika. Import węzłów nie gwarantuje przeniesienia wszystkich reguł, ustawień DNS ani pól zaawansowanych.

Ta krótka instrukcja opisuje zweryfikowany format wejściowy i podstawowy przebieg konfiguracji. Podlinkowana dokumentacja techniczna nie jest instrukcją krok po kroku dla użytkownika; nazwy elementów interfejsu mogą się różnić między wersjami.

- [Dokumentacja techniczna [English]](https://getsurfboard.com/docs/profile-format/overview/)

<a id="nekobox-android"></a>

## NekoBox for Android

**Format importu:** URI / Base64 · Clash proxies · sing-box outbounds

Import subskrypcji wyodrębnia obsługiwane węzły. Nie zakładaj, że reguły i inne ustawienia oryginalnego profilu zostaną zachowane.

### Szybka konfiguracja

1. Dodaj obsługiwany adres URL węzła lub zwykłą subskrypcję URI/Base64 w sekcji subskrypcji lub profili klienta. Odśwież subskrypcję i sprawdź, czy pojawiły się oczekiwane węzły.
2. Jeśli profil pozwala na wybór, wybierz węzeł lub grupę proxy, a następnie włącz tryb proxy/VPN opisany w dokumentacji klienta. Przyznaj systemowe uprawnienie VPN wyłącznie zainstalowanej oficjalnej aplikacji. Po połączeniu sprawdź rzeczywisty dostęp.
3. Jeśli aktualizacja się nie powiedzie, sprawdź adres URL, sieć i błąd HTTP. W razie błędu parsowania sprawdź format i wersję silnika. Jeśli import działa, ale połączenie nie, odśwież subskrypcję, wypróbuj inny obsługiwany węzeł i sprawdź dziennik błędów klienta. Udana aktualizacja lub test opóźnienia nie gwarantują dostępności ani bezpieczeństwa.

Sprawdź obsługiwane protokoły i zainstalowaną wersję silnika. Import węzłów nie gwarantuje przeniesienia wszystkich reguł, ustawień DNS ani pól zaawansowanych.

[Oficjalna instrukcja [中文]](https://matsuridayo.github.io/nb4a-configuration/)


<a id="shadowrocket"></a>

## Shadowrocket

**Format importu:** Shadowrocket subscriptions / profiles

Oficjalne instrukcje użytkownika są ograniczone. Skorzystaj z krótkich kroków konfiguracji i zweryfikowanej oficjalnej dokumentacji formatu poniżej.

### Szybka konfiguracja

1. Przygotuj obsługiwaną przez aplikację subskrypcję węzłów lub konfigurację pojedynczego węzła. Dodaj ją metodą importu opisaną w dokumentacji aplikacji, zaktualizuj subskrypcje, jeśli ta funkcja jest obsługiwana, i sprawdź, czy pojawiły się węzły. Lista węzłów i kompletny profil routingu to różne dane wejściowe.
2. Jeśli profil pozwala na wybór, wybierz węzeł lub grupę proxy, a następnie włącz tryb proxy/VPN opisany w dokumentacji klienta. Przyznaj systemowe uprawnienie VPN wyłącznie zainstalowanej oficjalnej aplikacji. Po połączeniu sprawdź rzeczywisty dostęp.
3. Jeśli aktualizacja się nie powiedzie, sprawdź adres URL, sieć i błąd HTTP. W razie błędu parsowania sprawdź format i wersję silnika. Jeśli import działa, ale połączenie nie, odśwież subskrypcję, wypróbuj inny obsługiwany węzeł i sprawdź dziennik błędów klienta. Udana aktualizacja lub test opóźnienia nie gwarantują dostępności ani bezpieczeństwa.

Sprawdź obsługiwane protokoły i zainstalowaną wersję silnika. Import węzłów nie gwarantuje przeniesienia wszystkich reguł, ustawień DNS ani pól zaawansowanych.

- [Oficjalne informacje o produkcie [English]](https://apps.apple.com/us/app/shadowrocket/id932747118)

<a id="stash"></a>

## Stash

**Format importu:** Stash / Clash YAML

### Szybka konfiguracja

1. Uzyskaj kompletny profil YAML zgodny z Clash/Mihomo. Zaimportuj go jako profil lokalny lub zdalny, zaktualizuj i wybierz. Zwykła subskrypcja podana powyżej nie jest kompletnym profilem YAML.
2. Jeśli profil pozwala na wybór, wybierz węzeł lub grupę proxy, a następnie włącz tryb proxy/VPN opisany w dokumentacji klienta. Przyznaj systemowe uprawnienie VPN wyłącznie zainstalowanej oficjalnej aplikacji. Po połączeniu sprawdź rzeczywisty dostęp.
3. Jeśli aktualizacja się nie powiedzie, sprawdź adres URL, sieć i błąd HTTP. W razie błędu parsowania sprawdź format i wersję silnika. Jeśli import działa, ale połączenie nie, odśwież subskrypcję, wypróbuj inny obsługiwany węzeł i sprawdź dziennik błędów klienta. Udana aktualizacja lub test opóźnienia nie gwarantują dostępności ani bezpieczeństwa.

Sprawdź obsługiwane protokoły i zainstalowaną wersję silnika. Import węzłów nie gwarantuje przeniesienia wszystkich reguł, ustawień DNS ani pól zaawansowanych.

[Oficjalna instrukcja [English]](https://stash.wiki/en/get-started)


<a id="loon"></a>

## Loon

**Format importu:** URI / Base64 · Loon configuration

Loon używa własnych formatów konfiguracji i subskrybowanych węzłów. Sprawdzaj każdy protokół i pole zamiast zakładać pełną zgodność z Surge lub Clash.

### Szybka konfiguracja

1. Dodaj obsługiwany adres URL węzła lub zwykłą subskrypcję URI/Base64 w sekcji subskrypcji lub profili klienta. Odśwież subskrypcję i sprawdź, czy pojawiły się oczekiwane węzły.
2. Jeśli profil pozwala na wybór, wybierz węzeł lub grupę proxy, a następnie włącz tryb proxy/VPN opisany w dokumentacji klienta. Przyznaj systemowe uprawnienie VPN wyłącznie zainstalowanej oficjalnej aplikacji. Po połączeniu sprawdź rzeczywisty dostęp.
3. Jeśli aktualizacja się nie powiedzie, sprawdź adres URL, sieć i błąd HTTP. W razie błędu parsowania sprawdź format i wersję silnika. Jeśli import działa, ale połączenie nie, odśwież subskrypcję, wypróbuj inny obsługiwany węzeł i sprawdź dziennik błędów klienta. Udana aktualizacja lub test opóźnienia nie gwarantują dostępności ani bezpieczeństwa.

Sprawdź obsługiwane protokoły i zainstalowaną wersję silnika. Import węzłów nie gwarantuje przeniesienia wszystkich reguł, ustawień DNS ani pól zaawansowanych.

[Oficjalna instrukcja [English]](https://nsloon.app/en/docs/Node/subscription/)


<a id="egern"></a>

## Egern

**Format importu:** Egern Profile.yaml / proxies YAML

Egern YAML to własny format profilu, a nie Clash/Mihomo YAML.

Oficjalne instrukcje użytkownika są ograniczone. Skorzystaj z krótkich kroków konfiguracji i zweryfikowanej oficjalnej dokumentacji formatu poniżej.

### Szybka konfiguracja

1. Uzyskaj kompletny profil w podanym wyżej formacie. Zaimportuj obsługiwany przez klienta plik lokalny lub adres URL profilu zdalnego, zaktualizuj profil i wybierz go. Nie zakładaj, że zwykłe subskrypcje węzłów i konfiguracje innych aplikacji są zamienne.
2. Jeśli profil pozwala na wybór, wybierz węzeł lub grupę proxy, a następnie włącz tryb proxy/VPN opisany w dokumentacji klienta. Przyznaj systemowe uprawnienie VPN wyłącznie zainstalowanej oficjalnej aplikacji. Po połączeniu sprawdź rzeczywisty dostęp.
3. Jeśli aktualizacja się nie powiedzie, sprawdź adres URL, sieć i błąd HTTP. W razie błędu parsowania sprawdź format i wersję silnika. Jeśli import działa, ale połączenie nie, odśwież subskrypcję, wypróbuj inny obsługiwany węzeł i sprawdź dziennik błędów klienta. Udana aktualizacja lub test opóźnienia nie gwarantują dostępności ani bezpieczeństwa.

Sprawdź obsługiwane protokoły i zainstalowaną wersję silnika. Import węzłów nie gwarantuje przeniesienia wszystkich reguł, ustawień DNS ani pól zaawansowanych.

Ta krótka instrukcja opisuje zweryfikowany format wejściowy i podstawowy przebieg konfiguracji. Podlinkowana dokumentacja techniczna nie jest instrukcją krok po kroku dla użytkownika; nazwy elementów interfejsu mogą się różnić między wersjami.

- [Dokumentacja techniczna [English]](https://egernapp.com/docs/configuration/policy_groups/)

<a id="streisand"></a>

## Streisand

**Format importu:** Supported node configurations

Oficjalne instrukcje użytkownika są ograniczone. Skorzystaj z krótkich kroków konfiguracji i zweryfikowanej oficjalnej dokumentacji formatu poniżej.

### Szybka konfiguracja

1. Przygotuj obsługiwaną przez aplikację subskrypcję węzłów lub konfigurację pojedynczego węzła. Dodaj ją metodą importu opisaną w dokumentacji aplikacji, zaktualizuj subskrypcje, jeśli ta funkcja jest obsługiwana, i sprawdź, czy pojawiły się węzły. Lista węzłów i kompletny profil routingu to różne dane wejściowe.
2. Jeśli profil pozwala na wybór, wybierz węzeł lub grupę proxy, a następnie włącz tryb proxy/VPN opisany w dokumentacji klienta. Przyznaj systemowe uprawnienie VPN wyłącznie zainstalowanej oficjalnej aplikacji. Po połączeniu sprawdź rzeczywisty dostęp.
3. Jeśli aktualizacja się nie powiedzie, sprawdź adres URL, sieć i błąd HTTP. W razie błędu parsowania sprawdź format i wersję silnika. Jeśli import działa, ale połączenie nie, odśwież subskrypcję, wypróbuj inny obsługiwany węzeł i sprawdź dziennik błędów klienta. Udana aktualizacja lub test opóźnienia nie gwarantują dostępności ani bezpieczeństwa.

Sprawdź obsługiwane protokoły i zainstalowaną wersję silnika. Import węzłów nie gwarantuje przeniesienia wszystkich reguł, ustawień DNS ani pól zaawansowanych.

- [Oficjalne informacje o produkcie [English]](https://streisand.pages.dev/)

<a id="potatso"></a>

## Potatso

**Format importu:** Mihomo / Clash YAML · supported node links

Oficjalne instrukcje użytkownika są ograniczone. Skorzystaj z krótkich kroków konfiguracji i zweryfikowanej oficjalnej dokumentacji formatu poniżej.

### Szybka konfiguracja

1. Uzyskaj kompletny profil YAML zgodny z Clash/Mihomo. Zaimportuj go jako profil lokalny lub zdalny, zaktualizuj i wybierz. Zwykła subskrypcja podana powyżej nie jest kompletnym profilem YAML.
2. Jeśli profil pozwala na wybór, wybierz węzeł lub grupę proxy, a następnie włącz tryb proxy/VPN opisany w dokumentacji klienta. Przyznaj systemowe uprawnienie VPN wyłącznie zainstalowanej oficjalnej aplikacji. Po połączeniu sprawdź rzeczywisty dostęp.
3. Jeśli aktualizacja się nie powiedzie, sprawdź adres URL, sieć i błąd HTTP. W razie błędu parsowania sprawdź format i wersję silnika. Jeśli import działa, ale połączenie nie, odśwież subskrypcję, wypróbuj inny obsługiwany węzeł i sprawdź dziennik błędów klienta. Udana aktualizacja lub test opóźnienia nie gwarantują dostępności ani bezpieczeństwa.

Sprawdź obsługiwane protokoły i zainstalowaną wersję silnika. Import węzłów nie gwarantuje przeniesienia wszystkich reguł, ustawień DNS ani pól zaawansowanych.

- [Oficjalne informacje o produkcie [English]](https://potatso.com/)

<a id="openclash"></a>

## OpenClash

**Format importu:** Clash / Mihomo YAML

### Szybka konfiguracja

1. Przed instalacją sprawdź oprogramowanie układowe, architekturę procesora, wymagane pakiety i dostępną pamięć. Wykonaj kopię zapasową konfiguracji routera i zachowaj działające połączenie do zarządzania. Importuj wyłącznie obsługiwaną subskrypcję lub profil, zaktualizuj je, wybierz węzeł lub grupę wyjściową i włącz wtyczkę zgodnie z jej oficjalną instrukcją.
2. Jeśli aktualizacja się nie powiedzie, sprawdź adres URL, sieć i błąd HTTP. W razie błędu parsowania sprawdź format i wersję silnika. Jeśli import działa, ale połączenie nie, odśwież subskrypcję, wypróbuj inny obsługiwany węzeł i sprawdź dziennik błędów klienta. Udana aktualizacja lub test opóźnienia nie gwarantują dostępności ani bezpieczeństwa.

Sprawdź obsługiwane protokoły i zainstalowaną wersję silnika. Import węzłów nie gwarantuje przeniesienia wszystkich reguł, ustawień DNS ani pól zaawansowanych.

[Oficjalna instrukcja [中文]](https://github.com/vernesong/OpenClash#快速开始)


<a id="passwall"></a>

## PassWall2 / PassWall

**Format importu:** Supported node URI subscriptions

Import subskrypcji wyodrębnia obsługiwane węzły. Nie zakładaj, że reguły i inne ustawienia oryginalnego profilu zostaną zachowane.

Oficjalne instrukcje użytkownika są ograniczone. Skorzystaj z krótkich kroków konfiguracji i zweryfikowanej oficjalnej dokumentacji formatu poniżej.

### Szybka konfiguracja

1. Przed instalacją sprawdź oprogramowanie układowe, architekturę procesora, wymagane pakiety i dostępną pamięć. Wykonaj kopię zapasową konfiguracji routera i zachowaj działające połączenie do zarządzania. Importuj wyłącznie obsługiwaną subskrypcję lub profil, zaktualizuj je, wybierz węzeł lub grupę wyjściową i włącz wtyczkę zgodnie z jej oficjalną instrukcją.
2. Jeśli aktualizacja się nie powiedzie, sprawdź adres URL, sieć i błąd HTTP. W razie błędu parsowania sprawdź format i wersję silnika. Jeśli import działa, ale połączenie nie, odśwież subskrypcję, wypróbuj inny obsługiwany węzeł i sprawdź dziennik błędów klienta. Udana aktualizacja lub test opóźnienia nie gwarantują dostępności ani bezpieczeństwa.

Sprawdź obsługiwane protokoły i zainstalowaną wersję silnika. Import węzłów nie gwarantuje przeniesienia wszystkich reguł, ustawień DNS ani pól zaawansowanych.

Ta krótka instrukcja opisuje zweryfikowany format wejściowy i podstawowy przebieg konfiguracji. Podlinkowana dokumentacja techniczna nie jest instrukcją krok po kroku dla użytkownika; nazwy elementów interfejsu mogą się różnić między wersjami.

- [Dokumentacja techniczna [English]](https://github.com/Openwrt-Passwall/openwrt-passwall2)
- [Dokumentacja techniczna [English]](https://github.com/Openwrt-Passwall/openwrt-passwall)

<a id="nikki"></a>

## Nikki

**Format importu:** Mihomo YAML: proxies / proxy-providers

### Szybka konfiguracja

1. Przed instalacją sprawdź oprogramowanie układowe, architekturę procesora, wymagane pakiety i dostępną pamięć. Wykonaj kopię zapasową konfiguracji routera i zachowaj działające połączenie do zarządzania. Importuj wyłącznie obsługiwaną subskrypcję lub profil, zaktualizuj je, wybierz węzeł lub grupę wyjściową i włącz wtyczkę zgodnie z jej oficjalną instrukcją.
2. Jeśli aktualizacja się nie powiedzie, sprawdź adres URL, sieć i błąd HTTP. W razie błędu parsowania sprawdź format i wersję silnika. Jeśli import działa, ale połączenie nie, odśwież subskrypcję, wypróbuj inny obsługiwany węzeł i sprawdź dziennik błędów klienta. Udana aktualizacja lub test opóźnienia nie gwarantują dostępności ani bezpieczeństwa.

Sprawdź obsługiwane protokoły i zainstalowaną wersję silnika. Import węzłów nie gwarantuje przeniesienia wszystkich reguł, ustawień DNS ani pól zaawansowanych.

[Oficjalna instrukcja [中文]](https://github.com/nikkinikki-org/OpenWrt-nikki/wiki)


<a id="homeproxy"></a>

## HomeProxy

**Format importu:** HomeProxy node subscriptions

HomeProxy zarządza węzłami i subskrypcjami przez własny interfejs. Sprawdź formaty obsługiwane przez zainstalowaną wersję. Korzystanie z sing-box wewnętrznie nie oznacza możliwości importu dowolnego kompletnego profilu sing-box JSON.

Oficjalne instrukcje użytkownika są ograniczone. Skorzystaj z krótkich kroków konfiguracji i zweryfikowanej oficjalnej dokumentacji formatu poniżej.

### Szybka konfiguracja

1. Przed instalacją sprawdź oprogramowanie układowe, architekturę procesora, wymagane pakiety i dostępną pamięć. Wykonaj kopię zapasową konfiguracji routera i zachowaj działające połączenie do zarządzania. Importuj wyłącznie obsługiwaną subskrypcję lub profil, zaktualizuj je, wybierz węzeł lub grupę wyjściową i włącz wtyczkę zgodnie z jej oficjalną instrukcją.
2. Jeśli aktualizacja się nie powiedzie, sprawdź adres URL, sieć i błąd HTTP. W razie błędu parsowania sprawdź format i wersję silnika. Jeśli import działa, ale połączenie nie, odśwież subskrypcję, wypróbuj inny obsługiwany węzeł i sprawdź dziennik błędów klienta. Udana aktualizacja lub test opóźnienia nie gwarantują dostępności ani bezpieczeństwa.

Sprawdź obsługiwane protokoły i zainstalowaną wersję silnika. Import węzłów nie gwarantuje przeniesienia wszystkich reguł, ustawień DNS ani pól zaawansowanych.

Ta krótka instrukcja opisuje zweryfikowany format wejściowy i podstawowy przebieg konfiguracji. Podlinkowana dokumentacja techniczna nie jest instrukcją krok po kroku dla użytkownika; nazwy elementów interfejsu mogą się różnić między wersjami.

- [Dokumentacja techniczna [English]](https://github.com/immortalwrt/homeproxy)
