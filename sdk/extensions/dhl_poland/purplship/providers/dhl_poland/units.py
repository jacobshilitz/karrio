from purplship.core.utils import Enum, Flag, Spec


class LabelType(Flag):
    BLP_LABEL = "BLP"
    LBLP_LABEL_A4_PDF = "LBLP"
    ZBLP_LABEL_ZPL = "ZBLP"

    """ Unified Label type mapping """
    PDF = LBLP_LABEL_A4_PDF
    ZPL = ZBLP_LABEL_ZPL


class PaymentType(Flag):
    shipper = "SHIPPER"
    receiver = "RECEIVER"
    user = "USER"

    """ Unified Payment type mapping """
    sender = shipper
    recipient = receiver
    third_party = user


class PackagingType(Flag):
    dhl_poland_envelope = "ENVELOPE"
    dhl_poland_package = "PACKAGE"
    dhl_poland_pallet = "PALLET"

    """ Unified Packaging type mapping """
    envelope = dhl_poland_envelope
    pak = dhl_poland_package
    tube = dhl_poland_package
    pallet = dhl_poland_pallet
    small_box = dhl_poland_package
    medium_box = dhl_poland_package
    large_box = dhl_poland_package
    your_packaging = dhl_poland_package


class Service(Enum):
    dhl_poland_premium = "PR"
    dhl_poland_polska = "AH"
    dhl_poland_09 = "09"
    dhl_poland_12 = "12"
    dhl_poland_connect = "EK"
    dhl_poland_international = "PI"


class Option(Flag):
    dhl_poland_delivery_in_18_22_hours = Spec.asKey("1722")
    dhl_poland_delivery_on_saturday = Spec.asKey("SATURDAY")
    dhl_poland_pickup_on_staturday = Spec.asKey("NAD_SOBOTA")
    dhl_poland_insuration = Spec.asKeyVal("UBEZP")
    dhl_poland_collect_on_delivery = Spec.asKeyVal("COD")
    dhl_poland_information_to_receiver = Spec.asKey("PDI")
    dhl_poland_return_of_document = Spec.asKey("ROD")
    dhl_poland_proof_of_delivery = Spec.asKey("POD")
    dhl_poland_delivery_to_neighbour = Spec.asKey("SAS")
    dhl_poland_self_collect = Spec.asKey("ODB")

    """ Unified Option type mapping """
    cash_on_delivery = dhl_poland_collect_on_delivery
    insurance = dhl_poland_insuration
