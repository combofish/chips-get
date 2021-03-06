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

;; 1.宏会在编译器在对源代码进行编译的时候进行简单替换，不会进行任何逻辑检测，即简单代码复制而已。
;; 2.宏进行定义时不会考虑参数的类型。
;; 3.参数宏的使用会使具有同一作用的代码块在目标文件中存在多个副本，即会增长目标文件的大小。
;; 4.参数宏的运行速度会比函数快，因为不需要参数压栈/出栈操作。
;; 5.参数宏在定义时要多加小心，多加括号。
;; 6.函数只在目标文件中存在一处，比较节省程序空间。
;; 7.函数的调用会牵扯到参数的传递，压栈/出栈操作，速度相对较慢。
;; 8.函数的参数存在传值和传地址（指针）的问题，参数宏不存在。

(setq foo '(a b c))
(remq 'b foo)
(a c)
(delq 'b foo)
(a c)
(delq 'a foo)
(c)

(assoc "a" '(("a" 97) ("b" 98)))
("a" 97)
(assq 'a '((a . 97) (b . 98)))
(a . 97)

(cdr (assoc "a" '(("a" 97) ("n" 98))))
(97)
(cdr (assq 'a '((a . 97) (b . 98))))
97

(assoc-default "a" '(("a" 97) ("b" 98)))
(97)

(rassoc '(97) '(("a" 97) ("b" 98)))
("a" 97)
(rassq '97 '((a . 97) (b . 98)))
(a . 97)

(setq foo '(("a" . 97) ("b" . 98)))
(if (setq bar (assoc "a" foo))
    (setcdr bar "this is a"))
foo
(("a" . "this is a") ("b" . 98))

;;  (setq foo (cons '("a" . "this is a") foo)))
foo
(("a" . "this is a") ("b" . 98))

(setq foo (cons '("a" . 97)
                (delq (assoc "a" foo) foo)))

(mapc '1+ '(1 2 3))
(1 2 3)
(mapcar '1+ '(1 2 3))
(2 3 4)

(setq bar 0)
(dolist (i (list 1 2 3 4 5 6))
  (setq bar (+ bar i)))
;;  (message "%d" bar))
(message "sum is %d." bar)

(list 'ha 'hs 'hd )
(ha hs hd)

(defun my-remove-if (predicate list)
  "use "
  (delq nil (mapcar (lambda (n)
                      (and (not (funcall predicate n)) n))
                    list)))
(defun evenp (n)
  (= (% n 2) 0))
(my-remove-if 'evenp '(0 1 2 3 4 5 6 7 ))
(1 3 5 7)

(mapcar (lambda (n)
          (setq n (* n n))) 
(not t)
nil

(and t nil)
nil

(and nil nil)
nil

(and 10 2)
2

(and 1 2 3 4 10 7)

(list 'a 'b 'c)
(a b c)

(safe-length '(1 . 2))
1
(safe-length '(a . b))
1

(vector 'foo 23 [bar baz] "rats")

(make-vector 9 'z)
[z z z z z z z z z]

(fillarray (make-vector 6 'a) 5)
[5 5 5 5 5 5]

;;将向量转换成列表可以用append函数。


;;测试列表是否为真列表
(defun circular-list-p (list)
  (and (consp list)
       (circular-list-p-1 (cdr list) list 0)))

(defun circular-list-p-1 (tail halftail len)
  (if (eq tail halftail)
      t
    (if (consp tail)
        (circular-list-p-1 (cdr tail)
                           (if (= (% len 2) 0)
                               (cdr halftail)
                             halftail)
                           (1+ len))
      nil)))

(setq foo 2)
(1+ foo)

(symbolp '+1)
nil

(symbolp '\+1)
t

(symbol-name '\+1)
"+1"

(setq foo (make-vector 10 0))
(intern-soft "abc" foo)
nil
(intern "abc" foo)
abc
(intern-soft "abc" foo)
foo
[0 0 0 0 0 0 0 0 0 abc]

(setq count 0)
(defun count-syms (s)
  (setq count (1+ count)))
(mapatoms 'count-syms)
count
38949
(length obarray)
15121

(set (intern "abc" foo) "I am abc")
"I am abc"

(symbol-name (intern "abc" foo))
"abc"

(message (buffer-name))
"use_3.el"

(defmacro inc (var)
  (list 'setq var (list '1+ var)))
(setq my-var 1)
(setq my-var (1+ my-var))
3

(inc my-var)
5

(macroexpand '(inc my-var))
(setq my-var (1+ my-var))

(quote (+ 1 1))
(+ 1 1)

(defun my-print (number)
  (message "This is a number : %d." number))
(my-print 2)
"This is a number : 2."
(my-print (+ 1 3))
"This is a number : 4."

(defmacro my-print-2 (number)
  `(message "This is a number : %d." ,number))
(my-print-2 3)
"This is a number : 3."
(my-print-2 (+ 2 3))
"This is a number : 5."

(pp (macroexpand '(my-print-2 (+ 2 3))))
(message "This is a number : %d."
	 (+ 2 3))
"(message \"This is a number : %d.\"
	 (+ 2 3))
"


(setq my-var 2)
(inc my-var)
4

(defmacro inc2 (var1 var2)
  (list 'progn (list 'inc var1) (list 'inc var2)))
(setq my-var 1)
(inc2 my-var my-var)
5

(macroexpand '(inc2 my-var my-var))
(progn (inc my-var) (inc my-var))

(macroexpand-all '(inc2 my-var my-var))
(progn (setq my-var (1+ my-var)) (setq my-var (1+ my-var)))

(+ 1 2 3 4 5)
15

"hello world"
"hello world"

(format t "hello world")


(defun myfun (aa bb &optional cc dd)
  "test optional arguments"
  (insert aa bb cc dd)
  )

;; call it
(myfun "1" "2" "3" "4")
1234nil

(myfun "myaa" "mybb" nil)
myaamybb

(defun ff(aa bb &rest cc)
     "test rest arguments"
     (message "%s" cc))
(ff "1" "2" "3" "4")
"(3 4)"

