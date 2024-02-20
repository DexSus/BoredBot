from deep_translator import GoogleTranslator


def translate_to_ukr(word):
    translator = GoogleTranslator(source='english', target='ukrainian')
    return translator.translate(word)
