from pathlib import Path

def target_file_path(input_dir: str, source_ext: str) -> list[str]:
    """
    get all file path matching the source_ext.
    if sub_dir provided, get all file path with parent dir plus sub_dir and the full file name.
    """
    # Dictionary to group files by their base name
    file_groups = {}

    folder_path = Path(input_dir)

    # Iterate through all files in the folder, extracting file path with the same file name
    for file in folder_path.rglob("*"):
        if file.is_file():
            # get file name without extension
            base_name = file.stem
            print(base_name)
            if base_name not in file_groups:
                file_groups[base_name] = set()
            file_groups[base_name].add(file)
    
    print(file_groups)

    # Identify file with only source extension and no other file with the same file name
    only_target_file = [
        file 
        for base_name, file_set in file_groups.items() 
        for file in file_set
        if file.suffix == source_ext and len(file_set) == 1
    ]
    print(only_target_file)

    target_files = []

    for file in only_target_file:
        target_files.append(str(file.resolve()))

    return target_files


def target_file_path_with_level(input_dir: str, source_ext: str, level: int) -> list[str]:
    """
    get all file path matching the source_ext.
    if sub_dir provided, get all file path with parent dir plus sub_dir and the full file name.
    """
    # Dictionary to group files by their base name
    file_groups = {}

    folder_path = Path(input_dir)
    
    # Iterate through files in the specific level folder, extracting file path with the same file name
    for depth in range(level + 1):
        # Create pattern like * for depth0, */* for depth1, */*/* for depth2
        pattern = '*/' * depth + '*'
        for path in folder_path.glob(pattern):
            if path.is_file():

                # get file name without extension
                base_name = path.stem
                print(base_name)
                if base_name not in file_groups:
                    file_groups[base_name] = set()
                file_groups[base_name].add(path)
    
    print(file_groups)

    # Identify file with only source extension and no other file with the same file name
    only_target_file = [
        file 
        for base_name, file_set in file_groups.items() 
        for file in file_set
        if file.suffix == source_ext and len(file_set) == 1
    ]
    print(only_target_file)

    target_files = []

    for file in only_target_file:
        target_files.append(str(file.resolve()))

    return target_files