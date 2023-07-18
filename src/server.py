import uvicorn
import time
import threading
from src.main.config.app import app
from src.scrapper.extractor import Extractor

def server():
    uvicorn.run(app=app, host='127.0.0.1', port=8000, reload=False)

def scrapping():
    while True:
        extractor = Extractor()
        extractor.extract()
        
        time.sleep(60)

def main():
    threading.Thread(target=server).start()
    threading.Thread(target=scrapping).start()

if __name__ == '__main__':
    main()
