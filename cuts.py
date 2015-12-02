import numpy as np

def generateCuts(t, x, b, n, epsilon):
    max_violation = 0
 
    for i in range(n):
        t_i = t[i]
        x_i = x[i]
        log_x = np.log(x_i)
        if(t_i > b[i]*log_x):
            if(t_i - b[i]*log_x > max_violation):
                max_violation = t_i - b[i]*log_x
                  
    if(abs(max_violation)<epsilon):
        return np.zeros(n), np.zeros(n)
    else:
        m = b/x 
        c = b*(- 1 + np.log(x))
        return m,c    