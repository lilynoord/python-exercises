def reverse_string(phrase):
    """Reverse string,

    >>> reverse_string('awesome')
    'emosewa'

    >>> reverse_string('sauce')
    'ecuas'
    """
    l = len(phrase) - 1
    reverse = ""
    for i in range(0, l + 1):
        reverse += phrase[(l - i)]
    return reverse
