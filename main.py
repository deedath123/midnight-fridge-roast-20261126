ENTRY = "My fridge locks at midnight and flashes 'nice try, champ' — I pay the power bill, it owns the leftovers, and at 2 a.m. I'm negotiating snacks with an appliance."


def main():
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
