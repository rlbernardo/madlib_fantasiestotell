# importando o módulo
from tkinter import *

# Inicialização da Janela do mid lab no windows
root = Tk()
root.geometry('500x500')
root.title('DataFlair-Mad Libs Generator')
Label(root, text='Gerador de MAD LIBS \n Divirta-se!', font='arial 25 bold').pack()
Label(root, text='Escolha um e clique :', font='arial 20 bold').place(x=40, y=80)

################Fantasias##############

def madlib1_divagando():
    nome = input('diga me seu nome : ') #Roberta
    profissão_ou_ocupação = input('coloque sua profissão ou ocupação: ') #desenvolvedora python
    hobbie1 = input('Me diga um hobbie favorito: ') #jogar valorant
    hobbie2 = input('me diga um hobbie que não é frequente: ') #desenhar
    esporte_radical = input('coloque um esporte radical: ')
    algo_nojento = input('me diga algo que te deixa enjoado ou que você acha nojento: ')
    sentimento_ruim = input('me diga uma sentimento ruim:')
    personagem_fictício1 = input('Me diga um personagem de filme que você admira: ')
    personagem_fictício2 = input('Me diga um cantor(a) famoso: ')
    disciplina_escolar = input('Me diga sua disciplina da escola/faculdade que reprovou ou não ficou na média: ')
    lugar_no_mundo = input('Um lugar no mundo que queira conhecer: ')
    banda_musical1 = input('me diga uma banda musical que não goste: ')
    roupa_inutil = input('Agora me diga uma peça de roupa que você acha inútil: ')
    cdca = input('Escolha apenas um: "comer, dormir, amar ou casar"?: ')
    eco_her_ven = input('Escolha apenas um: "economia, herança ou venda: ')
    ato1 = input('Praia ou Mar: ')
    ato2 = input('Me diga algo de constrangedor que já fez na frente de alguém: ')
    figura_pub_fem = input('Me diga uma mulher que seja famosa')
    escolha1 = input('Escolha um: "avião, carro, ônibus ou navio?": ')
    pet = input('nome do seu pet: ')
    final = input('Quando vc assiste um filme, você prefere "um final trágico", "um final feliz" ou "Continua": ')
    print(
        'Meu nome é' + nome + ', sou' + profissão_ou_ocupação + 'e gosto de' + hobbie1 + 'e' + hobbie2 + 'às vezes. Posso dizer com precisão que a minha vida é perfeita, mas sinto a necessidade de fazer algo a mais, algo como: ' + esporte_radical + 'ou' + algo_nojento + 'mas fico com' + sentimento_ruim + 'de sair me aventuranto e me esbarrar com o(a)' + personagem_fictício1 + 'e acabe tendo que aprender ' + disciplina_escolar + 'em' +lugar_no_mundo + 'ao som de' + banda_musical1 + 'usando apenas' + roupa_inutil + ', aí vou acabar desistindo antes mesmo de ter tentando me aventurar. Mas quer saber, eu vou' + cdca + 'muito, mas talvez eu me arrependa, porém vai valer a pena quando eu sair por ai e poder usufrui de toda a minha' + eco_her_ven + ' que adquiri no ' + ato1 + 'depois que eu' + ato2 + 'da' + figura_pub_fem + 'enquanto ela fazia algo vergonhoso que eu não posso mencionar, mas foi engraçado. Portanto, irei comprar as minhas passagens para ir de ' + escolha1 + 'viver com a tribo que batizei de ' + pet + 'e isso é um ' + final +
    )

root.mainloop()