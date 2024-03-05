"""conseguir html de cualquier pagina"""
import requests

if __name__ == "__main__":
    url="http://192.168.0.50:8080/share/page"
    response=requests.get(url)
    
    if response.status_code==200:
        print(response.content)
