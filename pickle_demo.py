import pickle 
import time

start_time = time.time()
shared_variable = 42 
 
with open("shared_variable.pickle", "wb") as f: 
    pickle.dump(shared_variable, f) 

with open("shared_variable.pickle", "rb") as f: 
    shared_variable = pickle.load(f) 
 
print(shared_variable) 
print("--- %s seconds ---" % (time.time() - start_time))
