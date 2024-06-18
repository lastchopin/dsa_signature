# DSA-Signaturen in Python

Dieses Projekt implementiert den Digital Signature Algorithm (DSA) zur Generierung von Schlüsseln, Signierung von Nachrichten und Verifikation von Signaturen unter Verwendung von Python. Es umfasst:

- DSA-Schlüsselgenerierung gemäß den Spezifikationen in [FIPS 186-4](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.186-4.pdf)
- DSA-Signaturalgorithmus mit SHA-256 Hashfunktion
- Demonstration der Kompromittierung des privaten Schlüssels bei Verwendung derselben Zufallszahl `r` für zwei verschiedene Signaturen

## Inhaltsverzeichnis

- [Hintergrund](#hintergrund)
- [Beschreibung](#beschreibung)
- [Installation](#installation)
- [Benutzung](#benutzung)

## Hintergrund

Der Digital Signature Algorithm (DSA) ist ein kryptografisches Verfahren, das auf dem Konzept der modularen Exponentiation und dem Problem der diskreten Logarithmen basiert. Es handelt sich dabei um ein asymmetrisches Kryptosystem, bei dem zwei Schlüssel erzeugt werden: Ein öffentlicher Schlüssel, der zum Verifizieren der Signatur verwendet wird, und ein privater Schlüssel, der zum Erstellen der Signatur dient. Daten können nur mit dem öffentlichen Schlüssel verifiziert werden und eine gültige Signatur kann nur mit dem privaten Schlüssel erstellt werden. DSA ist eine Variante der Schnorr- und ElGamal-Signaturschemata.

Das National Institute of Standards and Technology (NIST) schlug DSA im Jahr 1991 für den Einsatz im Digital Signature Standard (DSS) vor und nahm es 1994 als FIPS 186 an. Seitdem wurden fünf Überarbeitungen der ursprünglichen Spezifikation veröffentlicht, wobei die neueste Spezifikation FIPS 186-5 im Februar 2023 veröffentlicht wurde. Obwohl DSA patentiert ist, hat NIST das Patent weltweit lizenzfrei zur Verfügung gestellt. Laut der Spezifikation FIPS 186-5 wird DSA nicht mehr zur Erstellung digitaler Signaturen zugelassen sein, kann jedoch weiterhin zur Verifizierung von Signaturen verwendet werden, die vor dem Inkrafttreten dieses Standards erstellt wurden.

## Beschreibung

Dieses Projekt enthält eine vollständige Implementierung des DSA, einschließlich:

1. **Schlüsselgenerierung**: Erzeugt die DSA-Schlüsselparameter (p, q, g, a, beta) gemäß den Vorgaben in [FIPS 186-4](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.186-4.pdf).
2. **Signierung und Verifikation**: Signiert Nachrichten mit dem DSA-Signaturalgorithmus unter Verwendung der SHA-256 Hashfunktion und verifiziert die Signaturen korrekt.
3. **Kompromittierung des privaten Schlüssels**: Demonstriert, wie der private Schlüssel `a` kompromittiert werden kann, wenn dieselbe Zufallszahl `r` für zwei verschiedene Signaturen verwendet wird.

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

- `dsa_key_generation.py`: Erzeugt die DSA-Schlüssel.
- `dsa_sign_verify.py`: Signiert eine Nachricht und verifiziert die Signatur.
- `dsa_attack.py`: Demonstriert die Kompromittierung des privaten Schlüssels.

### Schlüsselgenerierung

Erstellen Sie die DSA-Schlüssel:
```bash
python dsa_key_generation.py
```

### Signieren einer Nachricht und Verifizieren der Signatur

Signieren Sie eine Nachricht und verifizieren Sie die Signatur:

```bash
python dsa_sign_verify.py
```

### Kompromittierung des privaten Schlüssels

Demonstrieren Sie die Kompromittierung des privaten Schlüssels:

```bash
python dsa_attack.py
```

