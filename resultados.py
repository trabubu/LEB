'''
Created on 13 dic. 2016

@author: Ana
'''
import pandas as pd
import numpy as np

class Dados():
    # Dados dos voluntarios
    # SARBG
    sarbg = pd.DataFrame([[20,24,25,29,25,23,23,22,20], [21,29,33,27,31,28,25,27,22], [21,26,29,30,32,32,36,36,33],
                          [21,26,32,30,26,25,33,30,24], [20,22,22,28,23,24,25,20,21], [21,24,24,31,28,25,27,23,22],
                          [20,26,28,28,25,30,34,31,27], [20,28,27,27,27,28,30,26,24], [21,24,30,29,27,28,29,25,24],
                          [21,23,20,20,28,30,33,35,29], [20,21,28,27,27,28,29,30,26], [20,22,25,35,29,28,30,26,25],
                          [20,25,27,24,25,29,27,26,24], [22,22,29,25,24,26,25,25,23], [20,33,33,24,28,29,33,34,29],
                          [20,22,21,24,29,27,28,33,26], [20,22,22,25,21,31,30,25,24], [20,26,25,24,27,27,29,26,24],
                          [20,24,25,28,29,24,26,23,22], [20,23,22,23,26,27,30,24,23]])
    sarbg.columns = [0,10,20,30,40,50,60,70,80]
    sarbg.index = ['v01', 'v02', 'v03', 'v04', 'v05', 'v06','v07', 'v08', 'v09', 'v10', 'v11', 'v12', 'v13', 'v14', 'v15',
                   'v16', 'v17', 'v18', 'v19', 'v20']
    sarbg_proporcao = 100*(sarbg/40)
    
    # SAS 
    sas = pd.DataFrame([[20,26,24,25,23,28,28,28,27], [20,21,26,24,28,27,29,25,25], [20,23,21,22,29,22,24,20,24],
                          [20,24,23,25,28,26,27,21,22], [20,24,22,23,27,27,24,29,25], [21,30,29,26,28,26,23,22,25],
                          [21,25,21,30,28,28,30,34,26], [20,24,27,28,27,29,31,25,23], [20,21,24,23,21,25,33,28,24],
                          [20,29,24,28,28,30,26,26,24], [20,23,24,29,30,27,30,30,25], [20,20,22,27,29,29,28,32,26],
                          [20,20,23,25,28,34,29,26,23], [22,29,27,29,24,29,29,27,24], [20,25,23,24,26,34,34,28,25],
                          [20,20,22,22,21,27,26,24,24], [21,26,25,25,26,30,27,24,23], [21,28,26,29,28,29,29,25,23],
                          [20,23,24,23,27,29,28,25,23], [20,26,24,27,29,25,26,24,22]])
    sas.columns = [0,10,20,30,40,50,60,70,80]
    sas.index = ['v01', 'v02', 'v03', 'v04', 'v05', 'v06','v07', 'v08', 'v09', 'v10', 'v11', 'v12', 'v13', 'v14', 'v15',
                   'v16', 'v17', 'v18', 'v19', 'v20']
    sas_proporcao = 100*(sas/40)
    
    # Limiares 
    
    # SE
    se_limiar = pd.DataFrame([[127.5,132,128.5,124,129.5,131],[128.5,131,127.5,86.5,90.5,87],[188.5,180.5,183,157.5,170.5,160.5],
                              [98.5,97.5,102.5,91.5,105.5,95.5],[60.5,70,61.4,67.5,75,70.5],[100,96.5,85.5,74.5,82.5,80],
                              [201.5,157.5,170.5,210.5,190.5,187.5],[98.5,88.5,98.5,100.5,85.5,92.5],[105.5,106.5,104.5,112.5,107.5,105.5],
                              [221.5,230.5,229.5,216.5,210.5,220.5],[151.5,168.5,162.5,145.5,151.5,147.5],[140.5,150.5,145.5,130.5,140.5,136.5],
                              [135.5,145,142.5,130.5,125.5,135.5],[52.5,67.5,55.5,65.5,60.5,48.5],[130.5,121.5,125.5,110.5,126.5,120.5],
                              [100,96.5,112,101.5,85.5,96.5],[83.5,95.5,85.5,90,97.5,84.5],[78.5,80.5,72.5,83.5,75,76.5],[139.5,145,132.5,140.5,135,147.5], 
                              [151.5,145.5,156.5,132.5,138.5,140.5]])
    se_limiar.columns = [1, 2, 3,4,5,6]
    se_limiar.index = ['v01', 'v02', 'v03', 'v04', 'v05', 'v06','v07', 'v08', 'v09', 'v10', 'v11', 'v12', 'v13', 'v14', 'v15',
                   'v16', 'v17', 'v18', 'v19', 'v20']
    # SAS
    sas_limiar = pd.DataFrame([[31.5,22.5,25.5],[18.5,19,18],[52.5,53.5,51],[9.5,9,8.5],[4.5,6,5.5],[2.5,2.5,2.5],[7.5,7.5,7.5],
                               [2.5,2,4.5],[7.5,7.5,7.5],[7.5,7.5,8.5],[7.5,7.5,7.5],[6.5,6.5,5],[10.5,9.5,7.5],
                               [5.5,5.5,6.5],[9.5,8,9],[5,5.5,5],[4.5,5.5,5],[12.5,15,14.5],[4.5,6,5.5], [2.5,5.5,6]])
    sas_limiar.columns = [1, 2, 3]
    sas_limiar.index = ['v01', 'v02', 'v03', 'v04', 'v05', 'v06','v07', 'v08', 'v09', 'v10', 'v11', 'v12', 'v13', 'v14', 'v15', 'v16', 'v17', 'v18', 'v19', 'v20']
    # SARBG
    sarbg_limiar = pd.DataFrame([[50.5,60,53.5],[19.5,19,19.5],[57.5,53.5,59.5],[25.5,27.5,24],[14.5,10.5,7.5],[25,28.5,26.5],
                                 [14.5,15.5,14.5],[21.5,24.5,23],[20.5,22.5,18.5],[31.5,32.5,28.5],[13.5,15.5,13.5],[68.5,62.5,56.5],[39.5,32.5,25.5],
                                 [7.5,9.5,8],[27.5,25,28.5],[25,35,32.5],[57.5,63.5,52.5],[25.5,30.5,27.5],[7.5,8.5,7.5],[20.5,24,22.5]])
    sarbg_limiar.columns = [1, 2, 3]
    sarbg_limiar.index = ['v01', 'v02', 'v03', 'v04', 'v05', 'v06','v07', 'v08', 'v09', 'v10', 'v11', 'v12', 'v13', 'v14', 'v15',
                   'v16', 'v17', 'v18', 'v19', 'v20']
    
    # Dados pessoais
    infos = pd.DataFrame([[26,'M','D'],[24, 'F', 'D'],[25, 'M', 'D'],[26,'F', 'D'],[32, 'F', 'D'],[27, 'M', 'D'],[29,'M', 'D'],
                          [25, 'F','D'],[29, 'M', 'D'],[26, 'M', 'D'],[26, 'M', 'D'],[28,'M','D'],[32,'M', 'C'],[32, 'F', 'D'],
                          [19, 'M', 'D'],[21, 'M','D'],[32, 'F', 'D'],[23, 'F', 'D'],[28, 'F', 'D'],[25, 'F', 'D']])
    infos.columns = ['idade', 'genero', 'mao']
    infos.index = ['v01', 'v02', 'v03', 'v04', 'v05', 'v06','v07', 'v08', 'v09', 'v10', 'v11', 'v12', 'v13', 'v14', 'v15',
                   'v16', 'v17', 'v18', 'v19', 'v20']
    
         
#     print(dados)
#     print(se_limiar)
#     print(sas_limiar)
#     print(sarbg_limiar)
    
    
    
    