#!/usr/bin/env python3
"""
Convenience script to run the Greeter CLI from the repository root.

Usage (from repo root):
    python run_greeter.py Alice
    python run_greeter.py Bob --lang es
"""

from greeter_cli.main import main

if __name__ == "__main__":
    main()
