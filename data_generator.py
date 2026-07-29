import numpy as np

import config as cfg

def data_generator_ecommmerce() -> np.column_stack:

    '''
        Gera uma base de dados de ecommerce e retorna:
        - Numero de visitas;
        - Tempo no site;
        - Quantidade de itens no carrinho;
        - Valor de compra.
    '''
        
    np.random.seed(cfg.SEED)

    visitas=np.random.randint(cfg.INIT_USERS, cfg.FINAL_USERS, size=cfg.NUM_USERS)

    tempo_no_site = np.random.normal(loc= 20, scale=5, size=cfg.NUM_USERS) + (visitas * 0.5)
    tempo_no_site = np.round(tempo_no_site, 2) #Arredonda para duas casas decimais

    itens_no_carrinho = np.random.randint(0, 8, size = cfg.NUM_USERS) + (visitas // 10)
    itens_no_carrinho = (itens_no_carrinho + (tempo_no_site//15)).astype(int)

    valor_compra = (itens_no_carrinho * 35) + np.random.normal(loc= 0, scale= 10, size=cfg.NUM_USERS)

    valor_compra[itens_no_carrinho == 0] = 0
    valor_compra[valor_compra < 0] = 0
    valor_compra=np.round(valor_compra,2)

    dados_ecommerce = np.column_stack((visitas, tempo_no_site, itens_no_carrinho, valor_compra))

    return dados_ecommerce