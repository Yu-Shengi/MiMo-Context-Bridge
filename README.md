# LLM-Context-Flux 🚀

**LLM-Context-Flux** 是一个高性能的代码上下文集成工具，专为开发者向大模型（LLM）提交项目背景而设计。它可以一键将整个工程的结构和代码合并为一个结构化的 Markdown 文档，并自动计算 Token 消耗。

## 🌟 核心特性
- **智能过滤**：自动识别 `.gitignore` 配置，跳过依赖库和二进制文件。
- **结构化输出**：自动生成可视化的目录树（Directory Tree）。
- **Token 估算**：集成 `tiktoken`，精确计算上下文长度，避免超出 LLM 上限。
- **代码高亮**：合并后的文档保留原始语言语法高亮，方便 AI 阅读。

## 🛠️ 快速开始

### 安装依赖
```bash
pip install tiktoken pathspec rich
