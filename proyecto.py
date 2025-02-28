import requests
import json
import pandas as pd

def app(event, context): #el nombre debe considir con el settings
	
	print("Evento recibido desde s3")
	print('Se cargo el archivo ', event)