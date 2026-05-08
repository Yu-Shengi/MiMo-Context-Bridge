import tiktoken
from pathlib import Path

class TokenCounter:
    """负责计算文本的 Token 数量"""
    def __init__(self, model="gpt-4"):
        try:
            self.encoder = tiktoken.encoding_for_model(model)
        except:
            self.encoder = tiktoken.get_encoding("cl100k_base")

    def count(self, text):
        return len(self.encoder.encode(text))

class FileAggregator:
    """负责扫描和读取符合条件的文件"""
    def __init__(self, root_path, extensions=None):
        self.root_path = Path(root_path)
        self.extensions = extensions or ['.py', '.js', '.ts', '.md', '.json', '.txt']

    def get_files(self, ignore_spec):
        for p in self.root_path.rglob("*"):
            if p.is_file() and p.suffix in self.extensions:
                if not ignore_spec.match_file(str(p.relative_to(self.root_path))):
                    yield p
