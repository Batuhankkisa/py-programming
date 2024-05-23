------------------------------------------

n = 100
if n > 500 and n %2==0:
  n = n * 7
else:
  n = n / 7

print(n)

-----------------------------

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

-------------------------------------------

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
