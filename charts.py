import matplotlib.pyplot as plt
import seaborn as sns

import config as cfg

def hist_graphic(
    valor_col,
    media_valor,
    mediana_valor,
    std_valor,
    xLabel,
    yLabel,
    titulo=None,
    figsize=cfg.FIG_SIZE_HIST,
    caminho=None):
    
    '''
        Gera um grafico di tipo histograma, indicando:
        - valor_col
        - media_valor
        -
    '''
    
    
    plt.figure(figsize=figsize)
    
    plt.hist(valor_col, bins = 30, color = 'skyblue', edgecolor = 'black', alpha = 0.7)
    plt.axvline(media_valor, color = 'red', linestyle='--', linewidth = 2, label= f'Media = R${media_valor:.2f}')
    plt.axvline(mediana_valor, color = 'orange', linestyle='--', linewidth = 2, label= f'Mediana = R${mediana_valor:.2f}')
    plt.axvline(media_valor + std_valor, color = 'green', linestyle=':', linewidth = 2, label= f'+1 DP = R${media_valor + std_valor:.2f}')
    plt.axvline(media_valor - std_valor, color = 'green', linestyle=':', linewidth = 2, label= f'-1 DP = R${media_valor - std_valor:.2f}')
    
    plt.title(titulo)
    
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    
    plt.legend()
    plt.grid(alpha = cfg.ALPHA_HIST)

    caminho = f"image/{titulo.replace(" ","")}.png"
    plt.tight_layout()
    plt.savefig(caminho, dpi=cfg.DPI, bbox_inches='tight') if caminho else None
    plt.show() 

def heatmap_graphic(
    dados,
    titulo=None,
    figsize=cfg.FIG_SIZE_HEATMAP,
    caminho=None):
    
    plt.figure(figsize=figsize)
    
    sns.heatmap(dados, annot = True, cmap = "Blues", fmt = ".2f")

    plt.title(titulo)
    
    caminho = f"image/{titulo.replace(" ","")}.png"
    plt.tight_layout()
    plt.savefig(caminho, dpi=cfg.DPI, bbox_inches='tight') if caminho else None
    plt.show()
    
    