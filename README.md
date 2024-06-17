# DSA-Signaturen in Python

Dieses Projekt implementiert den DSA (Digital Signature Algorithm) zur Generierung von Schlüsseln, Signierung von Nachrichten und Verifikation von Signaturen unter Verwendung von Python. Es umfasst:

- DSA-Schlüsselgenerierung gemäß den Spezifikationen in [FIPS 186-4](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.186-4.pdf)
- DSA-Signaturalgorithmus mit SHA-256 Hashfunktion
- Demonstration der Kompromittierung des privaten Schlüssels bei Verwendung derselben Zufallszahl `r` für zwei verschiedene Signaturen

## Inhaltsverzeichnis

- [Beschreibung](#beschreibung)
- [Installation](#installation)
- [Benutzung](#benutzung)
- [Beitragende](#beitragende)
- [Lizenz](#lizenz)

## Beschreibung

Dieses Projekt enthält eine vollständige Implementierung des DSA, einschließlich:

1. **Schlüsselgenerierung**: Erzeugt die DSA-Schlüsselparameter (p, q, alpha, a, beta) gemäß den Vorgaben in FIPS 186-4.
2. **Signierung**: Signiert Nachrichten mit dem DSA-Signaturalgorithmus unter Verwendung der SHA-256 Hashfunktion.
3. **Verifikation**: Verifiziert die Signaturen korrekt.
4. **Kompromittierung des privaten Schlüssels**: Demonstriert, wie der private Schlüssel `a` kompromittiert werden kann, wenn dieselbe Zufallszahl `r` für zwei verschiedene Signaturen verwendet wird.

## Installation

1. **Klonen Sie das Repository**:
    ```bash
    git clone https://github.com/lastchopin/dsa_signature.git
    ```

2. **Wechseln Sie in das Verzeichnis**:
    ```bash
    cd dsa_signature
    ```

3. **Installieren Sie die notwendigen Abhängigkeiten**:
    ```bash
    pip install -r requirements.txt
    ```

## Benutzung

Das Projekt besteht aus mehreren Python-Skripten:

- `key_generation.py`: Erzeugt die DSA-Schlüssel.
- `sign.py`: Signiert eine Nachricht.
- `verify.py`: Verifiziert eine Signatur.
- `attack.py`: Demonstriert die Kompromittierung des privaten Schlüssels.

### Schlüsselgenerierung

Erstellen Sie die DSA-Schlüssel:
```bash
python key_generation.py
```

### Signieren einer Nachricht

Signieren Sie eine Nachricht:
```bash
python sign.py
```

### Verifizieren einer Signatur

Verifizieren Sie eine Signatur:
```bash
python verify.py
```

### Kompromittierung des privaten Schlüssels

Demonstrieren Sie die Kompromittierung des privaten Schlüssels:
```bash
python attack.py
```


