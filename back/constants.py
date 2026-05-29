SIGN_TO_VOWEL = {
    "A": "a", "E": "e", "I": "i",
    "O": "o", "U": "u"
}

SIGN_TO_SERIES = {
    "P": "DYNAMIC", "T": "DYNAMIC", "K": "DYNAMIC",
    "D": "STATIC", "Q": "STATIC",
    "M": "SONORANT", "N": "SONORANT", "R": "SONORANT",
    "S": "SIBILANT",
    "Z": "AFFRICATE",
    "W": "GLIDE"
}

STAGES_RULES = {
    "STRONG": {
        "DYNAMIC": {"P": "pʰ", "T": "tʰ", "K": "kʰ"},
        "STATIC": {"D": "t'", "Q": "k'"},
        "SONORANT": {"R": "l", "N": "ŋ", "M": "pʰ"},
        "SIBILANT": {"S": "c"},
        "AFFRICATE": {"Z": "č"},
        "GLIDE": {"W": "v"}
    },
    "WEAK": {
        "DYNAMIC": {"P": "b", "T": "d", "K": "g"},
        "STATIC": {"D": "t", "Q": "k"},
        "SONORANT": {"R": "r", "N": "n", "M": "m"},
        "SIBILANT": {"S": "s"},
        "AFFRICATE": {"Z": "z"},
        "GLIDE": {"W": "w"}
    }
}
