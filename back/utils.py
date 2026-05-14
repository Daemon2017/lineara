from constants import SIGN_TO_VOWEL, SIGN_TO_PRE_PIE_STRESSED_CONSONANT, SIGN_TO_PRE_PIE_NON_STRESSED_CONSONANT, \
    SIGN_TO_PG_STRESSED_CONSONANT, SIGN_TO_PG_NON_STRESSED_CONSONANT, SIGN_TO_PIE_STRESSED_CONSONANT, \
    SIGN_TO_PIE_NON_STRESSED_CONSONANT
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
        return syllable[:vowel_idx], "".join(SIGN_TO_VOWEL.get(c, c.lower()) for c in syllable[vowel_idx:])


def build_layers_pure_chain(syllables, stressed_idx, r_to_l=False):
    pre_pie_list = []
    pg_parts = []
    pie_parts = []
    for i, syl in enumerate(syllables):
        c, v = parse_syllable(syl)
        if r_to_l and "R" in c:
            c = c.replace("R", "L")
        is_stressed = i == stressed_idx
        v_mapped = SIGN_TO_VOWEL.get(v, v.lower())
        if is_stressed:
            c_pre_pie = SIGN_TO_PRE_PIE_STRESSED_CONSONANT.get(c, c.lower())
            c_pg = SIGN_TO_PG_STRESSED_CONSONANT.get(c, c.lower())
            c_pie = SIGN_TO_PIE_STRESSED_CONSONANT.get(c, c.lower())
        else:
            c_pre_pie = SIGN_TO_PRE_PIE_NON_STRESSED_CONSONANT.get(c, c.lower())
            if c not in ("P", "T", "K", "D", "Q",) and c:
                c_pre_pie += "ʰ"
            c_pg = SIGN_TO_PG_NON_STRESSED_CONSONANT.get(c, c.lower())
            c_pie = SIGN_TO_PIE_NON_STRESSED_CONSONANT.get(c, c.lower())
        pre_pie_list.append((c_pre_pie, v_mapped))
        pg_parts.append(c_pg + v_mapped)
        pie_parts.append(c_pie + v_mapped)
    return "-".join([item[0] + item[1] for item in pre_pie_list]), "-".join(pg_parts), "-".join(pie_parts)


def generate_readings(word_hyphenated):
    syllables = [s.strip().upper() for s in word_hyphenated.split("-") if s.strip()]
    num_syllables = len(syllables)
    if num_syllables == 0:
        return
    has_r = any("R" in parse_syllable(s) for s in syllables)
    variants = []
    for stressed_idx in range(num_syllables):
        pre_pie_r, pg_r, pie_r = build_layers_pure_chain(syllables, stressed_idx, r_to_l=False)
        if has_r:
            pre_pie_l, pg_l, pie_l = build_layers_pure_chain(syllables, stressed_idx, r_to_l=True)
            variants.append(
                Variant(stressed_syllable_number=stressed_idx + 1,
                        pre_pie_r=pre_pie_r,
                        pg_r=pg_r, pg_l=pg_l,
                        pie_r=pie_r, pie_l=pie_l))
        else:
            variants.append(
                Variant(stressed_syllable_number=stressed_idx + 1,
                        pre_pie_r=pre_pie_r,
                        pg_r=pg_r,
                        pie_r=pie_r))
    return variants
