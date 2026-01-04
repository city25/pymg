"""Command-line interface for pymg (skeleton).

This module exposes `main()` which wires argparse to core functions.
"""
import argparse
import sys

from pymg import get_version


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="pymg", description="Python version manager (pymg)")
    parser.add_argument("--version", action="version", version=f"pymg {get_version()}")

    sub = parser.add_subparsers(dest="command")

    sub.add_parser("install", help="Install a Python version")
    sub.add_parser("uninstall", help="Uninstall a Python version")
    sub.add_parser("list", help="List installed versions")
    sub.add_parser("use", help="Switch version")
    sub.add_parser("current", help="Show current version")
    sub.add_parser("exec", help="Execute command with a specific version")

    return parser


def main(argv=None) -> int:
    argv = argv or sys.argv[1:]
    parser = build_parser()
    args = parser.parse_args(argv)

    # Minimal dispatch skeleton; real logic is in core modules.
    if args.command is None:
        parser.print_help()
        return 1

    print(f"Command: {args.command} (stub)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
