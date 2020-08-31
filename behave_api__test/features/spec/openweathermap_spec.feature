#language: pt

@test
Funcionalidade: Previsão do tempo

@previsao_do_tempo
Esquema do Cenário: Previsão do tempo
    Dado que sou usuário
    Quando eu requisitar a previsao do tempo da através do "<ID>" da cidade
    Então o serviço deve retornar status code "200"

    Exemplos: 
    |ID|
    |6323121|
    |3448433|
    |3471168|

@consultar_cidade
Esquema do Cenário: Consultar a cidade 
    Dado que sou usuário
    Quando eu requisitar a previsao do tempo da através do "<ID>" da cidade
    Então o serviço deve retornar a "<cidade>" consultada

    Exemplos: 
    |ID|cidade|
    |6323121|Florianopolis|
    |3448433|Sao Paulo|
    |3471168|Bahia|


