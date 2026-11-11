# Phase 8 — Auditoría de factibilidad del cambio de magnitud de coexpresión

**Estado:** auditoría exploratoria de método; no cambia el contrato ni autoriza
una afirmación externa.
**Fecha:** 2026-11-11.
**Datos empíricos abiertos:** exclusivamente TCGA congelado. No se abrió
expresión CPTAC-3 ni se calculó ninguna comparación TCGA–CPTAC-3.

## Conclusión ejecutiva

El estimando poblacional propuesto es científicamente adecuado como una
**descripción ponderada del cambio promedio de fuerza absoluta de
coexpresión**, y responde a una pregunta que ni la concordancia relativa `T`
ni la coherencia firmada responden. No es una distancia entre redes ni prueba
de preservación arista por arista. En particular, `Delta_M` cercano a cero sólo
dice que los aumentos y reducciones ponderados se compensan; no demuestra que
las magnitudes se hayan preservado.

Su sustituto directo con `|r|` es computable, pero no está libre de sesgo por
tamaño muestral. El problema es más grave cuando hay muchas correlaciones
débiles y los tamaños son muy distintos; HNSC contractual (`n=36`) es un caso
de alerta. Igualar `n` reduce el sesgo diferencial de precisión bajo una misma
distribución, pero descarta información y las repeticiones no son réplicas
biológicas. Debe ser una sensibilidad diagnóstica, no el estimador principal.

No se identificó una corrección universal de sesgo de `|r|` que conserve el
estimando sin imponer un modelo de correlaciones poblacionales no verificable.
Ni `atanh`, ni bootstrap no paramétrico, ni sustraer un piso de ruido cumplen
esa función. La recomendación es **mantener la medida solamente como efecto
descriptivo complementario**, informar el estimador directo de cohortes
completas junto con una sensibilidad de `n` igualado y bootstrap tumoral de
ambas cohortes, y explicitar el sesgo residual. No debe convertirse en una
compuerta binaria ni en una prueba por pares.

## 1. Resultado matemático: qué estima `Delta_M`

Con `q_ij,k=|w_i,k w_j,k|`, normalizado para sumar uno, el candidato es

```text
Delta_M(k,l) = sum_{i<j} q_ij,k (|rho_comparison,ij,l| -
                                  |rho_reference,ij,l|).
```

Un valor positivo indica mayor fuerza absoluta promedio en la comparación, uno
negativo menor fuerza, y uno cercano a cero igualdad sólo **en promedio
ponderado**. Si algunas aristas aumentan y otras disminuyen, las contribuciones
se cancelan según `q`; el resultado no identifica heterogeneidad, ni cuántas
aristas cambiaron, ni un límite máximo de discrepancia. Si cambia el signo de
una correlación pero conserva exactamente su magnitud, su contribución es cero.
Esto es intencional: la propiedad mide fuerza, no orientación.

Por ello aporta información que falta en `T`: una transformación afín positiva
de todas las aristas puede dejar `T=1` pese a atenuar sus magnitudes. También
aporta una comparación entre cohortes que la coherencia firmada interna no da.
A la inversa, no sustituye la coherencia: ignora tanto el signo de las
correlaciones como `sign(w_i w_j)`.

Los tres programas usan las mismas 2.852.466 aristas; son tres kernels sobre
las mismas matrices, no tres redes ni tres evidencias independientes. Además,
la concentración de los pesos amplifica la influencia de un subconjunto de
genes/aristas. El número efectivo de pares ponderados fue 441.654 (TX_01),
875.117 (TX_02) y 938.375 (TX_03); la fracción de peso de las aristas del 10%
superior fue 54,5%, 44,9% y 42,8%, respectivamente. Estos números no crean ese
número de réplicas: todas las aristas comparten tumores, genes y factores
latentes.

## 2. Sesgo de `|r|` y por qué depende de `n`

Para observaciones bivariadas normales independientes y `rho=0`, la densidad
exacta de `r` da

```text
E(|r|) = Gamma((n-1)/2) / {sqrt(pi) Gamma(n/2)}
       aproximadamente sqrt[2 / {pi (n-1)}].
```

Es estrictamente positivo. Sus valores exactos son 0,1358 (`n=36`), 0,1081
(`n=56`), 0,0792 (`n=103`) y 0,0683 (`n=138`). Así, incluso sin relación
poblacional, sólo cambiar de 103 a 138 casos cambia el piso esperado de
`|r|` en alrededor de 0,011; entre 36 y una cohorte grande puede ser mucho
mayor. La expresión asume normalidad y no es una corrección aplicable arista
por arista en tumores; ilustra el mecanismo.

Para `|rho|` pequeño, la distribución plegada de `r` conserva una parte
importante de ese piso, por lo que el sesgo hacia arriba es dominante. Para una
correlación moderada, el efecto depende simultáneamente de la dispersión y del
sesgo de la correlación firmada. Lejos de cero y con `rho>0`, la expansión de
primer orden de `E(r)` tiene sesgo negativo aproximado
`-rho(1-rho^2)/[2(n-1)]`; por tanto, no es correcto afirmar que `|r|` siempre
sobrestima `|rho|`. Cerca de correlaciones altas el plegado es despreciable y
puede predominar el sesgo hacia abajo, además de los límites en ±1. La varianza
de `r` y este sesgo son cosas distintas: reducir la varianza con más tumores no
garantiza que desaparezca un sesgo diferencial finito entre cohortes.

Cuando las dos poblaciones tienen distribuciones de `rho` diferentes, la
diferencia de sesgos no se deduce sólo de `n`: depende de cuántas aristas estén
cerca de cero, de su fuerza, y de su dependencia. No hay un número de pares
que arregle esta situación. Con 2.389 genes se estiman millones de aristas desde
los mismos pocos tumores; compartir genes y factores hace inválido tratar las
aristas como unidades independientes.

La normalidad bivariada es además una aproximación. Transformaciones de RNA,
colas pesadas, outliers, heterocedasticidad, mezcla de subtipos y pureza/
inmunidad/proliferación pueden alterar la distribución de `r`; un factor latente
puede mover grandes conjuntos de aristas conjuntamente. Esos fenómenos afectan
tanto la interpretación biológica como la calibración del sesgo.

## 3. Evidencia de simulación con verdad poblacional conocida

El diseño fijado antes de ejecutar está en
`PHASE8_COEXPRESSION_MAGNITUDE_AUDIT_DESIGN.md`. Se usaron 800 pares de
cohortes por condición, 60 genes en dos bloques firmados y matrices normales
multivariadas factoriales positivas definidas. El tamaño pequeño permite
repetición y conserva dependencia entre aristas, pero no pretende calibrar
tumores ni sustituir los 2.389 genes. Todos los pares tuvieron peso uniforme:
la concentración real se evaluó separadamente.

| Escenario (`n_ref`, `n_cmp`) | Delta poblacional | Directa: sesgo, DE, RMSE | Igualación: sesgo, DE, RMSE | Lectura |
| --- | ---: | --- | --- | --- |
| Igualdad (103, 138) | 0,0000 | -0,0015; 0,0307; 0,0308 | -0,0007; 0,0304; 0,0304 | diferencia pequeña de `n`; no implica inmunidad general al sesgo |
| Atenuación uniforme (103, 138) | -0,1125 | +0,0114; 0,0248; 0,0272 | +0,0181; 0,0244; 0,0304 | ambas recuperan el signo; igualar pierde precisión y no elimina sesgo residual |
| Incremento (103, 138) | +0,1000 | -0,0013; 0,0346; 0,0346 | -0,0017; 0,0348; 0,0348 | signo correcto 99,9%/99,8% en esta señal grande |
| Heterogéneo compensado (103, 138) | -0,0004 | +0,0024; 0,0291; 0,0291 | +0,0047; 0,0289; 0,0293 | un promedio casi cero es indetectable como patrón arista a arista |
| Reversión de signos (103, 138) | 0,0000 | -0,0014; 0,0312; 0,0312 | -0,0007; 0,0308; 0,0308 | deliberadamente invisible para una medida de magnitud |
| Factor latente compartido cambiado (103, 138) | -0,0012 | +0,0041; 0,0268; 0,0271 | +0,0071; 0,0262; 0,0271 | un cambio estructural puede dejar `Delta_M` próximo a cero |
| Igualdad (520, 36) | 0,0000 | +0,0154; 0,0321; 0,0355 | -0,0012; 0,0317; 0,0317 | sesgo diferencial claro en el extremo HNSC |
| Igualdad (543, 56) | 0,0000 | +0,0058; 0,0317; 0,0322 | -0,0008; 0,0315; 0,0315 | también persiste con UCEC |

La tasa de signo correcto no se informa cuando el valor poblacional es cero. En
la atenuación fue 100% para ambas estrategias y en el incremento 99,9% directa,
99,8% igualada. Esas tasas son condicionales al generador declarado, no potencia
para CPTAC-3. Las 32 submuestras de B generan una dispersión adicional dentro
de cada pareja simulada; promediarlas estabiliza un diagnóstico de tamaño, pero
no agrega tumores ni información biológica independiente.

## 4. Estrategias A–C

| Estrategia | Ventaja | Problema principal | Decisión |
| --- | --- | --- | --- |
| A. Cohortes completas | máxima información y menor pérdida de precisión; estima el sustituto más cercano al efecto descriptivo deseado | `E(|r|)` distinto si `n` y la distribución de `rho` difieren; puede atribuir precisión a biología | usar como punto descriptivo, nunca sin sensibilidad de tamaño |
| B. Igualar `n` por submuestreo | reduce el sesgo diferencial atribuible únicamente a precisión bajo misma población | tira observaciones, aumenta variabilidad y conserva sesgo común; repeticiones no son réplicas | usar como diagnóstico de robustez, no reemplazo automático de A |
| C. Corrección | en principio podría conservar datos si existiera modelo correcto | no hay corrección general de `|r|` con `rho` desconocido, dependencia y distribución tumoral no gaussiana | no adoptar corrección primaria |

Una transformación Fisher `atanh(r)` estabiliza aproximadamente la varianza de
la correlación firmada bajo normalidad; no estima `|rho|`, no preserva la escala
del estimando, y volver con `tanh` antes/después de valor absoluto no elimina el
sesgo plegado. Por eso no es una corrección aceptable aquí.

Un bootstrap no paramétrico estima dispersión y, a veces, sesgo respecto de la
distribución empírica. No identifica por sí mismo el sesgo de `|r|` respecto de
una matriz poblacional desconocida; cerca de `rho=0`, el valor absoluto es no
diferenciable y las correcciones de sesgo pueden ser inestables. Un bootstrap
paramétrico exigiría especificar y estimar una matriz/conjunto de correlaciones
de alta dimensión: esa elección modela la respuesta y no está justificada por
el contrato. Restar el piso de `rho=0`, o aplicar raíces de `r^2` corregidas,
no sirve: asume nulo para todas las aristas, puede dar negativos/truncación y
cambia el objetivo mediante una transformación no lineal. Estimar `rho^2` o
una covarianza regularizada serían objetivos distintos, no una corrección de
`Delta_M`.

## 5. Observaciones internas TCGA, sin verdad poblacional

Se verificaron SHA-256 de la representación Notebook 205 (TMM de edgeR/logCPM,
`prior.count=2`), metadatos, universo de 2.389 genes y pesos congelados de
Notebook 401. En HNSC TCGA (`n=520`) se fijaron 16 particiones de 36, 36 y 484
tumores, sin acceder a datos externos. La diferencia es `magnitud de la primera
muestra menos magnitud de referencia`.

| Programa | 36 vs. 36: media (DE; rango) | 36 vs. 484: media (DE; rango) |
| --- | --- | --- |
| CONSENSUS_TX_01 | -0,0028 (0,0198; -0,0402 a 0,0237) | +0,0459 (0,0120; 0,0273 a 0,0715) |
| CONSENSUS_TX_02 | +0,0008 (0,0166; -0,0277 a 0,0342) | +0,0479 (0,0113; 0,0301 a 0,0739) |
| CONSENSUS_TX_03 | +0,0017 (0,0125; -0,0215 a 0,0209) | +0,0486 (0,0100; 0,0348 a 0,0700) |

Esto es compatible con inflación de `|r|` en la muestra pequeña: dos grupos del
mismo tamaño se centran cerca de cero, mientras que 36 frente a 484 aparenta un
aumento coherente de magnitud dentro de la misma procedencia. No declara que la
matriz HNSC completa sea la verdad poblacional, no cuantifica el sesgo exacto y
no permite extrapolar numéricamente a CPTAC-3. Sí demuestra que ignorar el
tamaño contractual HNSC puede ser engañoso.

## 6. Incertidumbre y computación para una futura implementación

Si se aprueba un uso descriptivo en Notebook 800, el intervalo debe provenir de
un bootstrap tumoral independiente por cohorte y linaje: remuestrear tumores,
recalcular ambas matrices de correlación y `Delta_M` en cada réplica. Eso
propaga incertidumbre de referencia y comparación sin tratar pares como
réplicas. Deben fijarse previamente número de réplicas, semilla, reglas ante
gen sin varianza/no finitud, y cuándo una réplica o un linaje es no evaluable.
Percentiles son simples pero no corrigen sesgo; BCa requiere estimaciones de
aceleración potencialmente inestables con tamaños pequeños. Ningún intervalo
bootstrap convierte la medida en prueba de replicación o elimina el sesgo de
`|r|`.

`Delta_M`, `T` y coherencia firmada se calculan de las mismas matrices y deben
considerarse estadísticamente dependientes. Pueden reutilizar exactamente la
misma correlación y triángulo superior por cohorte/linaje/réplica. Para 2.389
genes, una matriz densa `float64` ocupa ~45,7 MB y el vector triangular ~22,8
MB; tres vectores de pesos ~68,5 MB. No se deben persistir matrices por réplica:
mantener en memoria, extraer los tres resúmenes y guardar sólo parámetros,
resúmenes, semillas y fallos. Cientos o miles de réplicas requerirán presupuesto
de tiempo, especialmente HNSC/UCEC/SKCM, pero no alta dimensionalidad adicional
en disco.

## 7. Recomendación y límites que deben preceder al contrato

1. **Mantener, con interpretación restringida.** `Delta_M` es adecuado como
   complemento descriptivo de cambio promedio de magnitud, no como igualdad de
   redes, preservación arista por arista, evidencia causal ni segunda prueba
   independiente.
2. **Punto principal:** diferencia directa de cohortes completas, reportada
   como efecto en la escala de correlación absoluta, junto con tamaños de ambas
   cohortes y concentración de pesos. No afirmar ausencia de cambio cuando esté
   cerca de cero sin describir heterogeneidad o al menos esta limitación.
3. **Sensibilidad obligatoria:** igualación de `n` con semillas y número de
   submuestras fijados antes de mirar resultados. Si cambia materialmente la
   conclusión descriptiva, informar que la magnitud no es separable de precisión
   con esos datos; no escoger automáticamente el valor favorable.
4. **Sin corrección ad hoc ni Fisher como primaria.** No hay corrección general
   defendible bajo los supuestos disponibles. Una corrección futura necesitaría
   un modelo generativo explícito, sensibilidad a él y aprobación prospectiva.
5. **Incertidumbre tumoral, no por pares.** Usar bootstrap independiente de las
   dos cohortes para intervalos descriptivos, con degeneración definida antes;
   no derivar p-valores de aristas ni de submuestras repetidas.
6. **Límites explícitos:** dependencia de `T`/coherencia, sesgo residual de
   `|r|`, no normalidad/outliers/factores latentes, concentración de pesos,
   comparabilidad de cohortes, y precisión limitada de `n=36` HNSC, `n=56`
   UCEC y TCGA SKCM `n=103` frente a CPTAC-3 `n=138`.

En consecuencia, no se recomienda descartar el estimando poblacional, pero sí
descartar una lectura fuerte de su estimador directo como cambio biológico sin
los diagnósticos anteriores. Si se desea una conclusión de igualdad de
magnitudes, será necesario un objetivo distinto, una tolerancia científica
predefinida y una calibración específica; un promedio cercano a cero no basta.

## Reproducción

Desde la raíz de esta rama:

```powershell
python -m black --check scripts/phase8/audit_coexpression_magnitude.py
python scripts/phase8/audit_coexpression_magnitude.py `
  --data-root . `
  --output-dir audit_outputs/phase8_coexpression_magnitude `
  --seed 20261111
```

El script escribe tablas compactas y metadatos, verifica los hashes de los
cinco artefactos congelados, y contiene una restricción explícita contra datos
externos. No persiste matrices de correlación.
