import numpy as np

def calculate(list):
         if len(numbers) != 9:
               raise ValueError("List must contain nine numbers.")
           matrix = np.array(numbers).reshape(3, 3)
           
           # Compute statistics
           return {
               'mean': [
                   matrix.mean(axis=0).tolist(),
                   matrix.mean(axis=1).tolist(),
                   matrix.mean().item()
               ],
               'variance': [
                   matrix.var(axis=0).tolist(),
                   matrix.var(axis=1).tolist(),
                   matrix.var().item()
               ],
               'standard deviation': [
                   matrix.std(axis=0).tolist(),
                   matrix.std(axis=1).tolist(),
                   matrix.std().item()
               ],
               'max': [
                   matrix.max(axis=0).tolist(),
                   matrix.max(axis=1).tolist(),
                   matrix.max().item()
               ],
               'min': [
                   matrix.min(axis=0).tolist(),
                   matrix.min(axis=1).tolist(),
                   matrix.min().item()
               ],
               'sum': [
                   matrix.sum(axis=0).tolist(),
                   matrix.sum(axis=1).tolist(),
                   matrix.sum().item()
               ]
           }
       
       # Optional: Test code (use main.py instead)
       if __name__ == "__main__":
           numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
           result = calculate(numbers)
           print(result)



    //return calculations
