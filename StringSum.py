# Girilen 2 rakamlardan oluşan string değeri veri dönüştürme yapmadan toplama fonksiyonu

def StringSum(val1, val2):
    sumx = [] # Toplama işleminin yapılacağı dizi
    len1=len(val1) # 1. değerin karakter sayısını değişkene atıyoruz: 6
    len2=len(val2) # 2. değerin karakter sayısını değişkene atıyoruz: 7
    
    if len1 != len2: # Girilen değerlerin karakter(basamak) sayıları eşit değil ise
        minus=len1-len2 # aradaki fark bir değişkene atanıyor : 1
        if(minus > 0 ): # fark pozitif ise val1 büyük olan
            while(minus > 0): # fark 0 olana kadar bir döngü başlıyor
                val2="0"+val2 # küçük olan değişkenin başına 0 ekleniyor
                minus-=1 # fark 1 azaltılıyor
        else: # fark(minus değişkeni) negatif ise val1 küçük olan
            while(minus < 0): # fark 0 olana kadar bir döngü başlıyor
                val1="0"+val1 # küçük olan değişkenin başına 0 ekleniyor
                minus+=1 # fark 1 azaltılıyor
                
# Programın bu aşamasında iki girdide aynı karakter sayısına sahip, bundan sonra kağıtta toplama işlemi mantığını koda dökeceğiz   
    lenx=len(val1)-1 # karakter sayısını bir azaltarak değişkene atıyoruz 
    #amacımız dizi üzerinde işlem yaparken son karakterden(birler basamağı) başlamak
    more=0
    while(lenx >= 0):
        temp=int(val1[lenx])+int(val2[lenx])+more # değerlerin son karakteri int'e çevrilerek toplanıyor
        
        if(len(str(temp)) == 2): # iki basamaklı ise
            sumx.append(str(temp-10)) # ikinci basamak son veriyi tutacağımız diziye ekleniyor
            more=1 #ilk basamak bir sonraki işlem için değişkene atanıyor
           
        else: # tek basamaklı ise
            sumx.append(str(temp))
            more=0 # tek basamaklı ise more 0 olarak özellikle atanıyor ki bir sonraki döngüde artı toplama yapılmasın
            
        lenx-=1 # sondan diğer basamağa geçiyor
        #print("::::::::::::",sumx[::-1],more,"   :", ) her döngünün sonunda hata ayıklama için verilerin çıktısını yazdırıyorum
    if(str(more) == "1"):#döngü bittikten sonra veri kalmışsa örn:(8+7=15 de ki 1) bunu veri dizinimizin sonuna ekleyelim
        sumx.append(more)
        
    sumx=sumx[::-1] # şu ana kadar veriyi tersten yazdık, (son basamak toplamı dizinin ilk karakterine yazıldı) bu yüzden ters çeviriyoruz
    result = ''.join(sumx) # diziyi değişken haline getiriyoruz
    return result # ve fonksiyon dönüşü olarak veriyoruz
#Fonksiyon bitişi   
value1=input("1. Değeri Giriniz: ")        
value2=input("2. Değeri Giriniz: ")        
print("Toplam: ",StringSum(value1,value2))
