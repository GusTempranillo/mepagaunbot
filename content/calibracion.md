---
title: "¿Acierta la máquina que clasifica por mí?"
resumen: "Le doy al clasificador las ofertas que yo ya había clasificado a mano, sin enseñarle mis respuestas, y publico en cuántas coincide y en cuáles no."
layout: calibracion
date: 2026-08-09
lastmod: 2026-08-09
---

Un modelo de lenguaje clasifica las ofertas del listado público aplicando [mis criterios publicados](https://github.com/GusTempranillo/mepagaunbot/blob/main/data/criterios.yaml). Eso plantea un problema evidente: si nadie comprueba al que mide, el resultado deja de ser «cuántas ofertas dejan entrar a alguien de España» y pasa a ser «cuántas cree un modelo que dejan entrar».

Prometer que lo reviso todo no resuelve nada, porque no se puede comprobar desde fuera y porque una revisión que no puedo sostener acabaría siendo un sello de goma. Así que en vez de prometer, mido.

Las ofertas que la plataforma me manda por correo son las únicas que clasifiqué a mano, una a una, antes de que existiera el clasificador. Son un patrón etiquetado gratis. Se las doy al modelo sin enseñarle mis respuestas, comparo, y lo que sale es esto.

Conviene decir lo que este número **no** demuestra. Son pocas ofertas. Son las de correo, que llegan con el asunto «matches your skills» y por tanto son las fáciles: el listado público es más variado y más raro, así que esta tasa es una cota optimista. Y `modalidad` no mide nada aquí, porque las veintitrés son remotas y acertar sin variación no tiene mérito.

Lo que sí se puede leer es la **forma** de los desacuerdos, que está abajo entera, uno por uno y con el veredicto al lado. Cuando el que se equivocó fui yo, lo digo y corrijo la fila.
