from deep_translator import GoogleTranslator

text = 'This is a sample text to translate.'

gt = GoogleTranslator(source='en', target='fr')
result = gt.translate(text)

print(result)