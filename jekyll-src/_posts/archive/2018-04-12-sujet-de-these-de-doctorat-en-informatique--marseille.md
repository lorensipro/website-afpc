---
layout: page
title_content: Sujet de th`ese de doctorat en informatique @ Marseille
title: Sujet de th`ese de doctorat en informati...
date_content: 2018-04-12 11:17:20.000000
tags:
  - archive
---
Titre : Vers une unification des algorithmes de résolution du problème de
satisfiabilité maximum



Aix-Marseille Université (www.univ-amu.fr)



Laboratoire d’Informatique et Systèmes (LIS – UMR 7020)



Equipe Contraintes, Algorithmes et Applications ( ́ www.lis-lab.fr/coala/)



Directeur de thèse : Djamal Habet



04 91 28 83 21



djamal.habet@univ-amu.fr





Résumé. Le problème de satisfiabilité maximum (Max-SAT) consiste à trouver une
interprétation des variables, d’une



formule propositionnelle sous forme normale conjonctive, qui maximise le
nombre de clauses satisfaites. Max-SAT est un problème NP-difficile et il est
l’une des versions d’optimisation du problème de satisfiabilité
propositionnelle (SAT).



Max-SAT possède plusieurs applications dans des domaines variés, qu’ils soient
académiques ou industriels, comme la coloration de graphes, max-clique, le
calcul de la largeur arborescente, le routage, la bio-informatique, la
synthèse de circuit, le diagnostic, etc.



Parmi les méthodes de résolution exactes pour Max-SAT, certaines approches se
distinguent en particulier. La première est basée sur des algorithmes de type
séparation et évaluation. Ils sont efficaces sur les instances aléatoires
[HLO07, LMP07, AH15a]. La seconde est basée sur des appels à un oracle SAT.
Les algorithms sous-jacents excellent sur les instances issues de problèmes
industriels portant sur des millions de variables [FM06, HMS11, KZFH12, MML14,
MDM14, NB14].



Les algorithmes de ces deux familles ont donc des performances divergentes
selon les caractéristiques des instances. Toutefois, ils partagent une mˆeme
opération centrale qui est celle de la recherche de sous-ensemble
inconsistants de clauses (ou cœurs inconsistants). Par contre, la détection et
le traitement de ces cœurs sont sensiblement différents d’une approche à une
autre : allant de l’application de la règle d’inférence par max-résolution à
l’ajout de contraintes de cardinalité et de l’application la propagation
unitaire simulée à l’appel à un oracle SAT. L’objectif de cette thèse est de
rapprocher ces deux familles d’algorithmes, qui sont développées séparément.
Il convient alors d’établir les relations entre les mécanismes de résolution
de ces deux familles. Par exemple, il est nécessaire d’étudier les liens entre
la transformation des cœurs inconsistants par la max-résolution et celui de
leur transformation par l’ajout de contraintes de cardinalité. Par ailleurs,
l’une des étapes sensibles dans les algorithmes séparation et évaluation est
l’apprentissage des transformations par inférence respectant des motifs
particuliers. La relation théorique entre ces motifs et la propagation
unitaire simulée a été mise en évidence par la propriété de l’UP-résilience
[AH15b]. Il reste toutefois nécessaire de concevoir des algorithmes capables
de vérifier efficacement cette propriété afin de généraliser cet
apprentissage.





Profil du candidat. Le candidat doit ˆetre diplˆomé (ou en cours de
validation) d’un Master 2 en Informatique (Bac+5) ou équivalent. De fortes
compétences en algorithmique sont nécessaires. Un bon niveau de programmation
en C/ C++ est un plus appréciable.



Date de but et lieu. Septembre/ octobre 2018, Marseille.





Modalités de candidature. Le dossier doit contenir les pièces suivantes :



— CV



— Relevés de notes M1 et M2 ainsi que le classement



— Lettre de motivation



— Lettre(s) de recommandation





L’envoi doit se faire sous forme de fichiers pdf à djamal.habet@univ-amu.fr
avant le 4 juin 2018.







Références





[AH15a] André Abramé and Djamal Habet. AHMAXSAT : Description and evaluation
of a branch and bound Max-SAT





solver. Journal on Satisfiability, Boolean Modeling and Computation, 9
:89–128, 2015.





[AH15b] André Abramé and Djamal Habet. On the resiliency of unit propagation
to max-resolution. In Qiang Yang and





Michael Wooldridge, editors, Proceedings of the 24th International Joint
Conference on Artificial Intelligence (IJCAI





2015), pages 268–274. AAAI Press, 2015.





[FM06] Zhaohui Fu and Sharad Malik. On solving the Partial MAX-SAT problem. In
Armin Biere and Carla P. Gomes,





editors, Proceedings of the 9th International Conference on Theory and
Applications of Satisfiability Testing (SAT





2006), volume 4121 of Lecture Notes in Computer Science, pages 252–265.
Springer Berlin Heidelberg, 2006.





[HLO07] Federico Heras, Javier Larrosa, and Albert Oliveras. MiniMaxSat : A
new weighted Max-SAT solver. In Jo ̃ao









Marques-Silva and Karem Sakallah, editors, Proceedings of the 10th
International Conference on Theory and Ap-





plications of Satisfiability Testing (SAT 2007), volume 4501 of Lecture Notes
in Computer Science, pages 41–55.









Springer Berlin / Heidelberg, 2007.





[HMS11] Federico Heras and Jo ̃ao Marques-Silva. Read-once resolution for
unsatisfiability-based Max-SAT algorithms. In





Toby Walsh, editor, Proceedings of the 22nd International Joint Conference on
Artificial Intelligence (IJCAI 2011),





pages 572–577. AAAI Press, 2011.





[KZFH12] Miyuki Koshimura, Tong Zhang, Hiroshi Fujita, and Ryuzo Hasegawa.
QMaxSAT : A Partial Max-SAT solver.





Journal on Satisfiability, Boolean Modeling and Computation, 8(1/2) :95–100,
2012.





[LMP07] Chu Min Li, Felip Manyà, and Jordi Planes. New inference rules for
Max-SAT. Journal of Artificial Intelligence





Research, 30 :321–359, 2007.





[MDM14] Ant ́onio Morgado, Carmine Dodaro, and Jo ̃ao Marques-Silva. Core-
guided MaxSAT with soft cardinality constraints.





In Barry O’Sullivan, editor, Proceedings of the 20th International Conference
on Principles and Practice of Constraint





Programming (CP 2014), volume 8656 of Lecture Notes in Computer Science, pages
564–573. Springer, 2014.





[MML14] Ruben Martins, Vasco Manquinho, and Inˆes Lynce. Open-WBO : A modular
MaxSAT solver,. In Carsten Sinz





and Uwe Egly, editors, Proceedings of the 17th International Conference on
Theory and Applications of Satisfiability





Testing (SAT 2014), volume 8561 of Lecture Notes in Computer Science, pages
438–445. Springer International





Publishing, 2014.





[NB14] Nina Narodytska and Fahiem Bacchus. Maximum satisfiability using core-
guided MaxSAT resolution. In Carla E.





Brodley and Peter Stone, editors, Proceedings of the 28th AAAI Conference on
Artificial Intelligence (AAAI 2014),





pages 2717–2723. AAAI Press, 2014.

