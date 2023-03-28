def panel_calc(d_podl, szer_pod, d_pan, szer_pan, ilosc_paneli_w_opakowaniu):
    powi_pomieszczenia = (d_podl * szer_pod) * 1.1
    powi_panela = d_pan * szer_pan
    ilosc_paneli_potrzebna = powi_pomieszczenia / powi_panela
    ilosc_opakowan_potrzebna = ilosc_paneli_potrzebna / ilosc_paneli_w_opakowaniu
    return ilosc_opakowan_potrzebna

print("Potrzeba : " + str(panel_calc(4, 4, 0.20, 1, 10)))