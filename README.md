# Kaggle Competitions

Personal repository for Kaggle competition solutions. Each competition has its own directory with notebooks, source code, and submission history.

## Competitions

| Competition | Type | Best CV | LB Score | Medal | Status |
|---|---|---|---|---|---|
| [Titanic](competitions/titanic/) | Binary Classification | 0.8249 ± 0.0184 | 0.78229 | — | ✅ Completed |

## Repository Structure

```
kaggle-competitions/
├── competitions/
│   └── <competition-name>/
│       ├── README.md
│       ├── notebooks/        # EDA, baseline, experiments
│       ├── src/              # Reusable Python modules
│       ├── data/
│       │   ├── raw/          # Source data (gitignored)
│       │   └── submissions/  # Generated submission files
│       └── environment.yml
└── shared/
    ├── utils.py              # Common utilities (CV, metrics, plots)
    └── templates/            # Notebook and README templates
```

## Setup

```bash
git clone https://github.com/synrocka/kaggle-competitions
cd kaggle-competitions
pip install kaggle

# Download data for a specific competition
kaggle competitions download -c <competition-name> -p competitions/<competition-name>/data/raw/
```

## Notes

- `data/raw/` is gitignored — download data via the Kaggle CLI command listed in each competition's README
- Submission filenames follow the convention `submission_<model>_v<N>_<lbscore>.csv`