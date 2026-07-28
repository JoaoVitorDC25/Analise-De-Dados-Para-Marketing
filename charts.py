import matplotlib.pyplot as plt
import seaborn as sns

import config as cfg

def hist_graphic(
    caminho=None):
    
    
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
    
    