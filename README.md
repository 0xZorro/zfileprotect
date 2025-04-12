# zfileprotect

**zfileprotect** ist ein Python-Tool zum Schutz von Word-, PDF- und Excel-Dateien mit einem Passwort.  
Es unterstützt sowohl manuelle Passworteingabe als auch automatische Passwortgenerierung.  
Das Tool ermöglicht zudem die Verarbeitung mehrerer Dateien und ganzer Verzeichnisse in einem Durchlauf.

---

## Funktionen

- Schutz von Word (`.docx`), PDF (`.pdf`) und Excel (`.xlsx`) Dateien mit einem Passwort
- Automatische Generierung sicherer Passwörter mit dem `-p`-Flag
- Unterstützung für mehrere Dateien und ganze Ordner
- Einfache Kommandozeilen-Bedienung über `argparse`

---

## Motivation

Dieses Projekt wurde als Lernübung im Bereich **Cybersecurity** entwickelt.  
Inspiriert vom Buch **„Ethical Hacking“ von Florian André Dalwick** war das Ziel, praxisnahe Tools zu entwickeln,  
die zur Datensicherheit beitragen – mit Fokus auf **Dateiverschlüsselung** und **passwortbasiertem Schutz**.

---

## Voraussetzungen

- Python 3.x
- `pywin32` (für Word- und Excel-Schutz)
- `PyPDF2` (für PDF-Schutz)

---

## Installation

Die benötigten Bibliotheken lassen sich mit `pip` installieren:

```bash
pip install pywin32 PyPDF2
```

---

## Verwendung

### Eine Datei mit einem eigenen Passwort schützen:

```bash
python zfileprotect.py "Test.pdf" --pwd=deinPasswort
```

### Mehrere Dateien mit demselben Passwort schützen:

```bash
python zfileprotect.py "file1.pdf" "file2.docx" "file3.xlsx" --pwd=deinPasswort
```

### Passwort automatisch generieren und Datei schützen:

```bash
python zfileprotect.py "Test.pdf" -p
```

### Alle unterstützten Dateien in einem Ordner verarbeiten:

```bash
python zfileprotect.py "C:\pfad\zum\verzeichnis" -p
```

Das Tool verarbeitet alle unterstützten Dateien im angegebenen Verzeichnis und versieht sie mit einem generierten Passwort.

---

## Lizenz

Dieses Projekt steht unter der MIT-Lizenz – siehe die Datei [LICENSE](LICENSE) für Details.

---

## Autor

**Created by Jose Luis Ocana**

Cybersecurity Learner | Python & C++ Tools

(GitHub: [0xZorro](https://github.com/0xZorro))  

TryHackMe: https://tryhackme.com/p/0xZorro

Contact: zorro.jose@gmx.de

---

## Beiträge

Du möchtest mithelfen? Super! Forke das Projekt, nimm Änderungen vor und stelle einen Pull Request.  
Achte bitte darauf, den Verhaltenskodex und die Projektstandards einzuhalten.

---

## Hinweis

**zfileprotect** ist ein Tool zu Lern- und privaten Zwecken. Durch die Nutzung erklärst du dich damit einverstanden,  
das Tool **nicht für illegale Aktivitäten zu verwenden**. Schütze nur Dateien, die dir gehören oder für die du  
ausdrücklich die Berechtigung hast. **Der Autor übernimmt keine Haftung für Missbrauch oder Schäden.**

---

# Haftungsausschluss

Der Autor übernimmt **keinerlei Verantwortung oder Haftung** für Schäden, Datenverluste, Missbrauch oder rechtliche Konsequenzen, die aus der Nutzung dieser Software resultieren.

Die Nutzung erfolgt **auf eigene Gefahr**. 

---

