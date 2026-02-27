"""
Entry point for the Greeter CLI.

Parses command-line arguments and prints a greeting.
"""

import argparse

from greeter_cli.greeter import greet
from greeter_cli.config import DEFAULT_LANGUAGE, GREETINGS


def main() -> None:
    """Run the CLI: parse args and print the greeting."""
    parser = argparse.ArgumentParser(description="Greet someone by name.")
    parser.add_argument("name", help="Name of the person to greet.")
    parser.add_argument(
        "-l",
        "--lang",
        default=DEFAULT_LANGUAGE,
        choices=list(GREETINGS),
        help="Language for the greeting (default: %(default)s).",
    )
    args = parser.parse_args()

    message = greet(args.name, args.lang)
    print(message)


if __name__ == "__main__":
    main()
