from googletrans import Translator
sent = str(input())
trans = Translator()
trans_sen = trans.translate(sent, src='en', dest='nl')
print(trans_sen)
