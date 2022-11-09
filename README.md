# PDF-Extractor
O objetivo central deste script é a extração de recursos variados de arquivos PDF

## Pontos importantes
É necessário diretórios de pdf's e de imagens, eles podem ser definidos manualmente criando-os e alterando os nomes após a `/` nas variáveis `workdir` e `output` dentro do script. Por padrão o script utilizará os diretórios `pdf` para leitura e `imagens` para output


## Criando o ambiente virtual
> Caso queira facilitar o processo, é possível utilizar o script `setup.sh` para criar e ativar o ambiente virtual padrão automaticamente (só para a primeira vez).  
> Para isso é possível rodar nativamente o script pelo Linux com o comando:
> ``` 
> ./setup.sh
> ``` 
> e no Windows através do terminal `Git Bash` com o comando:
> ``` 
> sh setup.sh
> ```

* Como boa prática de desenvolvimento é importante criar um ambiente virtual. Isso pode ser feito usando o seguite comando:
    ```
    python -m venv venv
    ```

* Para ativar o ambiente virtual, use um dos seguintes comandos para **Linux** ou **Windows** respectivamente:
    ```
    source venv/Scripts/activate
    ```
    ou
    ```
    ./venv/Scripts/activate
    ```
   > Esse passo precisa ser feito sempre que a máquina for reiniciada

* Com o ambiente virtual ativo, é o momento de instalar as dependências do script. Isso pode ser feito com o comando a seguir:
    ```
    pip install -r requirements.txt
    ```

## Execução
* Para rodar o script finalmente, execute o seguinte comando:
    ```
    python script.py
    ```