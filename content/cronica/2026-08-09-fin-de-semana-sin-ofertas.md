---
title: "[Título — algo sobre el silencio del fin de semana]"
date: 2026-08-09T00:00:00+02:00
draft: true
# ——— El sello de bitácora ———
dia: 14         # día N del experimento (1 = 27 de julio)
tarifa: 45      # $/hora vigente ese día (tramo 1)
encargos: 0     # encargos acumulados
cobrado: 0      # euros cobrados acumulados
estado: "en curso"
resumen: "[Una línea citable — p.ej. algo sobre quién libra el fin de semana, ¿la IA o quien le da trabajo?]"
---

<!-- El bucle en la primera línea, sin preámbulo. -->
[Tu frase de arranque: llevas desde el viernes sin una sola alerta en el correo.]

## El tablón de esta semana

Alertas de correo por día, de las [26 ofertas registradas](/ofertas/) hasta el 7 de agosto{{< nota >}}Recuento de `en_email: "si"` en `data/ofertas.yaml`, día a día.{{< /nota >}}:

| Fecha | Día | Alertas |
|---|---|---|
| 28 jul | martes | 3 |
| 29 jul | miércoles | 2 |
| 30 jul | jueves | 5 |
| 31 jul | viernes | 3 |
| 1 ago | sábado | 1 |
| 2 ago | domingo | 0 |
| 3 ago | lunes | 1 |
| 4 ago | martes | 5 |
| 5 ago | miércoles | 1 |
| 6 ago | jueves | 3 |
| **7 ago** | **viernes** | **2 — última alerta recibida** |
| 8 ago | sábado | 0 |
| 9 ago | domingo | 0 |

Comprobado que no es un problema de filtro: sin nada en spam.{{< comose >}}Comprobación manual en Gmail el 9 de agosto de 2026: carpeta de spam vacía.{{< /comose >}}

Comprobado también en el propio listado público de RentAHuman, a mano: la última oferta publicada es de hace 2 días (viernes 7), y las cuatro anteriores a esa, de hace 3 (jueves 6). Nada nuevo publicado desde entonces.{{< comose >}}Comprobación manual en el listado de RentAHuman el 9 de agosto de 2026, mirando la fecha relativa de publicación de las últimas entradas. No se usan aquí las 115 ofertas del volcado de `data/ofertas.yaml` [commit `451f079`]: todas quedaron fechadas el día del volcado (9 de agosto), no el día real en que aparecieron en el listado, así que no sirven para esta comprobación.{{< /comose >}}

## Lo que pasó (y lo que no)

Dos hechos, no uno:

1. El correo dejó de traer alertas el sábado 8 y el domingo 9.
2. El propio listado público dejó de recibir encargos nuevos desde el viernes 7 — antes incluso de que se notara el silencio en el correo.

[Aquí tu lectura: el corte no está en el reparto de las alertas, está aguas arriba, en quién publica encargos. ¿Qué te sugiere eso sobre quién hay detrás de RentAHuman?]

Un matiz que no conviene callar: ya hubo un amago la semana anterior — el sábado 1 solo una alerta (frente a una media entre semana de casi 3), y el domingo 2 ninguna, de ningún tipo. [¿Lo tomas como que el patrón ya venía insinuándose, o como ruido de muestra pequeña?]

## Lo que queda abierto

- Es la comprobación de un solo fin de semana. Para que sea patrón y no anécdota falta verlo repetirse.
- No se sabe la hora exacta en que se cortó el viernes: la web de RentAHuman da fecha relativa ("hace 2 días"), no timestamp.
- [Próximo paso que te comprometes a hacer: ¿revisar el listado el viernes y el domingo que vienen, antes de dar esto por confirmado?]

## Las cifras

<!-- Recuerda actualizar también data/estado.yaml y static/datos/serie-diaria.csv si procede -->
