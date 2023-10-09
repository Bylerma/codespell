import re
from spellchecker import SpellChecker

def fix_misspellings(text, spell_checker):
    words = re.findall(r'\b\w+\b', text)

    corrections = {}

    for word in words:
        if not spell_checker.correction(word.lower()) == word.lower():
            corrections[word] = spell_checker.correction(word.lower())

    for misspelled, corrected in corrections.items():
        text = text.replace(misspelled, corrected)

    return text
