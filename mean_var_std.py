import numpy as np


def calculate(list):
    
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
        
    else:
        
          arr = np.reshape(list, (3,3))


          calculations = {}

          # adding Mean value of each axis into the dictionary
          calculations['mean'] = [(arr.mean(axis = 0)).tolist(),
                               (arr.mean(axis = 1)).tolist(),
                                arr.mean()]

          # adding Variancof each axis into the dictionary
          calculations['variance'] = [(arr.var(axis = 0)).tolist(),
                                  (arr.var(axis = 1)).tolist(),
                                  arr.var()]

          # adding Standard Deviation of each axis into the dictionary
          calculations['standard deviation'] = [(arr.std(axis = 0)).tolist(),
                                             (arr.std(axis = 1)).tolist(),
                                             arr.std()]

          # adding Maximum value of each axis into the dictionary
          calculations['max'] = [(arr.max(axis = 0)).tolist(),
                              (arr.max(axis = 1)).tolist(),
                              arr.max()]

          # adding Minimum values of each axis into the dictionary
          calculations['min'] = [(arr.min(axis = 0)).tolist(),
                              (arr.min(axis = 1)).tolist(),
                              arr.min()]

          # addint Total_Sum of each axix into the dictionary
          calculations['sum'] = [(arr.sum(axis = 0)).tolist(),
                              (arr.sum(axis = 1)).tolist(),
                                arr.sum()]

          return calculations
