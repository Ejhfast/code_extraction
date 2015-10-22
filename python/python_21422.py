# spynner doesn't load XHR data
def load_page(br):
  br.wait(5)
  return 'Japan' in br.html
