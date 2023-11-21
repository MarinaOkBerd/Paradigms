#from scipy.stats import pearsonr
#import numpy as np

#var1 = np.random.randint(0, 10, 20)
#print(var1)
#var2 = np.random.randint(0, 10, 20)
#print(var2)

#print(pearsonr(var1, var2))


from functools import reduce
import numpy as np

var1 = np.random.randint(0, 10, 20)
print(var1)
var2 = np.random.randint(0, 10, 20)
print(var2)
if __name__ == '__main__':
    print(*map(lambda x, y: x / y, [(sum((z - reduce(lambda x, y: x + y, var1) / reduce(lambda x, y: x + 1, var1)) * (m - reduce(lambda x, y: x + y, var2) /
        reduce(lambda x, y: x + 1, var2)) for z, m in zip(var1, var2)))],
        [(sum((z - reduce(lambda x, y: x + y, var1) / reduce(lambda x, y: x + 1, var1)) ** 2 for z in var1) ** 0.5 * (sum((m - reduce(lambda x, y: x + y, var2) /
        reduce(lambda x, y: x + 1, var1)) ** 2 for m in var2) ** 0.5))]))