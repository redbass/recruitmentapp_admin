import csv

from lib.core_integration import get_json_from_core


def get_picklist_values(entity_name, none_value=None, as_dict=False):
    results = get_json_from_core(path='/api/picklist/' + entity_name,
                                 is_admin=False)

    values = [(p['key'], p['value']) for p in results]

    if none_value:
        values.insert(0, ('', none_value))

    return values


def csv_to_json_values(csv_file):
    reader = csv.DictReader(csv_file,
                            delimiter=',',
                            fieldnames=['key', 'value'],
                            skipinitialspace=True)

    result = []
    for row in reader:
        if row['key'] and row['value']:
            row['key'] = row['key'].rstrip()
            row['value'] = row['value'].rstrip()
            result.append(row)

    return result


def json_values_to_csv(json_values):
    rows = ['{key},{value}'.format(key=row[0], value=row[1])
            for row in json_values]
    return '\n'.join(rows)
