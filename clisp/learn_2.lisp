(defun get-one ()
  (format t "hahah"))

(defmacro get-ones ()
  (dotimes (i 10)   (get-one))
  (not nil))

(defun print4i () (dotimes (i 4) (print i)))

(defun fib (x)
  (do ((n 0 (1+ n))
       (cur 0 next)
       (next 1 (+ cur next)))
      ((= x n) cur)))

;;关键字形参
(defun foo (&key a b c) (list a b c))

(defun foo2 (&rest rest &key a b c)
  (list rest a b c))

(defun foo3 (n)
  (dotimes (i 10)
    (dotimes (j 10)
      (when (> (* i j) n)
	(return-from foo3 (list i j))))))

(defun plot (fn min max step)
  (loop for i from min to max by step do
       (loop repeat (funcall fn i) do (format t "*"))
       (format t "~%")))

(defun double2 (x)
  (* x x))
