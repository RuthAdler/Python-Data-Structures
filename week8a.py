text = "X-DSPAM-Confidence:    0.8475"
a= text.find ('0.8475')
x=(len(text))
fin=(text[a:x])
fin=float(fin)
print(fin)