# Selectable string filter
input_string = "I only want the vowels"
allowed_chars = 'AEIOUaeiou'
output_string = ''.join((c for c in input_string if c in list(allowed_chars)))
