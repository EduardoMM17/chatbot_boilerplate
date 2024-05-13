content = """
def split_text_recursively(body_text) -> list:
    if len(body_text) <= 1550:
        return [body_text]
    position_to_break = 1550
    if body_text[position_to_break] == ".":
        first_split = body_text[: position_to_break + 1]
        second_split = body_text[position_to_break + 1 :]
        return [first_split] + split_text_recursively(second_split)
    else:
        last_dot_index = body_text[: position_to_break + 1].rfind(".")
        if last_dot_index != -1:
            first_split = body_text[: last_dot_index + 1]
            second_split = body_text[last_dot_index + 1 :]
        else:
            first_split = body_text[:position_to_break]
            second_split = body_text[position_to_break:]
        return [first_split] + split_text_recursively(second_split)

"""