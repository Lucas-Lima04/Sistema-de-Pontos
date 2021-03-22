# Sistema-de-Pontos

Este projeto é um estudo sobre como melhorar o uso de um sistema legado de marcação de pontos com tempo de resposta muito longo. Apartir deste cenário foi desenvolvida uma API que, recebe o registro de ponto do usuário, salva em um banco de dados e retorna o status da ação ao mesmo tempo em que inicia uma rotina de enviar todos as requisições salvas nesse banco para o sistema legado, terceirizando assim o tempo de resposta e tornando o uso mais agradável.

## Como rodar?

Para rodar a aplicação é necessário baixar o repositório, certificar-se de ter as bibliotecas instaladas e rodar no terminal o comando "python app.py"

É possível também configurar seu próprio banco de dados, alterando as informações de conexão e o conector, caso utilize um diferente do MySQL.

![image](https://user-images.githubusercontent.com/55767971/111976859-df624980-8ae0-11eb-9c05-04802ab4abed.png)
