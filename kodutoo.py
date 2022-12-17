#Задание 6: Проверка имени
name=input("Sisesta oma nimi: ")
print(f"Tere, {name}!")
word={name}
täishäälikud=0
taashäälikud=0
for i in word:
    letter=i.lower()
    if letter=="a" or letter == "e" or\
       letter=="i" or letter == "o" or\
       letter=="u" or letter == "y":
        täishäälikud+=1
    else:
        taashäälikud+=1
print("Täishäälikud %i\nKaashäälikud %i" % (täishäälikud, taashäälikud))
#Задание 5:
#def all_eq(list):
#max_slovo=max(list,key=lambda x: len(x))
#max_len=len(max_slovo)
#return [item.ljust(max_len, '_') for item in list]
#print(all_eq(['крот', 'белка', 'выхухоль']))
#print(all_eq(['a', 'aa', 'aaa', 'aaaa', 'aaaaa']))
#print(all_eq(['qweasdqweas', 'q', 'rteww', 'ewqqqqq']))
#Задание 4: Сортировка
Natural_numbers=[1,4,10,3,2,17,0,9,78]
Natural_numbers.sort()
print(Natural_numbers)
Natural_numbers=[1,2,5,27,48,3,8,5,10,7,5]
Natural_numbers.sort(reverse=True)
print(Natural_numbers)
#Задание 3: Бесполезные числа
def bespolez(list):
    return max(list) / len(list)
print(bespolez([2, 48, 89]))
print(bespolez([18, 4, -4, 11.5, 0, 2]))
print(bespolez([-96, -0.05, -9.28, 11.1, 12.12, 55, 8.1]))

#Задание 2: Перемена мест
our_list=[1, 2, 3, 4]
#our_list=input().split()
i,j=0,len(our_list)-1
while i<j:
    our_list[i],our_list[j]=our_list[j],our_list[i]
    i,j=i+1,j-1
print(our_list)
#Задание 1: Почтовый индекс
maad=["Tallinn","Narva, Narva-Jõesuu","Kohtla-Järve Ida-Virumaa, Lääne-Virumaa", "Jõgevamaa", "Tartu linn", "Tartumaa, Põlvamaa, Võrumaa, Valgamaa", "Viljandimaa, Järvamaa, Harjumaa, Raplamaa", "Pärnumaa", "Läänemaa, Hiiumaa, Saaremaa"]
index=""
n=0
while type(index)!=int or n!=5:
    try:
        index=int(input("Sisesta indeks: "))
        n=len(str(index))
    except:
        print("Vale indeks!")
index_list=list(str(index))
print(maad[int(index_list[0])-1])
#list
nimi=input("Mis on sinu nimi?: ")
tahed=list(nimi)
n=len(tahed)
print(f"{n} tähed: {tahed}")
print("Remove kasutamine")
t=input("Sisesta täht, mis on vaja kustutada ära: ")
tahed.count(t)
nt=tahed.count(t)
print(nt)
j=0
if nt==0:
    print(f"{t} ei ole listis ")
else:
    #for i in range(nt):
    #    if tahed[i-j]==t:
    #        tahed.pop(i-j)
    #        j+=1
    for i in range(len(tahed)):
        if tahed[i-j]==t:
            tahed.pop(i-j)
            j+=1
    print(f"Nüüd {t} ei ole listis, on jäänud {tahed} ")
t=input("Mis täht on vaja otsida?: ")
print(f"Täht {t} seisab {tahed.index(t)+1} positsioonil")
