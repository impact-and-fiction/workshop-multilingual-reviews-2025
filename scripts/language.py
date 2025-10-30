import spacy
# Add Persian/Farsi parser
import dadmatools.pipeline.language as language


def load_language_nlp_model(lang_code):
    if lang_code == 'fa':
        # There are a lot of parser components, but we won't need all of them
        # pips = 'tok,lem,pos,dep,chunk,cons,spellchecker,kasreh,itf,ner,sent'
        
        # Here lemmatizer, pos tagger and dependency parser will be loaded
        # as tokenizer is the default tool, it will be loaded as well even without calling
        pips = 'tok,lem,pos,dep,chunk,sent'
        return language.Pipeline(pips)
        
    elif lang_code in spacy_model_map:
        return spacy.load(spacy_model_map[lang_code])
        
    else:
        raise ValueError(f"No parser for language code '{lang_code}'.")



code_lang_map = {
    'ar': 'Arabic',
    'cs': 'Czech',
    'da': 'Danish',
    'de': 'German',
    'el': 'Greek',
    'en': 'English',
    'es': 'Spanish',
    'fa': 'Persian',
    'fi': 'Finnish',
    'fr': 'French',
    'hi': 'Hindi',
    'hu': 'Hungarian',
    'id': 'Indonesian',
    'it': 'Italian',
    'ja': 'Japanese',
    'ko': 'Korean',
    'nl': 'Dutch',
    'no': 'Norwegian',
    'pl': 'Polish',
    'ps': 'Pashto',
    'pt': 'Portuguese',
    'ru': 'Russian',
    'sk': 'Slovak',
    'sl': 'Slovenian',
    'sr': 'Serbian',
    'sv': 'Swedish',
    'tr': 'Turkish',
    'uk': 'Ukranian',
    'ur': 'Urdu',
    'zh': 'Chinese' # (macro-language label)
}

lang_code_map = {lang: code for code, lang in code_lang_map.items()}

# Languages with SpaCy models and reviews in the multilingual dataset
spacy_model_map = {
    "da": "da_core_news_lg",
    "de": "de_core_news_lg",
    "el": "el_core_news_lg",
    "en": "en_core_web_lg",
    "es": "es_core_news_lg",
    "fi": "fi_core_news_lg",
    "fr": "fr_core_news_lg",
    "hr": "hr_core_news_lg",
    "it": "it_core_news_lg",
    "ja": "ja_core_news_lg",
    "ko": "ko_core_news_lg",
    "nl": "nl_core_news_lg",
    "pl": "pl_core_news_lg",
    "pt": "pt_core_news_lg",
    "ru": "ru_core_news_lg",
    "sl": "sl_core_news_lg",
    "sv": "sv_core_news_lg",
    "uk": "uk_core_news_lg",
    "zh": "zh_core_web_lg"
}

