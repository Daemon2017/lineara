SIGN_TO_VOWEL = {
    "A": "a",
    "E": "e", "I": "i",
    "O": "o", "U": "u"
}

SIGN_TO_SERIES = {
    "P": "DYNAMIC", "T": "DYNAMIC", "K": "DYNAMIC",
    "D": "STATIC", "Q": "STATIC",
    "M": "SONORANT", "N": "SONORANT", "R": "SONORANT",
    "S": "SIBILANT", "Z": "SIBILANT"
}

STAGES_RULES = {
    "STRONG": {
        "DYNAMIC": {"P": "pʰ", "T": "tʰ", "K": "kʰ"},
        "STATIC": {"D": "ṭ", "Q": "ḳ"},
        "SONORANT": {"M": "m", "N": "n", "R": "l"},
        "SIBILANT": {"S": "s", "Z": "c"}
    },
    "WEAK": {
        "DYNAMIC": {"P": "b", "T": "d", "K": "g"},
        "STATIC": {"D": "t", "Q": "k"},
        "SONORANT": {"M": "m", "N": "n", "R": "r"},
        "SIBILANT": {"S": "z", "Z": "c"}
    }
}
