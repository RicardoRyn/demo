# 项目上下文文件 (IFLOW.md)

## 项目概述

这是一个使用 Zensical 框架构建的文档项目，名为 "Project Demo"。该项目主要用于学习和演示各种项目相关操作，包含一个简单的 Python 应用作为示例代码，并配备了完整的文档系统。

## 项目结构

- `.github/` - GitHub 工作流配置
- `.jj/` - Jujutsu 版本控制系统目录
- `docs/` - 文档源文件目录
- `site/` - 构建后的网站输出目录
- `main.py` - 项目的主要 Python 源代码
- `pyproject.toml` - Python 项目配置文件
- `zensical.toml` - Zensical 文档生成器配置文件
- `README.md` - 项目说明文件

## 技术栈

- **Python 3.12+** - 项目编程语言
- **Zensical** - 文档生成框架 (类似 Material for MkDocs)
- **TOML** - 配置文件格式

## 代码项目详情

### 主要功能

项目包含一个简单的 Python 程序 (`main.py`)，其中包含一个 `main()` 函数和一个 `my_add()` 函数用于演示基本功能。

### 文档系统

项目使用 Zensical 作为文档生成工具，支持以下功能：
- 多语言支持 (当前配置为英语，但文档已翻译为中文)
- 深色/浅色主题切换
- 代码块高亮和注释
- 内容标签页
- 数学公式渲染
- 交互式图表
- 任务列表
- 工具提示等

## 构建和运行

### Python 程序运行
```bash
python main.py
```

### 文档系统
```bash
# 安装依赖 (使用 uv)
uv sync

# 启动文档服务器
zensical serve

# 构建文档站点
zensical build
```

## 开发约定

- 项目使用 Python 3.12 及以上版本
- 文档使用 Markdown 格式编写
- 使用 Zensical 特定的 Markdown 扩展语法 (如注释框、内容标签等)
- 配置文件使用 TOML 格式

## 项目配置

- **站点名称**: Project Demo
- **站点描述**: A new project generated from the default template project
- **作者**: Ricardo Ryn
- **网站URL**: https://ricardoryn.github.io/demo
- **主题**: Zensical (Material for MkDocs 衍生)
- **语言**: 英语 (支持多语言)