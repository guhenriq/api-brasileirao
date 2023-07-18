import pandas as pd

from selenium.webdriver.common.by import By
from .browser import Browser


class Extractor(Browser):
    def __init__(self) -> None:
        super().__init__()
        self.url = "https://www.google.com.br"

    def extract(self):
        # Navega até a página do google
        self.driver.get(self.url)

        # Pesquisa por brasileirão
        self.driver.implicitly_wait(10)
        input_search = self.driver.find_element(By.ID, "APjFqb")
        input_search.send_keys("brasileirão")
        
        self.driver.implicitly_wait(10)
        button_search = self.driver.find_element(
            By.XPATH,
            "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[1]",
        )
        button_search.click()
        
        # Clica na aba da tabela de classificação
        self.driver.implicitly_wait(10)
        li_classificacao = self.driver.find_element(By.XPATH, '//*[@id="sports-app"]/div/div[2]/div/div/div/ol/li[3]')
        li_classificacao.click()

        # Extrai os dados da tabela
        self.driver.implicitly_wait(10)
        tabela_classificacao = self.driver.find_element(By.CLASS_NAME, 'Jzru1c')

        df = pd.read_html(tabela_classificacao.get_attribute('outerHTML'))[0]

        df = df[['Rank', 'Clube', 'PtsPontos', 'PJPartidas jogadas', 
                 'VITVitórias', 'EEmpates', 'DERDerrotas', 'GMGols marcados',
                 'GCGols contra', 'SGSaldo de gols']]

        df.to_csv('data.csv', index=False, encoding='latin1', sep=';')

        self.driver.close()

        print('Dados atualizados!')