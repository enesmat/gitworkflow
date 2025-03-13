#!/bin/bash
echo "Willkommen in der Github-Autowerkstatt! Dein Rennwagen braucht einen Check!"

# Die geheime Speed-Dokumentation
DATEI="rennwagen_geheim_daten.txt"

# Bonus - Überprüfen, ob die geheime Datei existiert
if [ -f "$DATEI" ]; then
    echo "Die geheime Rennwagen-Datenbank '$DATEI' wurde gefunden! Der Motor startet auf Turbo!"
else
    echo "Ups! Die Datei '$DATEI' ist verschwunden! Wurde sie von einem gegnerischen Rennteam gestohlen?"
    echo "Keine Sorge, der Wagen läuft auch ohne die Daten, aber leider etwas langsamer :)"
fi