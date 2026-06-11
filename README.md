# Pinakes — la mia biblioteca

> *Πίνακες* — i «registri» con cui Callimaco catalogò la Biblioteca di Alessandria:
> il primo catalogo bibliotecario della storia. Da qui il nome di questo progetto.

**Pinakes** è un'app web per **inventariare e archiviare la propria biblioteca fisica**.
Pensata per un lettore appassionato o un bibliofilo: registra i libri che possiedi,
ti dice **dove collocarli sullo scaffale** secondo una classificazione ispirata alla
**Decimale Dewey**, e ti restituisce **statistiche e metriche** sulla tua collezione e sulle tue letture.

La funzione cruciale è la **schedatura tramite codice a barre**: dal telefono inquadri
l'ISBN sul retro del libro, l'app riconosce il volume, scarica i dati (titolo, autore,
editore, copertina…) e propone la sua **segnatura e collocazione ideale**.

---

## Funzionalità

- 📷 **Scanner ISBN** dal telefono — doppio motore: `BarcodeDetector` nativo (Chrome/Android)
  con fallback automatico a Quagga (iPhone/Safari e browser più vecchi).
- 🔎 **Lookup ISBN multi-database** — Google Books → Open Library → ricerca OL, con copertine.
- 🗂️ **Catalogo** — vista griglia/lista, ricerca, filtri (stato, categoria, voto), ordinamento,
  scheda dettaglio, modifica ed eliminazione.
- 📐 **Collocazione Dewey** — tassonomia a 14 categorie con sottocategorie; genera la
  **segnatura** automatica `CAT.SOTTO.AUTORE/STANZA.SCAFFALE` e mostra lo scaffale virtuale
  con i dorsi dei libri ordinati. Calcolatore «dove va questo libro».
- 📊 **Statistiche** — totali, letti nell'anno, pagine, voto medio, investimento, e grafici
  (categorie, stato, voti, pagine, top autori, formato, andamento nel tempo).
- 💾 **Backup & esportazione** — CSV (tutti o filtrati), backup JSON, lista Markdown, stampa,
  importazione con *merge intelligente* (no duplicati ISBN).
- 🌙 **Tema chiaro/scuro**, interfaccia **responsive** (telefono/tablet/desktop).
- 📲 **PWA installabile** — si aggiunge alla schermata home come un'app e **funziona offline**.

I dati sono salvati **in locale nel browser** (`localStorage`): nessun account, nessun server,
nessun dato inviato a terzi (tranne le chiamate di lookup ISBN e le immagini di copertina).
Per non perdere la collezione, esporta periodicamente un **backup JSON** dalla scheda *Backup*.

---

## Struttura del progetto

```
Pinakes/
├── index.html              # l'intera app (HTML + CSS + JS in un unico file)
├── manifest.webmanifest    # metadati PWA (nome, icone, colori)
├── sw.js                   # service worker (cache offline)
├── icons/                  # icone dell'app (generate da _build_icons.py)
│   ├── icon.svg
│   ├── icon-192.png · icon-512.png · icon-maskable-512.png
│   ├── apple-touch-icon.png · favicon-32.png
├── _build_icons.py         # rigenera le icone (richiede Python + Pillow)
├── .github/workflows/      # deploy automatico su GitHub Pages
├── README.md
├── COME-USARE.md           # guida d'uso quotidiano
└── COME-PUBBLICARE.md      # come mettere l'app online (necessario per lo scanner del telefono)
```

> **Scelta progettuale:** l'app resta un **unico file** `index.html`, collaudato e robusto.
> Un'eventuale modularizzazione del codice è rimandata; non è necessaria per gli scopi attuali.

---

## Identità visiva

L'interfaccia è **allineata e armonizzata con *Poetrify Translator***: stessa famiglia visiva,
così i due progetti si riconoscono come affini.

- **Tipografia editoriale** (identica a Poetrify): `Playfair Display` (titoli) · `Source Serif 4`
  (testo di lettura: autori, note, descrizioni) · `Source Sans 3` (interfaccia, etichette
  maiuscolette spaziate) · `JetBrains Mono` (segnatura, ISBN, codici).
- **Palette**: carta **avorio** `#fcfbf8`, inchiostro `#2c3539`, seppia `#6b6660`, regole sottili
  `#eae8e2`. Accento primario = **indaco `#1800ac`** — lo stesso «asse del brand di servizio» di
  Poetrify (brand, tab attive, pulsanti, focus, hover). L'**ocra `#9c6b3c`** resta accento caldo
  (stelle valutazione); il **cremisi `#a22e37`** è tenuto come token secondario (`--accent-lat`).
- **Masthead chiaro** come la topbar di Poetrify: sfondo paper, bordo inferiore + ombra leggera,
  brand «Pinakes» in indaco Playfair a sinistra con sottotitolo corsivo seppia, controlli a destra.
- **Motivi ripresi**: sfondo a gradiente `paper→avorio`, raggi stretti (6/10px), **nav-tab come
  segmented control** indaco pieno, etichette maiuscolette, regole sottili, **barra-accento a
  sinistra** sulle card (statistiche, riquadro collocazione), badge a **pill**, hover bordo-accento
  con sollevamento, ombre tenui.
- **Dark mode** sulla palette scura di Poetrify (paper `#1c1f24`, accento lavanda `#8b7dff`,
  masthead con gradiente indaco `#2a2541 → #1a1530`).

I token sono variabili CSS in `:root` / `[data-theme="dark"]`; un blocco «MOTIVI POETRIFY» in coda
al `<style>` raccoglie le rifiniture editoriali.

---

## Avvio in locale

Lo scanner e il service worker richiedono un contesto sicuro: vanno bene **`http://localhost`**
o **`https://`**. Aprire il file con doppio clic (`file://`) mostra l'app ma **fotocamera e
installazione PWA non funzionano**.

Dalla cartella del progetto:

```bash
python -m http.server 8000
```

poi apri **http://localhost:8000** nel browser.

---

## Pubblicazione (per usare lo scanner dal telefono)

La fotocamera del telefono funziona **solo via HTTPS**. Per usarla dal cellulare l'app va
messa online: il modo più semplice è **GitHub Pages**, con deploy automatico a ogni `push`
(lo stesso meccanismo di Poetrify). Vedi **[COME-PUBBLICARE.md](COME-PUBBLICARE.md)**.

---

## Note tecniche

- Nessun bundler, nessuna dipendenza da installare: librerie esterne (Chart.js, Quagga,
  Google Fonts) caricate da CDN e messe in cache dal service worker per l'uso offline.
- Compatibilità scanner: Android/Chrome usa il `BarcodeDetector` nativo; iOS/Safari usa Quagga.
- Dopo aver modificato `index.html` o gli asset, **incrementa `SHELL_CACHE`** in `sw.js`
  (es. `pinakes-shell-v1` → `v2`) per forzare l'aggiornamento della cache offline.
