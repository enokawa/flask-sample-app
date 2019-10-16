# flask-sample-app

```sh
$ export ENVIRONMENT="development"
$ docker-compose up -d --build
```

```sh
$ curl -s 0.0.0.0:5000 | jq
{
  "environment": "development",
  "message": "Hello, Flask!!"
}
```
