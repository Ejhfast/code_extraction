# python multiprocessing agents and udp listeners
p = [multiprocessing.Process(target=self.sockListener),multiprocessing.Process(target=self.initiateTransactions)]
for prc in p:
    prc.start()
