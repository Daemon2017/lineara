SIGN_TO_VOWEL = {
    "A": "a", "E": "e", "I": "i",
    "Ω": "ɔ", "O": "o", "U": "u"
}

SIGN_TO_SERIES = {
    "P": "II", "T": "II", "K": "II", "Q": "II",
    "D": "III",
    "M": "SONORANT", "N": "SONORANT", "R": "SONORANT"
}

STAGES_RULES = {
    "PRE_PIE": {
        "STRONG": {
            "II": {"P": "pʰ", "T": "tʰ", "K": "kʰ", "Q": "kʷʰ"},
            "III": {"D": "d"}
        },
        "WEAK": {
            "II": {"P": "b", "T": "d", "K": "g", "Q": "gʷ"},
            "III": {"D": "ð"}
        }
    }
}
