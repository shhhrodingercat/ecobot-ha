from datetime import date, datetime, timedelta

from homeassistant.components.calendar import CalendarEntity, CalendarEvent
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DOMAIN, RIFIUTI, CONF_ZONA, CONF_CALENDAR
from .coordinator import EcobotCoordinator


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    if not entry.data.get(CONF_CALENDAR, False):
        return

    coordinator: EcobotCoordinator = hass.data[DOMAIN][entry.entry_id]
    zona = entry.data[CONF_ZONA]
    async_add_entities([EcobotCalendar(coordinator, zona)])


class EcobotCalendar(CoordinatorEntity, CalendarEntity):
    """Calendario con tutti i ritiri della raccolta differenziata."""

    def __init__(self, coordinator: EcobotCoordinator, zona: str) -> None:
        super().__init__(coordinator)
        self._zona = zona
        self._attr_name = f"EcoBot {zona}"
        self._attr_unique_id = f"ecobot_calendar_{zona}"

    @property
    def event(self) -> CalendarEvent | None:
        """Restituisce il prossimo evento imminente."""
        eventi = self.coordinator.data.get("eventi_futuri", [])
        if not eventi:
            return None
        return self._build_event(eventi[0])

    async def async_get_events(
        self,
        hass: HomeAssistant,
        start_date: datetime,
        end_date: datetime,
    ) -> list[CalendarEvent]:
        eventi = self.coordinator.data.get("eventi_futuri", [])
        return [
            self._build_event(e)
            for e in eventi
            if start_date.date() <= date.fromisoformat(e["date"]) <= end_date.date()
        ]

    def _build_event(self, e: dict) -> CalendarEvent:
        d = date.fromisoformat(e["date"])
        nomi = [RIFIUTI[t] for t in e["tipi"]]
        return CalendarEvent(
            start=d,
            end=d + timedelta(days=1),
            summary=", ".join(nomi),
        )
