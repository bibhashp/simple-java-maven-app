def convert_plist_data_to_treetable1(plist_json_data, index):
    items = []

    def process_node(node, key, parent_id, current_index):
        node_type = type(node).__name__
        id = current_index if parent_id is None else f"{parent_id}.{current_index.split('.')[-1]}"
        current_index = id

        if node_type == 'dict':
            items.append({
                'id': current_index,
                'parentId': parent_id,
                'key': key,
                'TYPE': 'Dict',
                'Value': f'({len(node)} Items)'
            })
            for i, (k, v) in enumerate(node.items(), start=1):
                process_node(v, k, current_index, f"{current_index}.{i}")
        elif node_type == 'list':
            items.append({
                'id': current_index,
                'parentId': parent_id,
                'key': key,
                'TYPE': 'Array',
                'Value': f'({len(node)} Items)'
            })
            for i, v in enumerate(node, start=1):
                process_node(v, f'Item {i - 1}', current_index, f"{current_index}.{i}")
        elif node_type == 'str':
            items.append({
                'id': current_index,
                'parentId': parent_id,
                'key': key,
                'TYPE': 'str',
                'Value': node
            })
        elif node_type == 'int':
            items.append({
                'id': current_index,
                'parentId': parent_id,
                'key': key,
                'TYPE': 'Number',
                'Value': node
            })
        elif node_type == 'bool':
            items.append({
                'id': current_index,
                'parentId': parent_id,
                'key': key,
                'TYPE': 'boolean',
                'Value': node
            })
        elif node_type == 'float':
            items.append({
                'id': current_index,
                'parentId': parent_id,
                'key': key,
                'TYPE': 'Number',
                'Value': node
            })
        elif node_type == 'datetime':
            items.append({
                'id': current_index,
                'parentId': parent_id,
                'key': key,
                'TYPE': 'Date',
                'Value': node.isoformat()
            })

    current_index = f"{index}.1"
    for i, (key, value) in enumerate(plist_json_data.items(), start=1):
        process_node(value, key, None, f"{index}.{i}")

    return items


def convert_plist_data_to_treetable(plist_json_data, index):
    items = []

    def process_node(node, key, parent_id, current_index):
        node_type = type(node).__name__
        if node_type == 'dict':

            if parent_id:
                items.append({
                    'id': current_index,
                    'parentId': parent_id,
                    'key': key,
                    'TYPE': 'Dict',
                    'Value': f'({len(node)} Items)'
                })
            else:
                items.append({
                    'id': current_index,
                    'key': key,
                    'TYPE': 'Dict',
                    'Value': f'({len(node)} Items)'
                })
            parent_id = current_index
            current_index += 1
            for k, v in node.items():
                current_index = process_node(v, k, parent_id, current_index)
        elif node_type == 'list':
            items.append({
                'id': current_index,
                'parentId': parent_id,
                'key': key,
                'TYPE': 'Array',
                'Value': f'({len(node)} Items)'
            })
            parent_id = current_index
            current_index += 1
            for idx, v in enumerate(node):
                current_index = process_node(v, f'Item {idx}', parent_id, current_index)
        elif node_type == 'str':
            items.append({
                'id': current_index,
                'parentId': parent_id,
                'key': key,
                'TYPE': 'str',
                'Value': node
            })
            current_index += 1
        elif node_type == 'int':
            items.append({
                'id': current_index,
                'parentId': parent_id,
                'key': key,
                'TYPE': 'Number',
                'Value': node
            })
            current_index += 1
        elif node_type == 'bool':
            items.append({
                'id': current_index,
                'parentId': parent_id,
                'key': key,
                'TYPE': 'boolean',
                'Value': node
            })
            current_index += 1
        elif node_type == 'float':
            items.append({
                'id': current_index,
                'parentId': parent_id,
                'key': key,
                'TYPE': 'Number',
                'Value': node
            })
            current_index += 1
        elif node_type == 'datetime':
            items.append({
                'id': current_index,
                'parentId': parent_id,
                'key': key,
                'TYPE': 'Date',
                'Value': node.isoformat()
            })
            current_index += 1
        return current_index

    current_index = index * 100
    for key, value in plist_json_data.items():
        current_index = process_node(value, key, None, current_index)

    return items





# Example usage
plist_json_data = {
    "CBundle.plist": {
        "AvailableLibraries": [
            {
                "DebugSymbolsPath": "dSYMs",
                "LibraryIdentifier": "ios-arm64_x86_64-maccatalyst",
                "LibraryPath": "dumb.framework",
                "SupportedArchitectures": [
                    "arm64",
                    "x86_64"
                ],
                "SupportedPlatform": "ios",
                "SupportedPlatformVariant": "maccatalyst",
                "CFBundlePackageType": "XFWK",
                "XCFrameworkFormatVersion": "1.0"
            }
        ]
    }
}

index = 2
items = convert_plist_data_to_treetable(plist_json_data, index)
print(items)
#for item in items:
#    print(item)
