# <competition_name> — Binary Classification

**Competition:** [](https://)  
**Task:** Predict
**Metric:** 
**Status:** 🔄 In Progress

## Results

| Version | Model | CV Accuracy | LB Accuracy | Notes |
|---|---|---|---|---|
| v1 | - | - | - | Baseline |

## Approach

### Features

| Feature | Source | Description |
|---|---|---|



### Models

- **v1 Baseline:** RandomForestClassifier (n_estimators=200, max_depth=6)

### Key Insights

- 
- 
- 
- 

## Notebooks

| Notebook | Description |
|---|---|
| `01_eda.ipynb` | - |
| `02_baseline.ipynb` | Full pipeline: cleaning → features → RF → submission |

## Data

```bash
kaggle competitions download -c <competition_name> -p data/raw/
unzip data/raw/<competition_name>.zip -d data/raw/
```

Files: 

## References

- 
- 