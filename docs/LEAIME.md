# Zé Delivery - Desafio QA 

**O primeiro desafio é identificar 3 importantes fluxos para o aplicativo continuar funcionando. Eu identifiquei esses:**

- **Informar endereço:** Se o usuário não conseguir inserir o endereço não saberá se o serviço do Zé Delivery está disponível na região. E se estiver disponível, também não conseguirá ver os produtos, porque os produtos são ofertados de acordo com a cobertura atendida na região. 

- **Pagamento:** Se os serviços de pagamento estiverem fora do ar, a compra não é concluída e assim o pedido não é submetido. 


- **Carrinho:** Caso os produtos selecionados pelo usuário não estiverem sendo atualizados e calculados corretamente, trará grandes transtornos para o usuário que pode desistir da compra. 


**O segundo desafio é criar uma automação com algum dos cenários do primeiro desafio**

- Eu escolhi o do carrinho de compras!

![](https://media.giphy.com/media/H4QootsmfwZ6iEJUQ0/giphy.gif)


# Instalação do projeto:
Sistema operacional utilizado:

- Ubuntu 18.04

***

1. **Criar ambientes isolados com Pyenv**

    Eu prefiro criar ambientes isolados, para não causar danos ao python local, então separei dois passo a passo para ajudar. Mas sinta-se à vontade para fazer do seu jeito!

    [How To - virtualenv](https://gist.github.com/Geoyi/d9fab4f609e9f75941946be45000632b)

    [How To - pyenv-virtualenv](https://www.liquidweb.com/kb/how-to-install-pyenv-virtualenv-on-ubuntu-18-04/)


2. **Clone o repo do projeto**

 ```sh
 git clone git@github.com:thamyresmoraes/Ze-delivery.git`
```

***
3. **Acesse a pasta**

```sh
cd ze-challenge`
```

***

4. **Instale e crie um ambiente isolado com pyenv**
```sh 
pyenv install 3.8.5
```

```sh
pyenv virtualenv 3.8.5 ze-test
```

```sh
pyenv activate ze-test
```


***

5. **Instale as depências**

```sh
 pip install -r requirements.txt
```

# Rode os testes

**UI**

 `~\ze-challenge\ui-automation`

```bash 
    robot -v BROWSER:Chrome -i update_value -d target features
```


    
 **API**
 
 `~/ze-challenge/behave_api__test/features`

   `behave -t @previsao_do_tempo`
   
   `behave -t @consultar_cidade`

