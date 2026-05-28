SIGN_TO_VOWEL = {
    "A": "a", "E": "e", "I": "i",
    "O": "o", "U": "u"
}

SIGN_TO_SERIES = {
    "P": "DYNAMIC", "T": "DYNAMIC", "K": "DYNAMIC",
    "D": "STATIC", "Q": "STATIC",
    "M": "SONORANT", "N": "SONORANT", "R": "SONORANT"
}

STAGES_RULES = {
    "MINOAN": {
        "STRONG": {
            "DYNAMIC": {"P": "pʰ", "T": "tʰ", "K": "kʰ"},
            "STATIC": {"D": "t'", "Q": "k'"}
        },
        "WEAK": {
            "DYNAMIC": {"P": "b", "T": "d", "K": "g"},
            "STATIC": {"D": "t'", "Q": "k'"}
        }
    }
}
