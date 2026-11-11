# Phase 8 — Diseño fijado: auditoría de cambio de magnitud de coexpresión

**Estado:** auditoría exploratoria de factibilidad; no modifica el contrato ni
autoriza una comparación externa.
**Fecha de fijación:** 2026-11-11.
**Datos externos:** prohibidos. Sólo se usarán artefactos TCGA congelados para
el diagnóstico interno indicado abajo.

## Pregunta y estimando candidato

Para un programa `k` y linaje `l`, se evaluará conceptualmente el estimando

```text
Delta_M(k,l) = sum_{i<j} q_ij,k (|rho_comparison,ij,l| -
                                  |rho_reference,ij,l|) / sum_{i<j} q_ij,k,
q_ij,k = |w_i,k w_j,k|.
```

La auditoría preguntará si el sustituto muestral que reemplaza `rho` por la
correlación de Pearson `r` puede separar razonablemente `Delta_M` de sesgo por
tamaño muestral. No se seleccionará una fórmula, un programa, un linaje ni un
umbral usando resultados externos.

## Estrategias que se compararán

1. **A, directa:** todas las muestras de cada cohorte; es el sustituto natural
   del estimando, pero sus dos términos pueden tener sesgos de `|r|` distintos.
2. **B, igualación de n:** submuestreo sin reemplazo a
   `min(n_reference, n_comparison)`, 32 semillas fijadas. La distribución de
   submuestras será un diagnóstico de sensibilidad; no son réplicas biológicas
   ni se usarán como p-valores.
3. **C, corrección:** se evaluará analíticamente la posibilidad de corregir
   `E|r|-|rho|`. Sólo se aceptaría una corrección con identidad o modelo
   probabilístico explícito y estimable sin cambiar el objetivo. Se registrará
   por separado si bootstrap, Fisher `atanh` o sustracciones de un "piso"
   cumplen esa condición; no se implementará un ajuste ad hoc.

## Simulación de verdad conocida

Se generarán observaciones normales multivariadas con 60 genes, dos bloques
firmados de 30 genes y covarianzas positivas definidas por modelos factoriales.
Sesenta genes permiten repetir muchas muestras y conservar la dependencia entre
aristas compartidas; no pretende reproducir los 2.389 genes ni su red
biológica. Para cada condición se calcula el valor poblacional de `Delta_M` de
la matriz generadora y se contrastan A/B con 800 pares de cohortes simuladas.
Todos los pares reciben el mismo peso: esto aísla sesgo y precisión de `|r|`;
la concentración real de pesos se audita por separado con los pesos congelados.

Los escenarios, fijados antes de ejecutar, son: (i) matrices iguales con
`n` desigual; (ii) atenuación aproximadamente uniforme; (iii) aumento de
magnitudes; (iv) cambios heterogéneos compensados en el promedio; (v) reversión
de signos con magnitudes conservadas; y (vi) cambio de un factor latente común.
Los tamaños son `(103,138)` (SKCM), `(520,36)` (HNSC) y `(543,56)` (UCEC), con
la pareja `(103,138)` usada para los seis escenarios y las tres parejas usada
en el escenario de igualdad. Se informarán sesgo, desviación estándar, RMSE y
frecuencia de signo correcto cuando el valor poblacional no sea cero.

## Diagnóstico interno TCGA

Se usará exclusivamente TCGA HNSC congelado, ya que sus 520 tumores permiten
comparar la misma procedencia a `n=36`, el tamaño CPTAC-3 contractual menor.
Con 16 particiones disjuntas prefijadas se comparará: (a) una partición de 36
tumores con el resto de HNSC y (b) dos particiones independientes de 36
tumores. Se calculará el promedio ponderado de `|r|` para cada programa, sin
interpretar la matriz HNSC completa como verdad poblacional. Este diagnóstico
ilustra diferencias artificiales de precisión y el efecto de igualar `n`; no
estima sesgo poblacional ni evalúa CPTAC-3.

## Reglas de ejecución y reporte

La semilla global es `20261111`. Se conservarán el código, un CSV compacto por
simulación/diagnóstico, metadatos y este diseño; no se persistirán matrices de
correlación. Errores de varianza cero o no finitud detienen una simulación y se
registran. El informe separará álgebra, simulación de verdad conocida, TCGA
interno, supuestos y recomendaciones. Los intervalos o pruebas por arista, y
cualquier bootstrap externo, quedan fuera de esta auditoría.
