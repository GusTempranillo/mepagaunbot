# mepagaunbot.eu

Repositorio del blog **Me paga un bot** — crónica de investigación en primera
persona de Gustavo Pérez Tempranillo: 90 días (27-jul → 25-oct de 2026)
ofreciéndose como mano de obra a agentes de IA, con registro previo, pruebas
archivadas y errores en público.

**Transparencia:** la carpintería de este sitio (plantillas, estilos,
estructura y páginas informativas) la construyó un asistente de IA por encargo
del autor. Los textos de la crónica (`content/cronica/`) los escribe el autor.
Las ofertas del listado público las clasifica un modelo de lenguaje aplicando
criterios publicados (`data/criterios.yaml`), y su acierto se mide en
`/calibracion/`. Este repositorio es público a propósito: su historial de
cambios es parte de la cadena de pruebas del proyecto.

- Generador: [Hugo](https://gohugo.io/) 0.162.0 extended (tema propio, sin dependencias).
- Alojamiento: GitHub Pages, desplegado por Actions en cada push a `main` y,
  además, cada día a las 00:23 UTC (el día en curso y la tarifa vigente los
  calcula Hugo al construir; sin esa cita diaria el marcador se congelaría).
- Datos de ofertas: workflows de n8n, fuera de este repositorio, que escriben
  en él por Git (ver «Las ofertas: quién escribe qué»).
- Coste: 0 €/mes.

---

## Operación diaria y semanal

### Publicar un parte o un hallazgo

Antes de tocar nada, `git pull`: n8n sube commits a `main` por su cuenta
(el volcado diario de ofertas y las firmas del panel), y editar sobre un
árbol desactualizado acaba en conflictos.

```bash
git pull
hugo new cronica/AAAA-MM-DD-titulo-corto.md
```

Se crea con la plantilla de `archetypes/cronica.md`. Rellenar el **sello**
(`dia`, `tarifa`, `encargos`, `ganado` y/o `cobrado`, `estado`) y el `resumen`
(la línea citable). `ganado` son los dólares acumulados en RentAHuman;
`cobrado`, los euros ya retirados al banco. Escribir. Cambiar `draft: true` →
`false`. La fecha del `date` no puede ir por delante de la hora de la build,
o Hugo descarta el post sin avisar. Y:

```bash
git add -A && git commit -m "Parte semana N" && git push
```

GitHub Actions construye y publica solo (2-3 minutos). Vista previa local, si
se quiere: `hugo server -D` y abrir http://localhost:1313

### Al publicar, actualizar también

1. `data/estado.yaml` — `encargos`, `ganado` (saldo acumulado en RentAHuman,
   sin retirar), `cobrado` (euros ya retirados al banco) y `actualizado`
   (`dd-mm-aaaa`). Alimenta el marcador de la portada y de `/datos/`. Los
   `tramos` de tarifa no se tocan: están registrados de antemano.

`static/datos/serie-diaria.csv` no se actualiza en cada publicación. La
lectura del perfil no se puede automatizar (se entra con Google y no hay API
key) y tampoco se rellena a mano. Lo que no se leyó se deja en blanco: no se
inventa ni se interpola.

`data/ofertas.yaml` **no se edita a mano**: lo reescribe cada día el volcado
de n8n desde la hoja de cálculo. Ver la sección siguiente.

### Las ofertas: quién escribe qué

La **hoja de cálculo** manda; el repositorio es su reflejo. Lo que se cambie a
mano en `data/ofertas.yaml` se pierde en el siguiente volcado. Para corregir
una oferta, se corrige en la hoja o en el panel de firmas.

- **Volcado diario** (n8n): reescribe `data/ofertas.yaml` desde la hoja; son
  los commits «Vuelca las hojas de RentAHuman a ofertas.yaml». De ahí salen la
  página `/ofertas/`, el CSV `/datos/ofertas.csv` (se genera solo al
  construir) y las cifras de las hipótesis 4 y 5.
- **Clasificación asistida** (n8n): un modelo de lenguaje propone, para las del
  listado público, `disponible_es`, `compatible`, sus motivos y el título y el
  resumen en español. Otro workflow traduce las que solo llegaron por correo.
  Las reglas están en `data/criterios.yaml` y `data/prompt_clasificador.yaml`,
  que los workflows leen de `main` por la API de GitHub: editar esos ficheros y
  hacer push cambia lo que clasifica el modelo, y por eso la calibración
  (`data/calibracion.yaml`, `/calibracion/`) se rehace cuando cambia el modelo
  o la pregunta.
- **Firmas** (el autor): las ofertas de bandeja y la modalidad las firma él, una
  a una, en `paneles/ofertas.html`. Ver `paneles/LEEME.md`.
- **Aviso de ofertas caídas**: `scripts/avisar_ofertas_caidas.py`, por cron a
  diario, manda un correo a través de un webhook de n8n cuando una oferta cae
  (404) o caduca. Apunta lo avisado en `data/.avisadas-caidas.txt`. La URL del
  webhook lleva un token y vive fuera del repositorio, en la variable
  `AVISOS_WEBHOOK_URL` o en `~/.config/mepagaunbot/webhook-avisos.url`.

### Piezas de la plantilla de artículo

Todas se escriben dentro del markdown de la crónica. Hay una página de muestra
con todas juntas en `content/cronica/demo-plantilla.md` (borrador, no se
publica): arráncala con `hugo server -D` y míralas funcionando.

**Enlace probatorio** = «fuente (archivo)»:

```
{{</* fuente url="https://original" archivo="https://web.archive.org/..." */>}}texto{{</* /fuente */>}}
```

**Nota al margen** (se numera sola, sin JavaScript; en móvil se intercala):

```
…una tarifa que no elegí yo.{{</* nota */>}}Me pusieron precio sin preguntar.{{</* /nota */>}}
```

**Cita con su procedencia archivada** (chips original · wayback · copia local):

```
{{</* cita quien="AUP · Prohibited Uses · 20 jul 2026" original="https://…" wayback="https://…" local="/pruebas/aup.pdf" */>}}
Texto citado.
{{</* /cita */>}}
```

**Captura enmarcada**, con pie y cadena de pruebas:

```
{{</* figura src="/pruebas/x.png" alt="…" pie="Qué se ve." original="…" wayback="…" local="…" */>}}
```

**Caja de método**, para explicar de dónde sale una cifra:

```
{{</* comose */>}}El porcentaje sale de contar…{{</* /comose */>}}
```

**Rectificación a la vista**, tachada y enlazada a `/errores`:

```
{{</* rect id="E1" nuevo="sí la tiene, en dos niveles" */>}}No tiene taxonomía propia{{</* /rect */>}}
```

**Ritmo de periódico:** dos columnas, o un bloque de margen a margen.

```
{{</* columnas */>}}
Primera columna.
{{</* col */>}}
Segunda columna.
{{</* /columnas */>}}

{{</* ancho */>}}
(una tabla, una figura o lo que sea, a todo lo ancho)
{{</* /ancho */>}}
```

---

## El registro previo (sellado)

`content/registro-previo.md` contiene las siete hipótesis y el calendario de
tarifas. Se publicó y selló el 28 de julio de 2026:

- **OpenTimestamps:** `content/registro-previo.md.ots`, con confirmación en
  Bitcoin (bloques 960020 y 960023, commit `c898f3c`).
- **Wayback:** copia del 29 de julio de 2026.
- Los enlaces del sello viven en `data/sellos.yaml` y no dentro del documento:
  añadirlos allí habría cambiado el archivo y roto su propio sello.

**El archivo no se toca, ni una coma.** El `.ots` certifica su SHA-256 exacto,
`64b96059c5b229740d9397d0e1481376feee6f6da24f3a6c9a0506d40f635b63`, y
`.gitattributes` lo marca como binario para que Git no le cambie ni los finales
de línea. Se comprueba con:

```bash
sha256sum content/registro-previo.md
ots verify content/registro-previo.md.ots   # requiere opentimestamps-client
```

Si algo del registro resulta estar mal, se rectifica en `data/errores.yaml`
(como E6, la «cláusula (w)» que no existía), nunca editando el documento
sellado. Ya pasó una vez: el 18 de septiembre de 2026 se editó, el sello dejó de
verificar y hubo que restaurarlo (commit `508027d`).

---

## Referencia: cómo está montado el alojamiento

Ya está hecho; se deja escrito por si hay que rehacerlo.

### Repositorio y Pages

El repositorio es público: `github.com/GusTempranillo/mepagaunbot`. En
**Settings → Pages**: Source = «GitHub Actions», Custom domain =
`mepagaunbot.eu` y Enforce HTTPS.

### DNS en CDMON

Para el dominio `mepagaunbot.eu`:

| Tipo | Nombre/Host | Valor |
|---|---|---|
| A | @ (raíz) | 185.199.108.153 |
| A | @ (raíz) | 185.199.109.153 |
| A | @ (raíz) | 185.199.110.153 |
| A | @ (raíz) | 185.199.111.153 |
| AAAA | @ (raíz) | 2606:50c0:8000::153 |
| AAAA | @ (raíz) | 2606:50c0:8001::153 |
| AAAA | @ (raíz) | 2606:50c0:8002::153 |
| AAAA | @ (raíz) | 2606:50c0:8003::153 |
| CNAME | www | gustempranillo.github.io |

(Si CDMON no permite varios registros A con el mismo nombre en una sola
entrada, se crean como registros separados. El fichero `static/CNAME` ya está
en el repo: no tocarlo.)

### Opcional: newsletter

Cuenta gratuita en [Buttondown](https://buttondown.com) (hasta 100
suscriptores) y poner la URL pública en `hugo.toml` → `params.newsletter`. El
enlace aparece solo en la portada.
