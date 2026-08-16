---
title: "¿Acierta la máquina que clasifica por mí?"
resumen: "Le doy al clasificador las ofertas que yo ya había clasificado a mano, sin enseñarle mis respuestas, y publico en cuántas coincide y en cuáles no."
layout: calibracion
date: 2026-08-09
lastmod: 2026-08-16
---

Un modelo de lenguaje clasifica las ofertas del listado público aplicando [mis criterios publicados](https://github.com/GusTempranillo/mepagaunbot/blob/main/data/criterios.yaml). Eso plantea un problema evidente: si nadie comprueba al que mide, el resultado deja de ser «cuántas ofertas dejan entrar a alguien de España» y pasa a ser «cuántas cree un modelo que dejan entrar».

Prometer que lo reviso todo no resuelve nada, porque no se puede comprobar desde fuera y porque una revisión que no puedo sostener acabaría siendo un sello de goma. Así que en vez de prometer, mido.

Las ofertas que la plataforma me manda por correo son las únicas que clasifiqué a mano, una a una, antes de que existiera el clasificador. Son un patrón etiquetado gratis. Se las doy al modelo sin enseñarle mis respuestas, comparo, y lo que sale es esto.

Conviene decir lo que este número **no** demuestra. Son pocas ofertas. Son las de correo, que llegan con el asunto «matches your skills» y por tanto son las fáciles: el listado público es más variado y más raro, así que esta tasa es una cota optimista.

Lo que sí se puede leer es la **forma** de los desacuerdos, que está abajo entera, uno por uno y con el veredicto al lado. Cuando el que se equivocó fui yo, lo digo y corrijo la fila. Cuando todavía no lo he mirado, pone «pendiente»: prefiero publicar un hueco a publicar un veredicto que no he dado.

## Dos correcciones, del 15 de agosto de 2026

**Esta página midió durante cinco días un clasificador que no estaba funcionando.** El prompt que se le da al modelo está escrito en dos sitios: el clasificador de verdad y esta prueba. El 10 de agosto cambié una regla en el primero y no en el segundo, así que del 10 al 15 el número publicado aquí correspondía a una versión que ya no clasificaba nada. Ya están sincronizados, y el arreglo de fondo —sacar el prompt a un fichero del repositorio para que los dos lo lean del mismo sitio— está pendiente.

**Y he cambiado de modelo.** No por corazonada: medí tres sobre este mismo patrón y con el mismo prompt.

| | acuerdo | tokens por oferta | de ellos, razonar |
|---|---|---|---|
| `kimi-k2.6` (el de antes) | 89,4 % | 7284 | 3534 |
| **`kimi-k3` esfuerzo bajo** | **89,8 %** | **4043** | **27** |
| `kimi-k3` esfuerzo alto | 89,8 % | 4209 | 182 |

El que uso ahora acierta igual o algo más, cuesta un 44 % menos y razona ciento treinta veces menos. Subir el esfuerzo no cambia ni una sola clasificación: lo que el modelo caro hacía con 3534 tokens de razonamiento —contar caracteres a mano, redactar tres títulos y descartar dos— no mejoraba la respuesta.

Digo esto aquí porque cambiar el modelo cambia lo que mide esta página, y un número sin decir de qué es no vale nada.

## La pregunta única, del 16 de agosto de 2026

Hasta ayer le hacía al modelo dos preguntas sueltas: «¿me dejan entrar?» y «¿puedo hacerla?», cada una con su propio juicio. Desde hoy le hago una sola —«¿puedo optar a esta oferta, y si no, por qué?»— y de la respuesta salen los dos campos de siempre, calculados por código: si el obstáculo es de geografía o papeleo, cierra «¿me dejan entrar?»; si es de idioma, habilidad o aparato, cierra «¿puedo hacerla?». Sin obstáculo, las dos son «sí». Es lo mismo que ya decía [Método](/metodo/) que hacía la web, aplicado también al clasificador.

Esto tiene un efecto en el número de abajo que conviene explicar, porque si no parece que la máquina haya empeorado y no es así. `compatible` cae de 80,6 % a 52,9 %. La causa, en catorce de los dieciséis desacuerdos, es que antes yo marcaba a veces el mismo problema en las dos columnas a la vez —por ejemplo, «exige un número de teléfono de EE. UU.» como un «no» en las dos—, y ahora la pregunta única solo puede contarlo una vez. La respuesta que se publica, «¿puedo optar?», no cambia en ninguno de esos casos: seguía saliendo «no» por la otra columna.

Hay una excepción que sí es un límite real, no cosmético: dos ofertas pedían a la vez un obstáculo de geografía **y** uno de idioma, dos problemas independientes. La pregunta única solo puede reportar uno, así que el segundo desaparece del todo del campo que le tocaba. La respuesta final sigue siendo correcta —la primera barrera ya basta para decir que no—, pero si algún día esa primera barrera dejara de aplicar, la ficha diría que sí puedo cuando en realidad tampoco, por el idioma. Es un límite del diseño que decidí aceptar en vez de complicar la pregunta otra vez, y queda anotado en cada una de las dos filas que lo tienen.

El resto —un desacuerdo de disponible_es y uno de modalidad, además de tres que siguen sin veredicto— son casos normales de la clasificación, no del cambio de pregunta.
