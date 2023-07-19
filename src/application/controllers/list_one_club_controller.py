import pandas as pd

from fastapi.responses import JSONResponse


class ListOneClubController:

    def handler(self, id: int):

        try:
            data = pd.read_csv('data.csv', sep=';', encoding='latin1')

            clubes = data['Clube']

            clube = clubes.loc[id]

            response = {
                'data': {
                    'id': id, 
                    'clube': clube
                }
            }

            return JSONResponse(content=response, status_code=200)

        except KeyError:
            response_error = {'msg': 'clube não encontrado'}
            return JSONResponse(content=response_error, status_code=404)
        except:
            return JSONResponse(content={'msg': 'ocorreu um erro inesperado'}, status_code=400)
