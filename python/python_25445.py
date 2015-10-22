# Disable completion pop-up in python-mode shadowing indentation
;; (define-key map (kbd "TAB") 'py-indent-or-complete)
(define-key map (kbd "TAB") 'py-indent-line)
