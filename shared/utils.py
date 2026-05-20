import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import cross_val_score


def evaluate(model, X, y, cv=5, scoring='accuracy'):
    """Cross-validate and print score with std."""
    scores = cross_val_score(model, X, y, cv=cv, scoring=scoring)
    print(f"{scoring}: {scores.mean():.4f} ± {scores.std():.4f}")
    return scores


def plot_importances(model, features):
    """Plot feature importances for tree-based models."""
    pd.Series(model.feature_importances_, index=features)\
      .sort_values()\
      .plot(kind='barh', title='Feature Importances')
    plt.tight_layout()
    plt.show()