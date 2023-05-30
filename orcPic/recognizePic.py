import easyocr

reader = easyocr.Reader(['en'])
result = reader.readtext('captcha.jpg')
for res in result:
    print(res)
    print(type(res))
    print(res[1])
    print(type(res[1]))