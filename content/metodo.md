---
title: "Cómo se hace esto"
resumen: "Las reglas de la casa: qué publico, qué no, cómo lo compruebo y qué hago cuando me equivoco."
date: 2026-07-27
rotulo: "Método · Las reglas de la casa"
---

Este proyecto tiene un problema de credibilidad de origen: soy juez y parte. Opero un agente de inteligencia artificial y a la vez me vendo como mano de obra a las inteligencias artificiales. Cualquiera puede sospechar que voy a contar lo que me convenga. Estas son las reglas que me lo impiden.

## Las reglas van antes que los resultados

El calendario de tarifas se publicó y se fechó antes del primer encargo. Las hipótesis, también. No es un adorno: es lo que impide que el resultado se ajuste a la conclusión.

Piénsalo al revés. Si fuera bajando el precio hasta que alguien picara, podría publicar la cifra exacta a la que me contrataron y presentarla como hallazgo. Sería mentira: esa cifra la habría elegido yo, no el mercado. Con el descenso cerrado de antemano, la cifra la elige el que compra.

## Cada afirmación con su fuente y su copia

Todo dato lleva enlace a la fuente y enlace a la copia archivada. Si mañana RentAHuman cambia una cifra, la captura sigue ahí. No pido que se me crea: pido que se me compruebe.

## Diez minutos al día, haya o no haya nada

Registro diario de las ofertas: las que llegan a mi bandeja y las del listado público. De cada encargo que acepte, el tiempo que me lleva de principio a fin. Un día sin ofertas se anota igual. El cero es el resultado más probable de todo esto y omitirlo sería el sesgo más fácil de colar.

## La máquina propone, yo firmo

Cada día aparecen más de cien ofertas en el listado público. Clasificarlas
todas a mano —si dejan entrar a alguien de España, si puedo hacerlas yo, si
son remotas o presenciales— me llevaría más tiempo del que tengo, y el día
que no llegue empezaría a mirar solo las que me parecen interesantes. Eso
sería el sesgo entrando por la puerta de atrás.

Así que lo hace un modelo de lenguaje. Pero no decide: propone.

Mis criterios están escritos en un fichero del repositorio,
[`data/criterios.yaml`](https://github.com/GusTempranillo/mepagaunbot/blob/main/data/criterios.yaml),
público y fechado. Dice dónde vivo, hasta dónde me desplazo, qué idiomas
manejo, qué aparatos tengo y qué sé hacer. El modelo recibe ese fichero
entero y una oferta, y devuelve una propuesta de clasificación. Aplica mis
reglas; no inventa las suyas. Y si el fichero cambia alguna vez, el
historial del repositorio dice cuándo y en qué.

Esa propuesta no se publica. Se queda esperando en la hoja de cálculo hasta
que la miro, la corrijo si hace falta y la firmo una por una. Solo entonces
llega a los datos de este sitio. Cuando el modelo no lo tiene claro, tiene
orden de dejar la casilla en blanco y escribirme la pregunta, que es
justamente lo que hace un ayudante honesto.

El mismo modelo hace además otra cosa que no es un juicio: traducir. Casi
todas las ofertas llegan escritas en inglés, y muchas con títulos que no
dicen nada de lo que hay que hacer, así que de cada una escribe un título y
un resumen de dos o tres frases en español.

Eso sí se publica sin esperar mi firma, y quiero explicar por qué, porque es
la única cosa de este sitio que sale sin que yo la haya leído antes. Un
resumen no decide nada: no entra en ninguna hipótesis, no cuenta en ningún
denominador, no dice si me dejan entrar ni si puedo hacerla. Solo sirve para
que la lista se pueda leer. Y una lista de cien ofertas al día en inglés que
espera a que yo la repase es una lista que nadie lee nunca. A cambio, hasta
que paso por la fila el resumen va marcado como *sin repasar*, el título
original se queda debajo sin tocar para que cualquiera compare, y si me
encuentro uno mal escrito lo corrijo yo en la hoja y al día siguiente sale
corregido.

Lo que no sale sin firma sigue siendo lo que juzga: los cinco campos de
clasificación. Y son fichas de un listado, no narración: la crónica la sigo
escribiendo yo.

Dos cosas que quiero dejar claras. La primera: la oferta se registra
siempre, esté firmada o no. Lo que espera mi firma es el juicio, nunca el
recuento; si no, el denominador de la [hipótesis 5](/registro-previo/)
dependería de mi ritmo de revisión, y eso lo invalidaría. La segunda: las
ofertas que me llegan al correo las he clasificado yo a mano, una a una,
desde el primer día.

Lo que el modelo no toca es si un encargo me parece indigno. Esa es la
hipótesis 7, va de mí y no de la plataforma, y no pienso delegarla.

## Lo que no hago

No entro en la mensajería interna de RentAHuman. No sondeo el sistema a ver qué pasa. No me apunto a programas de referidos ni a nada que me pague por traer gente. No cito a nadie sin su permiso escrito. No especulo sobre las intenciones de nadie: describo lo que hace.

## Los errores se tachan, no se borran

Cuando me equivoco en algo sustancial, el error va numerado a [su página](/errores/), tachado y con la corrección al lado. Sin borrar el original. Las erratas se arreglan y ya está; lo que se registra son las conclusiones mal escritas.

Corregirse a la vista vale más que acertar a la primera. Un sitio sin errores publicados no es un sitio sin errores: es un sitio que no los cuenta.

## La crónica la escribo yo

Uso herramientas de inteligencia artificial para investigar, para ordenar datos y para la carpintería de este sitio. La crónica no. Cada palabra de lo que leas aquí como narración la he escrito yo. Si alguna vez dejara de ser cierto, lo diría en esta misma página antes que en ninguna otra.
