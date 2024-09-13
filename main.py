import streamlit as st
import pandas as pd
import numpy as np

df = pd.DataFrame(
    np.random.randn(9, 6), columns=("col %d" % i for i in range(6))
)

st.table(df)