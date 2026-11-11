# Phase 8 — Auditoría dirigida de coherencia firmada y concordancia estructural

**Estado:** auditoría de trabajo, no cambio contractual ni resultado externo.
**Fecha:** 2026-11-11.
**Datos empíricos:** exclusivamente TCGA congelado. No se abrió expresión
CPTAC-3 ni se calculó una comparación TCGA–CPTAC-3.

## Conclusión ejecutiva

La concordancia relativa de aristas y la coherencia firmada son propiedades
distintas y útiles sólo si se interpretan jerárquicamente. La primera compara
el orden relativo de las correlaciones entre una referencia TCGA y otra
representación; la segunda pregunta si una representación, por sí misma, tiene
correlaciones orientadas de acuerdo con los signos congelados. Ninguna es una
prueba independiente de la otra: ambas usan la misma matriz de correlaciones,
los mismos genes y pesos relacionados.

La recomendación es conservar la concordancia de aristas como **efecto
descriptivo de preservación relativa**, e incorporar obligatoriamente la
**mediana ponderada de coherencia firmada** como caracterización complementaria
interna de cada cohorte/linaje. La media ponderada debe conservarse como
sensibilidad de magnitud, no como una segunda condición de éxito. No se
justifica todavía una regla conjunta binaria de replicación ni una prueba
confirmatoria: faltan una calibración inferencial y decisiones previas sobre
incertidumbre, comparabilidad y confusión.

La mediana ponderada se prefiere para el resumen principal de coherencia porque
TX_01 concentra 75.3% de su energía de pesos en el 10% superior de genes; una
media puede quedar dominada por las pocas aristas muy cargadas. Esta preferencia
no surge de seleccionar un resultado externo: estaba fijada en el diseño antes
del cálculo. La media conserva valor descriptivo porque cuantifica la magnitud
promedio orientada que la mediana deliberadamente descarta.

## Diseño, procedencia y límites

El diseño fijo previo está en
`PHASE8_SIGNED_COHERENCE_AUDIT_DESIGN.md`. El script verificó SHA-256 de la
expresión TMM/logCPM de Notebook 205, metadatos de genes y muestras, universo
compartido y pesos de consenso contra el registro. Usó los 2,389 genes ordenados
sin cambios y los tres vectores de peso congelados. La representación TCGA es
la de Notebook 205: TMM de edgeR y logCPM con `prior.count=2`; no se normalizó
ni reestimó nada.

Además de los hashes, el script falla explícitamente si el universo compartido
no contiene exactamente 2,389 `gene_symbol` únicos; si el mapeo de esos genes a
`gene_name` en los metadatos TCGA es ambiguo, ausente o no cubre ese universo; si un programa tiene
un gen faltante/adicional/duplicado; o si sus genes no están en el orden
congelado. Los pesos se vuelven a alinear por `gene_symbol` sólo después de esas
comprobaciones; no se infiere su correspondencia por posición. También exige que
`final_sample_column_index` sea el vector contiguo `0..n-1`, que el número de
columnas HDF5 coincida, y que casos y muestras sean únicos. Por tanto, una
discrepancia de genes, pesos o columnas detiene la auditoría en vez de repararse
silenciosamente.

Los consensos no tienen signos arbitrarios añadidos posteriormente. Notebook
401 centró y normalizó las cargas de tumor y célula, orientó la carga celular
con el multiplicador de Notebook 400 y ancló la orientación final al componente
RNA tumoral. Los signos expresan esa orientación transcriptómica relativa; no
son dirección de resistencia, efecto causal ni regulación directa. Por ello la
coherencia firmada es una hipótesis estadística razonable sobre la organización
de una representación firmada, no una afirmación mecanística.

Para cada programa `k` y par `i<j`, se definieron
`s_ij=sign(w_i,k w_j,k)`, `q_ij=abs(w_i,k w_j,k)` y
`z_ij=s_ij r_ij`. Se calcularon exactamente dos resúmenes:

* `C_mean = sum(q_ij z_ij)/sum(q_ij)`;
* `C_median`, mediana ponderada de `z_ij` con pesos `q_ij`.

El código no explora otras fórmulas ni realiza selección de programa/linaje.
La implementación de mediana fue verificada contra el cálculo por ordenamiento
completo en una entrada aleatoria (`PASS`) y evita persistir las matrices de
aristas.

## A. Validez conceptual y redundancia

La concordancia candidata `T=corr_q(r_reference,r_comparison)` responde si las
aristas relativamente altas/bajas —incluido su signo observado— mantienen su
orden bajo los pesos del programa. No exige igualdad de magnitud: para
`b=c*a+d`, con `c>0`, `corr_q(a,b)=1`. Por tanto, una atenuación uniforme puede
tener concordancia perfecta. Tampoco usa los signos congelados: `q_ij` no cambia
si se invierte un signo individual o todos los signos de un programa.

La coherencia firmada usa esos signos y responde a otra pregunta: si pares del
mismo signo tienden a ser positivos y pares de signo opuesto negativos en una
cohorte. Puede ser positiva, nula o negativa. Una inversión global de todos los
pesos deja `s_ij` y ambos resúmenes inalterados, como debe ocurrir para la
orientación globalmente equivalente de un componente. Una inversión de un gen
afecta todas sus aristas incidentes. Esto no identifica causalidad ni distingue
un programa de un factor de pureza, proliferación o composición compartido.

Los tres programas comparten sus 2,852,466 pares. Sus pesos dan tres kernels
distintos, no tres redes ni tres pruebas independientes. El antecedente encontró
que las correlaciones entre vectores de pesos por arista eran bajas (-0.059 a
0.053), lo cual permite estimandos diferentes, pero no convierte sus resultados
en evidencia independiente. La concentración también importa: los números
efectivos de pares ponderados son 441,654 (TX_01), 875,117 (TX_02) y 938,375
(TX_03), pero esos pares siguen compartiendo tumores y genes.

En consecuencia, alta `T` y baja coherencia es compatible con un patrón relativo
que se conserva pero que no respeta ampliamente la orientación firmada (o con
una referencia que tampoco la exhibe); alta coherencia y baja `T` es compatible
con una organización firmada genérica, pero con una topología de aristas distinta
de TCGA. Alta/alta es evidencia descriptiva consistente con ambas propiedades;
baja/baja no apoya ninguna de ellas. Ninguna casilla establece por sí sola
replicación externa.

## B. Resúmenes firmados evaluados

| Resumen | Interpretación | Sensibilidad principal | Uso recomendado |
| --- | --- | --- | --- |
| Media ponderada | correlación orientada promedio, conservando magnitud | aristas extremas y cargas muy concentradas | sensibilidad de magnitud |
| Mediana ponderada | arista orientada típica bajo la asignación de importancia congelada | discontinuidad y dominancia de una masa ponderada concentrada | resumen principal descriptivo |

La dependencia entre pares invalida usar la dispersión de pares como error
estándar para cualquiera de los dos. Ambos pueden ser negativos; truncarlos en
cero borraría información. La media no se transforma en robusta por tener
millones de pares, y la mediana no es inmune a concentración de pesos. Un
valor alto interno tampoco equivale a replicación: no hace referencia a TCGA.

### Relación exacta de la media con la varianza del score

Sea `Z_i` la expresión de cada gen centrada y estandarizada **dentro del mismo
linaje** con desviación estándar muestral (`ddof=1`), y sea
`S=sum_i w_i Z_i` el score sin su estandarización posterior. Si las
correlaciones `r_ij` se calculan sobre esas mismas observaciones y los pesos son
los congelados, entonces

```text
Var(S) = sum_i w_i^2 + 2 sum_{i<j} w_i w_j r_ij
       = sum_i w_i^2 + 2 C_mean sum_{i<j}|w_i w_j|.
```

La primera igualdad es la expansión de la forma cuadrática `w' R w`; la segunda
usa `sign(w_i w_j)|w_i w_j|=w_i w_j`. Así, con pesos y escala fijados,
`C_mean` es una transformación afín de la varianza del score: no aporta
evidencia independiente de un score construido con esos mismos pesos y esa
misma estandarización. Es una descripción de la parte de covarianza cruzada,
no una propiedad adicional del score.

La identidad no debe trasladarse sin más a scores con otra normalización, genes
filtrados, pesos reescalados o estandarización posterior: cambian `R`, la escala
de `Z` o ambos. La mediana ponderada no participa en esta expansión cuadrática;
no tiene una identidad equivalente con la varianza y sigue siendo un resumen
robusto de una arista orientada típica, aunque comparte datos, genes y pesos con
el score. En la ejecución corregida, la identidad se verificó en los 21 pares
programa–linaje y el máximo error absoluto numérico fue registrado en los
metadatos de salida.

## C. Demostraciones y simulación sintética declarada

Hay dos propiedades algebraicas suficientes sin simulación: (i) la invariancia
afín positiva de `T`, que explica la atenuación uniforme; y (ii) la invariancia
de `q_ij` a signos congelados. La tabla sintética usa un modelo gaussiano de dos
bloques firmado, semilla 20261112, y correlaciones poblacionales; es una
demostración de comportamiento, no evidencia biológica ni calibración.

| Escenario | T relativo | Media firmada | Mediana firmada | Lectura |
| --- | ---: | ---: | ---: | --- |
| Conservación casi completa | 1.000 | 0.143 | 0.131 | ambas propiedades se mantienen |
| Atenuación uniforme | 1.000 | 0.045 | 0.041 | `T` no informa pérdida de magnitud |
| Reordenamiento local | 0.605 | 0.085 | 0.122 | el daño localizado separa medidas |
| Inversión entre grupos | -0.008 | -0.002 | -0.057 | signos y patrón quedan incompatibles |
| Factor global compartido | 0.690 | 0.143 | 0.068 | un factor puede afectar ambas sin especificidad |
| Factor mixto con baja coherencia | 0.169 | 0.013 | -0.117 | ejemplo de coherencia baja; no de alta `T` |

El último escenario es deliberadamente una construcción de factor mixto, no un
modelo biológico. Demuestra coherencia baja, pero su `T=0.169` **no** demuestra
alta concordancia relativa con coherencia baja; no se le atribuye esa conclusión.
Existe, no obstante, una demostración algebraica transparente para la media:
si `R` es una matriz de correlación de referencia y
`B=cR+(1-c)11'` con `0<c<1`, `B` también es una matriz de correlación y sus
aristas cumplen `b_ij=c r_ij+(1-c)`. Mientras la varianza ponderada de aristas
no sea degenerada, `T(R,B)=1`. A la vez,
`C_mean(B)=c C_mean(R)+(1-c) mu_s`, donde
`mu_s=sum(q_ij sign(w_iw_j))/sum(q_ij)`. En estos tres programas `mu_s` es
cercano a cero (-0.00107, -0.00076 y -0.00073), por lo que al disminuir `c` la
media puede acercarse a cero con `T` matemáticamente perfecto. Cerca de `c=0`
la varianza de aristas se vuelve casi degenerada y `T` es numéricamente frágil;
es una demostración de límite, no una receta ni una simulación adicional. No
hay una afirmación análoga automática para la mediana ponderada.

## D. Resultados TCGA-only y estabilidad

Los estimandos de línea completa están en
`audit_outputs/phase8_signed_coherence/tcga_signed_coherence_full.csv`; el
resumen compacto de ocho particiones disjuntas está en
`tcga_signed_coherence_split_summary.csv`. Todas las 21 estimaciones completas
fueron positivas. Sus rangos fueron 0.024–0.092 para la media y 0.017–0.070
para la mediana. Entre los 21 estimandos completos, media y mediana tuvieron
correlación 0.745: relacionadas, pero no sustituibles.

TX_01 presenta mayor diferencia media–mediana en varios linajes, coherente con
su concentración de pesos. Por ejemplo, en LUAD la media/mediana fue
0.066/0.032; en HNSC, 0.092/0.062. No debe interpretarse como superioridad del
programa: es sensibilidad esperable a cómo se asignó el peso congelado.

La estabilidad no fue uniforme. Las mitades de LUAD resultaron estrechas (por
ejemplo TX_01: mediana de medias 0.065, rango 0.062–0.072), mientras que HNSC
fue claramente más variable (TX_01: 0.087, 0.063–0.135; TX_02: 0.072,
0.042–0.109). UCEC, LUSC y PAAD también muestran amplitudes mayores que LUAD;
SKCM añade el desajuste conocido de que TCGA n=103 no permite dos mitades de su
tamaño fuente externo n=138. Estos resultados son precisión interna finita,
no selección retrospectiva ni umbral para CPTAC-3.

Los tamaños por mitad se fijaron antes de observar resultados como
`min(floor(n_TCGA/2), n_CPTAC3_contractual)` y la semilla fue 20261111. Las
particiones respetan el tumor como unidad. Correlaciones débiles son
especialmente vulnerables a tamaño muestral; genes/aristas de alto peso agravan
la influencia de pocos genes. La estabilidad heterogénea coincide con el
antecedente de `T` y refuerza que una única comparación externa puntual tendría
incertidumbre importante.

## E. Incertidumbre e inferencia

Para una implementación futura, un bootstrap estratificado por linaje a nivel
de tumor —remuestreando por separado TCGA y CPTAC-3, recalculando la matriz y
ambos resúmenes en cada réplica— es adecuado para describir incertidumbre de
estimación. Debe fijar antes: número de réplicas, semilla, tratamiento de genes
sin varianza/no finitud, percentiles/BCa y reglas de no evaluable. El bootstrap
debe propagar incertidumbre de ambas cohortes, no sólo de CPTAC-3.

No se ejecutó bootstrap externo porque está prohibido abrir esos datos. Tampoco
se construyeron p-valores por aristas: no son réplicas independientes. Un
intervalo bootstrap no es distribución nula ni prueba de replicación. Un nulo
de igualdad exacta de matrices requeriría otro estadístico, supuestos fuertes de
alta dimensión y una defensa de comparabilidad que aquí no existe. Mientras no
se acuerde eso, las 21 combinaciones deben informarse descriptivamente con
incertidumbre, sin multiplicidad inferencial ficticia.

## F. Recomendación metodológica y decisiones pendientes

Las cuatro alternativas consideradas producen esta decisión:

1. **Primaria `T` + complemento obligatorio de coherencia:** preferida, si
   “primaria” se entiende como prioridad científica descriptiva y no prueba
   confirmatoria. Conserva la pregunta comparativa y hace visible la orientación
   firmada omitida por `T`.
2. **Dos propiedades necesarias:** no recomendada aún. Requerir ambas como
   compuerta binaria inventaría umbrales y duplicaría evidencia correlacionada.
3. **Reformular la primaria:** necesario sólo si el objetivo pasa de patrón
   relativo a igualdad de magnitudes o una prueba confirmatoria calibrada. La
   coherencia no corrige por sí sola esa limitación de `T`.
4. **Descriptivo sin clasificación binaria:** necesario en esta etapa y
   compatible con la opción 1. Es la etiqueta inferencial recomendada.

Antes de modificar el contrato deben aprobarse: (a) que la mediana ponderada es
el resumen firmado central y la media una sensibilidad; (b) un resumen explícito
de cambio de magnitud para acompañar `T`; (c) diseño bootstrap completo de ambas
cohortes y evaluación de degeneración; (d) reglas outcome-blind de evaluabilidad
por linaje, especialmente HNSC/UCEC/SKCM; (e) qué covariables/proxies son válidos
y ajustables sin circularidad; y (f) si se mantiene descripción con intervalos o
se formula una hipótesis/nula realmente calibrable. Ninguna de estas decisiones
debe basarse en resultados CPTAC-3.

Si se aprueba, Notebook 800 debería: verificar identidades; normalizar y
proyectar sin modificar programas; calcular por linaje `T`, el resumen de
magnitud pendiente, mediana firmada y media de sensibilidad; estimar
incertidumbre tumoral de ambas cohortes; y presentar una interpretación conjunta
con limitaciones de confusión. No debe usar pares como unidades inferenciales ni
emitir una etiqueta binaria de replicación sin las decisiones anteriores.

## Reproducción

Desde la raíz de la rama de auditoría:

```powershell
python -m black --check scripts/phase8/audit_signed_program_coherence.py
python scripts/phase8/audit_signed_program_coherence.py `
  --data-root . `
  --output-dir audit_outputs/phase8_signed_coherence `
  --seed 20261111 --splits 8
```

Los únicos artefactos escritos son cuatro CSV compactos y un JSON de metadatos
bajo `audit_outputs/phase8_signed_coherence/`; no hay matrices de correlación
persistidas ni acceso a expresión externa.
