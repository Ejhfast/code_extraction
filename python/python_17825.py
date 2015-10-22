# How to quickly create a IPython shell in Emacs?
(defun ipython ()
  (interactive)
  (ansi-term "/usr/bin/ipython" "ipython"))
