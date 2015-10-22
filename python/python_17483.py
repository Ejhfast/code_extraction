# used .join(something) but result is not joined
def message_to_bits(message):
  return "".join("".join(str(bits.char_to_bits(char))) for char in message)
