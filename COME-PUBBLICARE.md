# Come pubblicare Pinakes online (GitHub Pages)

Per usare lo **scanner dal telefono** l'app deve stare su **HTTPS**: la fotocamera del
browser non funziona aprendo il file localmente. La via più semplice e gratuita è
**GitHub Pages**, con pubblicazione automatica a ogni modifica — esattamente come Poetrify.

---

## Prima pubblicazione (una volta sola)

1. **Crea un repository su GitHub** (es. `Pinakes`). Lascialo vuoto, senza README.

2. **Dalla cartella del progetto**, inizializza git e collega il repo
   (sostituisci `TUO-UTENTE`):

   ```bash
   cd C:\Users\fasci\Downloads\Pinakes
   git init
   git add -A
   git commit -m "Pinakes: prima versione"
   git branch -M main
   git remote add origin https://github.com/TUO-UTENTE/Pinakes.git
   git push -u origin main
   ```

3. **Attiva GitHub Pages**: nel repo → **Settings → Pages** →
   *Build and deployment* → **Source: GitHub Actions**.

4. Dopo qualche minuto l'app è online a:

   ```
   https://TUO-UTENTE.github.io/Pinakes/
   ```

   Apri questo indirizzo dal telefono e **installa l'app** (vedi `COME-USARE.md`).

> Il workflow di deploy è già pronto in `.github/workflows/deploy.yml`: non devi configurare nulla.

---

## Aggiornamenti successivi

Ogni volta che modifichi qualcosa:

```bash
cd C:\Users\fasci\Downloads\Pinakes
git add -A
git commit -m "descrizione della modifica"
git push
```

Il sito si ri-pubblica **da solo** in un paio di minuti.

> Se hai cambiato `index.html`, `sw.js` o le icone e sul telefono vedi ancora la versione
> vecchia, ricorda di aver incrementato `SHELL_CACHE` in `sw.js` (vedi README). In alternativa,
> chiudi e riapri l'app installata, oppure ricarica la pagina due volte.

---

## Alternative a GitHub Pages

Vanno bene anche **Netlify** o **Cloudflare Pages**: trascini la cartella e ottieni un URL
HTTPS. Qualunque hosting statico con HTTPS funziona — Pinakes non ha bisogno di alcun server.
