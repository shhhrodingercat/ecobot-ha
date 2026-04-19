import voluptuous as vol
from homeassistant import config_entries

from .const import DOMAIN, CONF_ZONA, CONF_CALENDAR, ZONE_LABELS


class EcobotConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1

    async def async_step_user(self, user_input: dict | None = None):
        errors: dict[str, str] = {}

        if user_input is not None:
            zona = user_input[CONF_ZONA]

            await self.async_set_unique_id(f"{DOMAIN}_{zona}")
            self._abort_if_unique_id_configured()

            label = ZONE_LABELS.get(zona, zona)
            return self.async_create_entry(title=label, data=user_input)

        # Dropdown ordinato alfabeticamente per nome leggibile
        options = dict(
            sorted(ZONE_LABELS.items(), key=lambda item: item[1])
        )

        schema = vol.Schema(
            {
                vol.Required(CONF_ZONA): vol.In(options),
                vol.Optional(CONF_CALENDAR, default=False): bool,
            }
        )

        return self.async_show_form(
            step_id="user",
            data_schema=schema,
            errors=errors,
        )
