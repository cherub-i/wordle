from language import Language


class Wordle:
    def __init__(
        self,
        language: str,
        target: str,
        disallowed_overall: str,
        musthave_overall: str,
    ):
        self.lang = Language(language)
        self.target = target
        self.disallowed_overall = disallowed_overall
        self.musthave_overall = musthave_overall
        self.possibility_room = list()
        self.results = list()

        self.calculate()

    def calculate(self):
        self.calculate_possibility_room()
        Wordle.calculate_possibilities(
            self.possibility_room, self.musthave_overall, "", self.results
        )

    def calculate_possibility_room(self):
        for target_pos in self.target.split("."):
            if target_pos.startswith("+"):
                self.possibility_room.append(list(target_pos[1:]))
            elif target_pos.startswith("-"):
                self.possibility_room.append(
                    [
                        char
                        for char in self.lang.CHARS
                        if char not in self.disallowed_overall
                        and char not in target_pos[1:]
                    ]
                )
            else:
                self.possibility_room.append(
                    [
                        char
                        for char in self.lang.CHARS
                        if char not in self.disallowed_overall
                    ]
                )

    def filter_by_dict(self, ignore_case: bool = True):
        new_results = list()

        for result in self.results:
            if self.lang.word_exists_in_dict(result, ignore_case):
                new_results.append(result)

        self.results = new_results

    @staticmethod
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
                if Wordle.list_is_subset_of_list(
                    musthave_overall, new_possibility
                ):
                    result_list.append(new_possibility)
            else:
                Wordle.calculate_possibilities(
                    possibilities_list,
                    musthave_overall,
                    new_possibility,
                    result_list,
                )

    @staticmethod
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


def main():
    target = "_.-ua.+b._.-a"
    # for target:
    # - use "." to separate characters
    # - use "_" when a character is completely unknown
    # - use "+" to indicate allowd characters (multiple possible characters or one already known character)
    # - use "-" to indicate disallowd characters (one or more characters)
    # example: "+p.+yi.+t._-aeiu.+n"
    disallowed_overall = "ricnto"
    musthave_overall = "uba"
    language = "es"

    wordle = Wordle(language, target, disallowed_overall, musthave_overall)
    print(f"{len(wordle.results)} after calculating possibilities")

    # wordle.filter_by_dict(True)
    # print(f"{len(wordle.results)} after filtering by dictionary")

    no_results = len(wordle.results)
    digits_max_result = len(str(no_results))
    print(f"{no_results} results")
    out = ""
    for result_number in range(no_results):
        result = wordle.results[result_number]
        out += f"{str(result_number).rjust(digits_max_result)}: "
        out += result
        out += f" ({wordle.lang.word_weight(result):.3f})"
        out += " | "
        if result_number % 6 == 0:
            print(out[:-3])
            out = ""
    print(out[:-3])


if __name__ == "__main__":
    main()
