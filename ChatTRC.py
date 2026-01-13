from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

print("Merhana.Ben ChatTRC.Ben duygularınızı algılarım")

Cümleler =[
    "LGS'den 300 alıp güzel bir liseye gittim.",
    "Mukkammal",
    "Allah'ım şükürler olsun!",
    "Yurdumuz işgal altında",
]

Etiketler = [
    0,
    0,
    0,
    1,
]

Dönüştürücü = CountVectorizer()
X = Dönüştürücü.fit_transform(Cümleler)

zeka = MultinomialNB()
zeka.fit(X, Etiketler)

print("ChatTRC kesinlikle öğrendi!\n")

Mesaj = input("Bir mesaj yazarmısınız?")

Mesaj_sayı = Dönüştürücü.transform([Mesaj])
sonuç = zeka.predict(Mesaj_sayı)

if sonuç[0] == 0:
  print("Bu mesaj güzel gibi")
else:
  print("Bu mesaj kötü gibi")from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

print("Merhana.Ben ChatTRC.Ben duygularınızı algılarım")

Cümleler =[
    "LGS'den 300 alıp güzel bir liseye gittim.",
    "Mukkammal",
    "Allah'ım şükürler olsun!",
    "Yurdumuz işgal altında",
]

Etiketler = [
    0,
    0,
    0,
    1,
]

Dönüştürücü = CountVectorizer()
X = Dönüştürücü.fit_transform(Cümleler)

zeka = MultinomialNB()
zeka.fit(X, Etiketler)

print("ChatTRC kesinlikle öğrendi!\n")

Mesaj = input("Bir mesaj yazarmısınız?")

Mesaj_sayı = Dönüştürücü.transform([Mesaj])
sonuç = zeka.predict(Mesaj_sayı)

if sonuç[0] == 0:
  print("Bu mesaj güzel gibi")
else:
  print("Bumesaj kötü gibi")
  print("Bu mesaj kötü gibi")
