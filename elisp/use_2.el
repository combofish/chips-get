;; This buffer is for text that is not saved, and for Lisp evaluation.
;; To create a file, visit it with C-x C-f and enter text in its buffer.
(setq mu-name "Bastien")
(insert "hello!")hello!
(insert "hello" "world")helloworld
(insert "hello,I am " mu-name)hello,I am Bastien
(defun hello () (insert "hello,I am " mu-name))
(hello)hello,I am Bastien
(defun hello (name)(insert "hello" name))
(hello "you")helloyou
(switch-to-buffer-other-window "*test*")
(progn
  (switch-to-buffer-other-window "*test*")
  (erase-buffer)
  (hello "there")
  (other-window 1))
nil
(let ((local-name "you"))
  (switch-to-buffer-other-window "*test*")
  (erase-buffer)
  (hello local-name)
  (other-window 1))
(format "hello %s" "visitor")

(defun hello (name)
  (insert (format "hello,%s!" name)))
(hello "you")hello,you!
(defun greeting (name)
  (let ((yourname "Liming"))
    (insert (format "helo%s!\n\n I am %s."
                    name
                    yourname))))
(greeting "you")heloyou!

I am Liming.
(read-from-minibuffer "Enter your name:")
(defun greeting (from-name)
  (let ((your-name (read-from-minibuffer "Enter your name:")))
    (switch-to-buffer-other-window "*test*")
    (erase-buffer)
    (insert (format "Hello, I am %s! You are %s."
                    from-name
                    your-name))
    (other-window 1)))
(greeting "Bastien")
Hello, I am Bastien! You are liming.
(setq list-of-names '("Liming" "Peng" "zul"))
(dolist (pkg list-of-names)
  (message "%s" pkg))



(car list-of-names)

(cdr list-of-names)
(push "zhangsan" list-of-names)
(mapcar 'hello list-of-names)hello,zhangsan!hello,Liming!hello,Peng!hello,zul!
(defun greeting ()
  (switch-to-buffer-other-window "*test*")
  (erase-buffer)
  (mapcar 'hello list-of-names)
  (other-window 1))
(greeting)
(defun replace-hello-by-bonjour ()
  (switch-to-buffer-other-window "*test*")
  (goto-char (point-min))
  (while (search-forward "hello" nil 't)
    (replace-match "Bonjour"))
  (other-window 1))
(replace-hello-by-bonjour)
(defun boldify-names()
  (switch-to-buffer-other-window "*test*")
  (goto-char (point-min))
  (while (re-search-forward "Bonjour \\(.+\\)!" nil 't)
    (add-text-properties (match-beginning 1)
                         (match-end 1)
                         (list 'face 'bold)))
  (other-window 1))
(boldify-names)
(defvar namelist-use '(
                   "hah"
                   "sfdj"
                   "jlsdj"
                   "jlsn"
                   "jl"
                   ) "default" )
(dolist (pkg namelist-use)
  (switch-to-buffer-other-window "*test*")
  (message "%s" pkg))

(message "haha")







(defvar combofish-packages-use '(
                       company
                       monokai-theme
                       ) "Default packages")

(setq package-selected-packages combofish-packages-use)

(dolist (pkg combofish-packages-use)
  (message "%s" pkg))



(defun combofish-packages-installed-p ()
  (loop for pkgs in combofish-packages-use
        when (not (combofish-packages-installed-p)) do (return nil)
        finally (return t)))

(unless (combofish-packages-installed-p)
  (message "s" "Refeshing package database...")
 ;; (package-refresh-contents)
  (dolist (pkgs combofish-packages-use)
    (when (not (combofish-packages-installed-p 'pkgs)))))


(setq foo '(1 2))
(push 'x foo)
(list 1 2 3 4 "haha")
(length (append '(a b) 'c))
(length (list 1 2 3 4 5))
(defvar mmmmmmm-mmmmm (list 'jj 'ji 'li 'jo) "hahah" )
(defun liming-fun1(name)
  (message "%s" name))
(mapc (liming-fun1 ) mmmmmmm-mmmmm)
(dolist (tmp mmmmmmm-mmmmm)
  (message "%s" tmp))
(setq mI-j "jj")
(when (not mmmmmmm-mmmmm mI-j))



    (unless (combofish/packages-installed-p)
      (message "%s" "Refeshing package database...")
      (package-refresh-contents)
      (dolist (pkg combofish/packages-use)
        (when (not (packages-installed-p pkg))
          (package-install pkg))))


