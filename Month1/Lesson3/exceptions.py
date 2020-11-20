def exceptions():
    raise ValueError


def main():
    try:
        1 / 0
    except Exception:
        return'Division by zero'

print(main())


