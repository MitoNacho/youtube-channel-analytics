def format_number(number):

    number = int(number)

    if number >= 1_000_000_000:

        value = number / 1_000_000_000

        return clean_decimal(value, "B")

    if number >= 1_000_000:

        value = number / 1_000_000

        return clean_decimal(value, "M")

    if number >= 1_000:

        value = number / 1_000

        return clean_decimal(value, "K")

    return str(number)


def clean_decimal(value, suffix):

    if value.is_integer():

        return f"{int(value)}{suffix}"

    return f"{round(value,1)}{suffix}"