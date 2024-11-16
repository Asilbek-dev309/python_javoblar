s="Yoshinngizni kiriting"
narx=""
while narx!= 'quit' or"exit":
    break
def sonlar(): 
    narx=input(s)
qi=int(narx)
if qi >7:
    narh= 2000
elif 7>=qi<18:
    narh= 5000
elif 18<=qi<65:
    narh=10000
elif qi>65:
    narh=0
    if narh==0:
        print("Sizga chipta bepul")
    else:
        print(f"Sizning chipta narxingiz:{narh}")
print("Rahmat")


savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
savol += "Musbat son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

while True:
    qiymat = input(savol)
    if float(qiymat)<0:
        continue
    elif qiymat=='Exit':
        break
    else:
        ildiz = float(qiymat)**(0.5)
        print(f"{qiymat} ning ildizi {ildiz} ga teng")
        
        
q=("Yaxshi ko'rgan kitobingizni kiriting,")
q+=("Agar 'exit' so'zini yozsangiz dastur tugaydi!!!\n>>>")
while True:
    kitob=input(q)
    if kitob=='exit':
        break
print("Rahmat")