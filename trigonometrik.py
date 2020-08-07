sifre = "hesap2"
s = input("parola : ")
if s != "hesap2":
	print("yanlis parola")
else :
	menu = """
(1)cos-sin , tan-cot çevirme
(2)trigonometrik kenar oranı hesaplama
(3)trigonometrik oran hesaplama(açıya göre)
(4)faktoriyel bulma(x!)
(5)birim çembersel trigonometri
(6) çıkış
"""
print(menu)

while True:
	s = input("işlem seçiniz ")
		
	if s == "1":
			t = input("trigonometrik oranı giriniz (örn.sin) : ")
			if t == "sin":
				a = input("{} acı degeri giriniz : ".format(t))
				a = int(a)
				if a >= 90:
					print("açı 90 a büyük ya da eşit olamaz")
				else:
					x = 90-int(a)
					print("cos{}".format(x))
			

			elif t == "cos":
				a = input("{} acı degeri giriniz : ".format(t))
				a = int(a)
				if a >= 90:
					print("açı 90 a büyük ya da eşit olamaz")
				else:
					x = 90-int(a)
					print("sin{}".format(x))
			

			elif t == "tan":
				a = input("{} acı degeri giriniz : ".format(t))
				a = int(a)
				if a >= 90:
					print("açı 90 a büyük ya da eşit olamaz")
				else:
					x = 90-int(a)
					print("cot{}".format(x))
			

			elif t == "cot":
				a = input("{} acı degeri giriniz : ".format(t))
				a = int(a)
				if a >= 90:
					print("açı 90 a büyük ya da eşit olamaz")
				else:
					x = 90-int(a)
					print("tan{}".format(x))
			

			else :
				print("lütfen trigonometrik bir deger giriniz : ")

	elif s == "2":
			z = input("trigonometrik oranı giriniz (örn.sin) : ")

			if z == "sin":
				a = input("açı degeri : ")
				kk = input("{} acısının karşısındaki kenar uzunlugu? : ".format(a))
				hk = input("hipotenüs uzunlugu? ")
				if kk>=hk:
					print("hipotenüs karşı kenardan küçük ya da eşit olamaz")
				else:
					print("sin{} = ".format(a),int(kk)/int(hk))

			elif z == "cos":
				a = input("açı degeri : ")
				kk = input("{} acısının komşu kenar uzunlugu? : ".format(a))
				hk = input("hipotenüs uzunlugu? ")
				if kk>=hk:
					print("hipotenüs komşu kenardan küçük ya da eşit olamaz")
				else:
					print("sin{} = ".format(a),int(kk)/int(hk))


			elif z == "cot":
				a = input("açı degeri : ")
				kk = input("{} acısının komşu kenar uzunlugu? : ".format(a))
				hk = input("{} acısının karşısındaki kenar uzunlugu? :".format(a))
				if kk == hk:
					print("hipotenüs karşı kenardan küçük ya da eşit olamaz")
				else:
					print("sin{} = ".format(a),int(kk)/int(hk))

			else :
				print("lütfen trigonometrik bir deger giriniz : ")

	elif s == "3":
			import math 
			
			x = input("trigonometrik oranı giriniz (örn.sin) : ")

			if x == "sin":
				aci = input("açı degeri giriniz : ")
				aci = float(aci)
				aci=math.radians(aci)
				print("sonuç = ",math.sin(aci))

			elif x == "cos":
				aci = input("açı degeri giriniz : ")
				aci = float(aci)
				aci=math.radians(aci)
				print("sonuç = ",math.cos(aci))

			elif x == "tan":
				aci = input("açı degeri giriniz : ")
				aci = int(aci)
				aci=math.radians(aci)
				print("sonuç = ",math.tan(aci))

			elif x == "cot":
				aci = input("açı degeri giriniz : ")
				if aci == "0":
					print("sıfıra bölünemez")
				else:
					aci = int(aci)
					aci=math.radians(aci)
					print("sonuç = ",math.tan(aci)**-1)

			else :
				print("lütfen trigonometrik bir deger giriniz : ")

	elif s == "4":
			import math
			x = input("hangi sayının faktoriyeli?? : ")
			x = int(x)
			y = math.factorial(x)
			print("sonuç: ",y)

	elif s == "5":
			x = input("trigonmetrik deger giriniz (örn.sin) : ")
			a = input("acı degeri giriniz : ")
			a = int(a)
			b = 180-a
			print("-{}".format(x),"{}".format(b))

	elif s == "6" :
			 print("bizi tercih etiğiniz için teşekkür ederiz...")
			 quit()

	else :
		print("lütfen menüden giriniz...")
