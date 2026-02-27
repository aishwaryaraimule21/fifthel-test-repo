"""
Greeter logic: builds and returns greeting messages.
"""

from greeter_cli.config import GREETINGS, DEFAULT_LANGUAGE


def greet(name: str, lang: str = DEFAULT_LANGUAGE) -> str:
    """
    Return a greeting string for the given name and language.

    Args:
        name: The name to greet.
        lang: Language code (e.g. 'en', 'es'). Falls back to default if unknown.

    Returns:
        A greeting string.
    """
    template = GREETINGS.get(lang, GREETINGS[DEFAULT_LANGUAGE])
    return template.format(name=name.strip())
