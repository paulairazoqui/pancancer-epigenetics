# Phase 8 — Auditoría de factibilidad del estadístico primario estructural

**Estado:** auditoría de trabajo; no modifica el contrato ni autoriza análisis
confirmatorio externo.  
**Fecha:** 2026-11-11.  
**Alcance de datos:** sólo TCGA congelado y simulación/algebra. No se leyó,
calculó ni inspeccionó expresión ni concordancia de coexpresión de CPTAC-3.

## Conclusión ejecutiva

El candidato es computable y puede ser útil como una **medida descriptiva de
concordancia relativa de patrones de aristas**, con incertidumbre obtenida por
remuestreo de tumores. No debe congelarse ni interpretarse todavía como una
prueba confirmatoria de “replicación estructural de tres programas” sin una
decisión metodológica adicional.

La razón principal no es computacional. Con el mismo conjunto de 2.389 genes
para los tres programas y pesos de arista `abs(w_i w_j)`, los tres números son
tres resúmenes ponderados de la misma comparación de dos redes completas. Son
estimandos matemáticamente distintos porque las magnitudes de los pesos difieren,
pero no aíslan tres subredes disjuntas ni usan directamente la orientación
firmada congelada. Por tanto, un resultado alto puede reflejar topología global
estable —incluidos ejes de proliferación, pureza, composición o plataforma— y no
un programa epigenético específico. La auditoría recomienda **modificar la
interpretación y completar la especificación antes de usarlo**; no recomienda
descartarlo como diagnóstico descriptivo.

No hay con estos recursos una hipótesis nula de “no replicación” que convierta
automáticamente el rango de reasignaciones de pesos, el bootstrap, o millones
de pares en un valor *p* válido. Si no se acuerda una nula/contrastación
defendible, el análisis externo debe permanecer como estimación descriptiva con
intervalos de incertidumbre y sensibilidades predefinidas.

## Evidencia, fuentes y límites de esta auditoría

### Artefactos verificados

El script verificó SHA-256 contra `config/artifact_registry.json` antes de
leerlos. Las identidades y hashes observados están en
`audit_outputs/phase8_primary_statistic/tcga_reference_stability_metadata.json`.
Los insumos fueron:

| Artefacto | ID congelado | SHA-256 |
| --- | --- | --- |
| Expresión TCGA TMM/logCPM | `phase2.205.rna_program_discovery_expression` | `0072307c...d97fc8` |
| Metadatos de genes TCGA | `phase2.205.rna_program_discovery_gene_metadata` | `e0cd2feb...3337e` |
| Metadatos de muestras TCGA | `phase2.205.rna_program_discovery_sample_metadata` | `04e33010...c2bb3be` |
| Universo compartido | `phase4.400.cross_system_shared_gene_universe` | `080fee12...0a84c` |
| Pesos consenso | `phase4.401.consensus_transcriptomic_gene_weights` | `09b33db8...472b39` |

Se revisaron el contrato vigente de Notebook 800 (en particular §§5–6), los
contratos de Phase 4, el registro y las políticas de ejecución/estilo. El
Notebook 800 existente se inspeccionó sólo desde el árbol de trabajo original:
es un archivo aún no rastreado, tiene 19 celdas y la celda final de carga de la
referencia TCGA no tenía salida. No se alteró. La worktree de auditoría parte de
`origin/main` en `5e1b3bd`.

### Qué es empírico, demostrable o supuesto

* **Empírico TCGA:** las particiones y sus resultados están más abajo. No son
  resultados CPTAC-3 ni una calibración de prueba.
* **Demostrable:** las invariancias del coeficiente de correlación y que los
  signos de los pesos no entran en `abs(w_i w_j)`.
* **Simulación:** no se necesitó una simulación numérica para esas invariancias;
  se muestran por algebra. Simulaciones futuras sólo serían útiles para evaluar
  cobertura/calibración bajo modelos generativos declarados, no para elegir el
  estadístico según CPTAC-3.
* **Supuestos no verificados:** que los tumores son unidades intercambiables
  dentro de cada linaje y que el TMM/logCPM y los covariables disponibles hacen
  comparable la dependencia entre cohortes. No se infiere de esta auditoría.

## A. Qué mide el candidato y qué no mide

Sea `a` el vector de `r_TCGA(i,j)` y `b` el vector de `r_CPTAC3(i,j)` para
`i < j`, y `q_ij = abs(w_i,k w_j,k)`. El candidato es la correlación de Pearson
ponderada entre `a` y `b`:

`T_k,l = cov_q(a,b) / sqrt(var_q(a) var_q(b))`.

Mide si las aristas que son relativamente grandes/pequeñas (y positivas/negativas
respecto de la media ponderada de cada vector) en TCGA tienden a ordenarse de
igual forma en CPTAC-3. Un valor alto indica concordancia de patrón relativo
en las aristas con más peso; cercano a cero, ausencia de relación lineal
ponderada; negativo, orden relativo inverso. Ninguno implica causalidad,
regulación directa, ni preservación de una red biológica específica.

### Fortalezas

* Compara el mismo conjunto de aristas de forma explícita, por linaje, y no
  confunde la mera computabilidad de un score con replicación.
* No requiere seleccionar aristas tras observar CPTAC-3 y puede reutilizar la
  matriz de correlaciones común para los tres pesos congelados.
* Al ponderar antes de resumir, reconoce que la construcción de cada consenso
  no asigna igual importancia a todos los genes.

### Limitaciones demostrables

1. **No mide igualdad de magnitudes.** Para cualquier `c > 0` y constante `d`,
   `corr_q(a, c a + d) = 1` si `var_q(a)>0`. Por ejemplo, una atenuación
   sustancial y uniforme de todas las correlaciones puede producir `T=1`.
   Una atenuación heterogénea puede reducir `T`, pero el estadístico no separa
   esa pérdida de un reordenamiento de aristas. Es indispensable acompañarlo de
   un resumen de diferencia/atenuación de magnitud preespecificado; ese resumen
   no es un segundo test independiente.
2. **Es invariante a los signos congelados.** Cambiar el signo de un gen, de un
   programa completo, o permutar sólo signos no cambia `q_ij`. Así, el
   candidato no evalúa que genes de signos opuestos tengan la relación esperada
   por el programa, ni la orientación firmada de Phase 4. El signo de la
   correlación observada sí contribuye a `a`/`b`, pero no se contrasta contra el
   signo `sign(w_i w_j)`.
3. **No detecta toda alteración estructural.** Dos redes con igual orden
   relativo de aristas pero densidad, varianza, modularidad, hubs, espectro,
   conectividad condicional o correlaciones parciales muy distintos pueden dar
   un `T` alto. Tampoco distingue un factor latente común de una red de
   interacciones directas.
4. **Puede ser degenerado.** Si `var_q(a)` o `var_q(b)` es cero o casi cero,
   el denominador se anula o el valor se vuelve numéricamente inestable. Aristas
   extremas, genes de varianza casi cero, outliers y una masa de aristas casi
   constantes pueden dominar la media/varianza. El uso de `atanh` por arista
   no arregla la dependencia y cerca de ±1 puede amplificar inestabilidad;
   sólo podría ser sensibilidad con reglas de recorte y justificación previas.

### Genes compartidos, pesos y “tres estructuras”

Hay 2.852.466 aristas para cada programa y linaje, y las tres usan exactamente
el mismo vector de aristas observadas. Por tanto, no hay tres evidencias
independientes ni tres redes estimadas a partir de conjuntos de genes distintos.
Hay tres kernels de ponderación aplicados a una red de referencia y una red
externa. Eso permite tres estimandos distintos, no tres replicaciones
independientes.

La auditoría verificó que los perfiles de pesos por arista no son casi idénticos:
las correlaciones de Pearson entre los tres vectores `abs(w_i w_j)` son -0,059
(TX_01–TX_02), -0,004 (TX_01–TX_03) y 0,053 (TX_02–TX_03). Esta diferenciación
de pesos evita afirmar que los tres resultados serían mecánicamente iguales,
pero no resuelve la especificidad: todos pueden responder a una propiedad global
de la misma red. Los signos permanecen ausentes de la ponderación primaria.

Factores de proliferación, pureza tumoral, inmunidad/estroma, composición celular,
batch, centro o plataforma pueden crear patrones de coexpresión estables en ambas
cohortes. Un `T` alto bajo esos factores es compatible tanto con conservación
biológica como con confusión compartida; sin covariables/proxies con diseño
identificable no se pueden separar. Ajustar usando proxies derivados de estos
mismos genes podría inducir circularidad y no debe hacerse automáticamente.

Las 2,85 millones de aristas no son 2,85 millones de réplicas: comparten genes,
muestras y factores latentes. Cualquier error estándar que las trate como
observaciones independientes será artificialmente pequeño.

## B. Estabilidad de la referencia TCGA

### Diseño TCGA-only ejecutado

Pregunta: ¿la red de referencia, estimada dentro de cada linaje, conserva su
patrón ponderado al cambiar los tumores usados para estimarla?  
Procedimiento: ocho particiones aleatorias disjuntas por linaje, semilla
`20261111`. Cada mitad contiene `min(floor(n_TCGA/2), n_CPTAC3_contractual)`
tumores. Se calcularon correlaciones génicas dentro de cada mitad y el mismo
`T` entre mitades. Los tamaños CPTAC-3 son sólo metadatos fijados por el
contrato y no se abrió expresión externa.  
Criterio: mediana y rango describen fiabilidad de referencia; variación amplia,
medianas bajas o imposibilidad de tamaño comparable señalan precisión limitada.
Inviabilidad: menos de tres tumores por mitad, varianza cero de un gen o fallo de
integridad. Ninguna ocurrió, pero esto no garantiza comparabilidad externa.

| Linaje | n TCGA | n externo contractual | n por mitad | ¿dos mitades del n externo? |
| --- | ---: | ---: | ---: | --- |
| LUAD | 512 | 178 | 178 | Sí |
| LUSC | 500 | 89 | 89 | Sí |
| STAD | 412 | 142 | 142 | Sí |
| SKCM | 103 | 138 | 51 | No |
| PAAD | 178 | 88 | 88 | Sí |
| UCEC | 543 | 56 | 56 | Sí |
| HNSC | 520 | 36 | 36 | Sí |

Mediana [mínimo–máximo] de la concordancia entre mitades (8 particiones):

| Linaje | TX_01 | TX_02 | TX_03 |
| --- | --- | --- | --- |
| LUAD | 0,878 [0,865–0,893] | 0,778 [0,751–0,795] | 0,834 [0,813–0,848] |
| LUSC | 0,836 [0,813–0,859] | 0,700 [0,695–0,746] | 0,735 [0,711–0,780] |
| STAD | 0,893 [0,878–0,907] | 0,825 [0,810–0,854] | 0,875 [0,849–0,894] |
| SKCM | 0,717 [0,705–0,729] | 0,724 [0,711–0,728] | 0,568 [0,554–0,579] |
| PAAD | 0,831 [0,763–0,858] | 0,783 [0,701–0,819] | 0,790 [0,716–0,829] |
| UCEC | 0,653 [0,616–0,676] | 0,505 [0,457–0,521] | 0,539 [0,475–0,563] |
| HNSC | 0,685 [0,581–0,727] | 0,572 [0,525–0,659] | 0,605 [0,523–0,639] |

Estos números muestran estabilidad heterogénea, no una calidad uniforme de la
referencia. HNSC y UCEC son particularmente sensibles; SKCM enfrenta además un
desajuste de soporte porque la fuente externa propuesta excede el TCGA del
linaje. PAAD tiene mitades de 88 y muestra más dispersión que los linajes grandes.
La concentración reduce el número efectivo de aristas ponderadas: 441.654,
875.117 y 938.375 para TX_01, TX_02 y TX_03 respectivamente (definido como
`1/sum(q_ij^2)` con `q` normalizado). Aun así, no son muestras independientes.

Distinciones críticas:

* **Estabilidad de red estimada:** lo que muestran las particiones; incorpora
  error finito de la estimación de correlaciones.
* **Reproducibilidad interna TCGA:** si nuevas muestras de la misma población y
  representación conservaran el patrón. Las particiones son evidencia limitada,
  potencialmente optimista por compartir procedencia, procesamiento y el sistema
  de descubrimiento.
* **Replicación externa:** requiere la cohorte independiente CPTAC-3, sus propios
  errores y amenazas de comparabilidad. No se demuestra por este análisis.

La selección/construcción de los programas estuvo vinculada al sistema TCGA. Por
ello, incluso una estabilidad interna alta puede estar optimista respecto de una
red no condicionada por el proceso de descubrimiento; no es un umbral para
CPTAC-3.

## C. Incertidumbre, hipótesis y calibración

Un bootstrap estratificado por linaje a nivel de tumor es la forma natural de
propagar incertidumbre de **estimación**: re-muestrear tumores con reemplazo por
separado en TCGA y CPTAC-3, recalcular ambas matrices y `T`, y reportar percentil
o BCa si se justifican suficientes réplicas/diagnósticos. Sus unidades son
tumores, no aristas. Debe declarar tratamiento de muestras duplicadas, genes de
varianza cero, semillas, réplicas y criterios de fallo. Un intervalo bootstrap
no es una distribución nula ni responde por sí solo si la similitud observada es
mayor que “no replicación”.

Una partición o submuestreo TCGA estima fiabilidad de referencia y sensibilidad
a `n`; tampoco genera una nula externa. Simulaciones sintéticas podrían evaluar
sesgo, cobertura y potencia condicional para modelos explícitos (p.ej., factor
latente común, atenuación de magnitud y rewiring localizado). No validan esos
modelos para tumores reales, ni deben calibrarse mirando CPTAC-3.

Una nula científicamente posible sería igualdad exacta de matrices de correlación
poblacionales dentro de linaje, o una nula operacional sobre una distancia entre
matrices. Pero el candidato es una medida de asociación, no una distancia a cero
ni un estadístico de igualdad; `T=1` no implica igualdad. Pruebas de igualdad de
covarianzas/correlaciones de alta dimensión existen bajo supuestos fuertes y
estadísticos distintos, pero aquí `p=2.389` y los tamaños por linaje son pequeños,
la normalidad/elipticidad y comparabilidad de población no están justificadas, y
la hipótesis de igualdad exacta probablemente no es la pregunta científica más
útil. Como antecedente metodológico, las pruebas de preservación de módulos
distinguen propiedades de red y usan calibración específica; no convierten la
correlación de aristas propuesta en test validado ([Langfelder et al., 2011](https://doi.org/10.1371/journal.pcbi.1001057)).

Por ahora la opción defendible es: efecto `T` + intervalo de incertidumbre
tumoral + diagnóstico de magnitud + estabilidad TCGA + sensibilidades, sin
significancia de hipótesis. Sólo si se adopta previamente una nula, supuestos y
un método calibrado para ese estimando puede discutirse prueba. En ese caso las
21 comparaciones (3×7) forman una familia con política preespecificada para
resultados no evaluables y corrección FDR/FWER; la corrección no repara un valor
*p* mal calibrado.

## D. Reasignación de magnitudes de pesos

Permutar las magnitudes `abs(w)` entre las 2.389 posiciones, manteniendo genes,
datos y fórmula, preguntaría: “¿la asignación original de importancia a genes
obtiene una concordancia distinta de asignaciones alternativas bajo esta red?”
No pregunta si el conjunto de genes es específico, si el programa replica
externamente, ni si los pesos son causalmente correctos.

Para una inferencia aleatorizada, haría falta que, bajo una nula explícita, las
posiciones génicas fueran intercambiables respecto de la estructura de red y el
proceso de construcción de los pesos. Esto es dudoso: genes difieren en varianza,
grado, expresión, anotación, correlación con factores latentes y pueden haber
sido elegidos/ponderados con TCGA. La concentración de pesos hace que algunas
reasignaciones cambien drásticamente el número efectivo de pares y, por tanto,
su variabilidad; el rango observado puede reflejar concentración y no
especificidad. El análisis sería una sensibilidad exploratoria condicionada a
esa reasignación, no un *p* de no-replicación, salvo justificación adicional.

No se usaron ni se proponen conjuntos alternativos de genes.

## E. Factibilidad computacional e implementación segura

Con 2.389 genes hay `2389*2388/2 = 2.852.466` aristas. Una matriz de correlación
densa `2389×2389` consume ~45,7 MB (float64; 43,6 MiB); un vector triangular,
~22,8 MB. Tres vectores de pesos ocupan ~68,5 MB. La expresión TCGA completa del
subuniverso (`9.965×2.389`, float64) ocupa ~190,5 MB. Con una matriz de
correlaciones, vectores temporales y el objeto HDF5, un proceso de 0,5–1 GB RAM
es una expectativa prudente; no es necesario persistir matrices grandes.

La ejecución auditada, ocho particiones × siete linajes, terminó en menos de un
minuto en el entorno local después de la verificación de hashes. Un bootstrap de
ambas cohortes multiplica aproximadamente el coste de estimar dos matrices por
réplica y por 21 estimandos; cientos/miles de réplicas requerirán presupuestar
tiempo, memoria y posiblemente paralelismo, sin cambiar semillas ni agregados.

Implementación transparente recomendada:

1. Cargar y alinear el universo congelado una vez; calcular una matriz de
   correlaciones por cohorte/linaje/remuestreo y extraer sólo el triángulo
   superior.
2. Reutilizar esos dos vectores de aristas para los tres programas; aplicar cada
   vector de pesos sin recomputar la red. Es una optimización algebraicamente
   exacta, no un cambio de estimando.
3. Usar float64, centrar/escalar por gen de forma explícita, comprobar
   finitud/varianza y marcar no evaluable ante degeneración. No materializar
   matrices de bootstrap en disco; persistir sólo resúmenes, parámetros y
   semillas.
4. Validar una implementación pequeña frente a `numpy.corrcoef` y documentar
   tolerancias. Una transformación `atanh` exige reglas previas para ±1.

## Recomendación y decisiones pendientes

**Recomendación:** no mantener el candidato sin cambios como estadístico
confirmatorio. Mantenerlo provisionalmente como efecto descriptivo de
concordancia relativa, sujeto a una especificación explícita de degeneración,
incertidumbre tumoral, magnitud y confusión. Antes de Notebook 800 deben acordarse:

1. Si el objetivo admite una medida que ignore por completo los signos de pesos;
   si no, formular y justificar una propiedad firmada diferente, sin modificar
   programas congelados ni seleccionar por resultados externos.
2. Si la pregunta primaria es patrón relativo, igualdad/atenuación de magnitud,
   o ambas separadas. Adoptar el resumen complementario de magnitud y sus reglas
   antes de abrir la concordancia externa.
3. Si se buscará una prueba con nula/calibración defendible o se limitará a
   estimación descriptiva con bootstrap tumoral. No usar pares como réplicas.
4. Diseño exacto de bootstrap para ambas cohortes, número de réplicas, manejo de
   fallos y evaluabilidad por linaje. SKCM, HNSC, UCEC y PAAD exigen atención
   particular; la fuente HNSC externa propuesta tiene n=36.
5. Familia de multiplicidad y criterio para “no evaluable”, condicional a que
   existan pruebas válidas.
6. Qué covariables/proxies tienen procedencia válida y ajuste identificable por
   linaje; de no haberlos, cómo se reportará la confusión residual.
7. Si la reasignación de pesos se implementa, su esquema, diagnóstico de
   concentración y etiqueta estrictamente no inferencial, salvo nueva defensa
   formal de intercambiabilidad.

## Reproducción

Desde la raíz de esta worktree:

```powershell
python -m black --check scripts/phase8/audit_tcga_reference_stability.py
python scripts/phase8/audit_tcga_reference_stability.py `
  --data-root .. `
  --output-dir audit_outputs/phase8_primary_statistic `
  --seed 20261111 --splits 8
```

`--data-root ..` señala explícitamente al árbol local que contiene los
artefactos congelados voluminosos; el script verifica hashes antes de usarlos.
No tiene rutas ni lecturas de expresión CPTAC-3. Las salidas son CSV/JSON
pequeños y reproducibles: resultados por partición, resumen, soporte por
linaje, solapamiento de pesos y metadatos/versiones.
