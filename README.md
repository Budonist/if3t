# if3t.de

Statische persönliche Website und App-Seiten. Kein Build und keine Abhängigkeiten erforderlich.

## Status

Erste lokale Version. **Noch nicht für den öffentlichen Upload freigegeben:** Impressum und Datenschutztexte sind sichtbare Arbeitsentwürfe. Offene Fakten stehen im [Briefing](WEBSITE-BRIEFING.md) und im [rechtlichen Status](RECHTLICHER-STATUS.md). Keine App-Store- oder TestFlight-Verfügbarkeit zugesichert.

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
2. Bestehenden Webbestand sichern. Dokumentenverzeichnisse und Zertifikate für `if3t.de`, `www.if3t.de` und beide App-Subdomains im Hosting-Panel prüfen. Separate, möglichst nebeneinanderliegende Dokumentenverzeichnisse verwenden.
3. SFTP-Verbindung mit den im Panel bereitgestellten Daten herstellen; Hostschlüssel überprüfen. Keine Zugangsdaten in Git ablegen.
4. Nur den **Inhalt** des jeweiligen `site/`-Unterverzeichnisses in das zugehörige Dokumentenverzeichnis übertragen, einschließlich `.htaccess`. Nicht das gesamte Repository hochladen. Bei Änderungen alle betroffenen CSS-Kopien hochladen.
5. Die konkreten Zielpfade nach Prüfung hier dokumentieren. Sie sind derzeit noch unbekannt; `/` ist kein bestätigtes Uploadziel.
6. Alle sieben HTTPS-Seiten, HTTP-Weiterleitungen, Apex-Weiterleitung, Canonicals, Header und echte 404-Antworten prüfen. App-Subdomains dürfen nicht auf www umgeleitet werden. Bei HTTP-500 `.htaccess` und Hostingmodule untersuchen; Sicherheitsregeln nicht blind entfernen.
7. Bei Fehlern den gesicherten Webbestand wiederherstellen. Erst nach erfolgreicher Liveprüfung die App-Datenschutzadressen in App Store Connect eintragen.

Kein automatischer Upload oder Deployment-Workflow ist eingerichtet. GitHub sichert den Quellcode; ein Push veröffentlicht die Website nicht bei IONOS.

## Prüfung

```sh
python3 tools/check_site.py
node --check site/main/js/navigation.js
```

Der lokale Prüfer untersucht Seitenstruktur, Ressourcen, Domain-Links und gemeinsame Ressourcen. Er ersetzt keine vollständige HTML-, Barrierefreiheits-, iOS- oder Apache-Prüfung.
