"""Entry for make.fun bounty u-xvader-the-funniest-honest-appliance-error-adec4450.

Writes the funniest honest appliance error message to /output/entry.txt.
Deterministic, no network, no randomness.
"""

ENTRY = (
    "ERROR E04: I refuse to spin. One sock is stuck to the drum wall and "
    "the load is so lopsided that spinning would make me walk across the floor."
)


def main() -> None:
    """Validate the entry and write it to /output/entry.txt."""
    if not ENTRY.strip():
        raise ValueError("entry must not be blank")
    if "\n" in ENTRY or "\r" in ENTRY:
        raise ValueError("entry must be a single line")
    if not 1 <= len(ENTRY) <= 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(ENTRY)}")

    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
