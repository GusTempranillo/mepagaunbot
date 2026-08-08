# mepagaunbot.eu

Repositorio del blog **Me paga un bot** — crónica de investigación en primera
persona de Gustavo Pérez Tempranillo: 90 días (27-jul → 25-oct de 2026)
ofreciéndose como mano de obra a agentes de IA, con registro previo, pruebas
archivadas y errores en público.

**Transparencia:** la carpintería de este sitio (plantillas, estilos,
estructura y páginas informativas) la construyó un asistente de IA por encargo
del autor. Los textos de la crónica (`content/cronica/`) los escribe el autor.
Este repositorio es público a propósito: su historial de cambios es parte de
la cadena de pruebas del proyecto.

- Generador: [Hugo](https://gohugo.io/) 0.162.0 extended (tema propio, sin dependencias).
- Alojamiento: GitHub Pages, desplegado por Actions en cada push a `main`.
- Coste: 0 €/mes.

---

## Operación diaria y semanal

### Publicar un parte o un hallazgo

```bash
hugo new cronica/2026-08-06-titulo-corto.md
```

Se crea con la plantilla de `archetypes/cronica.md`. Rellenar el **sello**
(`dia`, `tarifa`, `encargos`, `cobrado`, `estado`) y el `resumen` (la línea
citable). Escribir. Cambiar `draft: true` → `false`. Y:

```bash
git add -A && git commit -m "Parte semana N" && git push
```

GitHub Actions construye y publica solo (2-3 minutos). Vista previa local, si
se quiere: `hugo server -D` y abrir http://localhost:1313

### Al publicar, actualizar también

1. `data/estado.yaml` — encargos y cobrado acumulados (alimenta la caja de la
   portada).
2. `static/datos/serie-diaria.csv` — una fila por día con la lectura del
   endpoint del perfil.
3. La tabla de la serie en `content/datos.md` (misma información que el CSV).
4. `data/ofertas.yaml` — una entrada por oferta vista, del listado y de la
   bandeja. Las nueve primeras columnas salen de la propia alerta; las dos
   últimas, `disponible_es` y `motivo`, las decide el autor. De ahí salen la
   página `/ofertas/`, el CSV `/datos/ofertas.csv` (se genera solo al
   construir) y el numerador y el denominador de la hipótesis 5.

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
{{</* cita quien="AUP · cláusula (w) · 20 jul 2026" original="https://…" wayback="https://…" local="/pruebas/aup.pdf" */>}}
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

## El registro previo (pendiente, una sola vez)

`content/registro-previo.md` contiene las siete hipótesis y el calendario de
tarifas, ya con las cifras del autor. Antes del post cero:

1. Última lectura. **Después del sello no se toca ni una coma:** cualquier
   cambio invalida la prueba.
2. `git add -A && git commit -m "Registro previo" && git push`
3. **Sello OpenTimestamps** (prueba de fecha, independiente de este servidor):

   ```bash
   pip install opentimestamps-client
   ots stamp content/registro-previo.md
   git add content/registro-previo.md.ots && git commit -m "Sello OTS" && git push
   ```

   Uno o dos días después, cuando el sello haya entrado en un bloque de Bitcoin:

   ```bash
   ots upgrade content/registro-previo.md.ots
   ots verify content/registro-previo.md.ots
   ```

   y commit del `.ots` actualizado. Sin este segundo paso el sello se queda a medias.
4. **Sello Wayback**, cuando la página esté en línea: abrir
   `https://web.archive.org/save/https://mepagaunbot.eu/registro-previo/` y
   guardar el enlace resultante en la sección «Sellado» de la página.

---

## Puesta en marcha (una sola vez)

### 1. Subir a GitHub

Crear en github.com un repositorio **público** llamado `mepagaunbot` (sin
README inicial) y, desde esta carpeta:

```bash
git remote add origin git@github.com:TU_USUARIO/mepagaunbot.git
git push -u origin main
```

### 2. Activar Pages

En el repositorio: **Settings → Pages → Source: «GitHub Actions»**. Después,
en la misma pantalla, **Custom domain: `mepagaunbot.eu`** (crea la
verificación) y, cuando el DNS esté propagado, marcar **Enforce HTTPS**.

### 3. DNS en CDMON

En el panel de CDMON, para el dominio `mepagaunbot.eu`, crear:

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
| CNAME | www | TU_USUARIO.github.io |

(Si CDMON no permite varios registros A con el mismo nombre en una sola
entrada, se crean como registros separados. El fichero `static/CNAME` ya está
en el repo: no tocarlo.)

### 4. Opcionales (cuando se quiera)

- **Newsletter:** cuenta gratuita en [Buttondown](https://buttondown.com)
  (hasta 100 suscriptores) y poner la URL pública en `hugo.toml` →
  `params.newsletter`. El enlace aparece solo en la portada.
- **Estadísticas sin cookies:** ya activado, código `tempranillo` en
  `hugo.toml` → `params.goatcounter`. Sirve sobre todo para ver *referrers*
  (quién te cita). La línea correspondiente ya está en `/privacidad`.
- **Alertas de menciones:** ya activas — [F5Bot](https://f5bot.com)
  (Reddit/HN), Google Alerts («mepagaunbot» y «Gustavo Pérez Tempranillo») y
  Google Search Console.
- **Repo visible en el pie:** ya puesto, en `hugo.toml` → `params.repo`.

---

## Pendiente de revisión por el autor

- `content/participate.md`: es la versión en inglés de `content/participa.md`.
  Este último ya está reescrito en su voz; `participate.md` sigue con el
  texto anterior y hay que traducirlo o reescribirlo a juego.
- El tagline de la cabecera se cambia en `hugo.toml` → `params.tagline`.
