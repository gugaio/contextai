def extract_keys(json_obj, prefix=''):
    keys = []
    if isinstance(json_obj, dict):
        for key, value in json_obj.items():
            full_key = f"{prefix}.{key}" if prefix else key
            keys.append(full_key)
            keys.extend(extract_keys(value, full_key))
    elif isinstance(json_obj, list):
        for i, item in enumerate(json_obj):
            keys.extend(extract_keys(item, f"{prefix}[{i}]"))
    return keys

def extract_keys_comma_separated(json_obj):
    keys = extract_keys(json_obj)
    return ", ".join(keys)

def get_nested_value(data, nested_key):
    keys = nested_key.split('.')
    value = data.copy()
    for key in keys:
        key = key.strip()
        if key.endswith(']'):
            # Handle list index
            list_key, index = key[:-1].split('[')
            if isinstance(value, dict) and list_key in value and isinstance(value[list_key], list) and len(value[list_key]) > int(index):
                value = value[list_key][int(index)]
            else:
                return ""
        else:
            if isinstance(value, dict) and key in value:
                value = value[key]
            else:
                return ""
            
    return value