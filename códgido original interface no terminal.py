import funcoes

print ("{} ATENÇÂO {}".format("-="*20,"-="*20))
funcoes.baba()

baba = int(input("Existe uma feitura de Babalorixá na camarinha (contando com você): "))


while baba < 1 or baba > 2:
    print("Resposta Inválida, por favor tente novamente")
    baba = int(input("Existe uma feitura de Babalorixá na camirinha (contando com você): "))


amalaOxóssi = 0
amalaOgum = 0
amalaOxalá = 0
amalaXango = 0
amalaObaluae = 0
amalaIemanjá = 0
amalaOxum = 0
amalaIansa = 0
amalaNanã = 0


criação_oxossi = 0
criação_ogum = 0
criação_oxala = 0
criação_xango = 0
criação_obaulae = 0
criação_iemanja = 0
criação_oxum = 0
criação_iansa = 0
criação_nana = 0
criação_pg = 0
criação_exu = 0
criação_almas = 0


funcoes.lin()
funcoes.santos()
funcoes.lin()

primeiro = 'n/a'
segundo = 'n/a'

resp1 = int(input("Digite seu Santo de Frente: "))

while resp1 < 1 or resp1 > 9:
    print("Resposta Inválida, por favor tente novamente")
    resp1 = int(input("Digite seu Santo de Frente: "))

if resp1 == 1:
    amalaOxóssi += 1
    criação_oxossi += 1
elif resp1 == 2:
    amalaOgum += 1
    criação_ogum += 1
elif resp1 == 3:
    amalaOxalá += 1
    criação_oxala += 1
elif resp1 == 4:
    amalaXango += 1
    criação_xango += 1
elif resp1 == 5:
    amalaObaluae += 1
    criação_obaulae += 1
elif resp1 == 6:
    amalaIemanjá += 1
    criação_iemanja += 1
elif resp1 == 7:
    amalaOxum += 1
    criação_oxum += 1
elif resp1 == 8:
    amalaIansa += 1
    criação_iansa += 1
elif resp1 == 9:
    amalaNanã += 1
    criação_nana += 1

if 1 <= resp1 <= 5:
    generoprimeiro = "homem"
else:
    generoprimeiro = "mulher"

funcoes.lin()

santos_dict = {
    1: "oxossi",
    2: "ogum",
    3: "oxala",
    4: "xango",
    5: "obaluae",
    6: "iemanja",
    7: "oxum",
    8: "iansa",
    9: "nana"
}

primeiro = santos_dict.get(resp1, "n/a")

resp2 = -1

if generoprimeiro == "homem":
    funcoes.lin()
    funcoes.santamulher()
    funcoes.lin()
    resp2 = int(input("Digite seu Segundo Santo: "))
    while resp2 < 6 or resp2 > 9:
        print("Resposta Inválida, por favor tente novamente")
        resp2 = int(input("Digite seu Segundo(a) Santo(a): "))

elif generoprimeiro == "mulher":
    funcoes.lin()
    funcoes.santohomen()
    funcoes.lin()
    resp2 = int(input("Digite seu Segundo(a) Santo(a): "))
    while resp2 < 1 or resp2 > 4:
        print("Resposta Inválida, por favor tente novamente")
        resp2 = int(input("Digite seu Segundo(a) Santo(a): "))

segundo = santos_dict.get(resp2, "n/a")

if resp2 == 1:
    amalaOxóssi += 1
    criação_oxossi += 1
elif resp2 == 2:
    amalaOgum += 1
    criação_ogum += 1
elif resp2 == 3:
    amalaOxalá += 1
    criação_oxala += 1
elif resp2 == 4:
    amalaXango += 1
    criação_xango += 1
elif resp2 == 5:
    amalaObaluae += 1
    criação_obaulae += 1
elif resp2 == 6:
    amalaIemanjá += 1
    criação_iemanja += 1
elif resp2 == 7:
    amalaOxum += 1
    criação_oxum += 1
elif resp2 == 8:
    amalaIansa += 1
    criação_iansa += 1
elif resp2 == 9:
    amalaNanã += 1
    criação_nana += 1

funcoes.lin()

print(f"seu primeiro santo é {primeiro}")
print(f"seu segundo santo é {segundo}")
print(f"você é de santo(a) {generoprimeiro}")

funcoes.lin()
print ("Qual os Orixás do seu Pai/Mãe de santo?")
funcoes.santos()
paiprimeiro = int(input("Qual o primeiro santo do seu pai/mãe de santo?"))



while paiprimeiro < 1 or paiprimeiro > 9:
    funcoes.lin()
    print("Resposta Inválida, por favor tente novamente")
    casa = int(input("Qual o primeiro santo do seu pai/mãe de santo?"))

if paiprimeiro == 1:
    amalaOxóssi += 1
    criação_oxossi += 1
elif paiprimeiro == 2:
    amalaOgum += 1
    criação_ogum += 1
elif paiprimeiro == 3:
    amalaOxalá += 1
    criação_oxala += 1
elif paiprimeiro == 4:
    amalaXango += 1
    criação_xango += 1
elif paiprimeiro == 5:
    amalaObaluae += 1
    criação_obaulae += 1
elif paiprimeiro == 6:
    amalaIemanjá += 1
    criação_iemanja += 1
elif paiprimeiro == 7:
    amalaOxum += 1
    criação_oxum += 1
elif paiprimeiro == 8:
    amalaIansa += 1
    criação_iansa += 1
elif paiprimeiro == 9:
    amalaNanã += 1
    criação_nana += 1


generopaimae = "n/a"

if 1 <= paiprimeiro <= 5:
    generopaimae = "homem"
else:
    generopaimae = "mulher"

if generopaimae == "homem":
    funcoes.lin()
    funcoes.santamulher()
    funcoes.lin()
    paisegundo = int(input("Digite o Segundo Santo do seu pai/mae de santo: "))
    while paisegundo < 6 or paisegundo > 9:
        print("Resposta Inválida, por favor tente novamente")
        paisegundo = int(input("Digite o Segundo Santo do seu pai/mae de santo: "))


elif generopaimae == "mulher":
    funcoes.lin()
    funcoes.santohomen()
    funcoes.lin()
    paisegundo = int(input("Digite seu Segundo(a) Santo(a): "))
    while paisegundo < 1 or paisegundo > 5:
        print("Resposta Inválida, por favor tente novamente")
        paisegundo = int(input("Digite o Segundo(a) Santo(a) dele(a): "))

if paisegundo == 1:
    amalaOxóssi += 1
    criação_oxossi += 1
elif paisegundo == 2:
    amalaOgum += 1
    criação_ogum += 1
elif paisegundo == 3:
    amalaOxalá += 1
    criação_oxala += 1
elif paisegundo == 4:
    amalaXango += 1
    criação_xango += 1
elif paisegundo == 5:
    amalaObaluae += 1
    criação_obaulae += 1
elif paisegundo == 6:
    amalaIemanjá += 1
    criação_iemanja += 1
elif paisegundo == 7:
    amalaOxum += 1
    criação_oxum += 1
elif paisegundo == 8:
    amalaIansa += 1
    criação_iansa += 1
elif paisegundo == 9:
    amalaNanã += 1
    criação_nana += 1

funcoes.lin()
funcoes.feituras()
funcoes.lin()
feitura = int(input("Digite qual feitura será feita?: "))
while feitura < 1 or feitura > 4:
    print("Resposta Inválida, por favor tente novamente")
    feitura =  int(input("Digite qual feitura será feita?: "))



funcoes.lin()

if feitura == 1:
    amalaOxóssi += 1
    amalaOgum += 1
    amalaOxalá += 1
    amalaXango += 1
    amalaObaluae += 1
    amalaIemanjá += 1
    amalaOxum += 1
    amalaIansa += 1
    amalaNanã += 1

elif feitura == 2:
    amalaOxóssi += 1
    criação_oxossi += 1
    amalaOgum += 1
    criação_ogum += 1
    amalaOxalá += 1
    criação_oxala += 1
    amalaXango += 1
    criação_xango += 1
    amalaObaluae += 1
    criação_obaulae += 2
    amalaIemanjá += 1
    criação_iemanja += 1
    amalaOxum += 1
    criação_oxum += 1
    amalaIansa += 1
    criação_iansa += 1
    amalaNanã += 1
    criação_nana += 1
    criação_pg += 2
    criação_exu += 2
    criação_almas += 1

elif feitura == 3:
    if baba == 2:
        amalaOxóssi += 1
        criação_oxossi += 1
        amalaOgum += 1
        criação_ogum += 1
        amalaOxalá += 1
        criação_oxala += 1
        amalaXango += 1
        criação_xango += 1
        amalaObaluae += 1
        criação_obaulae += 2
        amalaIemanjá += 1
        criação_iemanja += 1
        amalaOxum += 1
        criação_oxum += 1
        amalaIansa += 1
        criação_iansa += 1
        amalaNanã += 1
        criação_nana += 1
        criação_pg += 2
        criação_exu += 2
        criação_almas += 1

funcoes.lin()

print("Esses são os amalás que você deverá servir:")
print(f"Amalá de Oxóssi: {amalaOxóssi}")
print(f"Amalá de Ogum: {amalaOgum}")
print(f"Amalá de Oxalá: {amalaOxalá}")
print(f"Amalá de Xangô: {amalaXango}")
print(f"Amalá de Obaluae: {amalaObaluae}")
print(f"Amalá de Iemanjá: {amalaIemanjá}")
print(f"Amalá de Oxum: {amalaOxum}")
print(f"Amalá de Iansa: {amalaIansa}")
print(f"Amalá de Nanã: {amalaNanã}")
funcoes.lin()


if feitura == 1:
    print("Na Feitura de oburi não se serve criações!")

    if baba == 1:
        funcoes.lin()
        print ("Esses são os santos que você deverá dar: ")
        print(f"Criação de Exu: {criação_exu}")
        print(f"Criação de Pomba Gira: {criação_pg}")
        if resp1 == 1:
            print(f"Criação de Oxóssi: {criação_oxossi}")
        elif resp1 == 2:
            print(f"Criação de Ogum: {criação_ogum}")
        elif resp1 == 3:
            print(f"Criação de Oxalá: {criação_oxala}")
        elif resp1 == 4:
            print(f"Criação de Xangô: {criação_xango}")
        elif resp1 == 5:
            print(f"Criação de Obaluae: {criação_obaulae}")
        elif resp1 == 6:
            print(f"Criação de Iemanjá: {criação_iemanja}")
        elif resp1 == 7:
            print(f"Criação de Oxum: {criação_oxum}")
        elif resp1 == 8:
            print(f"Criação de Iansa: {criação_iansa}")
        elif resp1 == 9:
            print(f"Criação de Nanã: {criação_nana}")
        if resp2 == 1:
            print(f"Criação de Oxóssi: {criação_oxossi}")
        elif resp2 == 2:
            print(f"Criação de Ogum: {criação_ogum}")
        elif resp2 == 3:
            print(f"Criação de Oxalá: {criação_oxala}")
        elif resp2 == 4:
            print(f"Criação de Xangô: {criação_xango}")
        elif resp2 == 5:
            print(f"Criação de Obaluae: {criação_obaulae}")
        elif resp2 == 6:
            print(f"Criação de Iemanjá: {criação_iemanja}")
        elif resp2 == 7:
            print(f"Criação de Oxum: {criação_oxum}")
        elif resp2 == 8:
            print(f"Criação de Iansa: {criação_iansa}")
        elif resp2 == 9:
            print(f"Criação de Nanã: {criação_nana}")
        if paiprimeiro == 1:
            print(f"Criação de Oxóssi: {criação_oxossi}")
        elif paiprimeiro == 2:
            print(f"Criação de Ogum: {criação_ogum}")
        elif paiprimeiro == 3:
            print(f"Criação de Oxalá: {criação_oxala}")
        elif paiprimeiro == 4:
            print(f"Criação de Xangô: {criação_xango}")
        elif paiprimeiro == 5:
            print(f"Criação de Obaluae: {criação_obaulae}")
        elif paiprimeiro == 6:
            print(f"Criação de Iemanjá: {criação_iemanja}")
        elif paiprimeiro == 7:
            print(f"Criação de Oxum: {criação_oxum}")
        elif paiprimeiro == 8:
            print(f"Criação de Iansa: {criação_iansa}")
        elif paiprimeiro == 9:
            print(f"Criação de Nanã: {criação_nana}")
        if paisegundo == 1:
            print(f"Criação de Oxóssi: {criação_oxossi}")
        elif paisegundo == 2:
            print(f"Criação de Ogum: {criação_ogum}")
        elif paisegundo == 3:
            print(f"Criação de Oxalá: {criação_oxala}")
        elif paisegundo == 4:
            print(f"Criação de Xangô: {criação_xango}")
        elif paisegundo == 5:
            print(f"Criação de Obaluae: {criação_obaulae}")
        elif paisegundo == 6:
            print(f"Criação de Iemanjá: {criação_iemanja}")
        elif paisegundo == 7:
            print(f"Criação de Oxum: {criação_oxum}")
        elif paisegundo == 8:
            print(f"Criação de Iansa: {criação_iansa}")
        elif paisegundo == 9:
            print(f"Criação de Nanã: {criação_nana}")
        funcoes.lin()
        print("Você deverá falar com outros irmãos recolhidos (caso houver), para se organizarem\n"
              " com as cirações ofecidas para os orixás da casa")
    elif baba == 2:
        print("Essas são as criações que você deverá dar:")
        print(f"Criação de Oxóssi: {criação_oxossi}")
        print(f"Criação de Ogum: {criação_ogum}")
        print(f"Criação de Oxalá: {criação_oxala}")
        print(f"Criação de Xangô: {criação_xango}")
        print(f"Criação de Obaluae: {criação_obaulae}")
        print(f"Criação de Iemanjá: {criação_iemanja}")
        print(f"Criação de Oxum: {criação_oxum}")
        print(f"Criação de Iansa: {criação_iansa}")
        print(f"Criação de Nanã: {criação_nana}")
        print(f"Criação de Exu: {criação_exu}")
        print(f"Criação de Pomba Gira: {criação_pg}")
        print(f"Criação de Santa Almas: {criação_almas}")
    funcoes.lin()
    print("Você deverá falar com outros irmãos recolhidos (caso houver), para se organizarem\n"
            " com as cirações ofecidas para os orixás da casa")



else:
    print("Essas são as criações que você deverá dar:")
    print(f"Criação de Oxóssi: {criação_oxossi}")
    print(f"Criação de Ogum: {criação_ogum}")
    print(f"Criação de Oxalá: {criação_oxala}")
    print(f"Criação de Xangô: {criação_xango}")
    print(f"Criação de Obaluae: {criação_obaulae}")
    print(f"Criação de Iemanjá: {criação_iemanja}")
    print(f"Criação de Oxum: {criação_oxum}")
    print(f"Criação de Iansa: {criação_iansa}")
    print(f"Criação de Nanã: {criação_nana}")
    print(f"Criação de Exu: {criação_exu}")
    print(f"Criação de Pomba Gira: {criação_pg}")
    print(f"Criação de Santa Almas: {criação_almas}")

funcoes.lin()
