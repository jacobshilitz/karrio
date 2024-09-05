import karrio.lib as lib
import karrio.core.units as units


class PackagingType(lib.StrEnum):
    """Carrier specific packaging type"""

    Drum = "Drum"
    Boxes = "Boxes"
    Rolls = "Rolls"
    Pipes = "Pipes"
    Bales = "Bales"
    Bags = "Bags"
    Pallet = "Pallet"
    Cylinder = "Cylinder"
    Pails = "Pails"
    Reels = "Reels"
    Crate = "Crate"
    Bucket = "Bucket"
    Bundle = "Bundle"
    Can = "Can"
    Carton = "Carton"
    Case = "Case"
    Coil = "Coil"
    Pieces = "Pieces"
    Skid = "Skid"

    """ Unified Packaging type mapping """
    tube = Cylinder
    pallet = Pallet
    small_box = Boxes
    medium_box = Boxes


class ShippingService(lib.StrEnum):
    """Carrier specific services"""

    # fmt: off
    eshipper_aramex_priority_letter_express = "2700"
    eshipper_aramex_priority_parcel_express = "2701"
    eshipper_canpar_express_letter = "4505"
    eshipper_canpar_express_pak = "4506"
    eshipper_canpar_express_parcel = "4507"
    eshipper_canpar_ground = "4500"
    eshipper_canpar_international = "4511"
    eshipper_canpar_select_letter = "4502"
    eshipper_canpar_select_pak = "4503"
    eshipper_canpar_select_parcel = "4504"
    eshipper_canpar_usa = "4501"
    eshipper_canpar_usa_select_letter = "4508"
    eshipper_canpar_usa_select_pak = "4509"
    eshipper_canpar_usa_select_parcel = "4510"
    eshipper_day_ross_ltl = "5500"
    eshipper_dhl_ground = "108"
    eshipper_dhl_esi_export = "104"
    eshipper_dhl_express_1030am = "102"
    eshipper_dhl_express_12pm = "103"
    eshipper_dhl_express_9am = "100"
    eshipper_dhl_express_worldwide = "101"
    eshipper_dhl_import_express = "105"
    eshipper_dhl_import_express_12pm = "107"
    eshipper_dhl_import_express_9am = "106"
    eshipper_trucking_a_duie_pyle = "1833"
    eshipper_trucking_aaa_cooper = "1816"
    eshipper_trucking_aaa_cooper_transportation = "1801"
    eshipper_trucking_absolute_transportation_services = "1851"
    eshipper_trucking_ama_transportation = "1817"
    eshipper_trucking_averitt_express = "1818"
    eshipper_trucking_blue_sky_express = "1852"
    eshipper_trucking_central_freight = "1819"
    eshipper_trucking_central_transport = "1845"
    eshipper_trucking_central_transport = "1850"
    eshipper_trucking_chi_cargo = "1842"
    eshipper_trucking_conway = "1820"
    eshipper_trucking_conway = "1808"
    eshipper_trucking_day_and_ross = "1813"
    eshipper_trucking_day_and_ross_r_and_l = "1814"
    eshipper_trucking_dayton = "1821"
    eshipper_trucking_dayton_freight = "1805"
    eshipper_trucking_dependable_highway_express = "1812"
    eshipper_trucking_drug_transport = "1822"
    eshipper_trucking_estes = "1848"
    eshipper_trucking_estes = "1823"
    eshipper_trucking_fedex_east = "1844"
    eshipper_trucking_fedex_national = "1826"
    eshipper_trucking_fedex_west = "1825"
    eshipper_trucking_galasso_trucking = "1853"
    eshipper_trucking_griley_air_freight = "1854"
    eshipper_trucking_jet_transportation = "1855"
    eshipper_trucking_lakeville_m_express = "1828"
    eshipper_trucking_land_air_express = "1824"
    eshipper_trucking_metro_transportation_logistics = "1856"
    eshipper_trucking_milan_express = "1829"
    eshipper_trucking_nebraska_transport = "1830"
    eshipper_trucking_new_england = "1831"
    eshipper_trucking_new_england_motor_freight = "1803"
    eshipper_trucking_new_penn = "1832"
    eshipper_trucking_new_penn_motor_express = "1804"
    eshipper_trucking_oak_harbor = "1857"
    eshipper_trucking_pitt_ohio = "1839"
    eshipper_trucking_r_and_l_carriers = "1847"
    eshipper_trucking_rhody_transportation = "1836"
    eshipper_trucking_roadrunner = "1846"
    eshipper_trucking_roadrunner_dawes = "1802"
    eshipper_trucking_roadway = "1809"
    eshipper_trucking_saia_motor_freight = "1837"
    eshipper_trucking_saia_inc = "1807"
    eshipper_trucking_southeastern_freightway = "1806"
    eshipper_trucking_southeastern_frgt = "1838"
    eshipper_trucking_stream_links_express = "1858"
    eshipper_trucking_tax_air = "1843"
    eshipper_trucking_tiffany_trucking = "1859"
    eshipper_trucking_ups = "1815"
    eshipper_trucking_ups_freight = "1860"
    eshipper_trucking_usf_holland = "1827"
    eshipper_trucking_usf_holland = "1811"
    eshipper_trucking_usf_reddaway = "1810"
    eshipper_trucking_usf_reddaway = "1835"
    eshipper_trucking_ward = "1840"
    eshipper_trucking_wilson = "1841"
    eshipper_trucking_wilson_truckingtfc = "1800"
    eshipper_trucking_yrc_roadway = "1849"
    eshipper_trucking_yrc_inc = "1834"
    eshipper_eshipper_canada_worldwide_air_freight = "16"
    eshipper_eshipper_canada_worldwide_next_flight_out = "15"
    eshipper_eshipper_ltl_apex_trucking = "4209"
    eshipper_eshipper_ltl_fastfrate_rail = "4207"
    eshipper_eshipper_ltl_kindersley_expedited = "4601"
    eshipper_eshipper_ltl_kindersley_rail = "4600"
    eshipper_eshipper_ltl_kindersley_rail = "4210"
    eshipper_eshipper_ltl_kindersley_regular = "4602"
    eshipper_eshipper_ltl_kindersley_road_ = "4211"
    eshipper_eshipper_ltl_mo_rail = "4204"
    eshipper_eshipper_ltl_mo_rail = "4205"
    eshipper_eshipper_ltl_western_canada_rail = "4203"
    eshipper_fastfrate_rail = "5929"
    eshipper_fedex_2day_freight = "33"
    eshipper_fedex_3day_freight = "34"
    eshipper_fedex_2nd_day = "29"
    eshipper_fedex_economy = "30"
    eshipper_fedex_first_overnight = "2"
    eshipper_fedex_fedex_intl_connect_plus = "5967"
    eshipper_fedex_intl_economy = "35"
    eshipper_fedex_intl_economy_freight = "32"
    eshipper_fedex_intl_priority = "5926"
    eshipper_fedex_intl_priority_express = "5927"
    eshipper_fedex_intl_priority_freight = "31"
    eshipper_fedex_priority = "1"
    eshipper_fedex_standard_overnight = "28"
    eshipper_fedex_freight_ltl_fedex_freight_economy = "5936"
    eshipper_fedex_freight_ltl_fedex_freight_priority = "5935"
    eshipper_project44_a_duie_pyle = "5968"
    eshipper_project44_aaa_cooper_transportation = "4030"
    eshipper_project44_aaa_cooper_transportation = "5955"
    eshipper_project44_aberdeen_express = "4041"
    eshipper_project44_abf_freight = "5960"
    eshipper_project44_averitt_express = "4028"
    eshipper_project44_central_freight_lines = "4015"
    eshipper_project44_central_transport = "4034"
    eshipper_project44_central_transport = "5964"
    eshipper_project44_chicago_suburban_express = "4035"
    eshipper_project44_clear_lane_freight = "4044"
    eshipper_project44_con_way_freight = "4006"
    eshipper_project44_con_way_freight = "5952"
    eshipper_project44_crosscountry_courier = "4032"
    eshipper_project44_day_ross = "4048"
    eshipper_project44_daylight_transport = "5958"
    eshipper_project44_dayton_freight_lines = "4021"
    eshipper_project44_dependable_highway_express = "4040"
    eshipper_project44_dependable_highway_express = "5965"
    eshipper_project44_dohrn_transfer_company = "4027"
    eshipper_project44_dugan_truck_line = "4025"
    eshipper_project44_estes_express_lines = "4010"
    eshipper_project44_estes = "5950"
    eshipper_project44_expedited_freight_systems = "4026"
    eshipper_project44_fedex_freight_canada = "4054"
    eshipper_project44_fedex_freight_canada = "4019"
    eshipper_project44_fedex_freight_east = "4008"
    eshipper_project44_fedex_freight_usa = "4055"
    eshipper_project44_fedex_national = "4009"
    eshipper_project44_forward_air = "5969"
    eshipper_project44_forwardair = "4011"
    eshipper_project44_frontline_freight = "4045"
    eshipper_project44_holland_motor_express = "4000"
    eshipper_project44_jp_express = "5961"
    eshipper_project44_lakeville_motor_express = "4023"
    eshipper_project44_midwest_motor_express = "4024"
    eshipper_project44_monroe_transportation_services = "4036"
    eshipper_project44_mountain_valley_express = "5963"
    eshipper_project44_nm_transfer = "4039"
    eshipper_project44_new_england_motor_freight = "4013"
    eshipper_project44_new_england_motor_freight = "4012"
    eshipper_project44_new_penn_motor_express = "4003"
    eshipper_project44_oak_harbor_freight = "5966"
    eshipper_project44_old_dominion_freight = "5954"
    eshipper_project44_pitt_ohio = "4020"
    eshipper_project44_pitt_ohio = "5956"
    eshipper_project44_rl_carriers = "5953"
    eshipper_project44_roadrunner_transportation_services = "4001"
    eshipper_project44_roadrunner_transportation_services = "4017"
    eshipper_project44_roadrunner_transportation_systems = "5951"
    eshipper_project44_saia_ltl_freight = "5957"
    eshipper_project44_saia_motor_freight = "4016"
    eshipper_project44_southeastern_freight_lines = "4031"
    eshipper_project44_southeastern_freight = "5970"
    eshipper_project44_southwestern_motor_transport = "4033"
    eshipper_project44_standard_forwarding = "4042"
    eshipper_project44_total_transportation_distribution = "4046"
    eshipper_project44_ups = "4022"
    eshipper_project44_ups = "4004"
    eshipper_project44_ups = "5959"
    eshipper_project44_usf_reddaway = "4029"
    eshipper_project44_valley_cartage = "4038"
    eshipper_project44_vision_express_ltl = "4014"
    eshipper_project44_ward_trucking = "4037"
    eshipper_project44_ward_trucking = "5962"
    eshipper_project44_xpo_logistics = "4059"
    eshipper_project44_yrc = "4002"
    eshipper_purolator_express = "4"
    eshipper_purolator_express_1030 = "6"
    eshipper_purolator_express_9am = "5"
    eshipper_purolator_expresscheque = "18"
    eshipper_purolator_ground = "13"
    eshipper_purolator_ground_1030 = "20"
    eshipper_purolator_ground_9am = "19"
    eshipper_purolator_puroletter = "7"
    eshipper_purolator_puroletter_1030 = "9"
    eshipper_purolator_puroletter_9am = "8"
    eshipper_purolator_puropak = "10"
    eshipper_purolator_puropak_1030 = "12"
    eshipper_purolator_puropak_9am = "11"
    eshipper_pyk_ground_advantage = "5701"
    eshipper_pyk_priority_mail = "5702"
    eshipper_sameday_h1_deliver_to_curbside = "3607"
    eshipper_sameday_h4_delivery_to_curbside = "3610"
    eshipper_sameday_h5_delivery_to_room_of_choice___2_man = "3611"
    eshipper_sameday_h6_delivery_packaging_removal___2_man = "3612"
    eshipper_sameday_ltl_service = "3606"
    eshipper_skip = "5902"
    eshipper_skip = "5901"
    eshipper_tforce_freight_ltl = "5931"
    eshipper_tforce_freight_ltl___guaranteed = "5932"
    eshipper_tforce_freight_ltl___guaranteed_am = "5933"
    eshipper_tforce_freight_tforce_standard_ltl = "5934"
    eshipper_tst_ltl_trucking = "1100"
    eshipper_ups_expedited = "601"
    eshipper_ups_express = "600"
    eshipper_ups_express_early_am = "605"
    eshipper_ups_ground = "608"
    eshipper_ups_second_day_air_am = "611"
    eshipper_ups_standard = "604"
    eshipper_ups_three_day_select = "606"
    eshipper_ups_next_day_air_saver = "609"
    eshipper_ups_saver = "607"
    eshipper_ups_worldwide_expedited = "603"
    eshipper_ups_worldwide_express = "602"
    eshipper_ups_worldwide_express_plus = "610"
    # fmt: on

    @staticmethod
    def carrier_id(service_id: str) -> str:
        return next(
            (_ for _, __ in CARRIER_SERVICES.items() if str(service_id) in __),
            "5000011",
        )

    @staticmethod
    def carrier(service_id: str) -> str:
        return CARRIER_IDS.get(ShippingService.carrier_id(service_id))


class ShippingOption(lib.Enum):
    """Carrier specific options"""

    eshipper_signature_required = lib.OptionEnum("signatureRequired", bool)
    eshipper_insurance_type = lib.OptionEnum("insuranceType")
    eshipper_dangerous_goods_type = lib.OptionEnum("dangerousGoodsType", bool)
    eshipper_cod = lib.OptionEnum("cod", float)
    eshipper_is_saturday_service = lib.OptionEnum("isSaturdayService", bool)
    eshipper_hold_for_pickup_required = lib.OptionEnum("holdForPickupRequired", bool)
    eshipper_special_equipment = lib.OptionEnum("specialEquipment", bool)
    eshipper_inside_delivery = lib.OptionEnum("insideDelivery", bool)
    eshipper_delivery_appointment = lib.OptionEnum("deliveryAppointment", bool)
    eshipper_inside_pickup = lib.OptionEnum("insidePickup", bool)
    eshipper_saturday_pickup_required = lib.OptionEnum("saturdayPickupRequired", bool)
    eshipper_stackable = lib.OptionEnum("stackable", bool)

    """ Unified Option type mapping """
    cash_on_delivery = eshipper_cod
    insurance = eshipper_insurance_type
    signature_confirmation = eshipper_signature_required
    saturday_delivery = eshipper_is_saturday_service
    hold_at_location = eshipper_hold_for_pickup_required
    dangerous_good = eshipper_dangerous_goods_type


def shipping_options_initializer(
    options: dict,
    package_options: units.ShippingOptions = None,
) -> units.ShippingOptions:
    """
    Apply default values to the given options.
    """

    if package_options is not None:
        options.update(package_options.content)

    def items_filter(key: str) -> bool:
        return key in ShippingOption  # type: ignore

    return units.ShippingOptions(options, ShippingOption, items_filter=items_filter)



CARRIER_IDS = {
    "27": "aramex",
    "45": "canpar",
    "55": "day_ross",
    "4": "dhl_express",
    "42": "eshipper",
    "68": "fastfrate",
    "1": "fedex",
    "71": "fedex_freight",
    "40": "project44",
    "2": "purolator",
    "57": "pyk",
    "36": "sameday",
    "59": "skip",
    "70": "tforce_freight",
    "6": "ups"
}

DEV_CARRIER_IDS = {
    "5000001": "aramex",
    "5000002": "canadapost",
    "5000003": "canpar",
    "5000017": "day_ross",
    "5000004": "dhl_express",
    "5000011": "eshipper",
    "5000005": "fedex",
    "8000010": "flashbird",
    "56": "fleet_optics",
    "5000008": "project44",
    "5000007": "purolator",
    "5000047": "pyk",
    "5000014": "sameday",
    "5000048": "skip",
    "5000015": "smartepost_intl",
    "5000010": "ups",
    "5000013": "usps",
}

CARRIER_SERVICES = {
    "56": ["5000458", "5000458", "5000458", "5000458"],
    "5000001": [
        "5000047",
        "5000047",
        "5000046",
        "5000046",
        "5000048",
        "5000048",
        "5000049",
        "5000049",
    ],
    "5000002": [
        "5000181",
        "5000181",
        "5000181",
        "5000028",
        "5000028",
        "5000028",
        "5000029",
        "5000029",
        "5000029",
        "5000025",
        "5000025",
        "5000025",
        "5000031",
        "5000031",
        "5000031",
        "5000035",
        "5000035",
        "5000035",
        "5000034",
        "5000034",
        "5000034",
        "5000033",
        "5000033",
        "5000033",
        "5000027",
        "5000027",
        "5000027",
        "5000024",
        "5000024",
        "5000024",
        "5000032",
        "5000032",
        "5000032",
        "5000026",
        "5000026",
        "5000026",
        "5000030",
        "5000030",
        "5000030",
    ],
    "5000003": [
        "5000134",
        "5000134",
        "5000134",
        "5000133",
        "5000133",
        "5000133",
        "5000132",
        "5000132",
        "5000132",
        "5000125",
        "5000125",
        "5000125",
        "5000128",
        "5000128",
        "5000128",
        "5000127",
        "5000127",
        "5000127",
        "5000126",
        "5000126",
        "5000126",
        "5000135",
        "5000135",
        "5000135",
        "5000184",
        "5000184",
        "5000184",
        "5000131",
        "5000131",
        "5000131",
        "5000130",
        "5000130",
        "5000130",
        "5000129",
        "5000129",
        "5000129",
    ],
    "5000004": [
        "5000020",
        "5000020",
        "5000021",
        "5000021",
        "5000019",
        "5000019",
        "5000015",
        "5000015",
        "5000023",
        "5000023",
        "5000014",
        "5000014",
        "5000180",
        "5000180",
        "5000017",
        "5000017",
        "5000016",
        "5000016",
        "5000018",
        "5000018",
        "5000186",
        "5000186",
        "5000022",
        "5000022",
    ],
    "5000005": [
        "5000172",
        "5000172",
        "5000172",
        "5000169",
        "5000169",
        "5000169",
        "5000175",
        "5000175",
        "5000175",
        "8000023",
        "8000023",
        "8000023",
        "8000022",
        "8000022",
        "8000022",
        "5000176",
        "5000176",
        "5000176",
        "5000179",
        "5000179",
        "5000179",
        "8000018",
        "8000018",
        "8000018",
        "8000017",
        "8000017",
        "8000017",
        "5000183",
        "5000183",
        "5000183",
        "5000171",
        "5000171",
        "5000171",
        "5000170",
        "5000170",
        "5000170",
        "5000174",
        "5000174",
        "5000174",
        "5000173",
        "5000173",
        "5000173",
        "5000178",
        "5000178",
        "5000178",
        "5000177",
        "5000177",
        "5000177",
    ],
    "5000007": [
        "5000008",
        "5000008",
        "5000008",
        "5000009",
        "5000009",
        "5000009",
        "5000007",
        "5000007",
        "5000007",
        "5000005",
        "5000005",
        "5000005",
        "5000006",
        "5000006",
        "5000006",
        "5000004",
        "5000004",
        "5000004",
        "5000012",
        "5000012",
        "5000012",
        "5000013",
        "5000013",
        "5000013",
        "5000010",
        "5000010",
        "5000010",
        "5000011",
        "5000011",
        "5000011",
        "5000002",
        "5000002",
        "5000002",
        "5000003",
        "5000003",
        "5000003",
        "5000001",
        "5000001",
        "5000001",
    ],
    "5000008": [
        "5000056",
        "5000053",
        "5000413",
        "5000109",
        "5000110",
        "5000088",
        "5000065",
        "5000089",
        "5000080",
        "5000055",
        "5000073",
        "5000098",
        "5000097",
        "5000093",
        "5000084",
        "5000082",
        "5000067",
        "5000068",
        "5000052",
        "5000058",
        "5000100",
        "5000094",
        "5000071",
        "5000054",
        "5000063",
        "5000064",
        "5000090",
        "5000087",
        "5000075",
        "5000104",
        "5000074",
        "5000069",
        "5000051",
        "5000096",
        "5000062",
        "5000060",
        "5000106",
        "5000108",
        "5000107",
        "5000059",
        "5000070",
        "5000105",
        "5000077",
        "5000061",
        "5000076",
        "5000078",
        "5000091",
        "5000072",
        "5000101",
        "5000099",
        "5000083",
        "5000057",
        "5000095",
        "5000086",
        "5000085",
        "5000066",
        "5000102",
        "5000079",
        "5000111",
        "5000092",
        "5000081",
        "5000103",
    ],
    "5000010": [
        "5000044",
        "5000044",
        "5000044",
        "5000037",
        "5000037",
        "5000037",
        "5000038",
        "5000038",
        "5000038",
        "5000042",
        "5000042",
        "5000042",
        "5000041",
        "5000041",
        "5000041",
        "5000039",
        "5000039",
        "5000039",
        "5000045",
        "5000045",
        "5000045",
        "5000043",
        "5000043",
        "5000043",
        "5000040",
        "5000040",
        "5000040",
        "5000036",
        "5000036",
        "5000036",
        "5000182",
        "5000182",
        "5000182",
    ],
    "5000011": [
        "5000115",
        "5000113",
        "5000112",
        "5000119",
        "5000114",
        "5000116",
        "5000123",
        "5000117",
        "5000122",
        "5000421",
        "5000419",
        "5000121",
        "5000420",
        "5000118",
        "5000124",
        "5000120",
        "5000414",
    ],
    "5000013": [
        "5000153",
        "5000153",
        "8000003",
        "5000152",
        "5000152",
        "5000151",
        "5000151",
        "5000150",
        "5000150",
        "5000155",
        "5000155",
        "5000154",
        "5000154",
        "5000149",
        "5000149",
        "5000148",
        "5000148",
        "5000147",
        "5000147",
        "8000002",
        "5000146",
    ],
    "5000014": [
        "5000168",
        "5000167",
        "5000166",
        "5000165",
        "5000164",
        "5000163",
        "5000162",
        "5000161",
        "5000160",
        "5000159",
        "5000158",
        "5000157",
        "5000156",
    ],
    "5000015": [
        "5000145",
        "5000145",
        "5000145",
        "5000144",
        "5000144",
        "5000144",
        "5000143",
        "5000143",
        "5000143",
        "5000142",
        "5000142",
        "5000142",
        "5000141",
        "5000141",
        "5000141",
        "5000140",
        "5000140",
        "5000140",
        "5000139",
        "5000139",
        "5000139",
        "5000138",
        "5000138",
        "5000138",
        "5000137",
        "5000137",
        "5000137",
        "8000053",
    ],
    "5000016": ["5000454"],
    "5000017": ["5000457"],
    "5000047": ["5000460", "5000460", "5000459", "5000459"],
    "5000048": ["8000020", "8000019"],
    "8000010": ["8000032"],
}


class TrackingStatus(lib.Enum):
    on_hold = ["on_hold"]
    delivered = ["delivered"]
    in_transit = ["in_transit"]
    delivery_failed = ["delivery_failed"]
    delivery_delayed = ["delivery_delayed"]
    out_for_delivery = ["out_for_delivery"]
    ready_for_pickup = ["ready_for_pickup"]
