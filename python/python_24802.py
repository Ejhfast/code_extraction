# Transferring Data using Audio using Python
for bit in data:
    for i in range(0, sampling_frequency * symbol_length):
        signal.append(sin(i * sample_length * symbol_frequency(bit)))
