# Desafio de back-end utilizando Python/Django

## Navedex API

### O Desafio:
Implementar uma API padrão RESTful utilizando Django, para o sistema navedex's

###Dependência:
<ul>[Docker](https://www.docker.com/get-started)

###Instalação:
1 - Iniciar os componentes da stack do projeto.

```sh 
docker-compose up
```
Nesse ponto você deve ter o projeto Django executando na porta 8000
http://localhost:8000

2 - Executar as migrações.:
```sh
docker-compose run web python manage.py migrate
```
3 - (opcional) Executer testes
```sh
docker-compose run web python manage.py test
```

###Implementações:

* Autenticação, cadastro e login
* Gerenciamento de Navers
* Gerenciamento de Projetos

Todas as urls e formato de objetos que devem ser enviados para api estão na documentação, utilizada Postman aqui(https://documenter.getpostman.com/view/9411050/T1LMin72?version=latest)



    