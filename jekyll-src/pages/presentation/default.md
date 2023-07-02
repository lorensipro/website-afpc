---
layout: page
show_meta: false
title: "Présentation de l'AFPC"
slogan: "Présentation de l'AFPC"
subheadline: "Association Française de programmation par Contraintes"
teaser: "Rôles et Attributions de l'AFPC, société scientifique"
header:
   image_fullwidth: "header_homepage_13.jpg"
permalink: "/presentation/"
---

{% for contenu in site.data.presentation.content %}
   {{ contenu }}
{% endfor %}
