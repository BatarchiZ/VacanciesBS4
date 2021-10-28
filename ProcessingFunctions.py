from natasha import (
    Segmenter,
    MorphVocab,

    NewsEmbedding,
    NewsMorphTagger,
    NewsSyntaxParser,
    NewsNERTagger,

    PER,
    NamesExtractor,

    Doc
)

segmenter = Segmenter()
morph_vocab = MorphVocab()
emb = NewsEmbedding()
morph_tagger = NewsMorphTagger(emb)
syntax_parser = NewsSyntaxParser(emb)
ner_tagger = NewsNERTagger(emb)
names_extractor = NamesExtractor(morph_vocab)

def preprocessNatasha(text:str)->str:
    doc = Doc(text)
    doc.segment(segmenter)
    doc.tag_morph(morph_tagger)
    for token in doc.tokens:
        token.lemmatize(morph_vocab)
        text = [i.lemma for i in doc.tokens if i.pos not in ['SCONJ','PRON','PART','PUNCT','ADP','CCONJ','DET']]
    return text


import re
def preprocessRe(text:str)->str:
    text = text.lower().strip()
    text = re.sub(r"[^0-9a-zA-Zа-яА-Я ]+","",text)
    return text


def preprocessPython(text:str)->str:
    text =text.lower().strip()
    return text


