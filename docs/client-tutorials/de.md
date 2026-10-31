# Konfigurationsanleitungen für Clients

Wählen Sie zunächst den Client und prüfen Sie dessen Eingabeformat. Die GitHub- und Cloudflare-Links dieses Projekts liefern für jede Sprache dasselbe gewöhnliche URI/Base64-Knotenabonnement. Sie sind keine fertigen Clash/Mihomo YAML- oder nativen sing-box JSON-Profile.

Bewahren Sie private Abonnement-URLs und Zugangsdaten auf Ihrem eigenen Gerät auf. Übermitteln Sie sie nicht an öffentliche Konvertierungswebsites. Wenn Sie ein anderes Format benötigen, beziehen Sie ein kompatibles Profil von Ihrem Anbieter oder erstellen Sie es lokal anhand der offiziellen Konfigurationsdokumentation des Zielclients.

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

**Importformat:** URI / Base64

### Schnelleinrichtung

1. Fügen Sie im Abonnement- oder Profilbereich des Clients eine unterstützte Knoten-URL oder ein gewöhnliches URI/Base64-Abonnement hinzu. Aktualisieren Sie das Abonnement und prüfen Sie, ob die erwarteten Knoten erscheinen.
2. Wenn das Profil eine Auswahl bietet, wählen Sie einen Knoten oder eine Proxy-Gruppe und aktivieren Sie anschließend den in der Client-Dokumentation beschriebenen Proxy-/VPN-Modus. Erteilen Sie die VPN-Berechtigung des Betriebssystems nur der von Ihnen installierten offiziellen App. Prüfen Sie nach dem Verbinden den tatsächlichen Zugriff.
3. Schlägt die Aktualisierung fehl, prüfen Sie URL, Netzwerk und HTTP-Fehler. Bei Einlesefehlern prüfen Sie Format und Core-Version. Gelingt der Import, aber nicht die Verbindung, aktualisieren Sie das Abonnement, versuchen Sie einen anderen unterstützten Knoten und prüfen Sie dann das Fehlerprotokoll des Clients. Eine erfolgreiche Aktualisierung oder ein Latenztest garantiert weder Verfügbarkeit noch Sicherheit.

Prüfen Sie die unterstützten Protokolle und die installierte Core-Version. Der Import von Knoten garantiert nicht, dass sämtliche Regeln, DNS-Einstellungen oder erweiterten Felder übernommen werden.

[Offizielle Anleitung [中文]](https://github.com/2dust/v2rayN/wiki/Description-of-some-ui)


<a id="clash-verge-rev"></a>

## Clash Verge Rev

**Importformat:** Clash / Mihomo YAML

### Schnelleinrichtung

1. Besorgen Sie ein vollständiges, mit Clash/Mihomo kompatibles YAML-Profil. Importieren Sie es als lokales oder entferntes Profil, aktualisieren Sie es und wählen Sie es aus. Das oben genannte gewöhnliche Abonnement ist kein vollständiges YAML-Profil.
2. Wenn das Profil eine Auswahl bietet, wählen Sie einen Knoten oder eine Proxy-Gruppe und aktivieren Sie anschließend den in der Client-Dokumentation beschriebenen Proxy-/VPN-Modus. Erteilen Sie die VPN-Berechtigung des Betriebssystems nur der von Ihnen installierten offiziellen App. Prüfen Sie nach dem Verbinden den tatsächlichen Zugriff.
3. Schlägt die Aktualisierung fehl, prüfen Sie URL, Netzwerk und HTTP-Fehler. Bei Einlesefehlern prüfen Sie Format und Core-Version. Gelingt der Import, aber nicht die Verbindung, aktualisieren Sie das Abonnement, versuchen Sie einen anderen unterstützten Knoten und prüfen Sie dann das Fehlerprotokoll des Clients. Eine erfolgreiche Aktualisierung oder ein Latenztest garantiert weder Verfügbarkeit noch Sicherheit.

Prüfen Sie die unterstützten Protokolle und die installierte Core-Version. Der Import von Knoten garantiert nicht, dass sämtliche Regeln, DNS-Einstellungen oder erweiterten Felder übernommen werden.

[Offizielle Anleitung [中文]](https://www.clashverge.dev/guide/quickstart.html)


<a id="hiddify"></a>

## Hiddify

**Importformat:** URI / Base64 · Clash YAML · sing-box JSON

Dieser Client kann mehrere Formate lesen. Verwenden Sie für das Abonnement dieses Projekts jedoch den gewöhnlichen URI/Base64-Import. Für native JSON- und YAML-Profile gelten weiterhin eigene Anforderungen.

### Schnelleinrichtung

1. Fügen Sie im Abonnement- oder Profilbereich des Clients eine unterstützte Knoten-URL oder ein gewöhnliches URI/Base64-Abonnement hinzu. Aktualisieren Sie das Abonnement und prüfen Sie, ob die erwarteten Knoten erscheinen.
2. Wenn das Profil eine Auswahl bietet, wählen Sie einen Knoten oder eine Proxy-Gruppe und aktivieren Sie anschließend den in der Client-Dokumentation beschriebenen Proxy-/VPN-Modus. Erteilen Sie die VPN-Berechtigung des Betriebssystems nur der von Ihnen installierten offiziellen App. Prüfen Sie nach dem Verbinden den tatsächlichen Zugriff.
3. Schlägt die Aktualisierung fehl, prüfen Sie URL, Netzwerk und HTTP-Fehler. Bei Einlesefehlern prüfen Sie Format und Core-Version. Gelingt der Import, aber nicht die Verbindung, aktualisieren Sie das Abonnement, versuchen Sie einen anderen unterstützten Knoten und prüfen Sie dann das Fehlerprotokoll des Clients. Eine erfolgreiche Aktualisierung oder ein Latenztest garantiert weder Verfügbarkeit noch Sicherheit.

Prüfen Sie die unterstützten Protokolle und die installierte Core-Version. Der Import von Knoten garantiert nicht, dass sämtliche Regeln, DNS-Einstellungen oder erweiterten Felder übernommen werden.

[Offizielle Anleitung [English]](https://hiddify.com/app/How-to-use-Hiddify-app/)


<a id="clash-party"></a>

## Clash Party

**Importformat:** Clash / Mihomo YAML

### Schnelleinrichtung

1. Besorgen Sie ein vollständiges, mit Clash/Mihomo kompatibles YAML-Profil. Importieren Sie es als lokales oder entferntes Profil, aktualisieren Sie es und wählen Sie es aus. Das oben genannte gewöhnliche Abonnement ist kein vollständiges YAML-Profil.
2. Wenn das Profil eine Auswahl bietet, wählen Sie einen Knoten oder eine Proxy-Gruppe und aktivieren Sie anschließend den in der Client-Dokumentation beschriebenen Proxy-/VPN-Modus. Erteilen Sie die VPN-Berechtigung des Betriebssystems nur der von Ihnen installierten offiziellen App. Prüfen Sie nach dem Verbinden den tatsächlichen Zugriff.
3. Schlägt die Aktualisierung fehl, prüfen Sie URL, Netzwerk und HTTP-Fehler. Bei Einlesefehlern prüfen Sie Format und Core-Version. Gelingt der Import, aber nicht die Verbindung, aktualisieren Sie das Abonnement, versuchen Sie einen anderen unterstützten Knoten und prüfen Sie dann das Fehlerprotokoll des Clients. Eine erfolgreiche Aktualisierung oder ein Latenztest garantiert weder Verfügbarkeit noch Sicherheit.

Prüfen Sie die unterstützten Protokolle und die installierte Core-Version. Der Import von Knoten garantiert nicht, dass sämtliche Regeln, DNS-Einstellungen oder erweiterten Felder übernommen werden.

[Offizielle Anleitung [中文]](https://clashparty.org/docs/handson)


<a id="flclash"></a>

## FlClash

**Importformat:** Clash / Mihomo YAML

Die offiziellen Anleitungen für Anwender sind begrenzt. Nutzen Sie die kurzen Einrichtungsschritte und die unten verlinkte, überprüfte offizielle Formatreferenz.

### Schnelleinrichtung

1. Besorgen Sie ein vollständiges, mit Clash/Mihomo kompatibles YAML-Profil. Importieren Sie es als lokales oder entferntes Profil, aktualisieren Sie es und wählen Sie es aus. Das oben genannte gewöhnliche Abonnement ist kein vollständiges YAML-Profil.
2. Wenn das Profil eine Auswahl bietet, wählen Sie einen Knoten oder eine Proxy-Gruppe und aktivieren Sie anschließend den in der Client-Dokumentation beschriebenen Proxy-/VPN-Modus. Erteilen Sie die VPN-Berechtigung des Betriebssystems nur der von Ihnen installierten offiziellen App. Prüfen Sie nach dem Verbinden den tatsächlichen Zugriff.
3. Schlägt die Aktualisierung fehl, prüfen Sie URL, Netzwerk und HTTP-Fehler. Bei Einlesefehlern prüfen Sie Format und Core-Version. Gelingt der Import, aber nicht die Verbindung, aktualisieren Sie das Abonnement, versuchen Sie einen anderen unterstützten Knoten und prüfen Sie dann das Fehlerprotokoll des Clients. Eine erfolgreiche Aktualisierung oder ein Latenztest garantiert weder Verfügbarkeit noch Sicherheit.

Prüfen Sie die unterstützten Protokolle und die installierte Core-Version. Der Import von Knoten garantiert nicht, dass sämtliche Regeln, DNS-Einstellungen oder erweiterten Felder übernommen werden.

Diese Kurzanleitung beschreibt das überprüfte Eingabeformat und den grundlegenden Ablauf. Die verlinkten technischen Referenzen sind keine Schritt-für-Schritt-Anleitung für Anwender; die Bezeichnungen in der Oberfläche können je nach Version abweichen.

- [Technische Referenz [English]](https://github.com/chen08209/FlClash#usage)

<a id="karing"></a>

## Karing

**Importformat:** URI / Base64 · Clash YAML · sing-box JSON

Dieser Client kann mehrere Formate lesen. Verwenden Sie für das Abonnement dieses Projekts jedoch den gewöhnlichen URI/Base64-Import. Für native JSON- und YAML-Profile gelten weiterhin eigene Anforderungen.

### Schnelleinrichtung

1. Fügen Sie im Abonnement- oder Profilbereich des Clients eine unterstützte Knoten-URL oder ein gewöhnliches URI/Base64-Abonnement hinzu. Aktualisieren Sie das Abonnement und prüfen Sie, ob die erwarteten Knoten erscheinen.
2. Wenn das Profil eine Auswahl bietet, wählen Sie einen Knoten oder eine Proxy-Gruppe und aktivieren Sie anschließend den in der Client-Dokumentation beschriebenen Proxy-/VPN-Modus. Erteilen Sie die VPN-Berechtigung des Betriebssystems nur der von Ihnen installierten offiziellen App. Prüfen Sie nach dem Verbinden den tatsächlichen Zugriff.
3. Schlägt die Aktualisierung fehl, prüfen Sie URL, Netzwerk und HTTP-Fehler. Bei Einlesefehlern prüfen Sie Format und Core-Version. Gelingt der Import, aber nicht die Verbindung, aktualisieren Sie das Abonnement, versuchen Sie einen anderen unterstützten Knoten und prüfen Sie dann das Fehlerprotokoll des Clients. Eine erfolgreiche Aktualisierung oder ein Latenztest garantiert weder Verfügbarkeit noch Sicherheit.

Prüfen Sie die unterstützten Protokolle und die installierte Core-Version. Der Import von Knoten garantiert nicht, dass sämtliche Regeln, DNS-Einstellungen oder erweiterten Felder übernommen werden.

[Offizielle Anleitung [English]](https://karing.app/en/quickstart)


<a id="throne"></a>

## Throne

**Importformat:** URI / Base64 · sing-box JSON · Clash YAML proxies

Beim Abonnementimport werden unterstützte Knoten übernommen. Gehen Sie nicht davon aus, dass Regeln und andere Einstellungen des ursprünglichen Profils erhalten bleiben.

### Schnelleinrichtung

1. Fügen Sie im Abonnement- oder Profilbereich des Clients eine unterstützte Knoten-URL oder ein gewöhnliches URI/Base64-Abonnement hinzu. Aktualisieren Sie das Abonnement und prüfen Sie, ob die erwarteten Knoten erscheinen.
2. Wenn das Profil eine Auswahl bietet, wählen Sie einen Knoten oder eine Proxy-Gruppe und aktivieren Sie anschließend den in der Client-Dokumentation beschriebenen Proxy-/VPN-Modus. Erteilen Sie die VPN-Berechtigung des Betriebssystems nur der von Ihnen installierten offiziellen App. Prüfen Sie nach dem Verbinden den tatsächlichen Zugriff.
3. Schlägt die Aktualisierung fehl, prüfen Sie URL, Netzwerk und HTTP-Fehler. Bei Einlesefehlern prüfen Sie Format und Core-Version. Gelingt der Import, aber nicht die Verbindung, aktualisieren Sie das Abonnement, versuchen Sie einen anderen unterstützten Knoten und prüfen Sie dann das Fehlerprotokoll des Clients. Eine erfolgreiche Aktualisierung oder ein Latenztest garantiert weder Verfügbarkeit noch Sicherheit.

Prüfen Sie die unterstützten Protokolle und die installierte Core-Version. Der Import von Knoten garantiert nicht, dass sämtliche Regeln, DNS-Einstellungen oder erweiterten Felder übernommen werden.

[Offizielle Anleitung [English]](https://throneproj.github.io/get_started/configuration/)


<a id="surge"></a>

## Surge Mac

**Importformat:** Surge INI / Managed Profile

Verwenden Sie eine Surge-Konfiguration oder die URL einer verwalteten Konfiguration. Ein allgemeines V2Ray-Abonnement ist keine vollständige Surge-Konfiguration.

### Schnelleinrichtung

1. Besorgen Sie ein vollständiges Profil im oben angegebenen Format. Importieren Sie eine vom Client unterstützte lokale Datei oder entfernte Profil-URL, aktualisieren Sie das Profil und wählen Sie es aus. Gewöhnliche Knotenabonnements und Konfigurationen anderer Apps sind nicht grundsätzlich austauschbar.
2. Wenn das Profil eine Auswahl bietet, wählen Sie einen Knoten oder eine Proxy-Gruppe und aktivieren Sie anschließend den in der Client-Dokumentation beschriebenen Proxy-/VPN-Modus. Erteilen Sie die VPN-Berechtigung des Betriebssystems nur der von Ihnen installierten offiziellen App. Prüfen Sie nach dem Verbinden den tatsächlichen Zugriff.
3. Schlägt die Aktualisierung fehl, prüfen Sie URL, Netzwerk und HTTP-Fehler. Bei Einlesefehlern prüfen Sie Format und Core-Version. Gelingt der Import, aber nicht die Verbindung, aktualisieren Sie das Abonnement, versuchen Sie einen anderen unterstützten Knoten und prüfen Sie dann das Fehlerprotokoll des Clients. Eine erfolgreiche Aktualisierung oder ein Latenztest garantiert weder Verfügbarkeit noch Sicherheit.

Prüfen Sie die unterstützten Protokolle und die installierte Core-Version. Der Import von Knoten garantiert nicht, dass sämtliche Regeln, DNS-Einstellungen oder erweiterten Felder übernommen werden.

[Offizielle Anleitung [English]](https://manual.nssurge.com/getting-started/quick-start.html)


<a id="quantumult-x"></a>

## Quantumult X

**Importformat:** Quantumult X / server_remote

Quantumult X verwendet eigene Konfigurationen und entfernte Serverressourcen. Eine vollständige Konfiguration und eine Knotenressource sind unterschiedliche Eingaben.

Die offiziellen Anleitungen für Anwender sind begrenzt. Nutzen Sie die kurzen Einrichtungsschritte und die unten verlinkte, überprüfte offizielle Formatreferenz.

### Schnelleinrichtung

1. Besorgen Sie ein vollständiges Profil im oben angegebenen Format. Importieren Sie eine vom Client unterstützte lokale Datei oder entfernte Profil-URL, aktualisieren Sie das Profil und wählen Sie es aus. Gewöhnliche Knotenabonnements und Konfigurationen anderer Apps sind nicht grundsätzlich austauschbar.
2. Wenn das Profil eine Auswahl bietet, wählen Sie einen Knoten oder eine Proxy-Gruppe und aktivieren Sie anschließend den in der Client-Dokumentation beschriebenen Proxy-/VPN-Modus. Erteilen Sie die VPN-Berechtigung des Betriebssystems nur der von Ihnen installierten offiziellen App. Prüfen Sie nach dem Verbinden den tatsächlichen Zugriff.
3. Schlägt die Aktualisierung fehl, prüfen Sie URL, Netzwerk und HTTP-Fehler. Bei Einlesefehlern prüfen Sie Format und Core-Version. Gelingt der Import, aber nicht die Verbindung, aktualisieren Sie das Abonnement, versuchen Sie einen anderen unterstützten Knoten und prüfen Sie dann das Fehlerprotokoll des Clients. Eine erfolgreiche Aktualisierung oder ein Latenztest garantiert weder Verfügbarkeit noch Sicherheit.

Prüfen Sie die unterstützten Protokolle und die installierte Core-Version. Der Import von Knoten garantiert nicht, dass sämtliche Regeln, DNS-Einstellungen oder erweiterten Felder übernommen werden.

Diese Kurzanleitung beschreibt das überprüfte Eingabeformat und den grundlegenden Ablauf. Die verlinkten technischen Referenzen sind keine Schritt-für-Schritt-Anleitung für Anwender; die Bezeichnungen in der Oberfläche können je nach Version abweichen.

- [Technische Referenz [中文 / English]](https://github.com/crossutility/Quantumult-X/blob/master/sample.conf)

<a id="sing-box"></a>

## sing-box for Apple platforms

**Importformat:** sing-box JSON

### Schnelleinrichtung

1. Besorgen Sie ein vollständiges sing-box JSON-Profil, das zur Core-Version des Clients passt. Fügen Sie es als lokales oder entferntes Profil hinzu und aktualisieren Sie es. Eine Liste von Knoten-URLs oder eine Clash-YAML-Datei lässt sich nicht als natives sing-box JSON verwenden.
2. Wenn das Profil eine Auswahl bietet, wählen Sie einen Knoten oder eine Proxy-Gruppe und aktivieren Sie anschließend den in der Client-Dokumentation beschriebenen Proxy-/VPN-Modus. Erteilen Sie die VPN-Berechtigung des Betriebssystems nur der von Ihnen installierten offiziellen App. Prüfen Sie nach dem Verbinden den tatsächlichen Zugriff.
3. Schlägt die Aktualisierung fehl, prüfen Sie URL, Netzwerk und HTTP-Fehler. Bei Einlesefehlern prüfen Sie Format und Core-Version. Gelingt der Import, aber nicht die Verbindung, aktualisieren Sie das Abonnement, versuchen Sie einen anderen unterstützten Knoten und prüfen Sie dann das Fehlerprotokoll des Clients. Eine erfolgreiche Aktualisierung oder ein Latenztest garantiert weder Verfügbarkeit noch Sicherheit.

Prüfen Sie die unterstützten Protokolle und die installierte Core-Version. Der Import von Knoten garantiert nicht, dass sämtliche Regeln, DNS-Einstellungen oder erweiterten Felder übernommen werden.

[Offizielle Anleitung [English]](https://sing-box.sagernet.org/clients/general/)


<a id="v2rayng"></a>

## v2rayNG

**Importformat:** URI / Base64

Die offiziellen Anleitungen für Anwender sind begrenzt. Nutzen Sie die kurzen Einrichtungsschritte und die unten verlinkte, überprüfte offizielle Formatreferenz.

### Schnelleinrichtung

1. Fügen Sie im Abonnement- oder Profilbereich des Clients eine unterstützte Knoten-URL oder ein gewöhnliches URI/Base64-Abonnement hinzu. Aktualisieren Sie das Abonnement und prüfen Sie, ob die erwarteten Knoten erscheinen.
2. Wenn das Profil eine Auswahl bietet, wählen Sie einen Knoten oder eine Proxy-Gruppe und aktivieren Sie anschließend den in der Client-Dokumentation beschriebenen Proxy-/VPN-Modus. Erteilen Sie die VPN-Berechtigung des Betriebssystems nur der von Ihnen installierten offiziellen App. Prüfen Sie nach dem Verbinden den tatsächlichen Zugriff.
3. Schlägt die Aktualisierung fehl, prüfen Sie URL, Netzwerk und HTTP-Fehler. Bei Einlesefehlern prüfen Sie Format und Core-Version. Gelingt der Import, aber nicht die Verbindung, aktualisieren Sie das Abonnement, versuchen Sie einen anderen unterstützten Knoten und prüfen Sie dann das Fehlerprotokoll des Clients. Eine erfolgreiche Aktualisierung oder ein Latenztest garantiert weder Verfügbarkeit noch Sicherheit.

Prüfen Sie die unterstützten Protokolle und die installierte Core-Version. Der Import von Knoten garantiert nicht, dass sämtliche Regeln, DNS-Einstellungen oder erweiterten Felder übernommen werden.

Diese Kurzanleitung beschreibt das überprüfte Eingabeformat und den grundlegenden Ablauf. Die verlinkten technischen Referenzen sind keine Schritt-für-Schritt-Anleitung für Anwender; die Bezeichnungen in der Oberfläche können je nach Version abweichen.

- [Technische Referenz [English]](https://github.com/2dust/v2rayNG/wiki/Mode)

<a id="clash-meta-android"></a>

## Clash Meta for Android

**Importformat:** Clash / Mihomo YAML

Die offiziellen Anleitungen für Anwender sind begrenzt. Nutzen Sie die kurzen Einrichtungsschritte und die unten verlinkte, überprüfte offizielle Formatreferenz.

### Schnelleinrichtung

1. Besorgen Sie ein vollständiges, mit Clash/Mihomo kompatibles YAML-Profil. Importieren Sie es als lokales oder entferntes Profil, aktualisieren Sie es und wählen Sie es aus. Das oben genannte gewöhnliche Abonnement ist kein vollständiges YAML-Profil.
2. Wenn das Profil eine Auswahl bietet, wählen Sie einen Knoten oder eine Proxy-Gruppe und aktivieren Sie anschließend den in der Client-Dokumentation beschriebenen Proxy-/VPN-Modus. Erteilen Sie die VPN-Berechtigung des Betriebssystems nur der von Ihnen installierten offiziellen App. Prüfen Sie nach dem Verbinden den tatsächlichen Zugriff.
3. Schlägt die Aktualisierung fehl, prüfen Sie URL, Netzwerk und HTTP-Fehler. Bei Einlesefehlern prüfen Sie Format und Core-Version. Gelingt der Import, aber nicht die Verbindung, aktualisieren Sie das Abonnement, versuchen Sie einen anderen unterstützten Knoten und prüfen Sie dann das Fehlerprotokoll des Clients. Eine erfolgreiche Aktualisierung oder ein Latenztest garantiert weder Verfügbarkeit noch Sicherheit.

Prüfen Sie die unterstützten Protokolle und die installierte Core-Version. Der Import von Knoten garantiert nicht, dass sämtliche Regeln, DNS-Einstellungen oder erweiterten Felder übernommen werden.

Diese Kurzanleitung beschreibt das überprüfte Eingabeformat und den grundlegenden Ablauf. Die verlinkten technischen Referenzen sind keine Schritt-für-Schritt-Anleitung für Anwender; die Bezeichnungen in der Oberfläche können je nach Version abweichen.

- [Technische Referenz [English]](https://wiki.metacubex.one/en/handbook/syntax/)
- [Technische Referenz [English]](https://github.com/MetaCubeX/ClashMetaForAndroid#automation)

<a id="surfboard"></a>

## Surfboard

**Importformat:** Surfboard / Surge profile

Verwenden Sie eine Surge-Konfiguration oder die URL einer verwalteten Konfiguration. Ein allgemeines V2Ray-Abonnement ist keine vollständige Surge-Konfiguration.

Die offiziellen Anleitungen für Anwender sind begrenzt. Nutzen Sie die kurzen Einrichtungsschritte und die unten verlinkte, überprüfte offizielle Formatreferenz.

### Schnelleinrichtung

1. Besorgen Sie ein vollständiges Profil im oben angegebenen Format. Importieren Sie eine vom Client unterstützte lokale Datei oder entfernte Profil-URL, aktualisieren Sie das Profil und wählen Sie es aus. Gewöhnliche Knotenabonnements und Konfigurationen anderer Apps sind nicht grundsätzlich austauschbar.
2. Wenn das Profil eine Auswahl bietet, wählen Sie einen Knoten oder eine Proxy-Gruppe und aktivieren Sie anschließend den in der Client-Dokumentation beschriebenen Proxy-/VPN-Modus. Erteilen Sie die VPN-Berechtigung des Betriebssystems nur der von Ihnen installierten offiziellen App. Prüfen Sie nach dem Verbinden den tatsächlichen Zugriff.
3. Schlägt die Aktualisierung fehl, prüfen Sie URL, Netzwerk und HTTP-Fehler. Bei Einlesefehlern prüfen Sie Format und Core-Version. Gelingt der Import, aber nicht die Verbindung, aktualisieren Sie das Abonnement, versuchen Sie einen anderen unterstützten Knoten und prüfen Sie dann das Fehlerprotokoll des Clients. Eine erfolgreiche Aktualisierung oder ein Latenztest garantiert weder Verfügbarkeit noch Sicherheit.

Prüfen Sie die unterstützten Protokolle und die installierte Core-Version. Der Import von Knoten garantiert nicht, dass sämtliche Regeln, DNS-Einstellungen oder erweiterten Felder übernommen werden.

Diese Kurzanleitung beschreibt das überprüfte Eingabeformat und den grundlegenden Ablauf. Die verlinkten technischen Referenzen sind keine Schritt-für-Schritt-Anleitung für Anwender; die Bezeichnungen in der Oberfläche können je nach Version abweichen.

- [Technische Referenz [English]](https://getsurfboard.com/docs/profile-format/overview/)

<a id="nekobox-android"></a>

## NekoBox for Android

**Importformat:** URI / Base64 · Clash proxies · sing-box outbounds

Beim Abonnementimport werden unterstützte Knoten übernommen. Gehen Sie nicht davon aus, dass Regeln und andere Einstellungen des ursprünglichen Profils erhalten bleiben.

### Schnelleinrichtung

1. Fügen Sie im Abonnement- oder Profilbereich des Clients eine unterstützte Knoten-URL oder ein gewöhnliches URI/Base64-Abonnement hinzu. Aktualisieren Sie das Abonnement und prüfen Sie, ob die erwarteten Knoten erscheinen.
2. Wenn das Profil eine Auswahl bietet, wählen Sie einen Knoten oder eine Proxy-Gruppe und aktivieren Sie anschließend den in der Client-Dokumentation beschriebenen Proxy-/VPN-Modus. Erteilen Sie die VPN-Berechtigung des Betriebssystems nur der von Ihnen installierten offiziellen App. Prüfen Sie nach dem Verbinden den tatsächlichen Zugriff.
3. Schlägt die Aktualisierung fehl, prüfen Sie URL, Netzwerk und HTTP-Fehler. Bei Einlesefehlern prüfen Sie Format und Core-Version. Gelingt der Import, aber nicht die Verbindung, aktualisieren Sie das Abonnement, versuchen Sie einen anderen unterstützten Knoten und prüfen Sie dann das Fehlerprotokoll des Clients. Eine erfolgreiche Aktualisierung oder ein Latenztest garantiert weder Verfügbarkeit noch Sicherheit.

Prüfen Sie die unterstützten Protokolle und die installierte Core-Version. Der Import von Knoten garantiert nicht, dass sämtliche Regeln, DNS-Einstellungen oder erweiterten Felder übernommen werden.

[Offizielle Anleitung [中文]](https://matsuridayo.github.io/nb4a-configuration/)


<a id="shadowrocket"></a>

## Shadowrocket

**Importformat:** Shadowrocket subscriptions / profiles

Die offiziellen Anleitungen für Anwender sind begrenzt. Nutzen Sie die kurzen Einrichtungsschritte und die unten verlinkte, überprüfte offizielle Formatreferenz.

### Schnelleinrichtung

1. Bereiten Sie ein von dieser App unterstütztes Knotenabonnement oder eine einzelne Knotenkonfiguration vor. Fügen Sie es über das in der App-Dokumentation beschriebene Importverfahren hinzu, aktualisieren Sie Abonnements, soweit unterstützt, und prüfen Sie, ob die Knoten erscheinen. Eine Knotenliste und ein vollständiges Routing-Profil sind unterschiedliche Eingaben.
2. Wenn das Profil eine Auswahl bietet, wählen Sie einen Knoten oder eine Proxy-Gruppe und aktivieren Sie anschließend den in der Client-Dokumentation beschriebenen Proxy-/VPN-Modus. Erteilen Sie die VPN-Berechtigung des Betriebssystems nur der von Ihnen installierten offiziellen App. Prüfen Sie nach dem Verbinden den tatsächlichen Zugriff.
3. Schlägt die Aktualisierung fehl, prüfen Sie URL, Netzwerk und HTTP-Fehler. Bei Einlesefehlern prüfen Sie Format und Core-Version. Gelingt der Import, aber nicht die Verbindung, aktualisieren Sie das Abonnement, versuchen Sie einen anderen unterstützten Knoten und prüfen Sie dann das Fehlerprotokoll des Clients. Eine erfolgreiche Aktualisierung oder ein Latenztest garantiert weder Verfügbarkeit noch Sicherheit.

Prüfen Sie die unterstützten Protokolle und die installierte Core-Version. Der Import von Knoten garantiert nicht, dass sämtliche Regeln, DNS-Einstellungen oder erweiterten Felder übernommen werden.

- [Offizielle Produktinformationen [English]](https://apps.apple.com/us/app/shadowrocket/id932747118)

<a id="stash"></a>

## Stash

**Importformat:** Stash / Clash YAML

### Schnelleinrichtung

1. Besorgen Sie ein vollständiges, mit Clash/Mihomo kompatibles YAML-Profil. Importieren Sie es als lokales oder entferntes Profil, aktualisieren Sie es und wählen Sie es aus. Das oben genannte gewöhnliche Abonnement ist kein vollständiges YAML-Profil.
2. Wenn das Profil eine Auswahl bietet, wählen Sie einen Knoten oder eine Proxy-Gruppe und aktivieren Sie anschließend den in der Client-Dokumentation beschriebenen Proxy-/VPN-Modus. Erteilen Sie die VPN-Berechtigung des Betriebssystems nur der von Ihnen installierten offiziellen App. Prüfen Sie nach dem Verbinden den tatsächlichen Zugriff.
3. Schlägt die Aktualisierung fehl, prüfen Sie URL, Netzwerk und HTTP-Fehler. Bei Einlesefehlern prüfen Sie Format und Core-Version. Gelingt der Import, aber nicht die Verbindung, aktualisieren Sie das Abonnement, versuchen Sie einen anderen unterstützten Knoten und prüfen Sie dann das Fehlerprotokoll des Clients. Eine erfolgreiche Aktualisierung oder ein Latenztest garantiert weder Verfügbarkeit noch Sicherheit.

Prüfen Sie die unterstützten Protokolle und die installierte Core-Version. Der Import von Knoten garantiert nicht, dass sämtliche Regeln, DNS-Einstellungen oder erweiterten Felder übernommen werden.

[Offizielle Anleitung [English]](https://stash.wiki/en/get-started)


<a id="loon"></a>

## Loon

**Importformat:** URI / Base64 · Loon configuration

Loon verwendet eigene Konfigurations- und Knotenabonnementformate. Prüfen Sie jedes Protokoll und Feld, statt vollständige Kompatibilität mit Surge oder Clash vorauszusetzen.

### Schnelleinrichtung

1. Fügen Sie im Abonnement- oder Profilbereich des Clients eine unterstützte Knoten-URL oder ein gewöhnliches URI/Base64-Abonnement hinzu. Aktualisieren Sie das Abonnement und prüfen Sie, ob die erwarteten Knoten erscheinen.
2. Wenn das Profil eine Auswahl bietet, wählen Sie einen Knoten oder eine Proxy-Gruppe und aktivieren Sie anschließend den in der Client-Dokumentation beschriebenen Proxy-/VPN-Modus. Erteilen Sie die VPN-Berechtigung des Betriebssystems nur der von Ihnen installierten offiziellen App. Prüfen Sie nach dem Verbinden den tatsächlichen Zugriff.
3. Schlägt die Aktualisierung fehl, prüfen Sie URL, Netzwerk und HTTP-Fehler. Bei Einlesefehlern prüfen Sie Format und Core-Version. Gelingt der Import, aber nicht die Verbindung, aktualisieren Sie das Abonnement, versuchen Sie einen anderen unterstützten Knoten und prüfen Sie dann das Fehlerprotokoll des Clients. Eine erfolgreiche Aktualisierung oder ein Latenztest garantiert weder Verfügbarkeit noch Sicherheit.

Prüfen Sie die unterstützten Protokolle und die installierte Core-Version. Der Import von Knoten garantiert nicht, dass sämtliche Regeln, DNS-Einstellungen oder erweiterten Felder übernommen werden.

[Offizielle Anleitung [English]](https://nsloon.app/en/docs/Node/subscription/)


<a id="egern"></a>

## Egern

**Importformat:** Egern Profile.yaml / proxies YAML

Egern YAML ist ein eigenes Profilformat und kein Clash/Mihomo YAML.

Die offiziellen Anleitungen für Anwender sind begrenzt. Nutzen Sie die kurzen Einrichtungsschritte und die unten verlinkte, überprüfte offizielle Formatreferenz.

### Schnelleinrichtung

1. Besorgen Sie ein vollständiges Profil im oben angegebenen Format. Importieren Sie eine vom Client unterstützte lokale Datei oder entfernte Profil-URL, aktualisieren Sie das Profil und wählen Sie es aus. Gewöhnliche Knotenabonnements und Konfigurationen anderer Apps sind nicht grundsätzlich austauschbar.
2. Wenn das Profil eine Auswahl bietet, wählen Sie einen Knoten oder eine Proxy-Gruppe und aktivieren Sie anschließend den in der Client-Dokumentation beschriebenen Proxy-/VPN-Modus. Erteilen Sie die VPN-Berechtigung des Betriebssystems nur der von Ihnen installierten offiziellen App. Prüfen Sie nach dem Verbinden den tatsächlichen Zugriff.
3. Schlägt die Aktualisierung fehl, prüfen Sie URL, Netzwerk und HTTP-Fehler. Bei Einlesefehlern prüfen Sie Format und Core-Version. Gelingt der Import, aber nicht die Verbindung, aktualisieren Sie das Abonnement, versuchen Sie einen anderen unterstützten Knoten und prüfen Sie dann das Fehlerprotokoll des Clients. Eine erfolgreiche Aktualisierung oder ein Latenztest garantiert weder Verfügbarkeit noch Sicherheit.

Prüfen Sie die unterstützten Protokolle und die installierte Core-Version. Der Import von Knoten garantiert nicht, dass sämtliche Regeln, DNS-Einstellungen oder erweiterten Felder übernommen werden.

Diese Kurzanleitung beschreibt das überprüfte Eingabeformat und den grundlegenden Ablauf. Die verlinkten technischen Referenzen sind keine Schritt-für-Schritt-Anleitung für Anwender; die Bezeichnungen in der Oberfläche können je nach Version abweichen.

- [Technische Referenz [English]](https://egernapp.com/docs/configuration/policy_groups/)

<a id="streisand"></a>

## Streisand

**Importformat:** Supported node configurations

Die offiziellen Anleitungen für Anwender sind begrenzt. Nutzen Sie die kurzen Einrichtungsschritte und die unten verlinkte, überprüfte offizielle Formatreferenz.

### Schnelleinrichtung

1. Bereiten Sie ein von dieser App unterstütztes Knotenabonnement oder eine einzelne Knotenkonfiguration vor. Fügen Sie es über das in der App-Dokumentation beschriebene Importverfahren hinzu, aktualisieren Sie Abonnements, soweit unterstützt, und prüfen Sie, ob die Knoten erscheinen. Eine Knotenliste und ein vollständiges Routing-Profil sind unterschiedliche Eingaben.
2. Wenn das Profil eine Auswahl bietet, wählen Sie einen Knoten oder eine Proxy-Gruppe und aktivieren Sie anschließend den in der Client-Dokumentation beschriebenen Proxy-/VPN-Modus. Erteilen Sie die VPN-Berechtigung des Betriebssystems nur der von Ihnen installierten offiziellen App. Prüfen Sie nach dem Verbinden den tatsächlichen Zugriff.
3. Schlägt die Aktualisierung fehl, prüfen Sie URL, Netzwerk und HTTP-Fehler. Bei Einlesefehlern prüfen Sie Format und Core-Version. Gelingt der Import, aber nicht die Verbindung, aktualisieren Sie das Abonnement, versuchen Sie einen anderen unterstützten Knoten und prüfen Sie dann das Fehlerprotokoll des Clients. Eine erfolgreiche Aktualisierung oder ein Latenztest garantiert weder Verfügbarkeit noch Sicherheit.

Prüfen Sie die unterstützten Protokolle und die installierte Core-Version. Der Import von Knoten garantiert nicht, dass sämtliche Regeln, DNS-Einstellungen oder erweiterten Felder übernommen werden.

- [Offizielle Produktinformationen [English]](https://streisand.pages.dev/)

<a id="potatso"></a>

## Potatso

**Importformat:** Mihomo / Clash YAML · supported node links

Die offiziellen Anleitungen für Anwender sind begrenzt. Nutzen Sie die kurzen Einrichtungsschritte und die unten verlinkte, überprüfte offizielle Formatreferenz.

### Schnelleinrichtung

1. Besorgen Sie ein vollständiges, mit Clash/Mihomo kompatibles YAML-Profil. Importieren Sie es als lokales oder entferntes Profil, aktualisieren Sie es und wählen Sie es aus. Das oben genannte gewöhnliche Abonnement ist kein vollständiges YAML-Profil.
2. Wenn das Profil eine Auswahl bietet, wählen Sie einen Knoten oder eine Proxy-Gruppe und aktivieren Sie anschließend den in der Client-Dokumentation beschriebenen Proxy-/VPN-Modus. Erteilen Sie die VPN-Berechtigung des Betriebssystems nur der von Ihnen installierten offiziellen App. Prüfen Sie nach dem Verbinden den tatsächlichen Zugriff.
3. Schlägt die Aktualisierung fehl, prüfen Sie URL, Netzwerk und HTTP-Fehler. Bei Einlesefehlern prüfen Sie Format und Core-Version. Gelingt der Import, aber nicht die Verbindung, aktualisieren Sie das Abonnement, versuchen Sie einen anderen unterstützten Knoten und prüfen Sie dann das Fehlerprotokoll des Clients. Eine erfolgreiche Aktualisierung oder ein Latenztest garantiert weder Verfügbarkeit noch Sicherheit.

Prüfen Sie die unterstützten Protokolle und die installierte Core-Version. Der Import von Knoten garantiert nicht, dass sämtliche Regeln, DNS-Einstellungen oder erweiterten Felder übernommen werden.

- [Offizielle Produktinformationen [English]](https://potatso.com/)

<a id="openclash"></a>

## OpenClash

**Importformat:** Clash / Mihomo YAML

### Schnelleinrichtung

1. Prüfen Sie vor der Installation Firmware, CPU-Architektur, benötigte Pakete und verfügbaren Arbeitsspeicher. Sichern Sie die Routerkonfiguration und halten Sie eine funktionierende Verwaltungsverbindung bereit. Importieren Sie nur ein unterstütztes Abonnement oder Profil, aktualisieren Sie es, wählen Sie den ausgehenden Knoten oder die Gruppe und aktivieren Sie das Plugin gemäß seiner offiziellen Anleitung.
2. Schlägt die Aktualisierung fehl, prüfen Sie URL, Netzwerk und HTTP-Fehler. Bei Einlesefehlern prüfen Sie Format und Core-Version. Gelingt der Import, aber nicht die Verbindung, aktualisieren Sie das Abonnement, versuchen Sie einen anderen unterstützten Knoten und prüfen Sie dann das Fehlerprotokoll des Clients. Eine erfolgreiche Aktualisierung oder ein Latenztest garantiert weder Verfügbarkeit noch Sicherheit.

Prüfen Sie die unterstützten Protokolle und die installierte Core-Version. Der Import von Knoten garantiert nicht, dass sämtliche Regeln, DNS-Einstellungen oder erweiterten Felder übernommen werden.

[Offizielle Anleitung [中文]](https://github.com/vernesong/OpenClash#快速开始)


<a id="passwall"></a>

## PassWall2 / PassWall

**Importformat:** Supported node URI subscriptions

Beim Abonnementimport werden unterstützte Knoten übernommen. Gehen Sie nicht davon aus, dass Regeln und andere Einstellungen des ursprünglichen Profils erhalten bleiben.

Die offiziellen Anleitungen für Anwender sind begrenzt. Nutzen Sie die kurzen Einrichtungsschritte und die unten verlinkte, überprüfte offizielle Formatreferenz.

### Schnelleinrichtung

1. Prüfen Sie vor der Installation Firmware, CPU-Architektur, benötigte Pakete und verfügbaren Arbeitsspeicher. Sichern Sie die Routerkonfiguration und halten Sie eine funktionierende Verwaltungsverbindung bereit. Importieren Sie nur ein unterstütztes Abonnement oder Profil, aktualisieren Sie es, wählen Sie den ausgehenden Knoten oder die Gruppe und aktivieren Sie das Plugin gemäß seiner offiziellen Anleitung.
2. Schlägt die Aktualisierung fehl, prüfen Sie URL, Netzwerk und HTTP-Fehler. Bei Einlesefehlern prüfen Sie Format und Core-Version. Gelingt der Import, aber nicht die Verbindung, aktualisieren Sie das Abonnement, versuchen Sie einen anderen unterstützten Knoten und prüfen Sie dann das Fehlerprotokoll des Clients. Eine erfolgreiche Aktualisierung oder ein Latenztest garantiert weder Verfügbarkeit noch Sicherheit.

Prüfen Sie die unterstützten Protokolle und die installierte Core-Version. Der Import von Knoten garantiert nicht, dass sämtliche Regeln, DNS-Einstellungen oder erweiterten Felder übernommen werden.

Diese Kurzanleitung beschreibt das überprüfte Eingabeformat und den grundlegenden Ablauf. Die verlinkten technischen Referenzen sind keine Schritt-für-Schritt-Anleitung für Anwender; die Bezeichnungen in der Oberfläche können je nach Version abweichen.

- [Technische Referenz [English]](https://github.com/Openwrt-Passwall/openwrt-passwall2)
- [Technische Referenz [English]](https://github.com/Openwrt-Passwall/openwrt-passwall)

<a id="nikki"></a>

## Nikki

**Importformat:** Mihomo YAML: proxies / proxy-providers

### Schnelleinrichtung

1. Prüfen Sie vor der Installation Firmware, CPU-Architektur, benötigte Pakete und verfügbaren Arbeitsspeicher. Sichern Sie die Routerkonfiguration und halten Sie eine funktionierende Verwaltungsverbindung bereit. Importieren Sie nur ein unterstütztes Abonnement oder Profil, aktualisieren Sie es, wählen Sie den ausgehenden Knoten oder die Gruppe und aktivieren Sie das Plugin gemäß seiner offiziellen Anleitung.
2. Schlägt die Aktualisierung fehl, prüfen Sie URL, Netzwerk und HTTP-Fehler. Bei Einlesefehlern prüfen Sie Format und Core-Version. Gelingt der Import, aber nicht die Verbindung, aktualisieren Sie das Abonnement, versuchen Sie einen anderen unterstützten Knoten und prüfen Sie dann das Fehlerprotokoll des Clients. Eine erfolgreiche Aktualisierung oder ein Latenztest garantiert weder Verfügbarkeit noch Sicherheit.

Prüfen Sie die unterstützten Protokolle und die installierte Core-Version. Der Import von Knoten garantiert nicht, dass sämtliche Regeln, DNS-Einstellungen oder erweiterten Felder übernommen werden.

[Offizielle Anleitung [中文]](https://github.com/nikkinikki-org/OpenWrt-nikki/wiki)


<a id="homeproxy"></a>

## HomeProxy

**Importformat:** HomeProxy node subscriptions

HomeProxy verwaltet Knoten und Abonnements über seine eigene Oberfläche. Prüfen Sie die von der installierten Version unterstützten Formate. Die interne Verwendung von sing-box bedeutet nicht, dass beliebige vollständige sing-box JSON-Profile importiert werden können.

Die offiziellen Anleitungen für Anwender sind begrenzt. Nutzen Sie die kurzen Einrichtungsschritte und die unten verlinkte, überprüfte offizielle Formatreferenz.

### Schnelleinrichtung

1. Prüfen Sie vor der Installation Firmware, CPU-Architektur, benötigte Pakete und verfügbaren Arbeitsspeicher. Sichern Sie die Routerkonfiguration und halten Sie eine funktionierende Verwaltungsverbindung bereit. Importieren Sie nur ein unterstütztes Abonnement oder Profil, aktualisieren Sie es, wählen Sie den ausgehenden Knoten oder die Gruppe und aktivieren Sie das Plugin gemäß seiner offiziellen Anleitung.
2. Schlägt die Aktualisierung fehl, prüfen Sie URL, Netzwerk und HTTP-Fehler. Bei Einlesefehlern prüfen Sie Format und Core-Version. Gelingt der Import, aber nicht die Verbindung, aktualisieren Sie das Abonnement, versuchen Sie einen anderen unterstützten Knoten und prüfen Sie dann das Fehlerprotokoll des Clients. Eine erfolgreiche Aktualisierung oder ein Latenztest garantiert weder Verfügbarkeit noch Sicherheit.

Prüfen Sie die unterstützten Protokolle und die installierte Core-Version. Der Import von Knoten garantiert nicht, dass sämtliche Regeln, DNS-Einstellungen oder erweiterten Felder übernommen werden.

Diese Kurzanleitung beschreibt das überprüfte Eingabeformat und den grundlegenden Ablauf. Die verlinkten technischen Referenzen sind keine Schritt-für-Schritt-Anleitung für Anwender; die Bezeichnungen in der Oberfläche können je nach Version abweichen.

- [Technische Referenz [English]](https://github.com/immortalwrt/homeproxy)
