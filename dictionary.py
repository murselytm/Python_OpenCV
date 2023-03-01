# Hashmapin python versiyonu

sozluk = {
    "book": "kitap",
    "table": "masa",
}
sozluk2 = dict(masa = "table", kitap = "book") #consturctor tanımı

sozluk["pencil"] = "kalem"
print(sozluk)

sozluk["book"] = "kitap 1"
print(sozluk["book"])

print(sozluk2)
del(sozluk["book"])
print(sozluk)