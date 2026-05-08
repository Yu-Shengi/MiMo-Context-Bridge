import os
import pathspec
from pathlib import Path
from core.processor import TokenCounter, FileAggregator
from utils.tree_gen import generate_tree

def main():
    root = Path(os.getcwd())
    ignore_patterns = [".git/", "__pycache__/", "node_modules/", "dist/"]
    spec = pathspec.PathSpec.from_lines('gitwildmatch', ignore_patterns)
    
    aggregator = FileAggregator(root)
    counter = TokenCounter()
    
    print("🔍 正在扫描项目文件...")
    content = f"# Project: {root.name}\n\n## Directory Structure\n```\n"
    content += generate_tree(root, spec)
    content += "
```\n\n"
    
    for file_path in aggregator.get_files(spec):
        rel_path = file_path.relative_to(root)
        print(f"📄 正在读取: {rel_path}")
        content += f"### File: {rel_path}\n"
        content += f"```{file_path.suffix[1:]}\n{file_path.read_text(errors='ignore')}\n```\n\n"
    
    token_total = counter.count(content)
    with open("LLM_READY_CONTEXT.md", "w", encoding="utf-8") as f:
        f.write(f"> **Token Count: {token_total}**\n\n" + content)
    
    print(f"✅ 完成！总计 Token: {token_total}")

if __name__ == "__main__":
    main()
