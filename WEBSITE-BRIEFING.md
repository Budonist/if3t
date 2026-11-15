# Website-Briefing für if3t.de

Stand: 15. November 2026

Dieses Dokument ist die Arbeitsgrundlage für die spätere Umsetzung. Es ersetzt das ursprüngliche Website-Briefing. Die Erstellung dieses Dokuments umfasst keine Website-Implementierung, Veröffentlichung oder Änderung der iOS-Apps.

## 1. Ziel und Umfang

Eine kleine, schnelle, deutschsprachige Website stellt Mark-Alexander Kaldenbach und seine beiden iOS-Projekte vor. Sie bietet Kontaktmöglichkeiten, ein Impressum sowie getrennte Datenschutzerklärungen für die Website und jede App.

Die erste Version umfasst eine persönliche Startseite, zwei kurze App-Seiten und die zugehörigen rechtlichen Seiten. Keine Konten, Formulare, Werbung, Analysewerkzeuge, eingebetteten Karten, Social-Media-Widgets oder extern nachgeladenen Schriftarten. Externe Profile und Dienste werden ausschließlich verlinkt.

Nicht Bestandteil: Änderungen an den Apps, Blog, automatisiertes Deployment, App-Store-Anbindung, Newsletter oder kostenpflichtige Dienste.

## 2. Technische Grundlage

- Statisches HTML5 und CSS, ohne Framework, Paketinstallation oder Build-Pflicht.
- JavaScript nur bei Bedarf für die mobile Navigation; Inhalte und Links bleiben ohne JavaScript zugänglich.
- UTF-8 und `lang="de"` auf allen Seiten.
- Hosting auf dem vorhandenen IONOS-Webspace; manuelle Übertragung per SFTP.
- Quellcode und Dokumentation im Repository `Budonist/if3t` versionieren. Keine Zugangsdaten oder personenbezogenen Testdaten einchecken.
- Vorhandenen Checkout verwenden; keinen zusätzlichen Git-Worktree anlegen.

## 3. Domains, URLs und Dateien

| Adresse | Inhalt |
| --- | --- |
| `https://www.if3t.de/` | Persönliche Startseite |
| `https://www.if3t.de/impressum.html` | Gemeinsames Impressum |
| `https://www.if3t.de/datenschutz.html` | Datenschutz der Website einschließlich App-Webseiten |
| `https://sonnenstand-app.if3t.de/` | Kurzvorstellung der Sonnenstands-App |
| `https://sonnenstand-app.if3t.de/datenschutz.html` | Datenschutz der Sonnenstands-App |
| `https://sektoren-app.if3t.de/` | Kurzvorstellung der Berlin Sektoren App |
| `https://sektoren-app.if3t.de/datenschutz.html` | Datenschutz der Berlin Sektoren App |

Für Version 1 werden ausdrücklich `.html`-Adressen verwendet. Damit benötigen die rechtlichen Seiten keine Rewrite-Regeln für endungslose URLs. Die App-Datenschutzadressen bleiben bei späteren Erweiterungen der Landingpages unverändert.

Vorgesehene Ablagestruktur:

```text
site/
  main/
    index.html
    impressum.html
    datenschutz.html
    .htaccess
    css/style.css
    js/navigation.js
    favicon.svg
  sonnenstand-app/
    index.html
    datenschutz.html
    .htaccess
    css/style.css
    favicon.svg
  sektoren-app/
    index.html
    datenschutz.html
    .htaccess
    css/style.css
    favicon.svg
README.md
WEBSITE-BRIEFING.md
```

Jeder der drei Bereiche wird einem eigenen Dokumentenverzeichnis zugeordnet. Die konkreten Serverpfade werden vor dem Upload im IONOS-Panel geprüft. Nicht voraussetzen, dass das SFTP-Verzeichnis `/` das richtige Veröffentlichungsziel ist. Möglichst getrennte, nebeneinanderliegende Dokumentenverzeichnisse verwenden, um unbeabsichtigte `.htaccess`-Vererbung zu vermeiden.

CSS wird lokal pro Bereich ausgeliefert. Die drei Kopien müssen bei Änderungen gemeinsam aktualisiert und auf identischen Inhalt geprüft werden. Keine domänenübergreifenden Ressourcenabhängigkeiten.

## 4. Erscheinungsbild und Bedienung

| Element | Vorgabe |
| --- | --- |
| Akzent | `#1A73E8` |
| Hover-Akzent | `#1557B0` |
| Hintergrund | `#FFFFFF` |
| Flächen | `#F5F7FA` |
| Haupttext | `#1A1A2E` |
| Nebentext | `#5A5A72` |
| Rahmen | `#E2E8F0` |
| Schrift | `system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif` |
| Inhaltsbreite | maximal 800 px |
| Grundschrift | 1 rem; keine feste Begrenzung der Textvergrößerung |

Ruhige Typografie, viel Weißraum, zurückhaltende Karten mit 8 px Rundung. Kein Foto, keine Hintergrundbilder und keine dekorativen Animationen. Marke als Text „if3t“; eine optionale Initiale „M“ ist rein dekorativ und für Screenreader auszublenden. Ein lokales SVG-Favicon verwenden.

Mobile zuerst entwickeln; ab 768 px kann die Hauptnavigation nebeneinander stehen. Ein Hamburger-Menü nur verwenden, wenn es die kleine Navigation tatsächlich verbessert. Falls vorhanden: echtes Button-Element, `aria-expanded`, `aria-controls`, sinnvolle Beschriftung und zuverlässige Tastaturbedienung. Ohne JavaScript bleibt die Navigation sichtbar.

Weitere Anforderungen:

- WCAG-AA-Kontraste für die tatsächlich verwendeten Farbpaare prüfen.
- Sichtbare Fokusmarkierung, Sprunglink zum Hauptinhalt, logische Überschriftenstruktur.
- Textlinks im Fließtext erkennbar, vorzugsweise unterstrichen.
- Keine horizontale Überbreite bei 320 px und bei vergrößerter Schrift.
- Dekorative Inline-SVGs ohne unnötige Screenreader-Ausgabe.
- Übergänge nur für konkrete Eigenschaften; `prefers-reduced-motion` berücksichtigen.
- Öffnung externer Profile im neuen Tab sichtbar ankündigen und mit `rel="noopener noreferrer"` absichern.

## 5. Inhalte der Startseite

### Kopfbereich

Marke „if3t“. Navigation zu Startseite, beiden App-Seiten und Impressum. Für domänenübergreifende Ziele vollständige HTTPS-URLs verwenden.

### Persönliche Vorstellung

- H1: „Mark-Alexander Kaldenbach“.
- Berufsbezeichnung: „Performance and Growth Marketing Strategist“.
- Ergänzender Satz: „Ich beschäftige mich mit Performance- und Growth-Marketing und entwickle eigene iOS-Projekte rund um Berlin.“
- E-Mail: `service@if3t.de` als `mailto:`-Link.
- LinkedIn: `https://www.linkedin.com/in/mark-alexander-kaldenbach/`.
- GitHub: `https://github.com/Budonist`.

Keine unbelegten Referenzen, Kundenlogos, Qualifikationen oder Leistungsversprechen ergänzen.

### App-Karten

**Sonnenstands-App** – Arbeitsname bis zur Bestätigung des öffentlichen Namens:

„Sonnenposition und geometrische Verschattung für einen Bereich rund um Berlin 10961 berechnen – mit interaktiver Karte und lokal verarbeiteten Gebäudedaten.“

**Berlin Sektoren App** – öffentliche Schreibweise vor Veröffentlichung bestätigen:

„Die historischen alliierten Sektoren Berlins auf einer interaktiven Karte entdecken – mit Standortanzeige, Informationen zu historischen Orten und lokal abgespielten Hymnen.“

Jede Karte enthält einen Link zur App-Seite sowie einen gesonderten Link zur App-Datenschutzerklärung. Kein Download- oder TestFlight-Button ohne bestätigte öffentliche Zieladresse. Keinen App-Store-Veröffentlichungsstatus behaupten.

## 6. Inhalte der App-Seiten

Jede Seite enthält App-Name, kurze Beschreibung, wenige belegte Funktionen, Link zur eigenen Datenschutzerklärung und Rücklink zur Hauptseite. Keine Screenshots in Version 1 erforderlich.

### Sonnenstands-App

- Berechnung der Sonnenposition und gebäudebedingten Verschattung auf dem Gerät.
- Auswahl eines Punkts durch Antippen der Karte; Datum und Uhrzeit einstellbar.
- Apple MapKit für die Kartendarstellung.
- Optionaler Standortzugriff im Vordergrund zur Orientierung auf der Karte.
- Gebündelte Gebäudedaten; begrenztes Berechnungsgebiet um Berlin 10961. Keine berlinweite Abdeckung versprechen.
- Geometrisches Modell, keine Wettervorhersage und keine Garantie tatsächlicher Besonnung.
- Keine numerische Genauigkeitszusage ohne gesonderte Validierung.

### Berlin Sektoren App

- Historische Sektoren und ausgewählte Orte auf einer Apple-MapKit-Karte.
- Standortbasierte Erkennung des aktuellen Sektors und von Sektorwechseln.
- Hintergrundstandort und Hintergrundaudio sind im Projekt vorgesehen.
- Lokale Benachrichtigungen bei Sektorwechseln nach entsprechender Freigabe.
- Lokal gebündelte Hymnen; Wikipedia-Zusammenfassungen für ausgewählte Orte mit lokalem Cache.
- Keine vollständige Offline-Funktion versprechen: Karte und neue Wikipedia-Inhalte können Internetzugriff benötigen.

## 7. Belegte Datenflüsse und Grenzen der Prüfung

Grundlage ist eine statische Prüfung folgender GitHub-Stände:

- `Budonist/Sun_Position_App_iOS_New`, Commit `56d694fc13848e426eeaf565a6049981fa2e1898`.
- `Budonist/berlin-sektoren`, Commit `768020fbf9b5022ec471e075d4b974351393c101`.

Es wurde kein iOS-Build ausgeführt und kein Netzwerkverkehr auf einem Gerät gemessen. Der tatsächlich verteilte Build kann abweichen. Apple-interne Verarbeitung lässt sich aus dem App-Code allein nicht abschließend bestimmen.

| Bereich | Sonnenstands-App | Berlin Sektoren App |
| --- | --- | --- |
| Standort | Core Location, optionale Vordergrundabfrage | Core Location, laufende Updates; Hintergrundbetrieb konfiguriert |
| Verarbeitung | Sonnen-/Schattenberechnung lokal | Sektorzuordnung lokal |
| Karte | Apple MapKit | Apple MapKit, Nutzerposition eingeblendet |
| Eigene externe Abrufe | Keine aktiven eigenen Abrufe im untersuchten Funktionscode festgestellt | Wikipedia REST API unter `de.wikipedia.org` beim Öffnen zugehöriger Ortsdetails, sofern nicht im Cache |
| Persistenz | Keine dauerhafte Standortablage im untersuchten Funktionscode gefunden; Koordinaten erscheinen in System-Log-Aufrufen | Wikipedia-Zusammenfassungen als JSON im App-Cache; keine Standort-Historie im untersuchten Funktionscode gefunden |
| Meldungen | Keine lokalen Benachrichtigungen gefunden | Lokale iOS-Benachrichtigungen mit Sektorbezug |
| Audio | Keine entsprechende Funktion festgestellt | Gebündelte Audiodateien, lokale Wiedergabe |
| Werbung, Analyse, Käufe | Keine entsprechenden aktiven Integrationen gefunden | Keine entsprechenden aktiven Integrationen gefunden |

Relevante Belege im Sonnenstands-Repository: `Sources/Models/LocationProvider.swift`, `Sources/Views/MapScreen.swift`, `Sources/Models/SolarComputationService.swift`, jeweils unter `swift_space/`, sowie `DATA_LICENSES.md`.

Relevante Belege im Sektoren-Repository: `swift_space/Sources/Models/LocationManager.swift`, `WikipediaService.swift`, `NotificationManager.swift`, `AppViewModel.swift`, `swift_space/Sources/Views/POIDetailView.swift` und `swift_space/project.yml`.

Beide Projekte enthalten generische API- und Keychain-Helfer. Deren bloße Existenz belegt weder einen aktiven Backendbetrieb noch Nutzerkonten. Für den geprüften Funktionscode wurden keine entsprechenden Aufrufe gefunden. Tatsächliche Release-Konfiguration vor Veröffentlichung abgleichen.

## 8. Anforderungen an die Datenschutztexte

Die folgenden Punkte sind eine redaktionelle Arbeitsgrundlage, keine bereits rechtlich freigegebene Datenschutzerklärung. Tatsachen dürfen nicht durch pauschale Zusicherungen ersetzt werden.

### Gemeinsam für beide Apps

- Verantwortlicher und Kontakt laut Abschnitt 9.
- Genaue App-Bezeichnung und Geltungsbereich.
- Datenarten, Zwecke, zutreffende Rechtsgrundlagen und gegebenenfalls Empfänger, Übermittlungen sowie Speicherdauer bzw. Löschkriterien erklären.
- Lokale Verarbeitung, Übertragung und dauerhafte Speicherung klar unterscheiden.
- Standortzugriff und Widerruf über iOS-Einstellungen beschreiben. Eine Betriebssystemfreigabe nicht ohne rechtliche Prüfung pauschal mit einer DSGVO-Einwilligung gleichsetzen.
- Apple MapKit als externen Kartendienst erklären; keine vollständige Offline- oder Nichtübertragungszusage.
- TestFlight nur aufnehmen, wenn dieser Verteilungsweg für die betreffende Version bestätigt ist. Apple-Verarbeitung und Entwicklerzugriff anhand der aktuellen Bedingungen und tatsächlichen Einladungs-/Feedbackwege beschreiben. Keine pauschale Anonymitätszusage.
- Betroffenenrechte mit ihren gesetzlichen Voraussetzungen und Beschwerderecht bei einer Datenschutzaufsichtsbehörde beschreiben. Rechte nicht pauschal ausschließen.
- Keine Werbung, keine eigenen Analysewerkzeuge und keine In-App-Käufe nur für den geprüften bzw. bestätigten Release-Stand erklären.
- Tatsächliches Veröffentlichungs-/Aktualisierungsdatum angeben.

### Zusätze Sonnenstands-App

- Standortabfrage im Vordergrund, Auswahl von Kartenpunkten und lokale Berechnung erklären.
- Koordinatenprotokollierung über `Logger` berücksichtigen; deren Verfügbarkeit, Schutz und Aufbewahrung im Release prüfen. Bis dahin nicht behaupten, Koordinaten würden niemals gespeichert.
- Gebündelte Geodaten von online geladenen MapKit-Kartendaten unterscheiden.
- Dokumentierte künftige WFS-Fallbacks nicht als bereits aktive App-Datenflüsse darstellen.
- Keine manuelle numerische Koordinateneingabe zusichern, solange sie im ausgelieferten Build nicht bestätigt ist.

### Zusätze Berlin Sektoren App

- Laufende Standortverarbeitung, Hintergrundnutzung, Sektorwechsel und automatische Hymnenwiedergabe erklären.
- Benachrichtigungsberechtigung und mögliche Anzeige des Sektors auf dem Sperrbildschirm beschreiben.
- Wikipedia-Abrufe erläutern: angefragter Artikel sowie technisch anfallende Verbindungsdaten wie IP-Adresse. Im geprüften Abruf werden keine GPS-Koordinaten ausdrücklich als Parameter mitgesendet.
- Lokalen Wikipedia-Cache erklären. Im untersuchten Dienst gibt es keine eigene zeitgesteuerte Cache-Löschung; keine erfundene Aufbewahrungsfrist angeben.
- Lokale Benachrichtigungen von serverseitigen Push-Diensten unterscheiden.

### Datenschutz der Website

Gilt für Hauptdomain und beide App-Webseiten. Mindestens behandeln:

- IONOS als Hostingdienstleister, Serverprotokolle und technisch erforderliche Verbindungsdaten.
- Verantwortlichkeiten, Rechtsgrundlagen, tatsächliche Aufbewahrungsfristen und gegebenenfalls Auftragsverarbeitung anhand des gebuchten Vertrags prüfen.
- Kontakt per E-Mail einschließlich Zweck und Aufbewahrung nach tatsächlicher Handhabung.
- Externe Links als Links erklären; keine externen Inhalte beim Seitenaufruf einbetten.
- Keine Tracking-Cookies oder anderen optionalen Speicherzugriffe einbauen. Ein Cookie-Banner nicht vorsorglich hinzufügen; Erforderlichkeit anhand der tatsächlich eingesetzten Technik beurteilen.
- Betroffenenrechte und Beschwerderecht.

## 9. Impressum und Kontakt

Vom ursprünglichen Briefing übernommene Angaben, vor Veröffentlichung vom Betreiber zu bestätigen:

```text
Mark-Alexander Kaldenbach
Gneisenaustraße 21
10961 Berlin
E-Mail: service@if3t.de
```

Für einschlägige Anbieterangaben den aktuellen § 5 DDG prüfen; keine alten TMG-Bausteine übernehmen. Ob zusätzliche Angaben erforderlich sind, richtet sich nach der tatsächlichen Tätigkeit, vorhandenen Register-/Steuerangaben und gegebenenfalls berufsrechtlichen Anforderungen. Keine Steuernummer veröffentlichen. § 18 Abs. 2 MStV nur aufnehmen, wenn dessen Voraussetzungen erfüllt sind. Keine pauschalen Haftungsausschlüsse als Ersatz für eine Prüfung verwenden.

## 10. Geodaten und Audio-Lizenzen

Die Datei `DATA_LICENSES.md` der Sonnenstands-App nennt Berliner LoD2-/DGM1-Daten unter Datenlizenz Deutschland – Zero – 2.0 sowie OSM unter ODbL 1.0. Diese Angaben mit den tatsächlich gebündelten Daten und deren Herkunft abgleichen. MapKit ist die Kartendarstellung; OSM nicht pauschal als deren Kartenanbieter nennen. Quellenhinweise von Datenschutzinformationen unterscheiden.

Die Sektoren-README bezeichnet die Hymnenaufnahmen als gemeinfrei. Vor Veröffentlichung Herkunft, konkrete Aufnahme, Rechteinhaber bzw. Gemeinfreiheitsnachweis und gegebenenfalls erforderliche Namensnennung dokumentieren. Eine freie Komposition allein belegt keine freien Aufnahme-/Leistungsschutzrechte.

## 11. Navigation und Metadaten

- Gemeinsamer Footer mit Copyright, Impressum, Website-Datenschutz und Kontakt.
- Auf App-Seiten zusätzlich gut sichtbarer Link zum Datenschutz der jeweiligen App.
- Footer-Links zur Hauptdomain auf allen Seiten vollständig als HTTPS-URLs angeben.
- Pro Seite eindeutiger Titel, sachliche Meta-Beschreibung und absoluter Canonical-Link zur eigenen Adresse.
- Open-Graph-Titel, Beschreibung, URL und Typ; kein erfundenes Vorschaubild.
- Start- und App-Seiten indexierbar. Rechtliche Seiten mit `noindex, follow`; nicht per `robots.txt` vom Abruf ausschließen, wenn Suchmaschinen das `noindex` erkennen sollen.
- Keine Meta-Aussage „keine personenbezogenen Daten“.

Vorschlag Startseite:

Titel: „if3t – Mark-Alexander Kaldenbach“

Beschreibung: „Mark-Alexander Kaldenbach: Performance- und Growth-Marketing sowie eigene iOS-Projekte rund um Berlin.“

## 12. Hosting, Sicherheit und Upload

- IONOS-Paket, Domainzuordnung und Zertifikatsabdeckung tatsächlich prüfen; kostenlose automatische Zertifikate pro Subdomain nicht voraussetzen.
- `if3t.de` auf `https://www.if3t.de/` mit erhaltenem Pfad umleiten. App-Subdomains behalten ihren Hostnamen.
- HTTP auf HTTPS umleiten; Redirects ohne Schleifen und möglichst ohne unnötige Ketten.
- `.htaccess` auf dem tatsächlichen Apache-/IONOS-Setup prüfen. Lokaler einfacher HTTP-Server validiert diese Regeln nicht.
- `X-Content-Type-Options`, Referrer-Policy und Schutz gegen fremde Einbettung setzen. Eine auf die lokalen Ressourcen abgestimmte Content Security Policy vorsehen und testen.
- HTML zur erneuten Validierung ausliefern; Ressourcen zunächst mit kurzer Cache-Dauer oder expliziter URL-Versionierung. Keine monatelangen unveränderlichen Caches für unversionierte Dateien.
- Komprimierung nutzen, sofern unterstützt. HSTS erst nach gesicherter HTTPS-Verfügbarkeit festlegen; kein ungeprüftes `includeSubDomains` oder Preload.
- Keine Verzeichnisauflistung. Repository, Briefing, Zugangsdaten und interne Dokumentation nicht auf den Webspace hochladen.
- Vor Upload vorhandenen Webbestand sichern. SFTP-Hostschlüssel prüfen; keine Passwörter in Dokumentation oder Repository.
- Nur die Inhalte der jeweiligen `site/`-Bereiche in die zugewiesenen Ziele übertragen, einschließlich `.htaccess`.

## 13. Abnahmekriterien

### Lokal vor Upload

- Alle sieben HTML-Seiten vorhanden und ohne Build-Prozess nutzbar.
- HTML geprüft; interne Links, lokale Ressourcen und Canonicals korrekt.
- Keine unbeabsichtigten externen Requests beim Laden der Website.
- Navigation funktioniert mit Tastatur und ohne JavaScript.
- Darstellung bei 320 px, typischer Smartphone-/Tabletbreite und Desktop sowie bei Textvergrößerung geprüft.
- Sichtbare Fokuszustände, Kontraste und Überschriftenstruktur geprüft.
- CSS-Kopien identisch; keine Zugangsdaten oder offenen Platzhalter in den Veröffentlichungsdateien.
- Datenschutzaussagen mit dem vorgesehenen App-Release abgeglichen; offene rechtliche und tatsächliche Fragen dokumentiert und vor Veröffentlichung geklärt.

### Nach Upload

- Alle vorgesehenen HTTPS-Adressen liefern den richtigen Inhalt und erfolgreiche Statuscodes.
- Zertifikate, HTTP-/Apex-Weiterleitungen, Sicherheitsheader und Cache-Verhalten geprüft.
- Unbekannte URLs liefern einen echten 404-Status.
- Links von jeder Subdomain zu Impressum und Website-Datenschutz funktionieren.
- Beide App-Datenschutzseiten sind öffentlich, ohne Anmeldung und mobil erreichbar.
- Endgültige App-Datenschutz-URLs erst nach erfolgreicher Prüfung in App Store Connect eintragen.
- Upload- und Wiederherstellungsanleitung mit den tatsächlich verwendeten Zielverzeichnissen dokumentiert, ohne Geheimnisse.

## 14. Offene Punkte und Reihenfolge

### Vor Abschluss der Texte bzw. Veröffentlichung klären

1. Öffentliche App-Namen und Übereinstimmung der geprüften Commits mit den verteilten Versionen.
2. TestFlight-Nutzung je App und tatsächlich verfügbare Entwicklerdaten.
3. IONOS-Hostingangaben, Protokollierung, Aufbewahrung und Vertragsgrundlagen.
4. Betreiberanschrift und gegebenenfalls zusätzliche Impressumsangaben.
5. Herkunft und Nutzungsrechte der konkreten Hymnenaufnahmen.
6. Release-Verhalten der Koordinatenprotokollierung sowie tatsächliche Hintergrundstandortfunktion.
7. Abgleich der verwendeten Geodaten mit Lizenznachweisen.

### Empfohlene Umsetzung

1. Auf Grundlage dieses Briefings Layout und statische Seiten erstellen. Unbestätigte Tatsachen in Arbeitsentwürfen kenntlich machen; nicht als bestätigte Rechtstexte veröffentlichen.
2. Offene Fakten parallel klären und Datenschutz-/Impressumstexte fertigstellen.
3. Lokale Abnahme durchführen und Upload vorbereiten.
4. Veröffentlichung als gesonderten Schritt durchführen und Live-Abnahme abschließen.

Die Website kann technisch entwickelt werden, bevor alle offenen Angaben vorliegen. Eine öffentliche Freigabe der rechtlichen Texte setzt deren Klärung voraus.


## 15. Aktualisierung nach Betreiberantworten

Privater Betrieb und die oben angegebene Anschrift sowie Kontaktadresse sind bestätigt. Beide Apps derzeit in TestFlight; App Store geplant. IONOS-Vertrags- und Aufbewahrungsangaben bleiben offen. Für die Hymnen fehlen Herkunftsnachweise; die Behauptung gemeinfreier Aufnahmen ist nicht belegt. Siehe `RECHTLICHER-STATUS.md`.

Die ursprüngliche Vorgabe „keine Bilder“ wird auf Betreiberwunsch ersetzt: visuellere Projektkarten und App-Seiten mit lokal eingebundenen Original-App-Icons. Echte Screenshots können später ergänzt werden. Technische Diagramme nicht als App-Oberflächen darstellen. Datenschutztexte bleiben bis zur Klärung der aufgelisteten Tatsachen Arbeitsentwürfe.
