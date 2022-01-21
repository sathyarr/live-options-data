from jsonfinder import jsonfinder

target_obj_keys_list = ['total', 'page', 'records', 'rows']
target_column_name = 'Symbol'


def get_rows_and_headers(target_script_tag):
    target_obj = {}
    target_column_names = []
    found = 0

    for start, end, obj in jsonfinder(target_script_tag, json_only=True):
        if isinstance(obj, dict) and list(obj.keys()) == target_obj_keys_list:
            target_obj = obj
            found += 1
        if obj and isinstance(obj, list) and obj[0] == target_column_name:
            target_column_names = obj
            found += 1

    if len(target_obj) == 0:
        raise ValueError('target rows not found')

    if len(target_column_names) == 0:
        raise ValueError('target column names not found')

    return target_obj, target_column_names
