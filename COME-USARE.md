# Come usare Pinakes

Guida pratica all'uso quotidiano. Nessuna competenza tecnica richiesta.

---

## 1. Installare l'app sul telefono

Una volta che Pinakes è online (vedi `COME-PUBBLICARE.md`), aprilo nel browser del telefono:

- **Android (Chrome):** menu ⋮ → *Installa app* / *Aggiungi a schermata Home*.
- **iPhone (Safari):** pulsante Condividi → *Aggiungi a Home*.

Comparirà l'icona di Pinakes come una vera app. Si apre a tutto schermo e **funziona anche
senza connessione** (i dati sono sul telefono; serve la rete solo per cercare un nuovo ISBN
e scaricare le copertine).

---

## 2. Aggiungere un libro

Tre modi, dalla scheda **Catalogo**:

### A) Con lo scanner (il più veloce) 📷
1. Tocca **▢ Scanner**.
2. Inquadra il **codice a barre** sul retro del libro. Con poca luce, tocca **🔦 Torcia**.
3. Con la **sola scansione**, Pinakes riconosce l'ISBN, cerca il libro e **compila da solo**
   titolo, autore, editore, anno, pagine, lingua, categoria e **copertina**. Ti basta controllare
   **stanza/scaffale** e toccare **Salva**.

> Lo scanner riconosce solo i codici dei libri (ISBN 978/979 o ISBN-10): i codici di altri
> prodotti vengono ignorati. Una piccola vibrazione conferma la lettura.

### B) Cercando l'ISBN a mano
1. Tocca **+ Aggiungi**.
2. Scrivi l'**ISBN** (10 o 13 cifre) nel campo in alto e premi **Cerca**.
3. Premi **Usa questi dati**, completa e **Salva**.

### C) Inserimento manuale
Tocca **+ Aggiungi** e compila i campi a mano (utile per libri senza ISBN: vecchie edizioni,
classici, libri antichi).

---

## 3. La collocazione (scheda *Collocazione*)

Pinakes assegna a ogni libro una **segnatura** in stile biblioteca:

```
NAR.02.ECO / SA.01
│   │   │     │   └─ scaffale 01
│   │   │     └───── stanza: Salotto
│   │   └─────────── prime 3 lettere del cognome autore
│   └─────────────── sottocategoria (Romanzo storico)
└─────────────────── categoria (Narrativa)
```

- Lo **scaffale virtuale** mostra i dorsi dei libri ordinati come andrebbero disposti:
  categoria → sottocategoria → cognome autore → titolo.
- Il riquadro **«Calcola Collocazione»** ti dice, dato un nuovo libro, **tra quali due volumi**
  va inserito sullo scaffale reale.

Le categorie (Narrativa, Poesia, Teatro, Saggistica, Storia, Arte, Scienze, ecc.) sono ispirate
alla **Classificazione Decimale Dewey**, adattata a una biblioteca personale.

---

## 4. Statistiche

La scheda **Statistiche** riassume la collezione: quanti libri, letti quest'anno, pagine totali,
voto medio, spesa, e grafici per categoria, stato di lettura, voti, autori più presenti,
formato e libri aggiunti nel tempo.

---

## 5. Backup (importante!)

I dati vivono **nel browser di questo dispositivo**. Se cancelli i dati del browser o cambi
telefono, **vanno persi** se non hai un backup.

Dalla scheda **Backup**:
- **Backup JSON** → salva un file con tutta la biblioteca. Fallo ogni tanto.
- **Importa** → ricarica un backup, oppure **unisci** due dispositivi senza creare duplicati.
- **Esporta CSV** → per aprire l'elenco in Excel / Fogli Google.
- **Lista Markdown** → una lista di lettura condivisibile.

> Suggerimento: per tenere i dati allineati tra telefono e computer, esporta un **JSON** da un
> dispositivo e **importalo (Unisci)** sull'altro.

---

## 6. Domande frequenti

**Lo scanner non parte / schermo nero.**
Serve la connessione **https** (o `localhost`) e il permesso fotocamera. Se hai aperto il file
con doppio clic non funziona: usa l'app pubblicata online o `python -m http.server`.

**Su iPhone lo scanner è più lento.**
Normale: iOS non ha lo scanner nativo e usa ZXing. Tieni il codice ben illuminato (usa la
**Torcia**), fermo e a ~15–20 cm. Su Android lo scanner nativo è più rapido.

**Ha scansionato ma dice "ISBN non trovato".**
Il libro potrebbe non essere nei cataloghi online (edizioni vecchie, locali o senza ISBN), oppure
la ricerca era momentaneamente satura: l'ISBN resta già scritto, completa i campi a mano e salva.

**Posso usarlo senza internet?**
Sì, per consultare e gestire la collezione. Serve la rete solo per cercare un **nuovo** ISBN
e scaricare le copertine.
