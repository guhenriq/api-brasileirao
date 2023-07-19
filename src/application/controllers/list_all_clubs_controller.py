import pandas as pd

from fastapi.responses import JSONResponse


class ListAllClubsController:

    def handler(self):

        try:
            data = pd.read_csv('data.csv', sep=';', encoding='latin1')

            clubes = []

            for idx, clube in data['Clube'].items():
                clubes.append({
                    'id': idx,
                    'clube': clube
                })
            
            return JSONResponse(content={'data': clubes}, status_code=200)
        
        except:
            return JSONResponse(content={'msg': 'ocorreu um erro inesperado'}, status_code=400)

        

