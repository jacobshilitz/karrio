import json

from oauthlib.oauth2.rfc6749.grant_types.authorization_code import code_challenge_method_s256

# Load the JSON data from the file
with open('schemas/carriers.json') as f:
    data = json.load(f)

for service in data:
    carrier_name = service["carrierDTO"]["name"]
    service_name = service["name"]
    id = service["id"]

    if carrier_name == 'Federal Express':
        carrier_name = 'Fedex'

    if not carrier_name in service_name:
        code = f"{carrier_name} {service_name}"
    else:
        code = f"{service_name}"

    code = ''.join(filter(lambda x: x.isalnum() or x in ['_', ' ', '-'], code.lower()))
    code = (code
            .replace('  ', '_')
            .replace(' ', '_')
            .replace('-', '_')
            .replace('e_shipper_', '')
            )

    code = "eshipper_" + code

    if id == 609:
        code = "eshipper_ups_next_day_air_saver"

    code = code + ' = "' + str(id) + '"'
    code = "    " + code
    print(code)
#
#
# # Generate the Python code
# python_code = 'class ShippingService(lib.StrEnum):\n'
# python_code += '    """Carrier specific services"""\n\n'
# for service in shipping_services_list:
#     python_code += f'    {service} = "{data[service]}"\n'
#
# # Save the Python code to a file
# with open('shipping_services.py', 'w') as f:
#     f.write(python_code)
#
# print('File generated: shipping_services.py')
