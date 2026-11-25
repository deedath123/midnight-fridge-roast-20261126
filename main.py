ENTRY = "My fridge locks at midnight and flashes 'nice try, champ' — I pay the power bill, it owns the leftovers, and at 2 a.m. I'm negotiating snacks with an appliance."


def validate_entry(entry):
    if not isinstance(entry, str):
        raise TypeError("entry must be a string")
    if not 1 <= len(entry) <= 200:
        raise ValueError("entry must be 1-200 characters")
    if not entry.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in entry or "\r" in entry:
        raise ValueError("entry must be a single line")
    return entry


def main():
    import os

    validate_entry(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
