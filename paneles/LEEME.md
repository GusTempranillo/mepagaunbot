# paneles/

Herramientas de trabajo del autor. **Hugo no las publica**: esta carpeta no
es `content/` ni `static/`, así que no llega a mepagaunbot.eu.

## `ofertas.html` — el panel de firmas

Una sola página, sin dependencias ni peticiones a terceros, para leer las
ofertas del día y firmarlas de una en una: «¿me dejan entrar?», «¿puedo
hacerla?» y la modalidad de las que llegan por correo.

La sirve n8n (workflow «RentAHuman panel de firmas»), que la descarga de
este repositorio en cada visita y le inyecta los datos de las dos pestañas
de la hoja de cálculo en el hueco `__DATOS__`. Editar este fichero y hacer
push es todo lo que hace falta para cambiar el panel: no hay que tocar n8n.

Lo que se firma se escribe en dos sitios a la vez:

1. **La hoja de cálculo**, que es la que manda: el volcado de las 06:30
   vuelve a escribir `data/ofertas.yaml` desde ella cada día, así que lo que
   no esté en la hoja se pierde a la mañana siguiente.
2. **`data/ofertas.yaml`**, por adelantado, para que la web no espere a
   mañana. Escribe exactamente lo mismo que escribirá el volcado, de modo
   que cuando este llegue no encuentre nada que cambiar.

El panel no tiene ningún botón para firmar en bloque, a propósito: una firma
que no se puede seguir a mano sería un sello de goma, y eso es justo lo que
`/calibracion/` existe para no ser.
