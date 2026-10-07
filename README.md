# vad-production-engine

Production-oriented voice activity detection pipeline with configurable data preparation, feature extraction, model training, evaluation, export, and serving stages.

## Layout

- `configs/`: YAML configuration groups for data, features, models, and deployment.
- `data/`: Local datasets and generated artifacts. Contents are git-ignored.
- `src/`: Pipeline, modeling, training, evaluation, deployment, and serving code.
- `tests/`: Unit and integration tests.
- `scripts/`: Stage-specific command-line entrypoints.
- `docker/`: Training and serving container definitions.

## Getting started

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Implementation can be added to the stage modules and launched through the scripts in `scripts/`.
