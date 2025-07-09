from pathlib import Path
from collections import deque


def filter_files_by_extension(path_list, extensions):
    """
    Filters a list of paths to include only files with specified extensions.

    Args:
        path_list (list): List of file paths (strings or Path objects)
        extensions (list): List of target extensions (e.g., ['.txt', '.md'])

    Returns:
        list: Filtered Path objects with specified extensions
    """
    # Convert extensions to lowercase for case-insensitive matching
    ext_set = {ext.lower() for ext in extensions}

    filtered_files = []
    for item in path_list:
        path = Path(item) if not isinstance(item, Path) else item

        # Skip directories and non-existent paths
        if not path.is_file():
            continue

        # Check if extension matches (case-insensitive)
        if path.suffix.lower() in ext_set:
            filtered_files.append(path)

    return filtered_files


def list_files_by_depth(root_path: str, max_depth: int) -> list[str]:
    """
    List files up to a specified depth level.
    Returns all available files if max_depth exceeds actual folder depth.
    """
    root = Path(root_path)
    if not root.is_dir():
        raise ValueError(f"Path '{root}' is not a directory")

    files = []
    queue = deque([(root, 0)])  # (folder_path, current_depth)

    while queue:
        current_dir, depth = queue.popleft()

        for item in current_dir.iterdir():
            if item.is_file() and depth <= max_depth:
                files.append(item)
            elif item.is_dir():
                next_depth = depth + 1
                if next_depth <= max_depth:
                    queue.append((item, next_depth))

    return files
