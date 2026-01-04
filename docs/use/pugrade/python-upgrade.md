### `python-upgrade`
用于将系统或全局默认 Python 安全升级到指定语义化版本或最新稳定版。`python-upgrade` 是一个高层快捷命令，封装了安装、迁移和切换等常见步骤，面向对细节不关心的终端用户。

## 概要行为

- 安装目标版本（从二进制或源码，根据实现与平台）。
- 可选迁移当前默认版本已安装的第三方包到新环境（`--migrate-packages`）。
- 将系统或全局默认 Python 指向新安装的版本（可通过 `--no-switch` 跳过）。
- 支持强制覆盖已安装版本（`--force`）与静默执行（`--quiet`）。

## 语法

- `python-upgrade [options] [version]`

如果不指定 `version`，默认安装并切换到最新稳定版。

### 常用选项

- `-f, --force`：覆盖已存在的安装（谨慎使用）。
- `-m, --migrate-packages`：在安装后尝试迁移全局/用户级已安装的包到新版本。
- `--no-switch`：安装但不修改系统/全局默认 Python 的指向。
- `-q, --quiet`：最低输出。
- `-v, --verbose`：详细日志输出。

## 使用场景与示例

- 快速升级到最新稳定版（自动迁移并切换）：

```bash
python-upgrade --migrate-packages
```

- 直接安装并切换到 3.14.2（不迁移）：

```bash
python-upgrade 3.14.2
```

- 安装但不更改当前默认（用于测试）：

```bash
python-upgrade 3.14.2 --no-switch
```

- 强制重新安装（覆盖已有相同版本）：

```bash
python-upgrade 3.14.2 --force
```

## 与 `pymg` 的区别（决策指南）

- `python-upgrade`：一键式、交互友好，适合个人用户想要“安全升级”的场景。
- `pymg`：提供细粒度子命令（`install`、`migrate`、`use` 等），适用于脚本化、CI、服务器或需要自定义安装行为的场景。

示例：同样目标的等价 `pymg` 流程：

```bash
pymg install 3.14.2 --build-from-source   # 或不加 --build-from-source 使用预编译包
pymg migrate <old-version> 3.14.2 --export-requirements
pymg use 3.14.2 --global
```

## 迁移与回滚策略

- 迁移：`python-upgrade` 在迁移包时会导出依赖清单（例如 `requirements.txt`）并在目标环境中尝试重建。若出现冲突或重要包无法安装，命令会中止并提示手动干预。
- 回滚：升级前 `python-upgrade` 建议保留旧版本（默认保留）并在失败时提供回滚提示；回滚命令可用 `pymg use <old-version>` 或 `pymg uninstall <new-version>` 配合恢复步骤。

## 配置项与可定制行为

配置文件位于 `~/.pymg/config.toml`（参见 docs/pymg.md）：

- `download.cache_dir`：下载缓存路径。
- `download.mirror`：下载镜像源。
- `install.default_packages`：新安装 Python 的默认包（例如 `pip,setuptools,wheel`）。

`python-upgrade` 在内部可能会尊重该配置或通过 CLI 参数覆盖。

## 常见问题与故障排查

- 安装失败（网络/证书）：检查 `PYMG_MIRROR` 或配置中 `download.mirror`，并重试；可先下载到缓存目录再本地安装。
- 迁移失败（包冲突）：检查导出的 `requirements.txt`，手动排查冲突包并优先安装核心依赖后重试迁移。
- 升级后默认 Python 未改变：确认没有设置 `PYMG_DISABLE_AUTO_USE` 环境变量或使用了 `--no-switch`。

## 自动化 / CI 建议

- 在 CI 中避免使用一次性 `python-upgrade`，改用 `pymg install` + `pymg use` 的可控流程。
- 将下载缓存放在共享缓存路径（`download.cache_dir`）以减少网络带宽。

---

更多实现细节与命令参考见：`docs/pymg.md`。