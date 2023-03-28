# URL y extraer datos
Genera un servicio que tenga la capacidad de recibir una URL como parámetro de
entrada y extraer los productos formateados de la página web, se tomará cualquier
url del menú del sitio para obtener los productos.

## Tecnologias usadas   
- **Beautiful Soup Python**
- **Docker**

## Comandos para correr la aplicación
```sh
git clone git@github.com:adcc662/Wallmart-Scrapy.git
cd Wallmart-scrapy
docker build -t walmart_menu .
docker run -v $(pwd):/app walmart_menu
```

