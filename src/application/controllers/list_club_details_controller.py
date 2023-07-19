import pandas as pd
import re

from fastapi.responses import JSONResponse


class ListClubDetailsController:

    def handler(self, id: int):

        try:
            data = pd.read_csv('data.csv', sep=';', encoding='latin1')

            clube = data.loc[id]
            
            rank_clube = self.normalize_rank(clube['Rank'])

            aproveitamento = self.calculate_aproveitamento(
                str(clube['PJPartidas jogadas']),
                str(clube['PtsPontos'])
            )

            details = {
                'id': id,
                'clube': str(clube['Clube']),
                'posicao': str(rank_clube['posicao']),
                'classificacao': str(rank_clube['classificacao']),
                'pontos': str(clube['PtsPontos']),
                'partidas': str(clube['PJPartidas jogadas']),
                'aproveitamento': str(aproveitamento),
                'vitorias': str(clube['VITVitórias']),
                'empates': str(clube['EEmpates']),
                'derrotas': str(clube['DERDerrotas']),
                'golsPros': str(clube['GMGols marcados']),
                'golsContra': str(clube['GCGols contra']),
                'saldoDeGols': str(clube['SGSaldo de gols'])
            }

            return JSONResponse(content={'data': details}, status_code=200)
        except:
            return JSONResponse(content={'msg': 'ocorreu um error inesperado'}, status_code=400)


    def normalize_rank(self, rank: pd.DataFrame): 
        if re.search(r'\d', rank):
            posicao_tabela = int(str(re.findall(r'\d+', rank)[0]).strip())

        if re.search(r'\D', rank, flags=re.I):
            classificacao = str(re.findall(r'[a-zA-ZÀ-ÿ\s]+', rank, flags=re.I)[0]).strip()
        else:
            classificacao = ''
        

        return {'posicao': posicao_tabela, 'classificacao': classificacao}
    
    def calculate_aproveitamento(self, partidas: str, pontos: str):
        maximo_pontos = int(partidas) * 3
        pontos_conquitados = int(pontos) 
        aproveitamento = (pontos_conquitados / maximo_pontos) * 100

        return f'{aproveitamento:.2f}%'
        

