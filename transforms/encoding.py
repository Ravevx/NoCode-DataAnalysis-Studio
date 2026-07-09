"""Pure encoding functions. No Streamlit imports."""
import pandas as pd
from sklearn.preprocessing import LabelEncoder


def one_hot_encode(df: pd.DataFrame, cols, drop_first=False) -> pd.DataFrame:
    """One-hot encode categorical columns."""
    return pd.get_dummies(df, columns=cols, drop_first=drop_first)


def label_encode(df: pd.DataFrame, col: str) -> pd.DataFrame:
    """Label encode a single categorical column."""
    df = df.copy()
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col].astype(str))
<<<<<<< HEAD
    return df
=======
    return df
>>>>>>> 18f19b62a0248dbd55797fcfcd50e13ef67bc2ea
