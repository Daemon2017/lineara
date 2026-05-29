import db
from constants import SIGN_TO_VOWEL, SIGN_TO_SERIES, STAGES_RULES
from variant import Variant


def parse_syllable(syllable):
    vowel_idx = -1
    for i, char in enumerate(syllable):
        if char in SIGN_TO_VOWEL:
            vowel_idx = i
            break
    if vowel_idx == -1:
        return syllable, ""
    else:
        return syllable[:vowel_idx], syllable[vowel_idx:]


def calculate_dynamic_mode(is_initial, is_stressed):
    return "STRONG" if is_initial or is_stressed else "WEAK"


def transform_sonorant(c, is_stressed, v_mapped):
    if is_stressed:
        c_mapped = c.lower()
    else:
        c_mapped = c.lower() + "̥"
        v_mapped = ""
    return c_mapped, v_mapped


def transform_consonant_by_type(c, is_stressed, mode, v_mapped):
    if c in SIGN_TO_SERIES:
        series = SIGN_TO_SERIES[c]
        if series == "SONORANT":
            c_mapped = STAGES_RULES[mode][series].get(c, c.lower())
            if not is_stressed:
                c_mapped = c_mapped + "̥"
                v_mapped = ""
        else:
            c_mapped = STAGES_RULES[mode][series].get(c, c.lower())
    else:
        c_mapped = c.lower()
    return c_mapped, v_mapped


def add_aspiration(c_mapped, lookup_c, mode):
    if mode == "STRONG" and SIGN_TO_SERIES.get(lookup_c) == "DYNAMIC" and not c_mapped.endswith("ʰ"):
        c_mapped += "ʰ"
    return c_mapped


def get_reconstruction(syllables, stressed_idx):
    parts = []
    for i, syl in enumerate(syllables):
        c, v = parse_syllable(syl)
        v_mapped = SIGN_TO_VOWEL.get(v, v.lower())
        if not c:
            parts.append(v_mapped)
            continue
        is_initial = (i == 0)
        is_stressed = (i == stressed_idx)
        mode = calculate_dynamic_mode(is_initial, is_stressed)
        c_mapped, v_mapped = transform_consonant_by_type(c, is_stressed, mode, v_mapped)
        c_mapped = add_aspiration(c_mapped, c, mode)
        parts.append(c_mapped + v_mapped)
    return "".join(parts)


def generate_readings(word_hyphenated):
    syllables = [s.strip().upper() for s in word_hyphenated.split("-") if s.strip()]
    num_syllables = len(syllables)
    if num_syllables == 0:
        return []
    variants = []
    for stressed_idx in range(num_syllables):
        minoan = get_reconstruction(syllables, stressed_idx)
        cognates_from_db = db.search_eurasiatic_cognate(minoan)
        variants.append(Variant(stressed_syllable_number=stressed_idx + 1, minoan=minoan, cognates=cognates_from_db))
    return variants
