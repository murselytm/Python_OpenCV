ogrenciList = ["Mursel", "Ahmet", "Ayten", "Ali", "Mursel"] #daha hızlı çalışır ve silme + ekleme yapılamaz

studentsSet = {"Mursel","Ahmet"} #daha hızlı çalışır ve silme + ekleme yapılır
studentsSet.update(["Ayşe","Fahriye"])
studentsSet.discard("ali")

ogrenciList2 = ogrenciList # bunu dediğimizde kopyaladığı listin ramdeki yerini referans olarak alıyor (c deki gibi) bu yüzden ogrenciList2 değişikli 1 i de etkiler
ogrenciList3 = ogrenciList.copy() #bunda listeyi kopyalar ve rame kendilerine özgü yeni yer açar
print(studentsSet)
print("Mursel Sayısı : " + str(ogrenciList.count("Mursel")))