# Emacs Unbind a Mode's KeyBinding
(add-hook 'python-mode-hook
          (lambda()
            (local-unset-key (kbd "C-c C-c"))))
