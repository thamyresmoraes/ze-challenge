# Zé Delivery - QA Challenge

Você pode ler esta documentação, em português,
[clicando aqui](docs/LEIAME.md)

**The first challenge is identity 3 important flows that keep the application working properly. I've identified these:**

- **Inform Address:** If the user can't enter address, he will not know if the Zé delivery service will be available in his region. And if it's available, the products will not be displayed in this case, because they are displayed to the user according to the coverage served in the region. 

-  **Payment:** If the payment services has unavailabe, the purchase can't be completed and the order can't be created. 

- **Cart:** If the products selected by the user are not being updated and calculated correctly in the cart, it will cause inconvenience for the user who can withdraw from the purchase. 

**The second challenge is create an automation test to a scenario from the first challenge**

I chose the cart!


![](https://media.giphy.com/media/H4QootsmfwZ6iEJUQ0/giphy.gif)
 

# Installing the Project
This mode are configured for the following OS only:

- Ubuntu 18.04

***


1. **Creating virtual environments with Pyenv**

    I prefer to create an isolated environment, so as not to cause any damage to the local python, so I separated two tutorials to help. But feel free to do it your way.

    [How To - virtualenv](https://gist.github.com/Geoyi/d9fab4f609e9f75941946be45000632b)

    [How To - pyenv-virtualenv](https://www.liquidweb.com/kb/how-to-install-pyenv-virtualenv-on-ubuntu-18-04/)


***

2. **Clone this repository**

 ```sh
 git clone git@github.com:thamyresmoraes/Ze-delivery.git`
```

***
3. **Go to project folder**

```sh
cd ze-challenge`
```

***

4. **Install and create virtualenv**
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

3. **Install dependencies**

```sh
 pip install -r requirements.txt
```

# Run tests

**UI**

 `~\ze-challenge\ui-automation`

```bash 
    robot -v BROWSER:Chrome -i update_value -d target features
```


    
 **API**
 `~/Ze-challenge/behave_api__test/features`

   `behave -t @previsao_do_tempo`
   
   `behave -t @consultar_cidade`
