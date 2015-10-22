# Write multiple NumPy arrays into CSV file in separate columns?
output = np.column_stack((arrA.flatten(),arrB.flatten(),arrC.flatten()))
np.savetxt('output.dat',output,delimiter=',')
