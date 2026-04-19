DOMAIN = "ecobot"
DB_FILENAME = "seta.db"

CONF_ZONA = "zona"
CONF_CALENDAR = "create_calendar"

PLATFORMS = ["sensor", "binary_sensor", "calendar"]

# Mapping colonne DB → nomi leggibili
RIFIUTI: dict[str, str] = {
    "i": "Indifferenziato",
    "o": "Organico",
    "c": "Carta e Cartone",
    "v": "Vetro e Alluminio",
    "p": "Plastica",
    "s": "Sfalci",
}

# Mapping codice DB → nome leggibile per il config flow
# I comuni con zone multiple hanno un codice per ogni zona
ZONE_LABELS: dict[str, str] = {
    # Borgaro Torinese
    "x001": "Borgaro Torinese – Zona A",
    "x002": "Borgaro Torinese – Zona B",
    # Brandizzo
    "x005": "Brandizzo – Zona 1",
    "x006": "Brandizzo – Zona 2",
    "x007": "Brandizzo – Zona 3",
    # Comuni singoli
    "x008": "Brozolo",
    "x064": "Brusasco",
    "x009": "Casalborgone",
    # Caselle Torinese
    "x010": "Caselle Torinese – Zona 1",
    "x011": "Caselle Torinese – Zona 2",
    "x012": "Caselle Torinese – Zona 3",
    "x013": "Caselle Torinese – Zona 4",
    "x014": "Caselle Torinese – Zona 5",
    # Comuni singoli
    "x015": "Castagneto Po",
    # Castiglione Torinese
    "x016": "Castiglione Torinese – Zona 1",
    "x017": "Castiglione Torinese – Zona 2",
    # Comuni singoli
    "x018": "Cavagnolo",
    # Chivasso
    "x019": "Chivasso – Zona 1",
    "x020": "Chivasso – Zona 2",
    "x021": "Chivasso – Zona 3",
    "x022": "Chivasso – Zona 4",
    "x023": "Chivasso – Zona 5",
    "x024": "Chivasso – Zona 6",
    # Comuni singoli
    "x025": "Cinzano",
    "x026": "Foglizzo",
    # Gassino Torinese
    "x027": "Gassino Torinese – Zona 3",
    "x028": "Gassino Torinese – Zona 4",
    "x029": "Gassino Torinese – Zona 4 BIS",
    # Comuni singoli
    "x030": "Lauriano",
    # Leinì
    "x031": "Leinì – Zona 1",
    "x032": "Leinì – Zona 2",
    "x033": "Leinì – Zona 3",
    "x034": "Leinì – Zona 4",
    "x035": "Leinì – Zona 5",
    "x036": "Leinì – Zona 6",
    # Comuni singoli
    "x037": "Lombardore",
    "x038": "Mappano",
    # Montanaro
    "x039": "Montanaro – Zona 1",
    "x040": "Montanaro – Zona 2",
    # Comuni singoli
    "x041": "Monteu da Po",
    "x042": "Rivalba",
    "x043": "Rondissone",
    # San Benigno
    "x044": "San Benigno – Zona Nord",
    "x045": "San Benigno – Zona Sud",
    # San Mauro Torinese
    "x046": "San Mauro Torinese – Zona Capoluogo",
    "x047": "San Mauro Torinese – Zona Oltrepo",
    # Comuni singoli
    "x048": "San Raffaele Cimena",
    "x049": "San Sebastiano da Po",
    "x050": "Sciolze",
    # Settimo Torinese
    "x051": "Settimo Torinese – Zona 1",
    "x052": "Settimo Torinese – Zona 2",
    "x053": "Settimo Torinese – Zona 3",
    "x054": "Settimo Torinese – Zona 4",
    "x055": "Settimo Torinese – Zona 5",
    "x056": "Settimo Torinese – Zona 6",
    # Comuni singoli
    "x057": "Torrazza Piemonte",
    # Verolengo
    "x058": "Verolengo – Zona 1",
    "x059": "Verolengo – Zona 2",
    # Comuni singoli
    "x060": "Verrua Savoia",
    # Volpiano
    "x061": "Volpiano – Zona Centro",
    "x062": "Volpiano – Zona Est",
    "x063": "Volpiano – Zona Ovest",
}
