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

## 核心命令概览

### `python-upgrade`
用于将系统默认 Python 升级到最新稳定版本。

常用用法：
- `python-upgrade` — 升级到最新稳定版
- `python-upgrade 3.12.0` — 升级到指定版本
- `python-upgrade 3.11` — 升级到指定系列的最新版
- `python-upgrade --force` — 强制重新安装
- `python-upgrade --migrate-packages` — 安装后自动迁移包

选项：`-f, --force`，`-m, --migrate-packages`，`-q, --quiet`，`-v, --verbose`

---

## 基础管理命令（详细）

### `pymg install <version>`
安装指定 Python 版本。

示例：
- `pymg install 3.11.3`
- `pymg install 3.12.0 --build-from-source`
- `pymg install 3.10.5 --install-dir=/opt/python/3.10.5`
- `pymg install latest`
- `pymg install 3.13.0a1 --prerelease`

选项：`--build-from-source`，`--prerelease`，`--install-dir PATH`

---

### `pymg uninstall <version>`
卸载指定 Python 版本。

示例：
- `pymg uninstall 3.9.7`
- `pymg uninstall 3.9.7 --force`
- `pymg uninstall 3.9.7 --clean-cache`

---

### `pymg list`
列出所有已安装或可用的 Python 版本。

示例：
- `pymg list` — 列出已安装版本
- `pymg list --available` — 仅显示可用版本
- `pymg list --verbose` — 显示详细信息
- `pymg list --remote` — 显示远程可安装版本

别名：`pymg ls`

---

### `pymg use <version>`
切换当前会话或全局的 Python 版本。

示例：
- `pymg use 3.11.3`
- `pymg use 3.11.3 --global`
- `pymg use 3.11.3 --local` — 在项目目录创建 `.python-version`
- `pymg use 3.11.3 --temp` — 仅当前 shell 有效

---

### `pymg current`
显示当前正在使用的 Python 版本。

示例：
- `pymg current`
- `pymg current --path`
- `pymg current --packages`

---

### `pymg which <version>`
显示指定版本的安装路径或相关路径信息。

示例：
- `pymg which 3.11.3`
- `pymg which 3.11.3 --executable`
- `pymg which 3.11.3 --site-packages`

---

## 高级管理命令

### `pymg alias <action> <name> [version]`
管理版本别名。

示例：
- `pymg alias create stable 3.11.3`
- `pymg alias list`
- `pymg alias remove testing`
- `pymg use stable`

---

### `pymg exec <version> <command...>`
在指定 Python 版本环境中执行命令。

示例：
- `pymg exec 3.11.3 python my_script.py`
- `pymg exec 3.10.0 pip install requests`
- `pymg exec 3.12.0 python`
- `pymg exec 3.11.3 pytest tests/ -v`

选项：`--inherit-packages`，`--clean-env`

---

### `pymg migrate <from_version> <to_version>`
迁移 Python 包和虚拟环境。

示例：
- `pymg migrate 3.10.0 3.11.3`
- `pymg migrate 3.10.0 3.11.3 --export-requirements`
- `pymg migrate 3.10.0 3.11.3 --only numpy,pandas`
- `pymg migrate 3.10.0 3.11.3 --force`

选项：`--export-requirements`，`--only PACKAGES`，`--exclude PACKAGES`，`-f, --force`

---

### `pymg doctor`
诊断 pymg 环境和常见问题。

示例：
- `pymg doctor`
- `pymg doctor --check network`
- `pymg doctor --check permissions`
- `pymg doctor --fix`

检查项：网络、权限、环境变量、依赖完整性、版本冲突

---

### `pymg cleanup`
清理缓存和临时文件。

示例：
- `pymg cleanup cache`
- `pymg cleanup backups`
- `pymg cleanup old-versions --keep 2`
- `pymg cleanup all --force`

选项：`--keep N`，`-f, --force`

---

### `pymg config <action> [key] [value]`
管理 pymg 配置。

示例：
- `pymg config list`
- `pymg config get download.cache_dir`
- `pymg config set download.cache_dir /tmp/pymg_cache`
- `pymg config reset`
- `pymg config edit`

常见配置项：`download.cache_dir`，`download.mirror`，`install.default_packages`，`global.version_file`

---

### `pymg benchmark <version>`
对指定 Python 版本进行性能基准测试。

示例：
- `pymg benchmark 3.11.3`
- `pymg benchmark 3.10.0 3.11.3 3.12.0`
- `pymg benchmark 3.11.3 --suite memory`
- `pymg benchmark 3.11.3 --output results.json`

测试套件：`cpu`，`memory`，`io`，`startup`

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
cd myproject
pymg install 3.11.3
pymg use 3.11.3 --local
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

# 5. 保留旧版本并最终卸载
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

默认位于 `~/.pymg/config.toml`，示例：

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

Q: 如何查看所有可安装的远程版本？

```
pymg list --remote
```

Q: 切换版本后 pip 命令仍然指向旧版本？

```
# 使用 pymg exec 确保在正确环境中操作
pymg exec 3.11.3 python -m pip install package_name
```

Q: 如何完全卸载 pymg？

```
pymg cleanup all --force
rm -rf ~/.pymg
# 并从 shell 配置文件中删除 PATH 修改
```

Q: 权限不足无法安装？

```
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
