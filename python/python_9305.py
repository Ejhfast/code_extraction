# Function creation at runtime in Python
for i in range(len(Names)):
    exec("def " + Names[i] + "(" + Args + "): " + Bodies[i]) #create locally
    globals()[Names[i]] = locals()[Names[i]]                           #assign to global space
