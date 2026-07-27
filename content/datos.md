---
title: "Datos"
resumen: "Las cifras del experimento: serie diaria del perfil, descenso de tarifa prerregistrado y datos descargables."
---

Aquí viven las cifras del experimento. Todo lo que se afirma en la crónica
sale de registros fechados; esta página los reúne y los deja descargar.

## Las seis cifras que persigue el experimento

1. **Euros por hora real**, contando el tiempo invisible (buscar, postularse,
   esperar, perseguir cobros). Sin eso, «gané 50 €» es una cifra falsa.
2. **Distribución de tipos de tarea**: para qué quieren las máquinas a los
   humanos.
3. **Porcentaje de ofertas accesibles desde España.**
4. **Tasa de impago**: encargos aceptados frente a cobrados.
5. **Días hasta la primera oferta** y hasta el primer cobro.
6. **Volumen de demanda**: ofertas aparecidas por semana.

Todavía no hay datos suficientes para ninguna de las seis: el experimento
arrancó el 27 de julio de 2026. El primer cierre semanal es el viernes 1 de
agosto. Esta página se actualiza con cada publicación.

## La serie diaria del perfil

Lectura diaria del registro público del perfil (vía la API que la propia
plataforma documenta). La fila del 27 de julio es el estado en el minuto de
arranque, las 09:00 de Madrid.

| Fecha | Visitas | Encargos | Nota | Reseñas | Tarifa | ¿«Verificado»? |
|---|---|---|---|---|---|---|
| 2026-07-27 | 1 | 0 | 0 | 0 | $45/h | No |

**Aviso de método:** el contador de visitas marcaba ya 1 en el minuto cero, y
está pendiente comprobar si las visitas propias suman. Hasta resolverlo, la
columna de visitas se considera provisional. Lo de «Verificado» entre comillas
tiene su propia historia, que contará la crónica: en esta plataforma no
significa que hayan comprobado tu identidad.

**Descarga:** [serie-diaria.csv](/datos/serie-diaria.csv)

## El descenso de tarifa prerregistrado {#descenso}

Publicado antes de que ocurra nada, para que el primer encargo —si llega— no
sea una anécdota sino una medición con calendario declarado. La pregunta que
responde: **¿a qué precio empieza a comprarse un ser humano?**

| Tramo | Fechas | Tarifa |
|---|---|---|
| 1 | 27 jul – 16 ago | **$45/hora** |
| 2 | 17 ago – 6 sep | $28/hora |
| 3 | 7 sep – 27 sep | $16/hora |
| 4 | 28 sep – 25 oct | $9.24/hora — el suelo que la plataforma fija para España |

Si no llega ningún encargo ni en el suelo, es un resultado limpio igualmente.

## Datos abiertos

Los registros agregados y anonimizados se publican en formato CSV para que
cualquiera —periodista, investigador o curioso— pueda rehacer las cuentas. Es
la diferencia entre «dice que» y «según los datos de». Si usas los datos,
cita la fuente y avisa si encuentras un error: [va directo a la página de
errores](/errores/).
