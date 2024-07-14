import django.db.models as models
import karrio.server.providers.models as providers


class EShipperSettings(providers.Carrier):
    CARRIER_NAME = "eshipper"

    class Meta:
        db_table = "eshipper-settings"
        verbose_name = "eShipper Settings"
        verbose_name_plural = "eShipper Settings"

    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

    @property
    def carrier_name(self) -> str:
        return self.CARRIER_NAME


SETTINGS = EShipperSettings
