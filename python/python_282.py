# How do I suppress python-mode's output buffer?
(defadvice py-execute-buffer (after advice-delete-output-window activate)
  (delete-windows-on "*Python Output*"))
