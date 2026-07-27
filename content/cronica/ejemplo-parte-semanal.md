---
title: "EJEMPLO — plantilla del parte semanal (no publicar)"
date: 2026-07-30T09:00:00+02:00
draft: true
dia: 4
tarifa: 45
encargos: 0
cobrado: 0
estado: "en curso"
resumen: "Este es el hueco de la línea citable: una frase que un tertuliano pueda leer en voz alta."
---

Este archivo es una plantilla de ejemplo con `draft: true`: **no se publica**
y puede borrarse. Muestra cómo queda el sello y qué estructura tiene un parte.

La primera línea del post es el titular, sin preámbulo. Después, las
secciones que apliquen:

## El tablón de esta semana

Ofertas aparecidas, cuántas accesibles desde España, a cuáles se optó.

## Lo que pasó (y lo que no)

Lo que no pasa también es dato.

## Encargos absurdos

Solo si los hay; si no, se borra la sección.

## Las cifras

Y al actualizar el post, actualizar también `data/estado.yaml` y
`static/datos/serie-diaria.csv`.
