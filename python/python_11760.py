# Create a loop over a function that prints out the elements the function it takes in, in a new row using a wrapper
def createManySomethings(Names, sizes):
    for (name, number) in zip(Names, sizes):
        createSomething([name], [number])
