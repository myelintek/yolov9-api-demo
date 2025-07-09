
## Build image

```
docker build -t yolov9-api .
```

## Run API

```
docker run --rm -p 8000:8000 yolov9-api
```

## demo invoke
```
(echo -n '{"image": "'; base64 ~/image.jpg; echo '"}') | curl -H "Content-Type: application/json" -d @- http:/
/localhost:8080/invoke
```
