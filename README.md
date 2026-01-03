# pymg
A module managed by Python.


# Python Upgrade (pymg) 命令手册

---
**版本**: 1.0.0  
**最后更新**: 2024-12-25  
**项目地址**: https://github.com/python-upgrade/pymg

---

## 简介

`python-upgrade`（简称 pymg）是一个跨平台的 Python 版本管理工具，允许您在系统中安装、卸载、切换和管理多个 Python 版本。它提供了简洁的命令行接口，避免了与 Python 自带命令的冲突。

---

## 安装

### 快速安装
```bash
curl -fsSL https://pymg.sh/install | bash
```

### 手动安装
```bash
git clone https://github.com/python-upgrade/pymg.git ~/.pymg
echo 'export PATH="$HOME/.pymg/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

### pip 安装
```bash
pip install pymg
```

---

## 核心命令

### `python-upgrade`
**主命令**，用于将系统默认 Python 升级到最新稳定版本

```bash
# 升级到最新稳定版
python-upgrade

# 升级到指定版本
python-upgrade 3.12.0

# 升级到指定系列的最新版
python-upgrade 3.11

# 强制重新安装
python-upgrade --force

# 安装后自动迁移包
python-upgrade --migrate-packages
```

**选项**:
- `-f, --force`: 强制覆盖已安装版本
- `-m, --migrate-packages`: 自动迁移旧版本的第三方包
- `-q, --quiet`: 静默模式
- `-v, --verbose`: 详细输出

---

## 基础管理命令

### `pymg install <version>`
安装指定 Python 版本

```bash
# 安装特定版本
pymg install 3.11.3

# 从源码编译安装
pymg install 3.12.0 --build-from-source

# 指定安装路径
pymg install 3.10.5 --install-dir=/opt/python/3.10.5

# 安装最新稳定版
pymg install latest

# 安装预发布版本
pymg install 3.13.0a1 --prerelease
```

**选项**:
- `--build-from-source`: 从源码编译
- `--prerelease`: 允许安装预发布版本
- `--install-dir PATH`: 自定义安装路径

---

### `pymg uninstall <version>`
卸载指定 Python 版本

```bash
# 卸载特定版本
pymg uninstall 3.9.7

# 强制卸载（不提示确认）
pymg uninstall 3.9.7 --force

# 卸载时清理相关缓存
pymg uninstall 3.9.7 --clean-cache
```

---

### `pymg list`
列出所有已安装的 Python 版本

```bash
# 列出所有版本
pymg list

# 仅显示可用版本
pymg list --available

# 显示详细信息
pymg list --verbose

# 显示远程可安装版本
pymg list --remote
```

**别名**: `pymg ls`

---

### `pymg use <version>`
切换当前会话使用的 Python 版本

```bash
# 切换到指定版本
pymg use 3.11.3

# 设置全局默认版本
pymg use 3.11.3 --global

# 设置当前项目版本（创建 .python-version 文件）
pymg use 3.11.3 --local

# 临时切换（仅在当前 shell 会话有效）
pymg use 3.11.3 --temp
```

---

### `pymg current`
显示当前正在使用的 Python 版本

```bash
# 显示当前版本
pymg current

# 显示详细路径信息
pymg current --path

# 显示版本已安装的包数量
pymg current --packages
```

---

### `pymg which <version>`
显示指定 Python 版本的安装路径

```bash
# 显示版本路径
pymg which 3.11.3

# 显示解释器完整路径
pymg which 3.11.3 --executable

# 显示 site-packages 路径
pymg which 3.11.3 --site-packages
```

---

## 高级管理命令

### `pymg alias <action> <name> [version]`
管理版本别名

```bash
# 创建别名
pymg alias create stable 3.11.3
pymg alias create testing 3.13.0

# 列出所有别名
pymg alias list

# 删除别名
pymg alias remove testing

# 使用别名切换版本
pymg use stable
```

---

### `pymg exec <version> <command...>`
在指定 Python 版本环境中执行命令

```bash
# 使用特定版本运行脚本
pymg exec 3.11.3 python my_script.py

# 在指定版本中安装包
pymg exec 3.10.0 pip install requests

# 运行交互式解释器
pymg exec 3.12.0 python

# 运行命令并传递参数
pymg exec 3.11.3 pytest tests/ -v
```

**选项**:
- `--inherit-packages`: 继承当前环境的包
- `--clean-env`: 在干净环境中运行

---

### `pymg migrate <from_version> <to_version>`
迁移 Python 包和虚拟环境

```bash
# 迁移所有已安装的包
pymg migrate 3.10.0 3.11.3

# 迁移并生成 requirements 文件
pymg migrate 3.10.0 3.11.3 --export-requirements

# 仅迁移特定包
pymg migrate 3.10.0 3.11.3 --only numpy,pandas

# 强制覆盖已存在的包
pymg migrate 3.10.0 3.11.3 --force
```

**选项**:
- `--export-requirements`: 生成迁移报告文件
- `--only PACKAGES`: 仅迁移指定包（逗号分隔）
- `--exclude PACKAGES`: 排除指定包
- `-f, --force`: 强制覆盖

---

### `pymg doctor`
诊断 pymg 环境和常见问题

```bash
# 运行完整诊断
pymg doctor

# 检查特定问题
pymg doctor --check network
pymg doctor --check permissions

# 自动生成修复建议
pymg doctor --fix
```

**检查项**:
- 网络连通性
- 文件权限
- 环境变量配置
- 依赖完整性
- 版本冲突

---

### `pymg cleanup`
清理缓存和临时文件

```bash
# 清理下载缓存
pymg cleanup cache

# 清理旧版本备份
pymg cleanup backups

# 清理所有未使用的版本
pymg cleanup old-versions --keep 2

# 深度清理（谨慎使用）
pymg cleanup all --force
```

**选项**:
- `--keep N`: 保留最近 N 个版本
- `-f, --force`: 跳过确认提示

---

### `pymg config <action> [key] [value]`
管理 pymg 配置

```bash
# 显示所有配置
pymg config list

# 获取配置值
pymg config get download.cache_dir

# 设置配置值
pymg config set download.cache_dir /tmp/pymg_cache

# 重置为默认配置
pymg config reset

# 编辑配置文件
pymg config edit
```

**配置项**:
- `download.cache_dir`: 缓存目录
- `download.mirror`: PyPI 镜像源
- `install.default_packages`: 新版本的默认包
- `global.version_file`: 版本文件路径

---

### `pymg benchmark <version>`
对指定 Python 版本进行性能基准测试

```bash
# 基准测试指定版本
pymg benchmark 3.11.3

# 对比多个版本
pymg benchmark 3.10.0 3.11.3 3.12.0

# 运行特定测试套件
pymg benchmark 3.11.3 --suite memory

# 导出测试结果
pymg benchmark 3.11.3 --output results.json
```

**测试套件**:
- `cpu`: CPU 性能测试
- `memory`: 内存分配测试
- `io`: 文件 I/O 测试
- `startup`: 启动时间测试

---

## 使用示例

### 场景 1：安装并切换到新版本
```bash
# 安装最新版
pymg install latest

# 设为全局默认
pymg use 3.12.0 --global

# 验证
python --version
```

### 场景 2：项目级版本管理
```bash
# 进入项目目录
cd myproject

# 安装项目所需版本
pymg install 3.11.3

# 创建本地版本文件（.python-version）
pymg use 3.11.3 --local

# 后续进入目录自动切换
```

### 场景 3：安全升级流程
```bash
# 1. 安装新版本
pymg install 3.12.0

# 2. 迁移旧版本包
pymg migrate 3.11.3 3.12.0 --export-requirements

# 3. 测试项目
pymg exec 3.12.0 pytest

# 4. 切换版本
pymg use 3.12.0 --global

# 5. 保留旧版本一段时间，确认无误后卸载
pymg uninstall 3.11.3
```

---

## 环境变量

| 变量名 | 说明 | 示例 |
|--------|------|------|
| `PYMG_ROOT` | pymg 安装根目录 | `/home/user/.pymg` |
| `PYMG_PYTHON_VERSION` | 强制指定版本 | `3.11.3` |
| `PYMG_MIRROR` | PyPI 镜像源 | `https://pypi.tuna.tsinghua.edu.cn/simple` |
| `PYMG_DISABLE_AUTO_USE` | 禁用自动切换 | `true` |

---

## 配置文件

配置文件位于 `~/.pymg/config.toml`：

```toml
[download]
cache_dir = "~/.pymg/cache"
parallel_downloads = 4
mirror = "https://pypi.org/"

[install]
compile_optimization = true
default_packages = ["pip", "setuptools", "wheel"]

[alias]
stable = "3.11.3"
latest = "3.12.0"
```

---

## 常见问题

### Q: 如何查看所有可安装的远程版本？
```bash
pymg list --remote
```

### Q: 切换版本后 pip 命令仍然指向旧版本？
```bash
# 使用 pymg exec 确保在正确环境中操作
pymg exec 3.11.3 python -m pip install package_name
```

### Q: 如何完全卸载 pymg？
```bash
pymg cleanup all --force
rm -rf ~/.pymg
# 并从 shell 配置文件中删除 PATH 修改
```

### Q: 权限不足无法安装？
```bash
# 使用用户模式安装
pymg install 3.11.3 --user
# 或调整安装目录
pymg config set install.prefix ~/python
```

---

## 版本历史

- **v1.0.0** (2024-12-25): 初始版本发布
- **v1.1.0** (计划中): 添加插件系统支持

---

## 贡献与反馈

欢迎提交 Issue 和 Pull Request！  
GitHub 仓库: https://github.com/python-upgrade/pymg  
文档地址: https://pymg.sh/docs