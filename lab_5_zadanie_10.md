Zadanie 1
```python
from folder_aplikacji.models import Osoba
osoby = Osoba.objects.all()
print(osoby)
```

Zadanie 2
``` python
osoba = Osoba.objects.get(id=3)
print(osoba)
```

Zadanie 3 
``` python
osoba_z_A = Osoba.objects.filter(imie__startswith = 'A')
print(osoba_z_A)
```

Zadanie 4 (do sprawdzenia)
``` python
stanowiska = Osoba.objects.values('stanowisko').distinct()
print(stanowiska)
```

Zadanie 5
``` python
from folder_aplikacji.models import Stanowisko 
Stanowisko.objects.values_list('nazwa', flat = True).order_by("-nazwa")
```

Zadanie 6
``` python
Osoba.objects.create(imie = 'Jan', nazwisko = 'Kowalski',plec = 2, stanowisko = Stanowisko.objects.get(id = 1))
```