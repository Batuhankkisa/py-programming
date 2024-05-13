#Soru 1:
# a.) 500’den büyük ve çift sayı olması durumunda 7 ile çarpılması, değilse 7 ile bölünmesini if kullanarak yazın

n = 100
if n > 500 and n %2==0:
  n = n * 7
else:
  n = n / 7

print(n)

# b.) 200’den küçük ve 3’e tam bölünüyorsa 10 ile çarpın, 200’den küçük ve 3’e tam bölünmüyorsa 3 ile çarpın,
#     200’den büyük ve 3’e tam bölünüyorsa 3’e bölün ve diğer durumlarda ise 5’e bölün.

n = 300
if n < 200 and n %3 ==0:
  n = n*10
elif n < 200 and n%3 != 0:
  n = n*3
elif n > 200 and n %3 ==0:
  n = n / 3
else:
  n = n / 5
print(n)

# Alternatively:
n = 300
if n > 200:
  if n % 3 ==0:
    n = n*10
  else:
    n = n*3
else:
  if n % 3 ==0: # Burada aslinda 200'e esit olma durumunda soruda istenene gore hatali davraniyoruz.
                # n % 3 ==0 and n !=200 yazmamiz gerekirdi. Yapana +5 puan
    n = n /3
  else:
    n = n / 5

# c.) Girilen sayı eğer 3’e ve 5’e tam bölünmüyorsa ekrana “n sayısı 3 ve 5 tam bolunmuyor” yazdırın (not kullanarak yapmalısınız). Eğer sadece 3’e tam bölünüyosa Fizz, sadece 5’e tam bölünüyorsa ise Buzz yazdırın. Eğer ikisine de tam bölünüyorsa ise ekrana “FizzBuzz” yazdırın.

n = 8

if not n % 3 ==0 and not n %5 == 0:
  print('n sayisi 3 ve 5 tam bolunmuyor')
elif not n % 3 == 0: # Demek ki burada 5'e bolunuyor
  print('Buzz')
elif not n % 5 == 0: # Demek ki burada 3'e bolunuyor
  print('Fizz')
else:
  print('FizzBuzz')

# Alternatif:
if not n % 3 ==0 and not n %5 == 0:
  print('n sayisi 3 ve 5 tam bolunmuyor')
elif n % 3 == 0 and n % 5 == 0:
  print('FizzBuzz')
elif n % 5 == 0: # Demek ki burada 5'e bolunuyor
  print('Buzz')
else:
  print('Fizz')
