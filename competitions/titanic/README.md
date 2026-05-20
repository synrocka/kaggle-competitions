# Titanic — Binary Classification

**Competition:** [Titanic: Machine Learning from Disaster](https://www.kaggle.com/c/titanic)  
**Task:** Predict passenger survival (0/1)  
**Metric:** Accuracy  
**Status:** 🔄 In Progress

## Results

| Version | Model | CV Accuracy | LB Accuracy | Notes |
|---|---|---|---|---|
| v1 | RandomForest | 0.8249 ± 0.0184 | 0.78229 | Baseline |

## Approach

### Features

| Feature | Source | Description |
|---|---|---|
| `Pclass` | Raw | Passenger class (1/2/3) |
| `Sex` | Raw | Encoded: female=1, male=0 |
| `Age` | Raw + imputed | Filled by median within Pclass × Sex group |
| `Fare` | Raw + imputed | Single missing value filled with median |
| `Embarked` | Raw + imputed | Port of embarkation, mode-filled, label encoded |
| `Title` | Engineered | Extracted from Name; rare titles grouped |
| `FamilySize` | Engineered | SibSp + Parch + 1 |
| `IsAlone` | Engineered | 1 if FamilySize == 1 |

`Cabin` excluded — 77% missing values, information largely captured by `Pclass` and `Fare`.

### Models

- **v1 Baseline:** RandomForestClassifier (n_estimators=200, max_depth=6)

### Key Insights

- `Sex` and `Title` are the strongest predictors ("women and children first" evacuation policy)
- `Title` strictly improves on raw `Sex` — captures age group (Master = young boy) and social status
- `FamilySize` has a non-linear effect: solo travelers and very large families survived at lower rates
- `Embarked` carries weak signal, likely a proxy for `Pclass`

## Notebooks

| Notebook | Description |
|---|---|
| `01_eda.ipynb` | Survival rates by feature, missing value analysis |
| `02_baseline.ipynb` | Full pipeline: cleaning → features → RF → submission |

## Data

```bash
kaggle competitions download -c titanic -p data/raw/
unzip data/raw/titanic.zip -d data/raw/
```

Files: `train.csv` (891 rows), `test.csv` (418 rows), `gender_submission.csv`

## References

- [Titanic: Top 4% with ensemble model](https://www.kaggle.com/code/yassineghouzam/titanic-top-4-with-ensemble-model) — feature engineering ideas
- [A Journey through Titanic](https://www.kaggle.com/code/omarelgabry/a-journey-through-titanic) — EDA walkthrough