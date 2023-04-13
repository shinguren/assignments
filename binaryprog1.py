#writing data to a binary file

import pickle
e = {'Namita':25000, 'Manya':30000, 'Tanu':20000}
f1=open('emp.dat','wb')
pickle.dump(e,f1)
print(" ** file created **")
f1.close()