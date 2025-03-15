import requests
import os

download_uris = [
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2018_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q2.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q3.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2020_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2220_Q1.zip",
]

def create_downloads_dir():
    download_dir = "downloads"
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)
    return download_dir

def download_file(url, download_dir):
    filename = url.split("/")[-1]  
    file_path = os.path.join(download_dir, filename)
    
    try:
        print(f"Baixando {filename}...")
        response = requests.get(url)
        response.raise_for_status() 
        with open(file_path, 'wb') as file:
            file.write(response.content)
        print(f"{filename} baixado com sucesso.")
        return file_path
    except requests.exceptions.RequestException as e:
        print(f"Erro ao baixar {filename}: {e}")
        return None


def main():
    download_dir = create_downloads_dir()
    print(f"A pasta 'downloads' foi criada em: {download_dir}")

    for url in download_uris:
        zip_file_path = download_file(url, download_dir)
        if zip_file_path:  
            print(f"Arquivo baixado em: {zip_file_path}")

if __name__ == "__main__":
    main()
import aiohttp
import asyncio
import os

download_uris = [
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2018_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q2.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q3.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2020_Q1.zip",
]

def create_downloads_dir():
    download_dir = "downloads"
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)
    return download_dir

async def download_file(session, url, download_dir):
    filename = url.split("/")[-1]
    file_path = os.path.join(download_dir, filename)
    
    async with session.get(url) as response:
        if response.status == 200:
            with open(file_path, 'wb') as file:
                file.write(await response.read())
            
