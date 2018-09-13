(defun hello-world () (format t "hellp world"))
(defun make-cd (title artist rating ripped)
  (list :title title :artist artist :rating rating :ripped ripped))
(defvar *db* nil)
(defun add-record (cd)
  (push cd *db*))
(defun dump-db()
  (dolist (cd *db*)
    (format t "~{~a: ~10t~a~%~}~%" cd)))

(defun dump-db-2()
  (format t "~{~{~a: ~10t~a~%~}~%~}" *db*))

(defun prompt-read (prompt)
  (format *query-io* "~a: " prompt)
  (force-output *query-io*)
  (read-line *query-io*))
(defun prompt-for-cd()
  (make-cd
   (prompt-read "Title")
   (prompt-read "Artiist")
   (or
    (parse-integer (prompt-read "Rating") :junk-allowed t) 0)
   (y-or-n-p "Ripped [y/n]: ")))
(defun add-cds()
  (loop (add-record (prompt-for-cd))
	(if (not (y-or-n-p "Another [y/n]: ")) (return))))
(defun save-db (filename)
  (with-open-file (out filename
		  :direction :output
		  :if-exists :supersede)
		  (with-standard-io-syntax
		   (print *db* out))))
(defun load-db (file-name)
  (with-open-file (in filename)
		  (with-standard-io-syntax
		   (setf *db* (read in)))))  
(defun select-by-artist (artist)
  (remove-if-not
   #'lambda (cd)
   (equal (getf cd :artist) artist) *db*))
(defun select (select-fn)
  (remove-if-not select-fn *db*))
(defun artist-selector (artist)
  #'(lambda (cd) (equal (getf cd :artist) artist)))
(defun foo (x y z)
  (list x y z))
(defun foo2 (&key a b c)
  (list a b c))
(defun foo3 (&key a (b 20) (c 30 c-p))
  (list a b c c-p))
(defun where (&key title artist rating ripped (ripped nil ripped-p)
		#'(lambda (cd)
		    (and
		     (if title (equal (getf cd :title) title) t)
		     (if artist (equal (getf cd :artist) artist) t)
		     (if rating (equal (getf cd :rating) rating) t)
		     (if ripped-p (equal (getf cd :ripped) ripped) t)))))
;; (defun update (select-fn &key title artist rating (ripped nil ripped-p))
;;   (setf *db*
;; 	(mapcar #'(lambda (row)
;; 		    (when (funcall select-fn row)
;; 		      (if title    (setf (getf row :title)   title))
;; 		      (if artist   (setf (getf row :artist)  artist))
;; 		      (if rating   (setf (getf row :rating)  rating))
;; 		      (if ripped-p (setf (getf row :ripped)  ripped)))
;; 		   row )
;; 		*db*)
;; 	))








