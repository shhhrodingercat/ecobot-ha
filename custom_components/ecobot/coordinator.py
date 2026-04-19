import sqlite3
import pathlib
import logging
from datetime import date, timedelta

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed

from .const import DOMAIN, RIFIUTI, CONF_ZONA, DB_FILENAME

_LOGGER = logging.getLogger(__name__)
DB_PATH = pathlib.Path(__file__).parent / DB_FILENAME


class EcobotCoordinator(DataUpdateCoordinator):
    """Legge il database SQLite e aggiorna i dati ogni ora."""

    def __init__(self, hass: HomeAssistant, entry: ConfigEntry) -> None:
        super().__init__(
            hass,
            _LOGGER,
            name=f"{DOMAIN}_{entry.data[CONF_ZONA]}",
            update_interval=timedelta(hours=1),
        )
        self.zona: str = entry.data[CONF_ZONA]

    async def _async_update_data(self) -> dict:
        try:
            return await self.hass.async_add_executor_job(self._fetch_data)
        except sqlite3.Error as err:
            raise UpdateFailed(f"Errore lettura database: {err}") from err

    def _fetch_data(self) -> dict:
        today = date.today().isoformat()
        tomorrow = (date.today() + timedelta(days=1)).isoformat()

        conn = sqlite3.connect(DB_PATH)
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()

        result: dict = {
            "prossima": {},
            "oggi": {},
            "domani": {},
            "eventi_futuri": [],
        }

        for col in RIFIUTI:
            # Prossima data di raccolta (None → sensor unavailable)
            cur.execute(
                f"SELECT MIN(date) AS d FROM [{self.zona}] WHERE {col} = 1 AND date >= ?",
                (today,),
            )
            row = cur.fetchone()
            result["prossima"][col] = row["d"] if row and row["d"] else None

            # Raccolta oggi
            cur.execute(
                f"SELECT {col} FROM [{self.zona}] WHERE date = ?",
                (today,),
            )
            row = cur.fetchone()
            result["oggi"][col] = bool(row and row[col] == 1)

            # Raccolta domani
            cur.execute(
                f"SELECT {col} FROM [{self.zona}] WHERE date = ?",
                (tomorrow,),
            )
            row = cur.fetchone()
            result["domani"][col] = bool(row and row[col] == 1)

        # Tutti gli eventi futuri per il calendario
        cols_sql = ", ".join(RIFIUTI.keys())
        cur.execute(
            f"SELECT date, {cols_sql} FROM [{self.zona}] WHERE date >= ? ORDER BY date",
            (today,),
        )
        for row in cur.fetchall():
            tipi = [col for col in RIFIUTI if row[col] == 1]
            if tipi:
                result["eventi_futuri"].append({"date": row["date"], "tipi": tipi})

        conn.close()
        return result
