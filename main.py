import enchant


def main():
    target = "_.-i.+e._.-e"
    # for target:
    # - use "." to separate characters
    # - use "_" when a character is completely unknown
    # - use "+" to indicate allowd characters (multiple possible characters or one already known character)
    # - use "-" to indicate disallowd characters (one or more characters)
    # example: "+p.+yi.+t._-aeiu.+n"
    disallowed_overall = "rtoshklbn"
    musthave_overall = "ei"
    language = "de"

    calculate_wordle(target, disallowed_overall, musthave_overall, language)


def calculate_wordle(target, disallowed_overall, musthave_overall, language):
    possibilities = create_possibility_list(target, disallowed_overall)

    results = list()
    calculate_possibilities(possibilities, musthave_overall, "", results)
    print(f"{len(results)} after calculating possibilities")

    results = filter_by_dict(results, language)
    print(f"{len(results)} after filtering by dictionary")
    show_results(results)


def create_possibility_list(
    target, disallowed_overall, disallowed_in_target=list()
):
    all_chars = "abcdefghijklmnopqrstuvwxyz"
    possibility_list = list()

    for target_pos in target.split("."):
        if target_pos.startswith("+"):
            possibility_list.append(list(target_pos[1:]))
        elif target_pos.startswith("-"):
            possibility_list.append(
                [
                    char
                    for char in all_chars
                    if char not in disallowed_overall
                    and char not in target_pos[1:]
                ]
            )
        else:
            possibility_list.append(
                [char for char in all_chars if char not in disallowed_overall]
            )

    return possibility_list


def calculate_possibilities(
    possibilities_list, musthave_overall, trunk, result_list
):
    last_position = len(possibilities_list)
    current_position = len(trunk)
    at_final_position = current_position == last_position - 1
    current_possibilities = possibilities_list[current_position]

    for poss in current_possibilities:
        new_possibility = trunk + poss
        if at_final_position:
            if list_is_subset_of_list(musthave_overall, new_possibility):
                result_list.append(new_possibility)
        else:
            calculate_possibilities(
                possibilities_list,
                musthave_overall,
                new_possibility,
                result_list,
            )


def list_is_subset_of_list(list_1: list, list_2: list):
    if isinstance(list_1, str):
        list_1 = list(list_1)
    if isinstance(list_2, str):
        list_2 = list(list_2)
    for element in list_1:
        try:
            list_2.remove(element)
        except ValueError:
            return False

    return True


def filter_by_dict(results, language):
    if language == "de":
        dictionary = enchant.Dict("de_DE_frami")
    elif language == "en":
        dictionary = enchant.Dict("en_US")
    else:
        return results

    return [
        result for result in results if dictionary.check(result.capitalize())
    ]


def show_results(results):
    count = 1
    no_results = len(results)
    digits_max_result = len(str(no_results))

    print(f"{no_results} results")
    for result in results:
        print(str(count).rjust(digits_max_result) + ": " + result)
        count += 1


if __name__ == "__main__":
    main()
