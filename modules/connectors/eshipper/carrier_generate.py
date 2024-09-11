import json
from collections import Counter


def clean_carrier_name(name):
    return 'Fedex' if name == 'Federal Express' else name


def generate_service_code(carrier_name, service_name):
    if carrier_name not in service_name:
        return f"{carrier_name} {service_name}"
    return service_name


def clean_code(code):
    code = ''.join(char.lower() for char in code if char.isalnum() or char in ['_', ' ', '-'])
    return (code
            .replace('  ', '_')
            .replace(' ', '_')
            .replace('-', '_')
            .replace('e_shipper_', '')
            )


def generate_base_code(service):
    carrier_name = clean_carrier_name(service["carrierDTO"]["name"])
    service_name = service["name"]

    code = generate_service_code(carrier_name, service_name)
    code = clean_code(code)
    code = "eshipper_" + code

    if service['id'] == 609:
        code = "eshipper_ups_next_day_air_saver"

    return code


def resolve_duplicate(code, service, iteration):
    if iteration == 1 and service["code"] and service["code"].lower() not in code:
        return f"{code}_{service['code'].lower()}"
    elif iteration == 2 and service["codeUs"] and service["codeUs"].lower() not in code:
        return f"{code}_{service['codeUs'].lower()}"
    elif iteration == 3 and service["mode"] and str(service["mode"]) not in code:
        return f"{code}_{service['mode']}"
    return code


def generate_codes(data):
    codes = [(generate_base_code(service), str(service["id"]), service) for service in data]
    duplicates = [code for code, count in Counter(code for code, _, _ in codes).items() if count > 1]

    for iteration in range(1, 5):  # Now we go up to 4 iterations
        new_codes = []
        duplicate_counts = {}  # To keep track of how many times we've seen each duplicate

        for code, id, service in codes:
            if code in duplicates:
                if iteration < 4:
                    new_code = resolve_duplicate(code, service, iteration)
                else:
                    # In the 4th iteration, append a number
                    duplicate_counts[code] = duplicate_counts.get(code, 0) + 1
                    new_code = f"{code}_{duplicate_counts[code]}"
            else:
                new_code = code
            new_codes.append((new_code, id, service))

        codes = new_codes
        duplicates = [code for code, count in Counter(code for code, _, _ in codes).items() if count > 1]

        if not duplicates:
            break

    return [(code, id) for code, id, _ in codes], duplicates


def main():
    with open('schemas/carriers.json') as f:
        data = json.load(f)

    final_codes, final_duplicates = generate_codes(data)

    print("Duplicates:", final_duplicates)

    # Uncomment to print all codes
    for code, id in final_codes:
        print(f'   {code} = "{id}"')


if __name__ == "__main__":
    main()
