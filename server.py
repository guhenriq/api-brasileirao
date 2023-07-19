import uvicorn
import time
import threading
from src.main.config.app import app
from src.scrapper.extractor import Extractor

def server():
    uvicorn.run(app=app, host='127.0.0.1', port=8000, reload=False)

def scrapping():
    while True:
        try:
            extractor = Extractor()
            extractor.extract()
            
        except Exception as e:
            print(e)
        finally:
            time.sleep(60)

def main():
    thread_server = threading.Thread(target=server)
    thread_server.start()

    thread_scrapping = threading.Thread(target=scrapping)
    thread_scrapping.daemon = True
    thread_scrapping.start()

if __name__ == '__main__':
    main()
