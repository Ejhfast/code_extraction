# Passing vim functions to vim's inbuilt python
import vim
os.environ['DJANGO_SETTINGS_MODULE'] = \
    vim.eval("""expand("%:p:h")""").split('/')[4] + '.settings'
