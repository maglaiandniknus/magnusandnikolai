#Nikolai Myhre sitt program - Laget den 18.01.18

while True:

    kode = input ("Enter Code: ")
    if kode=="Nikolai":
        print("-----------------------------------------------------------------------------")
        print("Access Granted")
        print("-----------------------------------------------------------------------------")

#Dette er passordet som kreves for å ta i bruk formel-hefte
#-------------------------------------------------------------------------------------------------------------------

        print("""Først skriv inn tittel på formel, deretter kan du skrive
inn typen formel du ønsker å bruke.

Er du usikker på de tilgjenglige formlene kan du skrive 'Formler'
hvor du da vil få opp en liste med ulike formler du kan bruke.

*Alle desimaltall må bli skrevet med '.' ikke ',' for at de skal funke.
*Alle ord må bli ordrett skrevet ellers vil du ikke oppnå ønskede resultater.
-----------------------------------------------------------------------------
""")

            
#Dette er meldingen som kommer inn når du har fått 'Godkjent Adgang'
#-------------------------------------------------------------------------------------------------------------------

        while True:

            liste = input("""
----------------------------------------------------------------------------------------
Du kan nå skrive formelen din; 'Ib', 'Ohm', 'Effekt', 'Kortsluttning' og 'Spenningsfall'
----------------------------------------------------------------------------------------
""")

            if liste=="Formler":
                print("""
Mulige formeler (Viktig å skrive nøyaktig hva det står):

-Ib            -Kortsluttning
  -3fase         -Ik2pmin
  -2fase         -Ik2pmaks
  -1fase         -Ik3pmaks

-Ohm           -Spenningsfall
  -U             -3fase
  -R             -2fase
  -I             -1fase
                 -DU%
-Effekt                 
  -P
  -U
  -I
""")

#Dette er listen som kommer opp når du har skrevet inn 'Hjelp'
#-------------------------------------------------------------------------------------------------------------------

            if liste=="Ib":
                bela = input("""Velg hva du leter etter 3fase, 2fase eller 1fase""")

#Her blir du spurt hva du vil finne ut av innenfor 'Belastningsstrømmer'
#-------------------------------------------------------------------------------------------------------------------

                if bela=="3fase":
                    print("Belastningsstrøm for 3fase")

                    P=float(input("Effekt(W): "))
                    U=float(input("Spenning(V): "))
                    cos=float(input("Cosφ: "))
                    n=float(input("Virkningsgrad(ƞ): "))

                    ans1=(U*cos*n*1.732050807568877)
                    ans2=(P/ans1)
                    print("{}{}".format(ans2, "A"))
                    print("""
--------------------------------------------------------------------------
""")

#Utregning for Ib - 3fase
#-------------------------------------------------------------------------------------------------------------------

                if bela=="2fase":
                    print("Belastningsstrøm for 2fase")

                    P=float(input("Effekt(P2): "))
                    U=float(input("Spenning(V): "))
                    Cos=float(input("Cosφ: "))


                    ans1=(U*Cos)
                    ans2=(P/ans1)
                    print("{}{}".format(ans2, "A"))
                    print("""
--------------------------------------------------------------------------
""")

#Utregning for Ib - 2fase
#-------------------------------------------------------------------------------------------------------------------

                if bela=="1fase":
                    print("Belastningsstrøm for 1fase")

                    P=float(input("Effekt(P2): "))
                    U=float(input("Spenning(V): "))
                    Cos=float(input("Cosφ: "))


                    ans1=(U*Cos)
                    ans2=(P/ans1)
                    print("{}{}".format(ans2, "A"))
                    print("""
--------------------------------------------------------------------------
""")

#Utregning for Ib - 1fase
#-------------------------------------------------------------------------------------------------------------------

            if liste=="Ohm":
                ohm = input ("""Velg hva du leter etter; U, R eller I""")

#Her blir du spurt hva du vil finne ut av innenfor 'Ohm's Lov'
#-------------------------------------------------------------------------------------------------------------------

                if ohm=="U":
                    print("U - Spenning")

                    R=float(input("Resistans(Ω): "))
                    I=float(input("Ampere(A): "))

                    ans1=(R*I)
                    print("{}{}".format(ans1, "V"))
                    print("""
--------------------------------------------------------------------------
""")

#Utregning for Ohm's Lov - U
#-------------------------------------------------------------------------------------------------------------------

                if ohm=="R":
                    print("R - Resistans")

                    U=float(input("Spenning(V): "))
                    I=float(input("Ampere(A): "))

                    ans1=(U/I)
                    print("{}{}".format(ans1, "Ω"))
                    print("""
--------------------------------------------------------------------------
""")

#Utregning for Ohm's Lov - R
#-------------------------------------------------------------------------------------------------------------------

                if ohm=="I":
                    print("I - Ampere")

                    U=float(input("Spenning(V): "))
                    R=float(input("Resistans(Ω): "))

                    ans1=(U/R)
                    print("{}{}".format(ans1, "A"))
                    print("""
--------------------------------------------------------------------------
""")

#Utregning for Ohm's Lov - I
#-------------------------------------------------------------------------------------------------------------------

            if liste=="Effekt":
                eff = input ("""Velg hva du leter etter; P, U eller I""")

#Her blir du spurt om hva du vil finne ut av innenfor 'Effekt-loven'
#-------------------------------------------------------------------------------------------------------------------


                if eff=="P":
                    print("P - Effekt")

                    U=float(input("Spenning(U): "))
                    I=float(input("Ampere(A): "))

                    ans1=(U*I)
                    print("{}{}".format(ans1, "W"))
                    print("""
--------------------------------------------------------------------------
""")

#Utregning for Effekt-loven - P
#-------------------------------------------------------------------------------------------------------------------

                if eff=="U":
                    print("U - Spenning")

                    P=float(input("Effekt(W): "))
                    I=float(input("Ampere(A): "))

                    ans1=(P/I)
                    print("{}{}".format(ans2, "V"))
                    print("""
--------------------------------------------------------------------------
""")

#Utregning for Effekt-loven - U
#-------------------------------------------------------------------------------------------------------------------

                if eff=="I":
                    print("I - Ampere")

                    U=float(input("Spenning(V): "))
                    P=float(input("Effekt(W): "))

                    ans1=(P/U)
                    print("{}{}".format(ans1, "A"))
                    print("""
--------------------------------------------------------------------------
""")

#Utregning for Effekt-loven - I
#-------------------------------------------------------------------------------------------------------------------

            if liste=="Kortsluttning":
                kort = input ("""Velg hva du leter etter; Ik2pmin, Ik2pmaks eller Ik3pmaks""")

#Her blir du spurt om hva du vil finne innenfor 'Kortsluttning'
#-------------------------------------------------------------------------------------------------------------------


                if kort=="Ik2pmin":
                    print("Ik2pmin")

                    Un=float(input("Nominelle Spenning(V): "))
                    Z=float(input("Zytre: "))
                    Rf=float(input("Rfase: "))
                    L=float(input("Lengde(m): "))

                    ans1=(0.95*Un)
                    ans2=(1.732050807568877*(Z+(Rf*L)))
                    ans3=(ans1/ans2)
                    print("{}{}{}{}{}".format(ans3, "kA", " = ", ans3*1000, "A"))
                    ("kA")

                    print("""
--------------------------------------------------------------------------
""")

#Utregning for Kortsluttning - Ik2pmin
#-------------------------------------------------------------------------------------------------------------------

                if kort=="Ik2pmaks":
                    print("Ik2pmaks")

                    Un=float(input("Nominelle Spenning(V): "))
                    Z=float(input("Zytre: "))
                    Rf=float(input("Rfase: "))
                    L=float(input("Lengde(m): "))

                    ans1=(1.1*Un)
                    ans2=(1.732050807568877*(Z+(Rf*L)))
                    ans3=(ans1/ans2)
                    ans4=(ans3/1.15)
                    print("{}{}{}{}{}".format(ans4, "kA", " = ", ans4*1000, "A"))
                    print("""
--------------------------------------------------------------------------
""")

#Utregning for Kortsluttning - Ik2pmaks
#-------------------------------------------------------------------------------------------------------------------

                if kort=="Ik3pmaks":
                    print("Ik3pmaks")

                    Un=float(input("Nominelle Spenning(V): "))
                    Z=float(input("Zytre: "))
                    Rf=float(input("Rfase: "))
                    L=float(input("Lengde(m): "))

                    ans1=(1.1*Un)
                    ans2=(1.732050807568877*(Z+(Rf*L)))
                    ans3=(ans1/ans2)
                    print("{}{}{}{}{}".format(ans3, "kA", " = ", ans3*1000, "A"))
                    print("""
--------------------------------------------------------------------------
""")

#Utregning for Kortsluttning - Ik3pmaks
#-------------------------------------------------------------------------------------------------------------------

            if liste=="Spenningsfall":
                spen = input ("""Velg hva du leter etter; 3fase, 2fase, 1fase og DU%""")

#Her blir du spurt om hva du vil finne innenfor 'Spenningsfall' - Motorbelastet
#-------------------------------------------------------------------------------------------------------------------


                if spen=="3fase":
                    print("ΔU for 3fase")

                    I=float(input("Ampere(A): "))
                    Pho=float(input("Resistivitet(ρ): "))
                    L=float(input("Lengde(m): "))
                    Cos=float(input("Cosφ: "))
                    A=float(input("Areal(A): "))

                    ans1=(I*Pho*L*1.732050807568877*Cos)
                    ans2=(ans1/A)
                    print("{}{}".format(ans2, "V"))
                    print("""
--------------------------------------------------------------------------
""")

#Utregning for Spenningsfall - 3fase
#-------------------------------------------------------------------------------------------------------------------

                if spen=="2fase":
                    print("ΔU for 2fase")

                    I=float(input("Ampere(A): "))
                    Pho=float(input("Resistivitet(ρ): "))
                    L=float(input("Lengde(m): "))
                    Cos=float(input("Cosφ: "))
                    A=float(input("Areal(A): "))

                    ans1=(I*Pho*L*2*Cos)
                    ans2=(ans1/A)
                    print("{}{}".format(ans2, "V"))
                    print("""
--------------------------------------------------------------------------
""")

#Utregning for Spenningsfall - 2fase
#-------------------------------------------------------------------------------------------------------------------

                if spen=="1fase":
                    print("ΔU for 1fase")

                    I=float(input("Ampere(A): "))
                    Pho=float(input("Resistivitet(ρ): "))
                    L=float(input("Lengde(m): "))
                    Cos=float(input("Cosφ: "))
                    A=float(input("Areal(A): "))

                    ans1=(I*Pho*L*2*Cos)
                    ans2=(ans1/A)
                    print("{}{}".format(ans2, "V"))
                    print("""
--------------------------------------------------------------------------
""")

#Utregning for Spenningsfall - 1fase
#-------------------------------------------------------------------------------------------------------------------

                if spen=="DU%":

                    U=float(input("Spenningsfall(V): "))
                    A=float(input("Tverrsnitt(A): "))

                    ans1=(U*100)
                    ans2=(ans1/A)
                    print("{}{}".format(ans2, "%"))
                    print("""
--------------------------------------------------------------------------
""")

#Utregning for Spenningsfall - ΔU%
#-------------------------------------------------------------------------------------------------------------------

            if liste=="Tversnitt":
                tver=input("Velg hva du leter etter; 3fase, 2fase eller 1fase")

#Søkeord 'Tversnitt' gir deg mulighet til å regne Amin
#-------------------------------------------------------------------------------------------------------------------

                if tver=="3fase":

                    Ib = float(input("Belastningsstrøm(A): "))
                    Pho = float(input("Resistivitet(ρ): "))
                    L = float(input("Lengde(m): "))
                    Cos = float(input("Cosφ: "))
                    Du = float(input("Spenningsfall(ΔV): "))

                    ans1=(Ib*1.732050807568877*Pho*L*Cos)
                    ans2=(ans1/Du)
                    print("{}{}".format(ans2, "V"))
                    print("""
--------------------------------------------------------------------------
""")

#Utregning av 3fase - Minste tversnitt
# -------------------------------------------------------------------------------------------------------------------

                if tver == "2fase":
                    Ib = float(input("Belastningsstrøm(A): "))
                    Pho = float(input("Resistivitet(ρ): "))
                    L = float(input("Lengde(m): "))
                    Cos = float(input("Cosφ: "))
                    Du = float(input("Spenningsfall(ΔV): "))

                    ans1 = (Ib * 2* Pho * L * Cos)
                    ans2 = (ans1 / Du)
                    print("{}{}"(ans2,"V"))
                    print("""
--------------------------------------------------------------------------
""")

# Utregning av 3fase - Minste tversnitt
# -------------------------------------------------------------------------------------------------------------------

                else:
                    print("""
=====================================================
Det ser ut som du har skrevet ordet feil. Prøv igjen!
=====================================================
""")

#Melding som kommer opp hvis du har skrevet en kode feil
#-------------------------------------------------------------------------------------------------------------------              

else:
    print("-----------------------------------------------------------------------------")
    print("Access Denied")
    print("-----------------------------------------------------------------------------")

#Alt under her vil ikke være passord beskyttet
#-------------------------------------------------------------------------------------------------------------------