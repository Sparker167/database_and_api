# Project 3

### Launch containers

- To launch database, api and container for populate database
```
docker-compose up -d
```

### Use API

Our api contains 3 routes


 - **/status** : To get the api status

 ```{bash}
 curl GET 'http://18.202.19.114:5000/status
 ```

- **/getpokemon/myType** : To get all pokemon where `Type 1` is myType where myType is one of **(_Water_, _Grass_, _Fire_,  _Ground_, _Fairy_, _Normal_, _Fighting_, _Poison_, _Bug_)**

 ```{bash}
 curl GET 'http://18.202.19.114:5000/getpokemon/Grass
 ```

- **/createpokemon** : To Insert a new pokemon in the database
```{bash}
curl --location --request POST 'http://18.202.19.114:5000/createpokemon' --header 'Content-Type: application/json' --data-raw '{"num":"589", Name":"pokOCI", Type1":"Genie"}'
```