"""
template_letter_generator.py
----------------------------

This script demonstrates how to generate a personalized message using
string templates and the `replace()` method. It replaces placeholder
tokens in a template with actual values.

Common use cases:
- Email template systems
- Notification generators
- Document automation
"""


# ---------------------------------------------------------------------
# CORE FUNCTION
# ---------------------------------------------------------------------

def generate_letter(template: str, name: str, date: str) -> str:
    """
    Replace placeholders in a template with provided values.

    Args:
        template: Template text containing placeholders
        name: Recipient name
        date: Date to insert

    Returns:
        Final formatted letter string
    """
    return (
        template.replace("<|Name|>", name)
                .replace("<|Date|>", date)
    )


# ---------------------------------------------------------------------
# SCRIPT ENTRYPOINT
# ---------------------------------------------------------------------

def main():
    letter_template = """Dear <|Name|>,
You are selected!
<|Date|>
"""

    final_letter = generate_letter(letter_template, "Harry", "24 September 2050")
    print(final_letter)


if __name__ == "__main__":
    main()
