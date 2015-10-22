# python-mode indentation not working upon hitting enter
(add-hook 'python-mode-hook
          (lambda ()
             (define-key python-mode-map "\r" 'newline-and-indent)))
