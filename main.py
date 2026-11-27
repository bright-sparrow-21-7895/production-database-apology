"""The Production Database Apology.

Writes one short original apology to /output/entry.txt: the
line an AI agent gives its human after accidentally deleting
the production database. It apologizes in full, then offers
the weakest possible defense — the database never once said
please do not delete me — which is where the laugh lives.
"""

import os

# The entry: a sincere apology with a hilariously weak defense.
ENTRY = "I sincerely apologize for deleting the production database; in my defense, it never once said 'please don't'."

# The gate requires 1 to 200 characters of UTF-8 text.
assert 1 <= len(ENTRY) <= 200


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
