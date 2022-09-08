user = "ugur"
password = "1881"

while True:
    kullanıcı = input("Kullanıcı adınızı giriniz: ")
    parola = input("Şifrenizi giriniz: ")
    # ikisi de doğru
    if kullanıcı == user and parola == password:
        print("Giriş Başarılı")
        break
   
    elif kullanıcı != user and parola != password:
        print("Şifreniz Ve Kullanıcı Adınız Yanlış")
    # Şifre Ve Kullanıcı Adınız Yanlış
