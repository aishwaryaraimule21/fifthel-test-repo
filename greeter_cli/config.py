"""
Configuration for the Greeter CLI.

Holds default settings and supported options (e.g. languages).
"""

# Supported languages and their greeting templates.
# Format: "Hello, {name}!"
GREETINGS: dict[str, str] = {
    "en": "Hello, {name}!",
    "es": "¡Hola, {name}!",
    "fr": "Bonjour, {name}!",
}

DEFAULT_LANGUAGE = "en"
