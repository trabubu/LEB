'''
Created on 13 dic. 2016

@author: Ana
'''

from resultados import Dados#infos, se_limiar, sas_limiar, sarbg_limiar, sarbg_proporcao, sas_proporcao
import matplotlib.pyplot as plt
import numpy as np



def fazer_plot_1_voluntario(df_proporcoes1 = None, df_proporcoes2 = None, num_voluntario = None, salvar = False, titulo = None):
    '''
    Funcao que faz o plot dos resultados dos dois sa para cada um dos voluntarios
    '''
    # Definir nivel intensidades
    intensidades = np.arange(0, 90, 10)  
    
    # Fazer plot
    if df_proporcoes1 is not None and df_proporcoes2 is not None: 
        if num_voluntario is None:
            for v in df_proporcoes1.index:
                plt.figure(figsize=(16,10))
                plt.plot(intensidades, df_proporcoes1.loc[v], label = 'sarbg', c = 'gray', lw = 2)
                plt.plot(intensidades, df_proporcoes2.loc[v], label = 'sas', c = 'green', lw = 2)
                plt.plot(intensidades, [67.5,67.5,67.5,67.5,67.5,67.5,67.5,67.5,67.5], c = 'orange', label = 'p<0.05', linestyle = '--')
                plt.plot(intensidades, [72.5, 72.5, 72.5, 72.5, 72.5, 72.5, 72.5, 72.5, 72.5], c = 'red', label = 'p<0.01', linestyle = '--')
                plt.xlabel('% de intensidade sobre o limiar dos SA', fontsize = 14)
                plt.ylabel('Proporcao de acerto', fontsize = 14)
                plt.legend(bbox_to_anchor=(1.01, 1), loc=2, borderaxespad=0., fontsize = 12)
                plt.ylim(48,92)
#                 plt.ylim(min(df_proporcoes1.loc[v].min(), df_proporcoes2.loc[v].min()) - 2, 
#                          max(df_proporcoes1.loc[v].max(), df_proporcoes2.loc[v].max(), 72.5) + 2)
                plt.grid()
                if titulo is not None:
                    plt.title(titulo)
                else:
                    plt.title('Resultados voluntario ' + v, fontsize = 17)
                if salvar is True:
                    plt.savefig(v + '_resultados.png')
                else:
                    plt.show()
                


          
if __name__ == '__main__':
    
    sarbg_proporcao = Dados.sarbg_proporcao
    sas_proporcao = Dados.sas_proporcao
    sas_limiar = Dados.sas_limiar
    sarbg_limiar = Dados.sarbg_limiar
    se_limiar = Dados.se_limiar
    infos = Dados.infos
    
    fazer_plot_1_voluntario(sarbg_proporcao, sas_proporcao, salvar= True) 
                
    
    