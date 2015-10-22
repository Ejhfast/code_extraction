# Emacs set spacing for inline (end of line) comments
(add-hook 'python-mode-hook
      (lambda () (set (make-local-variable 'comment-inline-offset) 2)))
