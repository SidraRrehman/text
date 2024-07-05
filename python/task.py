from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import requests

app = FastAPI()
url='https://freetestapi.com/api/v1/weathers'
response = requests.get(url)
data=response.json()
templates = Jinja2Templates(directory="html_directory")

@app.get("/")
def read_root(request: Request):
    cities = [{"city": item["city"], "id": item["id"]} for item in data]
    return templates.TemplateResponse("index.html", {"request": request, "cities": cities})

@app.get("/city/{city_name}", response_class= HTMLResponse)
def read_city(city_name:str , request: Request):
    city_data= next((item for item in data if item["city"].lower() == city_name.lower()) , None)
    if city_data:
      return templates.TemplateResponse("cities_details.html", {"request": request, "city_data": city_data})
    else:
        return templates.TemplateResponse("not found.html", {"request": request, "city_name": city_name})
    

@app.get("/details/",response_class= HTMLResponse)
def go_home(request:Request):
    return templates.TemplateResponse("home1.html",{"request":request,"cities":data})

   


