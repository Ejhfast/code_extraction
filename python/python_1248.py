# Emacs customization
(add-hook 'c-mode-common-hook
      '(lambda ()
         (define-key c-mode-base-map (kbd "RET") 'newline-and-indent)))
