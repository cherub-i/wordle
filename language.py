import enchant


class Language:
    CHARS = "abcdefghijklmnopqrstuvwxyz"
    CHAR_FREQUENCY_DE = {  # Deutsch
        "a": 6.51,
        "b": 1.89,
        "c": 3.06,
        "d": 5.08,
        "e": 17.4,
        "f": 1.66,
        "g": 3.01,
        "h": 4.76,
        "i": 7.55,
        "j": 0.27,
        "k": 1.21,
        "l": 3.44,
        "m": 2.53,
        "n": 9.78,
        "o": 2.51,
        "p": 0.79,
        "q": 0.02,
        "r": 7,
        "s": 7.27,
        "t": 6.15,
        "u": 4.35,
        "v": 0.67,
        "w": 1.89,
        "x": 0.03,
        "y": 0.04,
        "z": 1.13,
    }
    CHAR_FREQUENCY_EN = {  # Englisch
        "a": 8.167,
        "b": 1.492,
        "c": 2.782,
        "d": 4.253,
        "e": 12.702,
        "f": 2.228,
        "g": 2.015,
        "h": 6.094,
        "i": 6.966,
        "j": 0.153,
        "k": 0.772,
        "l": 4.025,
        "m": 2.406,
        "n": 6.749,
        "o": 7.507,
        "p": 1.929,
        "q": 0.095,
        "r": 5.987,
        "s": 6.327,
        "t": 9.056,
        "u": 2.758,
        "v": 0.978,
        "w": 2.36,
        "x": 0.15,
        "y": 1.974,
        "z": 0.074,
    }
    CHAR_FREQUENCY_FR = {  # Französisch
        "a": 7.636,
        "b": 0.901,
        "c": 3.26,
        "d": 3.669,
        "e": 14.715,
        "f": 1.066,
        "g": 0.866,
        "h": 0.737,
        "i": 7.529,
        "j": 0.545,
        "k": 0.049,
        "l": 5.456,
        "m": 2.968,
        "n": 7.095,
        "o": 5.378,
        "p": 3.021,
        "q": 1.362,
        "r": 6.553,
        "s": 7.948,
        "t": 7.244,
        "u": 6.311,
        "v": 1.628,
        "w": 0.114,
        "x": 0.387,
        "y": 0.308,
        "z": 0.136,
    }
    CHAR_FREQUENCY_ES = {  # Spanisch
        "a": 12.53,
        "b": 1.42,
        "c": 4.68,
        "d": 5.86,
        "e": 13.68,
        "f": 0.69,
        "g": 1.01,
        "h": 0.7,
        "i": 6.25,
        "j": 0.44,
        "k": 0,
        "l": 4.97,
        "m": 3.15,
        "n": 6.71,
        "o": 8.68,
        "p": 2.51,
        "q": 0.88,
        "r": 6.87,
        "s": 7.98,
        "t": 4.63,
        "u": 3.93,
        "v": 0.9,
        "w": 0.02,
        "x": 0.22,
        "y": 0.9,
        "z": 0.52,
    }
    CHAR_FREQUENCY_IT = {  # Italienisch
        "a": 11.74,
        "b": 0.92,
        "c": 4.5,
        "d": 3.73,
        "e": 11.79,
        "f": 0.95,
        "g": 1.64,
        "h": 1.54,
        "i": 11.28,
        "j": 0,
        "k": 0,
        "l": 6.51,
        "m": 2.51,
        "n": 6.88,
        "o": 9.83,
        "p": 3.05,
        "q": 0.51,
        "r": 6.37,
        "s": 4.98,
        "t": 5.62,
        "u": 3.01,
        "v": 2.1,
        "w": 0,
        "x": 0,
        "y": 0,
        "z": 0.49,
    }
    CHAR_FREQUENCY_SE = {  # Schwedisch
        "a": 11.74,
        "b": 0.92,
        "c": 4.5,
        "d": 3.73,
        "e": 11.79,
        "f": 0.95,
        "g": 1.64,
        "h": 1.54,
        "i": 11.28,
        "j": 0,
        "k": 0,
        "l": 6.51,
        "m": 2.51,
        "n": 6.88,
        "o": 9.83,
        "p": 3.05,
        "q": 0.51,
        "r": 6.37,
        "s": 4.98,
        "t": 5.62,
        "u": 3.01,
        "v": 2.1,
        "w": 0,
        "x": 0,
        "y": 0,
        "z": 0.02,
    }
    CHAR_FREQUENCY_PO = {  # Polnisch
        "a": 8,
        "b": 1.3,
        "c": 3.8,
        "d": 3,
        "e": 6.9,
        "f": 0.1,
        "g": 1,
        "h": 1,
        "i": 7,
        "j": 1.9,
        "k": 2.7,
        "l": 3.1,
        "m": 2.4,
        "n": 4.7,
        "o": 7.1,
        "p": 2.4,
        "q": 0,
        "r": 3.5,
        "s": 3.8,
        "t": 2.4,
        "u": 1.8,
        "v": 0,
        "w": 3.6,
        "x": 0,
        "y": 3.2,
        "z": 5.1,
    }

    def __init__(self, language: str):
        if language == "en":
            self.frequency: dict = Language.CHAR_FREQUENCY_EN
            self.dict = enchant.Dict("en_US_1")
        elif language == "de":
            self.frequency: dict = Language.CHAR_FREQUENCY_DE
            self.dict = enchant.Dict("de_DE_frami")
        elif language == "es":
            self.frequency: dict = Language.CHAR_FREQUENCY_ES
            self.dict = enchant.Dict("es")
        else:
            raise ValueError

    def word_weight(self, word: str):
        weight = 0
        existing_chars = ""

        for char in word:
            if char not in existing_chars:
                existing_chars += char
                weight += self.frequency.get(char) / 100

        return weight / len(word)

    def word_exists_in_dict(self, word: str, ignore_case: bool):
        if ignore_case:
            word = word.upper()
        return self.dict.check(word)
