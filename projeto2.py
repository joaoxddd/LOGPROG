
tabelaVerdade = []


def criarformula(choques):
    formula = []
    formulaAux = []

    formula = ['¬', [choques[0][0], '^', choques[0][1]]]
    if len(choques) == 1:
        return formula
    else:
        i = 1
        while i < len(choques):
            formulaAux = ['¬', [choques[i][0], '^', choques[i][1]]]
            formula = [formulaAux, '^', formula]
            i += 1
        return formula


def valorVerdadeBemEspecifico(formula, truth):
    x = valor_verdade(formula, truth)
    return x


def valor_verdade(phi, verdade):
    x = int(phi)
    if x.isnumeric():
        return verdade[phi]
    if phi[0] == '¬':
        return not valor_verdade(phi[1], verdade)
    if type(phi[1]) == str:
        if phi[1] == '^':
            return valor_verdade(phi[0], verdade) and valor_verdade(phi[2], verdade)
        if phi[1] == 'v':
            return valor_verdade(phi[0], verdade) or valor_verdade(phi[2], verdade)
        if phi[1] == '>':
            if valor_verdade(phi[0], verdade) == True and valor_verdade(phi[2], verdade) == False:
                return False
            else:
                return True


# Função para gerar uma tabela verdade (número de variáveis da tabela(fixo), número de variáveis da tabela(recursivo))
def geraTabelaVerdade(m, n):
    bits = 2**m  # determina quantos linhas terá a tabela, valor fixo
    repeticoes_coluna = (bits//(2**n))*2
    repeticoes_linha = (2**n//2)//2
    contador = 0  # Esse contador será sempre incrementado até a quantidade de bits e será zerado quando a função repetir
    if not tabelaVerdade:  # essa condição cria a primeira coluna da tabela
        for i in range(bits // 2):
            tabelaVerdade.append('0')
            i += 1
        for i in range(bits // 2):
            tabelaVerdade.append('1')
    for j in range(repeticoes_coluna):
        for i in range(repeticoes_linha):
            tabelaVerdade[contador] = tabelaVerdade[contador] + '0'
            contador += 1
        for i in range(repeticoes_linha):
            tabelaVerdade[contador] = tabelaVerdade[contador] + '1'
            contador += 1
        j += 1
    if n == 1:
        return tabelaVerdade
    else:
        return geraTabelaVerdade(m, n-1)


def makeTruth(numeroDeAtomicas):
    tabelaAux = geraTabelaVerdade(numeroDeAtomicas, numeroDeAtomicas)
    indice = {}
    auxIndice = []
    dicionario = []
    for j in range(len(tabelaAux)):
        for k in range(numeroDeAtomicas):
            if tabelaAux[j][k] == '0':
                auxIndice = ({str(k+1): False})
                indice = {**indice, **auxIndice}
            else:
                auxIndice = ({str(k+1): True})
                indice = {**indice, **auxIndice}
            if k == numeroDeAtomicas-1:
                dicionario.append(indice)
    return dicionario


def satisfativel(numeroAtomicas):
    contadorInsatisfativel = 0
    interpretacoes = makeTruth(numeroAtomicas)
    for i in range(len(interpretacoes)):
        #formula = criarformula(choques)
        formula = [['1', '^', '2'], '>', ['3', 'v', '4']]
        y = valorVerdadeBemEspecifico(formula, interpretacoes[i])
        
        # Para Solucionar a satisfabilidade de outras formulas, basta, aqui, apresentar a formula
        # seguindo a modelagem proposta neste codigo Exemplo: ([['p', '^', 'q'], 'v', [['s', 'v', 'r'], 'v', ['s', '^', 'p']]])
        # os parenteses são subtituidos por colchetes, pois a hierarquia da formula é respeita com base no colchete
        # alem disso, os conectivos basicos em String são : '^'==AND, 'v'==OR, '¬'==NOT, '>'==IMPLIES
        if y == True:
            print('A interpretacao é satisfatível >>>', interpretacoes[i])
            contadorInsatisfativel = contadorInsatisfativel + 1
    if contadorInsatisfativel == 0:
        print('a formula não possui interpretacao que satisfaca, logo e insatisfativel')
    return

def validaCNF(formula):
    contador = 0
    clausula = []
    for i in range (len(formula)):
        clausula = formula[i]
        for j in range (len(clausula)):
            for k in range (len(clausula)):
                if clausula [j] == clausula [k] and k!=j:
                    if clausula [k-1] == '¬':
                        contador = contador + 1
    if contador == len(formula):
        print("e valida")
        return
    print("não e valida")
    return


numeroAtomicas = 4

choques = [['1', '2'], ['3', '4']]
satisfativel(numeroAtomicas)

#formula = [['1', 'v', '2','v','¬','2'], ['3', 'v', '4','v','¬','4'], ['3','v','¬','3']]
#formula = [['1', 'v', '2'], ['3', 'v', '4','v','¬','4'], ['3','v','¬','3']]
#validaCNF(formula)
