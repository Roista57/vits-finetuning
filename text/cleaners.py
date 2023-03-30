import re
import pyopenjtalk

pyopenjtalk._lazy_init()

from text.japanese import japanese_to_romaji_with_accent

def japanese_cleaners(text):
    text = f'[JA]{text}[JA]'
    text = re.sub(r'\[JA\](.*?)\[JA\]', lambda x: japanese_to_romaji_with_accent(
        x.group(1)).replace('ts', 'ʦ').replace('u', 'ɯ').replace('...', '…')+' ', text)
    text = re.sub(r'\s+$', '', text)
    text = re.sub(r'([^\.,!\?\-…~])$', r'\1.', text)
    return text

def korean_cleaners(text):
    '''Pipeline for Korean text'''
    from text.korean import latin_to_hangul, number_to_hangul, divide_hangul
    text = latin_to_hangul(text)
    text = number_to_hangul(text)
    text = divide_hangul(text)
    text = re.sub(r'([\u3131-\u3163])$', r'\1.', text)
    return text
