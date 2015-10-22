# No tab completion for IPython in Emacs textmode
(eval-after-load "python"
  '(define-key inferior-python-mode-map "\t" 'python-shell-completion-complete-or-indent)
