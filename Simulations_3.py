import numpy as np
import matplotlib.pyplot as plt

#dane cen półproduktów są zapisywane jako ceny za ilość wymaganą do wyprodukowania
# pojedyniczej jednostki wyprodukowania
####Dane wejściowe symulacji:
k_wody = 0.625
k_cukru = 0.05
k_miety = 0.09
k_cytryny = 2
k_dojazdu = 8.8
k_stoiska = 100
k_utensylia = 60
cena = 3.5
cena_r = 3.5
czas = 72
el_cenowa = -1.35
#start koniec pracy (godziny)
start = 8
end = 16


def profit(popyt):
    return (cena-k_wody-k_cukru-k_miety-k_cytryny)*popyt

def popyt_korpo():
    delta_cena = (cena - cena_r) / cena_r
    delta_popyt = delta_cena * el_cenowa
    korpo_li = []
    for x in range(50):
        korpo_li.append(np.random.normal(9, 1))
        korpo_li.append(np.random.normal(17, 1))
    popyt_ki = 0
    for x in korpo_li:
        if x > start:
            if x < end:
                popyt_ki = popyt_ki + 1
    if round(popyt_ki*(1+delta_popyt)) < 0:
        return 0
    else:
        return round(popyt_ki*(1+delta_popyt))

def popyt_gastro():
    delta_cena = (cena - cena_r) / cena_r
    delta_popyt = delta_cena * el_cenowa
    gastro_li = []
    for x in range(40):
        gastro_li.append(np.random.normal(15, 1))
        gastro_li.append(np.random.normal(21, 1))
    popyt_gi = 0
    for x in gastro_li:
        if x > start:
            if x < end:
                popyt_gi = popyt_gi + 1
    if round(popyt_gi*(1+delta_popyt)) < 0:
        return 0
    else:
        return round(popyt_gi*(1+delta_popyt))

def popyt_park():
    delta_cena = (cena - cena_r) / cena_r
    delta_popyt = delta_cena * el_cenowa
    park_li = []
    for x in range(60):
        park_li.append(np.random.normal(12, 2))
    popyt_pi = 0
    for x in park_li:
        if x > start:
            if x < end:
                popyt_pi = popyt_pi + 1
    if round(popyt_pi*(1+delta_popyt)) < 0:
        return 0
    else:
        return round(popyt_pi*(1+delta_popyt))



#####Przykładowe zagęszczenie ludzi w ciągu dnia:
korpo_l = []
for x in range(50):
    korpo_l.append(np.random.normal(9, 1))
    korpo_l.append(np.random.normal(17, 1))

gastro_l = []
for x in range(40):
    gastro_l.append(np.random.normal(15, 1))
    gastro_l.append(np.random.normal(21, 1))

park_l = []
for x in range(60):
    park_l.append(np.random.normal(12, 2))


popyt_k = 0
popyt_g = 0
popyt_p = 0

for x in korpo_l:
    if x > start:
        if x < end:
            popyt_k = popyt_k + 1

for x in gastro_l:
    if x > start:
        if x < end:
            popyt_g = popyt_g + 1

for x in park_l:
    if x > start:
        if x < end:
            popyt_p = popyt_p + 1

plt.hist(korpo_l, bins=25, alpha=0.6, color='b', label='Ilość ludzi w centrum korporacyjnym')
plt.hist(gastro_l, bins=25, alpha=0.6, color='r', label='Ilość ludzi w centrum gastronomicznym')
plt.hist(park_l, bins=25, alpha=0.6, color='g', label='Ilość ludzi w parku')
plt.xlabel('Godzina')
plt.ylabel('Ilość ludzi')
plt.title('Histogram ilości ludzi w godzinach w 3 lokalizacjach')
plt.legend()
plt.show()

#######Zysk w parku
zysk = []
okresy = []
min_profit = []
max_profit = []
for t in range(czas):
    zysk.append(profit(popyt_park())-k_dojazdu)
    okresy.append(t+1)
    min_profit.append(min(zysk))
    max_profit.append(max(zysk))

fig, ax = plt.subplots()
ax.plot(okresy, zysk)
plt.xlabel('Dzień')
plt.ylabel('Zysk')
plt.title("Zysk w parku", fontdict=None, loc='center', pad=None)
ax.plot(okresy, min_profit, linestyle='dashed', label='Minimalny zysk')
ax.plot(okresy, max_profit, linestyle='dashed', label='Maksymalny zysk')
ax.legend()
plt.show()

#######Zysk w korpo
zysk = []
okresy = []
min_profit = []
max_profit = []
for t in range(czas):
    zysk.append(profit(popyt_korpo())-k_dojazdu)
    okresy.append(t+1)
    min_profit.append(min(zysk))
    max_profit.append(max(zysk))

fig, ax = plt.subplots()
ax.plot(okresy, zysk)
plt.xlabel('Dzień')
plt.ylabel('Zysk')
plt.title("Zysk w centrum korporacyjnym", fontdict=None, loc='center', pad=None)
ax.plot(okresy, min_profit, linestyle='dashed', label='Minimalny zysk')
ax.plot(okresy, max_profit, linestyle='dashed', label='Maksymalny zysk')
ax.legend()
plt.show()

#######Zysk w gastro
zysk = []
okresy = []
min_profit = []
max_profit = []
for t in range(czas):
    zysk.append(profit(popyt_gastro())-k_dojazdu)
    okresy.append(t+1)
    min_profit.append(min(zysk))
    max_profit.append(max(zysk))

fig, ax = plt.subplots()
ax.plot(okresy, zysk)
plt.xlabel('Dzień')
plt.ylabel('Zysk')
plt.title("Zysk w centrum gastronomicznym", fontdict=None, loc='center', pad=None)
ax.plot(okresy, min_profit, linestyle='dashed', label='Minimalny zysk')
ax.plot(okresy, max_profit, linestyle='dashed', label='Maksymalny zysk')
ax.legend()
plt.show()
#######Podwyżka ceny w T=36 do 5,25PLN
zysk = []
okresy = []
min_profit = []
max_profit = []
for t in range(36):
    zysk.append(profit(popyt_gastro())-k_dojazdu)
    okresy.append(t+1)
    min_profit.append(min(zysk))
    max_profit.append(max(zysk))

cena = 5.25
for t in range(36, 72):
    zysk.append(profit(popyt_gastro())-k_dojazdu)
    okresy.append(t+1)
    min_profit.append(min(zysk))
    max_profit.append(max(zysk))

fig, ax = plt.subplots()
ax.plot(okresy, zysk)
plt.xlabel('Dzień')
plt.ylabel('Zysk')
plt.title("Podwyżka ceny lemoniady w T=36 z 3,5 PLN do 5,25 PLN w centrum gastronomicznym", fontdict=None, loc='center', pad=None)
ax.plot(okresy, min_profit, linestyle='dashed', label='Minimalny zysk')
ax.plot(okresy, max_profit, linestyle='dashed', label='Maksymalny zysk')
ax.legend()
plt.show()
cena = 3.5

#######Wzrost ceny półproduktów (cytryny z 2 PLN do 3 PLN) w T=36
zysk = []
okresy = []
min_profit = []
max_profit = []
for t in range(36):
    zysk.append(profit(popyt_gastro())-k_dojazdu)
    okresy.append(t+1)
    min_profit.append(min(zysk))
    max_profit.append(max(zysk))

k_cytryny = 3
for t in range(36, 72):
    zysk.append(profit(popyt_gastro())-k_dojazdu)
    okresy.append(t+1)
    min_profit.append(min(zysk))
    max_profit.append(max(zysk))

fig, ax = plt.subplots()
ax.plot(okresy, zysk)
plt.xlabel('Dzień')
plt.ylabel('Zysk')
plt.title("Podwyżka ceny cytryny w T=36 z 2 PLN do 3 PLN w centrum gastronomicznym", fontdict=None, loc='center', pad=None)
ax.plot(okresy, min_profit, linestyle='dashed', label='Minimalny zysk')
ax.plot(okresy, max_profit, linestyle='dashed', label='Maksymalny zysk')
ax.legend()
plt.show()
k_cytryny = 2

#######Wzrost ceny półproduktów
zysk = []
okresy = []
min_profit = []
max_profit = []
for t in range(36):
    zysk.append(profit(popyt_gastro())-k_dojazdu)
    okresy.append(t+1)
    min_profit.append(min(zysk))
    max_profit.append(max(zysk))

k_wody = 0.9375
for t in range(36, 72):
    zysk.append(profit(popyt_gastro())-k_dojazdu)
    okresy.append(t+1)
    min_profit.append(min(zysk))
    max_profit.append(max(zysk))

fig, ax = plt.subplots()
ax.plot(okresy, zysk)
plt.xlabel('Dzień')
plt.ylabel('Zysk')
plt.title("Podwyżka ceny wody o 50%", fontdict=None, loc='center', pad=None)
ax.plot(okresy, min_profit, linestyle='dashed', label='Minimalny zysk')
ax.plot(okresy, max_profit, linestyle='dashed', label='Maksymalny zysk')
ax.legend()
plt.show()
k_wody = 0.625

#######Wzrost ceny półproduktów
zysk = []
okresy = []
min_profit = []
max_profit = []
for t in range(36):
    zysk.append(profit(popyt_gastro())-k_dojazdu)
    okresy.append(t+1)
    min_profit.append(min(zysk))
    max_profit.append(max(zysk))

k_cukru = 0.075
for t in range(36, 72):
    zysk.append(profit(popyt_gastro())-k_dojazdu)
    okresy.append(t+1)
    min_profit.append(min(zysk))
    max_profit.append(max(zysk))

fig, ax = plt.subplots()
ax.plot(okresy, zysk)
plt.xlabel('Dzień')
plt.ylabel('Zysk')
plt.title("Podwyżka ceny cukru o 50%", fontdict=None, loc='center', pad=None)
ax.plot(okresy, min_profit, linestyle='dashed', label='Minimalny zysk')
ax.plot(okresy, max_profit, linestyle='dashed', label='Maksymalny zysk')
ax.legend()
plt.show()
k_cukru = 0.05

#######Wzrost ceny półproduktów
zysk = []
okresy = []
min_profit = []
max_profit = []
for t in range(36):
    zysk.append(profit(popyt_gastro())-k_dojazdu)
    okresy.append(t+1)
    min_profit.append(min(zysk))
    max_profit.append(max(zysk))

k_miety = 0.135
for t in range(36, 72):
    zysk.append(profit(popyt_gastro())-k_dojazdu)
    okresy.append(t+1)
    min_profit.append(min(zysk))
    max_profit.append(max(zysk))

fig, ax = plt.subplots()
ax.plot(okresy, zysk)
plt.xlabel('Dzień')
plt.ylabel('Zysk')
plt.title("Podwyżka ceny mięty o 50%", fontdict=None, loc='center', pad=None)
ax.plot(okresy, min_profit, linestyle='dashed', label='Minimalny zysk')
ax.plot(okresy, max_profit, linestyle='dashed', label='Maksymalny zysk')
ax.legend()
plt.show()
k_miety = 0.09

#######Wzrost ceny dojazdu (z 8.8 PLN do 13,2 PLN) w T=36
zysk = []
okresy = []
min_profit = []
max_profit = []
for t in range(36):
    zysk.append(profit(popyt_gastro())-k_dojazdu)
    okresy.append(t+1)
    min_profit.append(min(zysk))
    max_profit.append(max(zysk))

k_dojazdu = 13.2
for t in range(36, 72):
    zysk.append(profit(popyt_gastro())-k_dojazdu)
    okresy.append(t+1)
    min_profit.append(min(zysk))
    max_profit.append(max(zysk))

fig, ax = plt.subplots()
ax.plot(okresy, zysk)
plt.xlabel('Dzień')
plt.ylabel('Zysk')
plt.title("Podwyżka ceny dojazdu w T=36 z 8,8 PLN do 13,2 PLN w centrum gastronomicznym", fontdict=None, loc='center', pad=None)
ax.plot(okresy, min_profit, linestyle='dashed', label='Minimalny zysk')
ax.plot(okresy, max_profit, linestyle='dashed', label='Maksymalny zysk')
ax.legend()
plt.show()
k_dojazdu = 8.8


#######Histogram zysków parku:
cena = 4.4
zysk_calkowity_l = []
for x in range(1000):
    zysk = []
    for t in range(czas):
        zysk.append(profit(popyt_park())-k_dojazdu)
    zysk_calkowity = sum(zysk) - k_utensylia - k_stoiska
    zysk_calkowity_l.append(zysk_calkowity)

print("Wartość maksymalna:")
print(max(zysk_calkowity_l))
print("Wartość minimalna:")
print(min(zysk_calkowity_l))
print("Wartość średnia:")
print(sum(zysk_calkowity_l)/1000)
zysk_calkowity_lm = zysk_calkowity_l.copy()
zysk_calkowity_lm.sort()
mid = len(zysk_calkowity_lm) // 2
res = (zysk_calkowity_lm[mid] + zysk_calkowity_lm[~mid]) / 2
plt.hist(zysk_calkowity_l, bins=25, alpha=0.6, color='b')
print("Wartość mediany:")
print(res)
sucess = 0
for x in zysk_calkowity_l:
    if x > 3590:
        sucess = sucess + 1
print("Ilość sukcesów:")
print(sucess)
print("Procent sukcesów:")
print(sucess/10)

plt.xlabel('Całkowity zysk')
plt.ylabel('Ilość symulacji')
plt.title('Całkowity zysk przez okres 72 dni w parku w godzinach 8:00-16:00')
plt.show()

#######Histogram zysków korpo:
cena = 4.4
zysk_calkowity_l = []
for x in range(1000):
    zysk = []
    for t in range(czas):
        zysk.append(profit(popyt_korpo())-k_dojazdu)
    zysk_calkowity = sum(zysk) - k_utensylia - k_stoiska
    zysk_calkowity_l.append(zysk_calkowity)

print("Wartość maksymalna:")
print(max(zysk_calkowity_l))
print("Wartość minimalna:")
print(min(zysk_calkowity_l))
print("Wartość średnia:")
print(sum(zysk_calkowity_l)/1000)
zysk_calkowity_lm = zysk_calkowity_l.copy()
zysk_calkowity_lm.sort()
mid = len(zysk_calkowity_lm) // 2
res = (zysk_calkowity_lm[mid] + zysk_calkowity_lm[~mid]) / 2
plt.hist(zysk_calkowity_l, bins=25, alpha=0.6, color='b')
print("Wartość mediany:")
print(res)
sucess = 0
for x in zysk_calkowity_l:
    if x > 3590:
        sucess = sucess + 1
print("Ilość sukcesów:")
print(sucess)
print("Procent sukcesów:")
print(sucess/10)

plt.hist(zysk_calkowity_l, bins=25, alpha=0.6, color='b')
plt.xlabel('Całkowity zysk')
plt.ylabel('Ilość symulacji')
plt.title('Całkowity zysk przez okres 72 dni w centrum korporacyjnym w godzinach 8:00-16:00')
plt.show()

#######Histogram zysków gastro:
cena = 4.4
zysk_calkowity_l = []
for x in range(1000):
    zysk = []
    for t in range(czas):
        zysk.append(profit(popyt_gastro())-k_dojazdu)
    zysk_calkowity = sum(zysk) - k_utensylia - k_stoiska
    zysk_calkowity_l.append(zysk_calkowity)

print("Wartość maksymalna:")
print(max(zysk_calkowity_l))
print("Wartość minimalna:")
print(min(zysk_calkowity_l))
print("Wartość średnia:")
print(sum(zysk_calkowity_l)/1000)
zysk_calkowity_lm = zysk_calkowity_l.copy()
zysk_calkowity_lm.sort()
mid = len(zysk_calkowity_lm) // 2
res = (zysk_calkowity_lm[mid] + zysk_calkowity_lm[~mid]) / 2
plt.hist(zysk_calkowity_l, bins=25, alpha=0.6, color='b')
print("Wartość mediany:")
print(res)
sucess = 0
for x in zysk_calkowity_l:
    if x > 3590:
        sucess = sucess + 1
print("Ilość sukcesów:")
print(sucess)
print("Procent sukcesów:")
print(sucess/10)

plt.hist(zysk_calkowity_l, bins=25, alpha=0.6, color='b')
plt.xlabel('Całkowity zysk')
plt.ylabel('Ilość symulacji')
plt.title('Całkowity zysk przez okres 72 dni w centrum gastronomicznym w godzinach 8:00-16:00')
plt.show()

#######Cena a zysk całkowity:
cena = 3.5
ceny = []
min_profit = []
max_profit = []
zysk_calkowity_l = []
for x in range(1000):
    cena = 2.5 + x/200
    ceny.append(cena)
    zysk = []
    for t in range(czas):
        zysk.append(profit(popyt_gastro())-k_dojazdu)
    zysk_calkowity = sum(zysk) - k_utensylia - k_stoiska
    zysk_calkowity_l.append(zysk_calkowity)
    min_profit.append(min(zysk_calkowity_l))
    max_profit.append(max(zysk_calkowity_l))

fig, ax = plt.subplots()
ax.plot(ceny, zysk_calkowity_l)
plt.xlabel('Cena lemoniady')
plt.ylabel('Zysk całkowity')
plt.title("Zysk całkowity na przestrzeni 72 dni w zależności od ceny lemoniady", fontdict=None, loc='center', pad=None)
ax.plot(ceny, min_profit, linestyle='dashed', label='Minimalny zysk')
ax.plot(ceny, max_profit, linestyle='dashed', label='Maksymalny zysk')
ax.legend()
print(max(zysk_calkowity_l))
print(zysk_calkowity_l.index(max(zysk_calkowity_l)))
print(ceny[zysk_calkowity_l.index(max(zysk_calkowity_l))])
plt.show()


