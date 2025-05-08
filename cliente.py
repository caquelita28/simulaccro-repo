import requests
import json



def main():
        # Realizar la petición GET a la API
        respuesta = requests.get("http://192.168.1.16:8080")
        datos = respuesta.text
        print(datos)
        return datos

if __name__ == '__main__':
    main()