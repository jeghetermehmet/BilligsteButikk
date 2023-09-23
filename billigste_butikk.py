def finnButikk(handeliste, prisliste, butikker):
    butikk_indeks = 0
    minste_pris = 0
    i = 0
    for butikk in prisliste:
        prispaabutikk = 0
        for vare in butikk:
            if vare in handeliste:
                prispaabutikk += butikk[vare]
        if prispaabutikk < minste_pris:
            minste_pris = prispaabutikk
            butikk_indeks = i
        i += 1
    return butikker[butikk_indeks]

#I denne oppgaven skal du skrive en funksjon finnButikk() som finner ut hvilken butikk som er billigst å handle på. Funksjonen tar imot 3 argumenter:

#En liste handleliste som er en liste av strenger som er alle varene du skal kjøpe. Du kan anta at man bare skal kjøpe én av hver.
#En liste prisListe som inneholder ordbøker med prisene av de forskjellige varene på hver butikk.
#    prisListe = [
#        {"salat" : 12, "fisk" : 99, "melk" : 12, "brod" :12},
#        {"salat" : 22, "fisk" : 60, "melk" : 18, "brod" :21},
#        {"salat" : 8, "fisk" : 120, "melk" : 10, "brod" :19},
#        {"salat" : 18, "fisk" : 40, "melk" : 30, "brod" :59},
#        {"salat" : 15, "fisk" : 200, "melk" : 40, "brod" :9},
#   ]
#En liste butikker med navn på butikker. Indeksene i prisListe og butikker samsvarer, altså prisListe[0] er prisene til butikker[0].
#    butikker = ["Rema1000", "Meny", "Kiwi","Spar", "Joker"]
#Implementer funksjonen finnButikk() som tar imot argumentene beskrevet over og returnerer navnet på butikken det er billigst å handle på.

#Eksempel: finnButikk(["salat","melk"], butikker, prisListe) skal returnere "Kiwi"#






    