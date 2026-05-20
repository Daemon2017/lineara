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


def calculate_dynamic_mode(is_initial, is_stressed, mode, stage):
    if stage == "PRE_PIE":
        mode = "STRONG" if is_initial or is_stressed else "WEAK"
    return mode


def transform_sonorant(c, is_stressed, stage, v_mapped):
    if stage == "PRE_PIE" and not is_stressed:
        c_mapped = c.lower() + "̥"
        v_mapped = ""
    else:
        c_mapped = c.lower()
    return c_mapped, v_mapped


def transform_consonant_by_type(c, is_stressed, lookup_c, mode, stage, v_mapped):
    if lookup_c in SIGN_TO_SERIES:
        series = SIGN_TO_SERIES[lookup_c]
        if series == "SONORANT":
            c_mapped, v_mapped = transform_sonorant(c, is_stressed, stage, v_mapped)
        else:
            c_mapped = STAGES_RULES[stage][mode][series].get(c, c.lower())
    else:
        c_mapped = c.lower()
    return c_mapped, v_mapped


def add_aspiration(c_mapped, lookup_c, mode, stage):
    if stage == "PRE_PIE" and mode == "STRONG":
        if SIGN_TO_SERIES.get(lookup_c) == "II":
            if not c_mapped.endswith("ʰ"):
                c_mapped += "ʰ"
    return c_mapped


def get_reconstruction_for_stage(stage, syllables, stressed_idx, r_to_l=False):
    parts = []
    for i, syl in enumerate(syllables):
        c, v = parse_syllable(syl)
        if r_to_l and "R" in c:
            c = c.replace("R", "L")
        v_mapped = SIGN_TO_VOWEL.get(v, v.lower())
        if not c:
            parts.append(v_mapped)
            continue
        mode = "STRONG"
        is_initial = (i == 0)
        is_stressed = (i == stressed_idx)
        mode = calculate_dynamic_mode(is_initial, is_stressed, mode, stage)
        lookup_c = "R" if c in ("R", "L") else c
        c_mapped, v_mapped = transform_consonant_by_type(c, is_stressed, lookup_c, mode, stage, v_mapped)
        c_mapped = add_aspiration(c_mapped, lookup_c, mode, stage)
        parts.append(c_mapped + v_mapped)
    return "-".join(parts)


def generate_readings(word_hyphenated):
    syllables = [s.strip().upper() for s in word_hyphenated.split("-") if s.strip()]
    num_syllables = len(syllables)
    if num_syllables == 0:
        return []
    variants = []
    for stressed_idx in range(num_syllables):
        pre_pie_r = get_reconstruction_for_stage("PRE_PIE", syllables, stressed_idx, r_to_l=False)
        variants.append(Variant(stressed_syllable_number=stressed_idx + 1, pre_pie_r=pre_pie_r))
    return variants
