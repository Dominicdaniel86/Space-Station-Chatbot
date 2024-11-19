# Space Station Chatbot

## Anforderungen

- Einen regelbasierten Chatbot aufbauen
- Webanwendung, welche unter localhost läuft
- Kurze Entwicklungsdauer (~2 Monate)
- Kein zu hoher Tech-Stack, Technologien mit Vorkenntnissen einsetzen
- Themengebiete außerhalb des Scopes sollen kompetent gemieden werden

### Funktionsumfang

- Chatbot, welcher Fragen eines gewissen Rahmens beantworten kann
- Simple, leicht bedienbare UI, mit Weltraum-Thematik
- Einfache Login-Funktion mit vorgefertigten Usern (Datenbank)
- Integration von APIs mit erweiterten Informationen zum Themengebiet
- Dokumentation auf GitLab, samt Interaktionsfluss

### Optionaler Funktionsumfang/ Aussicht

- Authentifizierung und Autorisierung
- Skalierbarkeit mit mehreren Nutzern
- Datenschutz in der Datenbank
- Mehrsprachigkeit
- Logging
- Analyse- und Feedbacktools
- Testing-Strategie

## Thematik und Inhalt

- Grundlegende Informationen über das Leben, der alltäglichen Arbeit und Experimenten auf einer Raumstation
- Informationen zum Training und Ausbildung der Astronauten
- Bedeutung der Raumfahrttechnologie
- Zielgruppen: Schüler, Studenten und angehende Weltraumpiloten

### Erweiterter Scope

- Herausforderungen und psychologische Auswirkungen

### Umfangreicher Scope

- Zukünftige Raumfahrtmissionen
- Aufbau von Raumkolonien
- Rolle der Raumfahrt in der Zukunft der Menschheit

## Technologieauswahl

### Programmiersprache

- [Python]
- Java
- [JavaScript]
- Ruby
- C#

Python für die Logik des Chatbots

- Einfachheit und Lesbarkeit
- Große Anzahl an Bibliotheken (NLTK, spaCy)
- Mangelnde Skalierbarkeit und Leistung für den Scope ausreichend
- Gute Integration mit vielen Systemen und Frameworks
- Gute Dokumentation

JavaScript für die Webinteraktionen

- Gute Ergänzung zu Python
- Für die Frontend-Entwicklung

### Chatbot-Frameworks

Kategorien:

- Gute Integration mit Web-Frameworks
- Gute Dokumentation und leicht Verständlich, durch die kurze Entwicklungsdauer
- Regelbasierter Ansatz
- Generell und nicht spezialisiert

Auswahl:

- Botpress (persönliche Präferenz, Fokus auf Python statt JS)
- [Rasa]
- ChatterBot (doch zu einfach, evtl. schwerer in Web-Framework einbindbar)
- Microsoft Bot Framework (zu komplex)
- Dialogflow (Zwang zur Nutzung der Google-Infrastruktur)
- Wit.ai (eventuell beschränkte Funktionsoptionen)

### Web-Framework

- [Flask]
- Django (zu starr und schwergewichtig für den Scope)

### Weitere Komponenten

- Datenbank
- API-Anbindungen
- Container-Technologie
- Logging, Testing und Analytik
