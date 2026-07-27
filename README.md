# mepagaunbot.eu

Repositorio del blog **Me paga un bot** — crónica de investigación en primera
persona de Gustavo Pérez Tempranillo: 90 días (27-jul → 25-oct de 2026)
ofreciéndose como mano de obra a agentes de IA, con prerregistro, pruebas
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

### Convención de evidencia

Enlace probatorio = «fuente (archivo)». Hay un shortcode:

```
{{</* fuente url="https://original" archivo="https://web.archive.org/..." */>}}texto{{</* /fuente */>}}
```

---

## El prerregistro (pendiente, una sola vez)

`content/prerregistro.md` está en `draft: true` con **cifras candidatas que
NO valen**: son propuestas del asistente. Antes del post cero:

1. Sustituir cada `[X]` por la cifra propia y añadir la apuesta arriesgada.
2. Borrar el aviso de borrador, poner la fecha y `draft: false`.
3. Commit y push. Cuando la página esté en línea:
4. **Sello Wayback:** abrir `https://web.archive.org/save/https://mepagaunbot.eu/prerregistro/` y guardar el enlace resultante en la sección «Sellado».
5. **Sello OpenTimestamps:** `pip install opentimestamps-client` y
   `ots stamp content/prerregistro.md` → añadir el fichero `.ots` al repo
   (`git add content/prerregistro.md.ots`). Días después, `ots upgrade` y
   commit del `.ots` actualizado.

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
- **Estadísticas sin cookies:** cuenta en
  [GoatCounter](https://www.goatcounter.com) y poner el código en
  `hugo.toml` → `params.goatcounter`. Sirve sobre todo para ver *referrers*
  (quién te cita). Si se activa, añadir una línea en `/privacidad`.
- **Alertas de menciones:** [F5Bot](https://f5bot.com) (Reddit/HN),
  Google Alerts («mepagaunbot» y «Gustavo Pérez Tempranillo») y Google
  Search Console.
- **Repo visible en el pie:** poner la URL del repositorio en `hugo.toml` →
  `params.repo`.

---

## Pendiente de revisión por el autor

- `content/sobre-mi.md` y `content/participa.md` / `participate.md`: hablan
  en su voz; ensamblados desde los documentos aprobados del proyecto, pero
  debe leerlos y hacerlos suyos antes de difundir el blog.
- `content/cronica/ejemplo-parte-semanal.md`: plantilla de ejemplo
  (`draft: true`), borrar cuando ya no haga falta.
- El tagline de la cabecera se cambia en `hugo.toml` → `params.tagline`.
