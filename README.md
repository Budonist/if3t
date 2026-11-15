# if3t.de

Statische persönliche Website und App-Seiten. Kein Build und keine Abhängigkeiten erforderlich.

## Status

Erste lokale Version. **Noch nicht für den öffentlichen Upload freigegeben:** Impressum und Datenschutztexte sind sichtbare Arbeitsentwürfe. Offene Fakten stehen im [Briefing](WEBSITE-BRIEFING.md) und im [rechtlichen Status](RECHTLICHER-STATUS.md). Beide Apps werden laut Betreiber über TestFlight verteilt; ein App-Store-Release ist geplant.

## Lokale Vorschau

Aus dem Repository-Verzeichnis in drei Terminals starten:

```sh
python3 -m http.server 8000 --bind 127.0.0.1 --directory site/main
python3 -m http.server 8001 --bind 127.0.0.1 --directory site/sonnenstand-app
python3 -m http.server 8002 --bind 127.0.0.1 --directory site/sektoren-app
```

Die Ports entsprechen den drei späteren Domains. Produktionslinks sind bewusst absolut und zeigen auf die späteren Domains. Für eine vollständig lokal verlinkte Vorschau `python3 tools/preview.py` verwenden: Der Server bildet alle drei Hosts lokal unter Port 8000–8002 ab und ersetzt deren Links ausschließlich in der HTTP-Antwort. Quelldateien bleiben unverändert. Beenden mit Strg+C.

Ein einfacher Python-Server führt `.htaccess` nicht aus. HTTPS, Apache-Weiterleitungen, Sicherheitsheader und Caching müssen auf einem passenden Apache-System bzw. beim IONOS-Livetest separat geprüft werden.

## Bearbeitung

Inhalte liegen unter `site/main`, `site/sonnenstand-app` und `site/sektoren-app`. CSS und Favicon werden pro Domain lokal ausgeliefert. Änderungen an gemeinsamen Ressourcen in alle drei Bereiche übernehmen. JavaScript nur für die Hauptnavigation; ohne JavaScript bleibt sie sichtbar.

## Upload zu IONOS (gesonderter Freigabeschritt)

1. Rechtliche Texte und Betreiberangaben abschließen; Entwurfshinweise erst danach entfernen. Öffentliche App-Namen, Release-Versionen, TestFlight, Geodaten- und Audio-Lizenzen bestätigen.
2. Bestehenden Webbestand sichern. Dokumentenverzeichnisse und Zertifikate für `if3t.de`, `www.if3t.de` und beide App-Subdomains im Hosting-Panel prüfen. Die unten dokumentierten verschachtelten Dokumentenverzeichnisse verwenden. Domainzuordnungen im Panel kontrollieren; die Dateipfade allein belegen diese noch nicht.
3. SFTP-Verbindung mit den im Panel bereitgestellten Daten herstellen; Hostschlüssel überprüfen. Keine Zugangsdaten in Git ablegen.
4. Nur den **Inhalt** des jeweiligen `site/`-Unterverzeichnisses in das zugehörige Dokumentenverzeichnis übertragen, einschließlich `.htaccess`. Nicht das gesamte Repository hochladen. Bei Änderungen alle betroffenen CSS-Kopien hochladen.
5. Die folgenden Zielpfade verwenden. Je nach SFTP-Benutzer kann dessen sichtbares Startverzeichnis bereits `/if3t` sein. Nicht versehentlich einen zusätzlichen Ordner `if3t` darin erzeugen und keine Spiegelung mit Löschen unbekannter Serverdateien verwenden.
6. Alle sieben HTTPS-Seiten, HTTP-Weiterleitungen, Apex-Weiterleitung, Canonicals, Header und echte 404-Antworten prüfen. App-Subdomains dürfen nicht auf www umgeleitet werden. Bei HTTP-500 `.htaccess` und Hostingmodule untersuchen; Sicherheitsregeln nicht blind entfernen.
7. Bei Fehlern den gesicherten Webbestand wiederherstellen. Erst nach erfolgreicher Liveprüfung die App-Datenschutzadressen in App Store Connect eintragen.

### Vom Betreiber gemeldete Verzeichnisse

Absoluter Hauptpfad: `/kunden/homepages/26/d125682115/htdocs/if3t`.

| Inhalt aus dem Repository | Relativer Webspace-Pfad | Vorgesehene Domain |
| --- | --- | --- |
| `site/main/` | `/if3t` | `if3t.de` und `www.if3t.de` |
| `site/sonnenstand-app/` | `/if3t/sonnenstand-app` | `sonnenstand-app.if3t.de` |
| `site/sektoren-app/` | `/if3t/sektoren-app` | `sektoren-app.if3t.de` |

Die Subdomains wurden laut Betreiber angelegt. Ihre Zuordnung zu diesen Dokumentenverzeichnissen und SSL-Abdeckung bleiben live zu prüfen. Die Haupt-`.htaccess` beschränkt Hauptdomain-Weiterleitungen auf die Hauptdomain-Hosts. Direkte Aufrufe der App-Unterpfade über die Hauptdomain werden auf die App-Subdomains umgeleitet. Die App-Verzeichnisse enthalten jeweils eine eigene `.htaccess`.

Bei einem vorbereiteten Upload-ZIP entspricht dessen Ordner `if3t/` dem vorhandenen Serververzeichnis `/if3t`: **Ordnerinhalt zusammenführen**, nicht `/if3t/if3t` erzeugen. Bei separatem Upload der Hauptseite die bereits vorhandenen App-Unterordner nicht löschen.

Der aktuelle Inhalt ist eine Arbeitsversion mit sichtbaren rechtlichen Entwurfshinweisen. Ein Upload auf einen öffentlich erreichbaren Webspace macht diese Dateien öffentlich. Für einen geschützten Test muss ein Zugriffsschutz auf allen drei Domains tatsächlich eingerichtet und geprüft werden; das Paket selbst enthält keinen Passwortschutz.

Kein automatischer Upload oder Deployment-Workflow ist eingerichtet. GitHub sichert den Quellcode; ein Push veröffentlicht die Website nicht bei IONOS.

## Prüfung

```sh
python3 tools/check_site.py
node --check site/main/js/navigation.js
```

Der lokale Prüfer untersucht Seitenstruktur, Ressourcen, Domain-Links und gemeinsame Ressourcen. Er ersetzt keine vollständige HTML-, Barrierefreiheits-, iOS- oder Apache-Prüfung.
