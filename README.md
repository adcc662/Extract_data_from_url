# URL y extraer datos
Genera un servicio que tenga la capacidad de recibir una URL como parámetro de
entrada y extraer los productos formateados de la página web, se tomará cualquier
url del menú del sitio para obtener los productos.

## Tecnologias usadas   
- **Beautiful Soup Python**
- **Docker**

## Comandos para correr la aplicación
```sh
git clone git@github.com:adcc662/Extract_data_from_url.git
cd Extract_data_from_url
docker build -t product-extractor .
docker run -p 8000:8000 product-extractor
```

