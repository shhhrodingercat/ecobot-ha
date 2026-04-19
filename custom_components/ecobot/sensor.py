from datetime import date

from homeassistant.components.sensor import SensorDeviceClass, SensorEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DOMAIN, RIFIUTI, CONF_ZONA
from .coordinator import EcobotCoordinator


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    coordinator: EcobotCoordinator = hass.data[DOMAIN][entry.entry_id]
    zona = entry.data[CONF_ZONA]

    async_add_entities(
        EcobotDateSensor(coordinator, zona, col, nome)
        for col, nome in RIFIUTI.items()
    )


class EcobotDateSensor(CoordinatorEntity, SensorEntity):
    """Sensore che mostra la prossima data di raccolta per un tipo di rifiuto."""

    _attr_device_class = SensorDeviceClass.DATE

    def __init__(
        self,
        coordinator: EcobotCoordinator,
        zona: str,
        col: str,
        nome: str,
    ) -> None:
        super().__init__(coordinator)
        self._zona = zona
        self._col = col
        self._attr_name = f"EcoBot {zona} {nome}"
        self._attr_unique_id = f"ecobot_{zona}_{col}_prossima"

    @property
    def native_value(self) -> date | None:
        val = self.coordinator.data["prossima"].get(self._col)
        if val is None:
            return None
        try:
            return date.fromisoformat(val)
        except (ValueError, TypeError):
            return None

    @property
    def available(self) -> bool:
        return self.coordinator.last_update_success and self.native_value is not None
