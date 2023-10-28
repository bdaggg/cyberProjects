# XSS-FINDER
 Herkese merhabalar bu projemde get methoduyla çalışan bir web sitesinde XSS açığının bulunup bulunmadığını kontrol eden bir python kodu yazdım.
 Test için yine python ile sizin local ip adressinizle 80 portunda get methoduyla çalışan bir site yaptım testlerimizi buradan yapabiliriz.
 
 
![Ekran Görüntüsü (180)](https://user-images.githubusercontent.com/110742864/236263057-4a8b1787-b7ff-4b3a-9887-f8d4b42ab5f2.png)

tester.py dosyamızı çalıştırdığımızda yukarıdaki gibi bir get methoduyla çalışan site bizi karşılıyor.


![Ekran Görüntüsü (181)](https://user-images.githubusercontent.com/110742864/236263257-b8c9f40a-ead3-403e-af30-61605be79fc7.png)


enter some text kısmına test yazıp submit butonuna tıkladığımız zaman aşağıdaki gibi bir görüntü bizleri karşılıyor.


![Ekran Görüntüsü (183)](https://user-images.githubusercontent.com/110742864/236263430-1fac3335-c875-4a4c-99a7-1c41d382ac2e.png)


yazdığımız test ifadesini URL içerisinde görüyoruz bu şekilde sitemizin get methodu kullandığını anlıyoruz.

sitemizin get methodunu kullandığını anladıtan sonra sıra xss finder kodumuzu çalıştırmaya geliyor. dosyamızı çalıştırınca bizden hedef URL istiyor. hedef URL girilince kodumuz çalışıyor ve açığı bulunca ekrana açık bulundu yazıp açığı bulduran ifadeyi ekrana basıyor.


![Ekran Görüntüsü (185)](https://user-images.githubusercontent.com/110742864/236263573-49b3d633-4085-4d5a-abac-c3663e605020.png)



