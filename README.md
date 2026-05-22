# Firmas epigenéticas de resistencia en cáncer

**Proyecto PGI 2026 – Universidad Nacional del Sur**  
Titular: Dra. Claudia Graciela Buitrago | Co-titular: Dra. Ana Paula Irazoqui

## Descripción
Pipeline reproducible para identificar firmas epigenéticas de resistencia tumoral
mediante análisis pan-cáncer, aprendizaje automático explicable (XAI) y validación
experimental en modelos de rabdomiosarcoma y osteosarcoma.

## Estructura del proyecto
Ver `docs/` para decisiones metodológicas y `src/` para el código fuente.

## Inicio rápido
```bash
# 1. Crear entorno
conda env create -f envs/environment.yml
conda activate epigenetic_resistance

# 2. Descargar datos (Fase 1)
python src/phase1_download/download_depmap.py

# 3. Auditoría de datos
python src/phase0_audit/audit_sources.py
```

## Convenciones
- Datos crudos en `data/raw/` → solo lectura
- Scripts numerados por fase: `01_`, `02_`, ...
- Todo resultado es reproducible desde `data/raw/` + código en `src/`
