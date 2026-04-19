from homeassistant.components.binary_sensor import BinarySensorEntity
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

    entities = []
    for col, nome in RIFIUTI.items():
        entities.append(EcobotBinarySensor(coordinator, zona, col, nome, "oggi"))
        entities.append(EcobotBinarySensor(coordinator, zona, col, nome, "domani"))
    async_add_entities(entities)


class EcobotBinarySensor(CoordinatorEntity, BinarySensorEntity):
    """Binary sensor: True se quel rifiuto viene raccolto oggi o domani."""

    def __init__(
        self,
        coordinator: EcobotCoordinator,
        zona: str,
        col: str,
        nome: str,
        quando: str,  # "oggi" | "domani"
    ) -> None:
        super().__init__(coordinator)
        self._zona = zona
        self._col = col
        self._quando = quando
        label = "Oggi" if quando == "oggi" else "Domani"
        self._attr_name = f"EcoBot {zona} {nome} {label}"
        self._attr_unique_id = f"ecobot_{zona}_{col}_{quando}"

    @property
    def is_on(self) -> bool:
        return self.coordinator.data[self._quando].get(self._col, False)
