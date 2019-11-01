# Many Time Pad Cracker

### Groupe : 
- Marine LHUILLIER
- Enzo TUIHAGI
- Mathilde REMAZEILLES-GEILER

## Utilisation

### Première partie - texte déchiffré partiellement - Python 3.6

En premier lieu nous déchiffrons le texte partiellement avec la commande suivante :

```bash
directory/first_part> python3.6 first_part/decrypt.py
```

ce qui donne le résultat suivant : 

```
what Is a Hacker#
the Jargon F##e##o#t#ins a#b#nc# ## #e#i#itio## of#t#e #e## #h###er###m#st #aqi#g to d##a##h ##chn#cal ##ep#ne## a#d a ##l#gh# i# ##lv##g p#o#l##s #nd #v#rc##in# l###t## I# y#r w##t #o #no# #o# to ##cam# a hacker# t##r#h  onl# tyo #re re#l#y ###ev####
there is a c##m##i#y# a sh#r#d #u##u#e# #f ex##rt #r#gr#m##r# ### n###o#kin# pi#ard# t##b##ra##s i#s hi##or# b##k #hr#u## #ec#de# ## t## fi#s# ##me#sha#i#g ##ni#om###e## a#d #oe ##rl#es# A#P#n#t #x##rgm#n#s##Th# #em##u# cf th#s mul#ure o#i#in###d #########l#a##er g ###ke## #u##t t## ####r###z #ac#### ####kv## ###xlo###a###gs###t## #da# #tn## t###y rH###ir#n#ak# ### W###d #### #e# w##kl ## y## a e #a## o#h#h## #u#t#r#g i# wou #av#o##n ###ut##n#o #t a## ###e# pe#the ## #t #n#w wh# ###o###ea## ####  o#n#o######i #cu ##ya ##c###g
the hacker m##d##e# #s not#c#nf#n## #o#t#is s##twa#e#ha#k## #u###re###h#re #rb #eop#e ##y##pp## th# hac##r #tt##ud# to ##h#r #hi#g## lthe e#e#t##ni#s o# #us## a#tu###y##yo# c#i f##d #t #t #h# #ig#e## be#e#s##f #n# s##b#ci or #rt  S#ftwar# #ac###s #########n#hthe i n###d ##i#i## el##w#### ###tm#y #### ####k ##c###sn ### ###  ### ##a#a #h#tnthe ###kk  ###yr#n#s #e###y ###ep####n# #f ##ebp##ti##l#  m#d##m a # ##c#e# #o# s #n  Bu# i#o##et###t ##n#hi# do##m### #e w### f##u# o# #he s#i###o###ea##i####syo#n# ######eh#okbyou a## ###i###d###o##i##r#h#a##a# #nc###### #### ## ##n## dw### ####e#a##e#k
there is ano##e##g#o#p of #e#pl# ##o#l#u#ly c##l t#e#se#v## #a###rs###u# ar#n to Th#se##d##pe##le #main## a#ol##ce#t #a##s# w#o #e##a ##ck #u# ## b#eak#n# i##o #om###e## a#d #ore##in# t#e #h#n# s#s##m  #e#l##ac#e#s ##k# xhese#peapl# crac#e#s ### w######### a ## dmiw### t##m# ##al ##c#### ### l# t#### #### g## ###  a### #the ###s##l#  #n#  ## v### l i###  a # o#j### t### b#### #b#e ##  r##k ##c# ito ##es#o# ##k# #o# #kha#kkr a#y a ##  ### b## a a#le ## ###w#re ###s ##k#s #o# an #u### ###  ##g####rw a # ###### l#  j##  j##r### ### ### ## ## a # ## a #  ###### #### ## ## ##   ### #### a ## a                                                     
the basic di##e##n#e#is th#s# hackers #u#ld t##ngs# #ra#k##s#b###k ###m#
## you want ## ## a #acker# #ee# ##a#i#g# If you want to ## a ###ck### #o r#ac #he #lt## ## n##sgr#up a## g#t ##ad# to ## #iv# to ##n ## th# #l##me# af#e# f##di#g ### you #re# t ## s#ar# a# #o# t#i## wo# #r## A#d#th## a mll I#m ioi#g to #a# a###t #########
you can vali##t##t#e#chall#n#e #i## a #O#BcRY##OaL#A#sF#i#
```

A partir d'ici nous cherchons des morceaux de phrases potentiels et passons à l'étape 2.



### Deuxième partie - texte déchiffré totalement - Python 2.7

Pour cette seconde étape, nous utilisons la commande suivante : 

```bash
directory/second_part> python2.7 cracker.py file.txt.crypt "what is a hacker?" 0
```

celle-ci se compose : 
- du fichier chiffré
- d'un morceau de phrase supposé
- de la ligne contenant ce morceau de phrase

cette première nous donne le résultat suivant :

```
what is a hacker?
the JArgon File c
there is a commun
the hAcker mind-s
there is aNother
the bAsic Differe
if yoU wanT to be
you cAn vaLidate
```

et ainsi de suite avec le premier texte partiellement déchiffré et le résultat des commandes du second code nous trouvons des morceaux de phrases de plus en plus long.

Finalement, avec la commande suivante : 


```bash
directory/second_part> python2.7 cracker.py file.txt.crypt "there is a community, a shared culture, of expert programmers" 2
```

Nous déchiffrons jusqu'à la partie du texte qui nous intéresse :

```
what Is a Hacker?
the Jargon File contains a bunch of definitions of the term "
there is a community, a shared culture, of expert programmers
the hacker mind-set is not confined to this software-hacker c
there is another group of people who loudly call themselves h
the basic difference is this: hackers build things, crackers
if you want to be a hacker, keep reading. If you want to be a
you can validate the challenge with : nOOBcRYPTOaLWAysFail
```

Et bien entendu, on valide le challenge : **nOOBcRYPTOaLWAysFail**





### NB

Ayant effectué les travaux sur des PC différents, nous avons deux versions de python.Les encodages et décodages en hexa et bytes ayant changés d'une version à l'autre, nous n'avons pas réussi à adapter nos fichiers sur une seule et même version de python.
