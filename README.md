# ♻️ EcoBot – Raccolta Differenziata

[![HACS Custom](https://img.shields.io/badge/HACS-Custom-orange.svg)](https://github.com/hacs/integration)
[![HA Version](https://img.shields.io/badge/Home%20Assistant-2024.1%2B-blue.svg)](https://www.home-assistant.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Buy Me a Coffee](https://img.shields.io/badge/Buy%20me%20a%20coffee-☕-yellow.svg)](https://www.buymeacoffee.com/ecobot)

Integrazione per Home Assistant che fornisce sensori e calendario per la **raccolta differenziata porta a porta** nei Comuni della provincia di Torino serviti da **Seta S.p.a.**

> Questo progetto nasce come evoluzione del [bot Telegram EcoBot](https://github.com/shhhrodingercat/ecobot), ora dismesso.

---

## 📍 Comuni supportati

Borgaro Torinese · Brandizzo · Brozolo · Brusasco · Casalborgone · Caselle Torinese · Castagneto Po · Castiglione Torinese · Cavagnolo · Chivasso · Cinzano · Foglizzo · Gassino Torinese · Lauriano · Leinì · Lombardore · Mappano · Montanaro · Monteu da Po · Rivalba · Rondissone · San Benigno · San Mauro Torinese · San Raffaele Cimena · San Sebastiano da Po · Sciolze · Settimo Torinese · Torrazza Piemonte · Verolengo · Verrua Savoia · Volpiano

I comuni con più zone di raccolta (ad es. Chivasso, Settimo Torinese, Leinì) sono suddivisi per zona.

---

## ✨ Funzionalità

- **6 sensori data** per ogni zona configurata: mostrano la prossima data di raccolta per ciascun tipo di rifiuto
  - 🗑️ Indifferenziato
  - 🥕 Organico
  - 📦 Carta e Cartone
  - 🫙 Vetro e Alluminio
  - 🥤 Plastica
  - 🌿 Sfalci
- **Entità calendario** opzionale con tutti i ritiri futuri come eventi all-day, integrabile nella card calendario di Lovelace
- **Raggruppamento per dispositivo**: tutte le entità di una zona appaiono sotto un unico device nella pagina integrazioni
- **Multi-zona**: puoi aggiungere più zone ripetendo la configurazione
- **Icone personalizzate** per ogni tipo di rifiuto
- Sensori vanno in `unavailable` a fine anno, in attesa del nuovo calendario

---

## 🔧 Installazione

### Tramite HACS (consigliato)

1. In HACS vai su **tre puntini → Custom repositories**
2. Inserisci `https://github.com/shhhrodingercat/ecobot-ha` come URL
3. Categoria: **Integration**
4. Clicca **Add**, poi cerca **EcoBot** e installa
5. Riavvia Home Assistant

### Manuale

1. Copia la cartella `custom_components/ecobot/` in `/config/custom_components/`
2. Riavvia Home Assistant

---

## ⚙️ Configurazione

1. Vai su **Impostazioni → Dispositivi e servizi → Aggiungi integrazione**
2. Cerca **EcoBot**
3. Seleziona il tuo Comune o Zona dal menu a tendina
4. Scegli se creare anche l'entità calendario
5. Conferma

Per aggiungere più zone, ripeti la procedura dall'inizio.

---

## 🔔 Notifiche

L'integrazione non invia notifiche autonomamente — questa è una scelta consapevole per lasciare massima flessibilità. Puoi creare un'automazione in pochi clic:

```yaml
automation:
  - alias: "Notifica raccolta differenziata"
    trigger:
      - platform: time
        at: "18:30:00"
    condition:
      - condition: template
        value_template: >
          {{ states('sensor.indifferenziato') == now().date() + timedelta(days=1) | string }}
    action:
      - service: notify.mobile_app_tuotelefono
        data:
          message: "Domani: Indifferenziato 🗑️"
```

---

## 📅 Aggiornamento calendario

Il database delle raccolte viene aggiornato una volta l'anno quando Seta S.p.a. pubblica i nuovi ecocalendari. Segui il repository per ricevere notifiche di aggiornamento.

---

## ⚠️ Disclaimer

Questo progetto è personale e non ha alcuna affiliazione ufficiale con Seta S.p.a. o con i Comuni coinvolti. I dati potrebbero non essere aggiornati o potrebbero contenere errori: verifica sempre con il tuo Comune di residenza.

---

## ☕ Supporta il progetto

Se ti è utile e vuoi contribuire ai costi di sviluppo e manutenzione:

[![Buy Me a Coffee](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/ecobot)

---

## 👤 Sviluppatore

Sviluppato da **Matteo Miccichè**  
[LinkedIn](https://www.linkedin.com/in/miccichematteo/) · [Segnala un bug](https://github.com/shhhrodingercat/ecobot-ha/issues)
