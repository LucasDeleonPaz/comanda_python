# **COMANDA - PYTHON**
Programa escrito para gerenciamento de comandas em restaurantes. O programa conta com 4 funções, sendo elas: Cadastro de produtos (pratos, bebidas e itens), Listagem dos produtos, Cadastro de consumo (lançando a mesa onde o consumo aconteceu e um dicionário com id do item e quantidade) e calculo de consumo (Recebe a mesa que se quer fechar e retorna o valor total à ser pago)

## SOBRE A UTILIZAÇÃO DO PROGRAMA
Ao rodar o programa **"main.py"**, o mesmo carrega uma lista de ações possíveis, pedindo para digitar um número que servirá para direcionar o programa para a função desejada. <br/>
    1 - Cadastrar um novo produto <br/>
    2 - Listar todos os produtos <br/>
    3 - Lançar consumo numa mesa <br/>
    4 - Valor total do consumo de uma mesa <br/>
    
Uma vez selecionando a ação, o programa direciona para as próximas ações, onde o mesmo pede informações que são necessárias para continuar a rodagem do mesmo, 
por exemplo, para cadastrar um produto, você deve informar o nome do produto e o preço do mesmo, assim, a função fica a cargo de montar o dicionário que ficará na base de dados.

## SOBRE A ORGANIZAÇÃO DO PROGRAMA
O mesmo fora organizado entre pastas, separando as funções e funcionalidades, setorizando cada parte do código, onde busco a organização e facilidade de manutenção posterior do mesmo.
Composto pela estrutura hierárquica que pode ser vista abaixo, busco orientar o código, deixando na **main.py** somente a chamada de cada função.<br/>

**ESTRUTURA HIERÁRICA**
  **MANAGEMENT**
    ╚ __init__.py
    ╚ tab_handler.py
  **UTILS**
    ╚ __init__.py
    ╚ json_handler.py
  .gitignore
  main.py
  menu.json
  tables.json
  
## MANAGEMENT
Pasta contendo 2 programas, sendo o **"__init__.py"** responsável por informar ao Python que se trata de uma "pacote" com módulos. E o programa **"tab_handler.py"** onde faço o cálculo final da comanda, retornando ao usuário um dicionário contendo o subtotal e a data da criação daquela comanda.

## UTILS
Pasta contendo 2 programas, sendo o **"__init__.py"** responsável por informar ao Python que se trata de uma "pacote" com módulos. E o programa **"json_handler.py"** que é responsável por gerenciar toda a abertura, alteração e consumo das informações de ambos os arquivos **".json"** contidos no programa.

## JSON - MENU
Arquivo que serve de base de dados dos produtos vendidos pela empresa. 

## JSON - TABLES
Arquivo que serve de base de dados para cadastro do que fora consumido, recebendo o nome da mesa onde se quer adicionar tal consumo e os produtos consumidos.
