(message "hello world")
;; This buffer is for text that is not saved, and for Lisp evaluation.
;; To create a file, visit it with <open> and enter text in its buffer.

(defun circle-area (radix)
  (let ((pi 3.14)
        (area))
    (setq area (* pi radix  radix))
    (message "%.2f" area)))
(circle-area 3)
"28.26"

(defun circle-area (radix)
  (let* ((pi 3.14)
         (area (* pi radix radix)))
    (message "%.2f" area)))
(circle-area 3)
"28.26"

(funcall (lambda (name)
           (let ((pi 3.1415) (area))
                 (setq area (* name name pi))
                 (message "%.2f" area)))
         3 )
"28.27"

(setq foo (lambda (name)
            (let* ((pi 3.1415)
              (area (* pi name name)))
              (message "%.2f" area))))
(funcall foo 3)
"28.27"

(progn
  (setq foo 3)
  (message "Square of %d is %d" foo (* foo foo)))
"Square of 3 is 9"

(if (> 4 3)
    4 3)

(defun max-which (a b)
  (if (> a b)
      a b))
(max-which 4 5)

(defun fib (n)
  (cond ((= n 0) 0)
        ( (= n 1) 1)
        (t (+ (fib (- n 1))
              (fib (- n 2))))))
(fib 30)
832040

(while (> 2 1)
  (message "hall"))

(defun fact (x y)
  (let ((result 1))
    (while (> y 1)
      (setq result (* result  x)
            y (- y 1)))
    (message "%d..." result)))
(fact 4 2)
"4..."

"4..."

(defun square-number-p (n)
  (and (>= n 0)
       (= (/ n (sqrt n) (sqrt n)))))
(square-number-p 16)
t

(message "%d" most-negative-fixnum)
"-2305843009213693952"
(message "%d" most-positive-fixnum)
"2305843009213693951"

(eql 3 3.)
t

(= 3 3.)
t

(= 3 3.0)
t

(eql 3 3.0)
nil

(/ 5 6)
0

(setq foo 10)
10
(setq foo (1+ foo))
11
(setq foo (1- foo))
10

(sin 3.14)
0.0015926529164868282

(logb 4)
2

(exp 1)
2.718281828459045

(random t)
-347345313351804027

(random t)
23481216579790151

(setq foo "abc\000abc")
"abc abc"
(message foo)
"abc abc"

?A
65

?a
97

?\\
92

?\+
43

?+
43

(logior (lsh 1 27) ?A)
134217793

?\M-A
134217793

(fact 2 15)
"16384..."

(defun string-empty (str)
  (not (string> str "")))
(string-empty "ha")
nil
(string-empty "")
t

(make-string 8 ?a)
"aaaaaaaa"
(string ?a ?b ?c)
"abc"

(substring "123456" 2 4)
"34"

(concat "1" "2" "3" "jj")
"123jj"

(string-to-number "123")
123
(number-to-string 123)
"123"

(string-to-number "k")
0

(format "%#o" 1024)
"02000"

(defun number-to-bin-string (number)
  (require 'calculator)
  (let ((calculator-output-radix 'bin)
        (calculator-radix-grouping-mode nil))
    (calculator-number-to-string number)))
(number-to-bin-string 1024)
"10000000000"

(concat '(?a ?b ?c ?d ?e))
"abcde"
(concat [?a ?b ?c ?d ?e])
"abcde"
(vconcat "abcdef")
[97 98 99 100 101 102]
(append "abcdef" nil)
(97 98 99 100 101 102)

(progn
  (string-match "3\\(4\\)" "01234567890123456789034354545665445323")
  (match-data))
(3 5 4 5)

(let ((start 0))
  (while (string-match "34" "012345678901234556" start)
    (princ (format "find at %d\n" (match-beginning 0)))
    (setq start (match-end 0))))
find at 3
find at 13
nil

(setq foo "")
""
(message foo)
""
(setq foo '("haaaaah" . 0))
(message "%s" foo)
"(haaaaah . 0)"

(setq foo '(1 2 3 4 5 6))
(1 2 3 4 5 6)
(setq foo '(1 2))
(1 2)
(setq foo '("j" "k"))
("j" "k")
(setq foo [1 2 3 5])
[1 2 3 5]

'(nil . nil)
(nil)
(car (read "(1 . 2)"))
1
(eq (car nil) (cdr nil))
t
(null '())
t

(setq foo '(1 . 2))
(1 . 2)
(cdr (cons 'y foo))
(1 . 2)
(message "%s" foo)
"(1 . 2)"
(push 'x foo)
(x 1 . 2)
(message "%s" foo)
"(x 1 . 2)"
(list 1 2 3 4)
(1 2 3 4)
(setq foo '(1 2 3 4 5))
(1 2 3 4 5)
(setq foo (list 1 2 3 4 5))
(1 2 3 4 5)
(setq foo (list "ha" "u"))
("ha" "u")
(message "%s" foo)
"(ha u)"
(append foo "w")
("ha" "u" . "w")
(message "%s" foo)
"(ha u)"
(append (append (append foo '(1 nil)) '("w" nil)) "w")
("ha" "u" 1 nil "w" nil . "w")

(append "w" "j" foo)
(119 106 "ha" "u")

(append '(a b) '(c) '(d))
(a b c d)
(append '(ajjl asjl) '(ji) '(jljkj mjn kjls mjl))
(ajjl asjl ji jljkj mjn kjls mjl)

(append (append (append (append foo '(1)) '("w")) "w" nil) '(ui))
("ha" "u" 1 "w" 119 ui)

(append (append (append (append foo '(1)) '("w")) "w" nil) 'ui)
(jo ji 1 "w" 119 . ui)

(setq foo '(jjlji))
(jjlji)

(setq foo 'ji)
ji

(setq foo (list '(jo) '(ji)))
((jo) (ji))

(setq foo (list 'jo 'ji))
(jo ji)

(nth 3 '(1 2 3 4 5))
4

(nth 0 '(a v d))
a

foo
(jo ji)

(setq foo '(a b c))
(a b c)
(setcar foo 'x)
x
foo
(x b c)
(setcdr foo '(y z))
(y z)

(setq foo '(x y z))
(x y z)
(setcdr foo foo)
(x . #0)

(setq foo "jji")
"jji"

(setq foo nil)
(push 'x foo)
(push 'b foo)
(pop foo)
foo
(x)

(length "hallo world")
11

(setq foo '(a b c))
(a b c)
(reverse foo)
(c b a)
foo
(a b c)

(nreverse foo)
(c b a)
foo
(a)
;;破坏性的函数。

(setq foo '(1 2 3 4 2 1))
(sort foo '<)
(1 1 2 2 3 4)

























  


