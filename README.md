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


# LLM-Context-Flux 🚀

[![License MIT](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Xiaomi MiLM Compatible](https://img.shields.io/badge/Xiaomi-MiLM--Ready-orange.svg)](https://github.com/Xiaomi/MiLM)

**LLM-Context-Flux** 是一个专为大语言模型（LLM）开发者设计的高性能代码上下文集成工具。它能将复杂的本地工程项目无损地转化为适合 AI 理解的结构化 Markdown，并实时计算 Token 消耗，是提升 AI 辅助编程效率的必备神器。

## 📖 项目背景

在利用 ChatGPT、Claude 或小米 MiLM 处理大型代码库任务（如重构、Debug、功能实现）时，开发者常面临以下痛点：
1. **上下文碎片化**：手动复制文件容易遗漏层级关系。
2. **Token 溢出**：无法精准预知代码量是否超过模型窗口限制。
3. **噪声干扰**：无关的二进制文件、缓存文件干扰 AI 判断。

本项目通过自动化管道（Pipeline）解决上述问题，让 AI “秒懂”你的整个项目。

## ✨ 核心特性

- **📂 智能树状视图**：自动生成完整的项目目录结构。
- **🔍 深度依赖过滤**：完美支持 `.gitignore` 规范，自动剔除 `node_modules`、`venv` 及各类缓存。
- **📊 精确 Token 计量**：集成 `tiktoken` 库，支持 cl100k_base 编码，预估 API 调用成本。
- **🧩 模块化设计**：核心逻辑与 UI 逻辑解耦，支持作为 Python 模块集成到其他系统。
- **📑 自动化排版**：输出的 Markdown 包含文件路径锚点及对应的语法高亮块。

## 🛠️ 技术架构

项目采用生产级目录结构，确保可扩展性：
- `core/`: 核心引擎，负责文件扫描、编码处理及 Token 分析。
- `utils/`: 工具箱，包含递归算法实现的项目树生成器。
- `examples/`: 预生成的输出示例。
- `main.py`: 项目入口，集成命令行交互逻辑。

## 🚀 快速开始

### 1. 环境准备
确保你的系统已安装 Python 3.8 或更高版本。

```bash
# 克隆仓库
git clone [https://github.com/你的用户名/LLM-Context-Flux.git](https://github.com/你的用户名/LLM-Context-Flux.git)
cd LLM-Context-Flux

# 安装依赖
pip install -r requirements.txt
