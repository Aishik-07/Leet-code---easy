def response(hey_bob):
    hey_bob = hey_bob.strip()

    if hey_bob == "":
        return "Fine. Be that way!"

    is_question = hey_bob.endswith("?")
    is_yelling = hey_bob.isupper() and any(char.isalpha() for char in hey_bob)

    if is_question and is_yelling:
        return "Calm down, I know what I'm doing!"
    elif is_yelling:
        return "Whoa, chill out!"
    elif is_question:
        return "Sure."
    else:
        return "Whatever."