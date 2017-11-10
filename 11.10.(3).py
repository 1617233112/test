Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> tup1 = ('physics','chemistry',1997,2000);
>>> tup2 = (1,2,3,4,5);
>>> tup3 = "a","b","c","d";
>>> tup1 = ();
>>> tup1 = (50,);
>>> 
>>> tup1 = ('physics','chemistry',1997,2000);
>>> tup2 = (1,2,3,4,5,6,7);
>>> print "tup1[0]:",tup1[0]
tup1[0]: physics
>>> print "tup2[1:5]:",tup2[1:5]
tup2[1:5]: (2, 3, 4, 5)
>>> tup1[0]: physics
SyntaxError: invalid syntax
>>> 
