"""
Main entry point for the Python Website Prototype.

This module provides convenient commands for building and serving the website.
"""

import subprocess
import sys
from pathlib import Path


def get_project_root() -> Path:
    """Return the project root directory."""
    return Path(__file__).parent


def build() -> None:
    """Build the website using Pelican."""
    project_root = get_project_root()
    print("Building website...")
    subprocess.run(
        [sys.executable, "-m", "pelican", "content", "-o", "output", "-s", "pelicanconf.py"],
        cwd=project_root,
        check=True,
    )
    print("Website built successfully! Output is in the 'output' directory.")


def serve() -> None:
    """Build and serve the website locally for development."""
    project_root = get_project_root()
    print("Building and serving website...")
    print("Visit http://localhost:8000 to view your site.")
    print("Press Ctrl+C to stop the server.")
    subprocess.run(
        [sys.executable, "-m", "pelican", "--listen", "--autoreload"],
        cwd=project_root,
        check=True,
    )


def publish() -> None:
    """Build the website for production using publish settings."""
    project_root = get_project_root()
    print("Building website for production...")
    subprocess.run(
        [sys.executable, "-m", "pelican", "content", "-o", "output", "-s", "publishconf.py"],
        cwd=project_root,
        check=True,
    )
    print("Production build complete! Output is in the 'output' directory.")


def main() -> None:
    """Main entry point with command routing."""
    if len(sys.argv) < 2:
        print("Python Website Prototype")
        print("=" * 40)
        print("\nAvailable commands:")
        print("  build   - Build the website")
        print("  serve   - Build and serve locally with auto-reload")
        print("  publish - Build for production")
        print("\nUsage: uv run python main.py <command>")
        return

    command = sys.argv[1].lower()
    commands = {
        "build": build,
        "serve": serve,
        "publish": publish,
    }

    if command in commands:
        commands[command]()
    else:
        print(f"Unknown command: {command}")
        print("Available commands: build, serve, publish")
        sys.exit(1)


if __name__ == "__main__":
    main()
