SIGN_TO_VOWEL = {
    "A": "a", "E": "e", "I": "i",
    "Ω": "ɔ", "O": "o", "U": "u"
}

SIGN_TO_SERIES = {
    "P": "DYNAMIC", "T": "DYNAMIC", "K": "DYNAMIC", "Q": "DYNAMIC",
    "D": "STATIC",
    "M": "SONORANT", "N": "SONORANT", "R": "SONORANT"
}

STAGES_RULES = {
    "MINOAN": {
        "STRONG": {
            "DYNAMIC": {"P": "pʰ", "T": "tʰ", "K": "kʰ", "Q": "kʷʰ"},
            "STATIC": {"D": "t'"}
        },
        "WEAK": {
            "DYNAMIC": {"P": "b", "T": "d", "K": "g", "Q": "gʷ"},
            "STATIC": {"D": "t'"}
        }
    }
}
