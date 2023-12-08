class Jaccard:
    def two_word_dist(w1: str, w2: str) -> int:
        '''This funcion dont care about Capitals and normalize arabic text'''

        return 0

    def word_with_list(w1: str, lst: list[str]) -> list[str]:
        return ["", "", ""]


class Levenshtein:
    def two_word_dist(w1: str, w2: str) -> int:
        '''This funcion dont care about Capitals'''

        return 0

    def word_with_list(w1: str, lst: list[str]) -> list[str]:

        return ["", "", ""]


class Naive:
    def count():
        '''just number of common unique words between them'''
        raise NotImplemented
