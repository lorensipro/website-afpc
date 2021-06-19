---
#
# Use the widgets beneath and the content will be
# inserted automagically in the webpage. To make
# this work, you have to use › layout: frontpage
#
layout: frontpage
slogan: Association Française pour la Programmation par Contraintes
header:
   image_fullwidth: header-schemas.jpg
   text: "
<p>L'AFPC (Association Française pour la Programmation par Contraintes) est association de loi 1901. Sa vocation est de réunir toutes les personnes s'intéressant, professionnellement ou non, à la <a href=\"http://fr.wikipedia.org/wiki/Programmation_par_contraintes\">programmation par contraintes</a> : son étude, ses fondements théoriques, ses applications, son évolution, son enseignement et sa diffusion. Les domaines couverts incluent : la programmation en logique, la programmation par contraintes et leurs extensions, la logique, les problèmes de satisfaction de contraintes discrets et continus (SAT, CSP), la programmation mathématique et l'optimisation combinatoire.</p>\r\n<p>L'AFPC est née le 21 juin 2004 de la fusion de l'AFPLC (Association Française de Programmation Logique et de Programmation par Contraintes) et de la communauté animée par la conférence JNPC (Journées sur la résolution pratique de Problèmes NP-Complets).</p>"
widget1:
  title: "La PPC, c'est quoi ?"
  url: '/ppc/'
  image: "widget-puzzle.png"
  text: "La programmation par Contraintes (PPC pour les intimes) est considérée comme le <strong>graal</strong> de la programmation. Vous décrivez votre problème et la PPC le résoud. Découvrez ce qui se cache derrière et pourquoi il s'agit d'un domaine très important et très actif en Intelligence Artificielle, depuis plus de 60 ans !"
widget2:
  title: "Les JFPC"
  url: '/jfpc/'
  image: "jfpc/jfpc-amphi-2015-thumb.png"
  text: "L'AFPC organise son évènement scientifique annuel autour des Journées Francophones de Programmation par Contraintes. Durant 3 à 4 jours, les chercheurs du domaine se rencontrent et échangent autour de leurs derniers travaux, qu'ils soient originaux ou pubiés récemment dans les meilleurs conférences internationales.  C'est aussi l'occasion pour les jeunes chercheurs du domaine de faire connaissance avec la communauté grâce à une forte convivialité qui entoure ces rencontres."
widget3:
  title: "Travaux autour de la PPC"
  url: '/ressources/'
  image: widget-travaux.png
  text: "La communauté francophone est très active au niveau international et ces journées sont aussi l'occasion de présenter les meilleurs résultats publiés dans les conférences internationales de renom."
#
# Use the call for action to show a button on the frontpage
#
# To make internal links, just use a permalink like this
# url: /getting-started/
#
# To style the button in different colors, use no value
# to use the main color or success, alert or secondary.
# To change colors see sass/_01_settings_colors.scss
#
callforaction:
  url: https:/https://www.i3s.unice.fr/jfpc_2021/
  text: Aller vers le site des JFPC 2021 >
  style: alert
permalink: /index.html
#
# This is a nasty hack to make the navigation highlight
# this page as active in the topbar navigation
#
homepage: true
---


