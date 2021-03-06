;; This buffer is for text that is not saved, and for Lisp evaluation.
;; To create a file, visit it with C-x C-f and enter text in its buffer.
(message "hha")
"hha"
(defun pen(name)
  (message "hahah,%s" name))
pen
(pen "liming")
"hahah,liming"
(pen "peng")
"hahah,peng"
(setq foo "I'm foo")
"I'm foo"
(message foo)
"I’m foo"
(defvar foo "Did I know your name?"
  "A demo variable")
foo
(defvar bar "I'm bar"
  "A Demo variable named \"bar\"")
bar
(defun circle-area (radix)
  (let ((pi 3.1415926)area)
    (setq area (* pi radix radix))
    (message "area is %.2f" area)))
circle-area
(circle-area 3)
"area is 28.27"
(defun circle-area2 (radix)
  (let* ((pi 3.1415926)
	 (area (* pi radix radix)))
    (message "area is %.2f" area)))
circle-area2
(circle-area2 3)
"area is 28.27"
(setq foo (lambda (name)
	    (message "hello,%s!." name)))
(lambda (name) (message "hello,%s!." name))
(funcall foo "liming")
"hello,liming!."
(progn
  (setq foo 3)
  (message "Square of %d is %d." foo (* foo foo)))
"Square of 3 is 9."
(defun my-max (a b)
  (if (> a b)
      a b))
my-max
(my-max 3 4)
4
(defun fib (n)
  (cond ((= n 0) 0)
	((= n 1) 1)
	(t (+ (fib (- n 1))
	   (fib (- n 2))))))
fib
(fib 10)
55
(defun factorial (n)
  (let ((res 1))
    (while (> n 1)
      (setq res (* res n)
	    n (- n 1)))
    res))
factorial
(factorial 10)
3628800
(defun hello-world (&optional name)
  (or name (setq name "liming"))
  (message "hello,%s." name))
hello-world
(hello-world)
"hello,liming."
(hello-world "peng")
"hello,peng."
(defun square-number-p (n)
  (and (>= n 0)
       (= (/ n (sqrt n)) (sqrt n))))
square-number-p
(square-number-p -1)
nil
(square-number-p 25)
t
(message most-positive-fixnum)
#b101100
44
#o54
44
#x2c
44
#24r1k
44
(message "haha %.2f" (/ 0.0 0.0))
"haha -nan"
(integerp 1.)
t
(numberp 1)
t
(floatp -0.0e+NaN)
t
(floatp 1.)
nil
(zerop 9)
nil
(zerop 0)
t
(setq foo (- (+ 1.0 1.0e-3) 1.0))
0.0009999999999998899
(setq bar 1.0e-3)
0.001
(= foo bar)
nil
(defvar fuzz-factor 1.0e-6)
fuzz-factor
(defun approx-equal (x y)
  (or (and (= x 0) (= y 0))
      (< (/ (abs (- x y))
	    (max (abs x) (abs y)))
	 fuzz-factor)))
approx-equal
(approx-equal foo bar)
t
(eql 1.0 1)
nil
(= 1 1.0)
t
(/= 1. 2)
t
(setq foo 10)
10
(setq foo (1+ foo))
11
(setq foo (1- foo))
10
(setq foo "abc\000abc")
"abc abc"
?A
65
?a
97
?\\
92
(logior (lsh 1 27) ?A)
134217793
?\M-A
134217793
(stringp "haha")
t
(defun string-emptyp (str)
  (not (string< "" str)))
string-emptyp
(string-emptyp "")
t
(make-string 5 ?x)
"xxxxx"
(string ?a ?b ?c)
"abc"
(substring "0123456789" 3)
"3456789"
(substring "0123456789" 4 8)
"4567"
(concat "haha" "liming")
"hahaliming"
(message case-fold-search)
(case-fold-search)
(string-to-number "256")
256
(number-to-string 256)
"256"
(format "%#o" 256)
"0400"
(defun number-to-bin-string (number)
  (require 'calculator)
  (let ((calculator-ouput-radix 'bin)
	(calculator-radix-grouping-mode nil))
       (calculator-number-to-string number)))
number-to-bin-string
number-to-bin-string
(number-to-bin-string 256)
"256"
(concat '(?a ?b ?c ?d ?e))
"abcde"
(concat [?a ?b ?c ?d ?e ?f])
"abcdef"
(vconcat "abcdef")
[97 98 99 100 101 102]
(append "abcdef" nil)
(97 98 99 100 101 102)
(downcase "The cat in the hat")
"the cat in the hat"
(downcase ?X)
120
(upcase "The cat in the hat")
"THE CAT IN THE HAT"
(capitalize "The CAT in the Hat")
"The Cat In The Hat"
(upcase-initials "The CAT in the hAt")
"The CAT In The HAt"
(string-match "34" "0123456789")
3
(string-match "34" "012345678910123456789" 10)
14
(string-match "2*" "232*3=696")
0
(string-match (regexp-quote "2*") "232*3=696")
2
(progn
  (string-match "3\\(4\\)" "012345678910123456789")
  (match-data))
(3 5 4 5)
(let ((start 0))
  (while (string-match "34" "012345678910123456789" start)
    (princ (format "find at %d \n" (match-beginning 0)))
    (setq start (match-end 0))))
find at 3 
find at 14 
nil
(let ((str "01234567890123456789"))
(string-match "34" str)
(princ (replace-match "x" nil nil str 0))
(princ "\n")
(princ str))
012x567890123456789
01234567890123456789"01234567890123456789"
'(1 . 2)
(1 . 2)
'(1 . nil)
(1)
nil
nil
'()
nil
(read "(1 . 2)"
"(1 . 2)"
(car nil)
nil
(cdr ())
nil
(consp '(1 . 2))
t
(cons 1 2)
(1 . 2)
(cons 1 '())
(1)
(setq foo '(a b))
(a b)
(cons 'x foo)
(x a b)
(push 'x foo)
(x a b)
foo
(x a b)
(list 1 23 4)
(1 23 4)
'((+ 1 2) 3)
((+ 1 2) 3)
(list (+ 1 2) 3)
(3 3)
(append '(a b) '(c))
(a b c)
(append '(a b) 'c)
(a b . c)
(append [a b] "cd" nil)
(a b 99 100)
(nth 3 '(0 1 2 3 4 5))
3
(setq foo '(a b c))
(a b c)
(setcar foo 'x)
x
foo
(x b c)
(setcdr foo  '(y z))
(y z)
foo
(x y z)
(setq foo '(a b c))
(setcdr foo foo)
(x . #0)






















