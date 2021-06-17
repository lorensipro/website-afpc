---
#
# Use the widgets beneath and the content will be
# inserted automagically in the webpage. To make
# this work, you have to use › layout: frontpage
#
layout: frontpage
header:
   image_fullwidth: header-schemas.jpg
   text: "
<p>L'AFPC (Association Française pour la Programmation par Contraintes) est association de loi 1901. Sa vocation est de réunir toutes les personnes s'intéressant, professionnellement ou non, à la <a href=\"http://fr.wikipedia.org/wiki/Programmation_par_contraintes\">programmation par contraintes</a> : son étude, ses fondements théoriques, ses applications, son évolution, son enseignement et sa diffusion. Les domaines couverts incluent : la programmation en logique, la programmation par contraintes et leurs extensions, la logique, les problèmes de satisfaction de contraintes discrets et continus (SAT, CSP), la programmation mathématique et l'optimisation combinatoire.</p>\r\n<p>L'AFPC est née le 21 juin 2004 de la fusion de l'AFPLC (Association Française de Programmation Logique et de Programmation par Contraintes) et de la communauté animée par la conférence JNPC (Journées sur la résolution pratique de Problèmes NP-Complets).</p>"
widget1:
  title: "La PPC, c'est quoi ?"
  url: '/ppc/'
  image: "widget-puzzle.png"
  text: 'Every good portfolio website has a blog with fresh news, thoughts and develop&shy;ments of your activities. <em>Feeling Responsive</em> offers you a fully functional blog with an archive page to give readers a quick overview of all your posts.'
widget2:
  title: "Les JFPC"
  url: '/jfpc/'
  image: "jfpc/jfpc-amphi-2015-thumb.png"
  text: '<em>Feeling Responsive</em> is heavily customizable.<br/>1. Language-Support :)<br/>2. Optimized for speed and it&#39;s responsive.<br/>3. Built on <a href="http://foundation.zurb.com/">Foundation Framework</a>.<br/>4. Seven different Headers.<br/>5. Customizable navigation, footer,...'
widget3:
  title: "Travaux autour de la PPC"
  url: '/ressources/'
  image: widget-travaux.png
  text: '<em>Feeling Responsive</em> is free and licensed under a MIT License. Make it your own and start building. Grab the <a href="https://github.com/Phlow/feeling-responsive/tree/bare-bones-version">Bare-Bones-Version</a> for a fresh start or learn how to use it with the <a href="https://github.com/Phlow/feeling-responsive/tree/gh-pages">education-version</a> with sample posts and images. Then tell me via Twitter <a href="http://twitter.com/phlow">@phlow</a>.'
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


