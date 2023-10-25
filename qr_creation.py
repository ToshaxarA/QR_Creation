import segno
 
# создаем код
qrcode = segno.make_qr("Your link")
 # сохраняем его в файл "qr.png"
# qrcode.save("qr.png") 
 
# аналогично можно сохранить в другие форматы
# qrcode.save("qr.pdf")
# qrcode.save("qr.eps")
qrcode.save("qr.svg")
qrcode.show()


"""
Из интересных возможностей, представляемых библиотекой, можно отметить наличие встроенных функций-хелперов для кодирования определенной информации. Некоторые из них:

Кодирование email

segno.helpers.make_email(to, cc=None, bcc=None, subject=None, body=None)
 
# Параметры:
# to -  кому письмо
# cc -  список получателей копии письма
# bcc -  список получателей слепой копии письма
# subject -  тема письма
# body -  текст письма
Кодирование геокоординат

segno.helpers.make_geo(lat, lng)
 
# Параметры:
# lat -  широта
# lng -  долгота
Кодирование настроек wifi

segno.helpers.make_wifi(ssid, password=None, security=None, hidden=False)
 
# Параметры:
# ssid -  SSID сети
# password -  пароль
# security -  тип аутентификации ("WEP" или "WPA").
# hidden -  является ли сеть скрытой
Кодирование MeCard


segno.helpers.make_mecard(name, reading=None, email=None, phone=None, videophone=None, memo=None, nickname=None, birthday=None, url=None, pobox=None, roomno=None, houseno=None, city=None, prefecture=None, zipcode=None, country=None)
Кодирование vCard версии 3.0


segno.helpers.make_vcard(name, displayname, email=None, phone=None, fax=None, videophone=None, memo=None, nickname=None, birthday=None, url=None, pobox=None, street=None, city=None, region=None, zipcode=None, country=None, org=None, lat=None, lng=None, source=None, rev=None, title=None, photo_uri=None, cellphone=None, homephone=None, workphone=None)
Например, кодирование email:


from segno import helpers
 
qrcode = helpers.make_email("tom@gmail.com", cc=None, bcc=None, subject="Тема письма", body="Содержимое письма")
qrcode.save("email_qr.png", scale=5)
Или кодирование настроек wifi:


from segno import helpers
 
qrcode = helpers.make_wifi(ssid="MyWifi", password="1234567890", security="WPA")
qrcode.save("wifi-access.png", scale=10)
"""