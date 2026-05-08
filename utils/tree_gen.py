def generate_tree(path, ignore_spec, prefix=""):
    """递归生成目录树字符串"""
    tree_str = ""
    paths = sorted([p for p in path.iterdir() if not ignore_spec.match_file(str(p.name))])
    for i, p in enumerate(paths):
        connector = "└── " if i == len(paths) - 1 else "├── "
        tree_str += f"{prefix}{connector}{p.name}\n"
        if p.is_dir():
            extension = "    " if i == len(paths) - 1 else "│   "
            tree_str += generate_tree(p, ignore_spec, prefix + extension)
    return tree_str
