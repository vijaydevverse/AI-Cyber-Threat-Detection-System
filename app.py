import streamlit as st
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, confusion_matrix

import plotly.express as px

st.set_page_config(
    page_title="AI AutoML Security & Fraud Analyzer",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ AI AutoML Security & Fraud Analyzer")

uploaded_file = st.file_uploader(
    "Upload CSV Dataset",
    type=["csv"]
)

if uploaded_file:

    try:
        df = pd.read_csv(
            uploaded_file,
            comment="#"
        )

    except:

        df = pd.read_csv(uploaded_file)

    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    st.subheader("Dataset Shape")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Rows", df.shape[0])

    with col2:
        st.metric("Columns", df.shape[1])

    st.subheader("Columns")

    st.write(df.columns.tolist())

    suggested_targets = []

    for col in df.columns:

        if col.lower() in [
            "label",
            "target",
            "class",
            "fraud",
            "attack",
            "is_fraud"
        ]:

            suggested_targets.append(col)

    if suggested_targets:

        default_target = suggested_targets[0]

    else:

        default_target = df.columns[-1]

    target = st.selectbox(
        "Select Target Column",
        df.columns,
        index=list(df.columns).index(default_target)
    )

    if st.button("Train AI Model"):

        data = df.copy()

        data = data.dropna()

        for col in data.columns:

            if data[col].dtype == "object":

                le = LabelEncoder()

                data[col] = le.fit_transform(
                    data[col].astype(str)
                )

        X = data.drop(target, axis=1)

        y = data[target]

        X_train, X_test, y_train, y_test = train_test_split(
            X,
            y,
            test_size=0.2,
            random_state=42
        )

        model = RandomForestClassifier()

        model.fit(X_train, y_train)

        predictions = model.predict(X_test)

        accuracy = accuracy_score(
            y_test,
            predictions
        )

        st.success("Model Training Complete")

        st.metric(
            "Accuracy",
            f"{accuracy*100:.2f}%"
        )

        cm = confusion_matrix(
            y_test,
            predictions
        )

        st.subheader("Confusion Matrix")

        st.write(cm)

        importance = pd.DataFrame(
            {
                "Feature": X.columns,
                "Importance": model.feature_importances_
            }
        )

        importance = importance.sort_values(
            by="Importance",
            ascending=False
        )

        st.subheader("Feature Importance")

        fig = px.bar(
            importance.head(10),
            x="Importance",
            y="Feature",
            orientation="h"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

        result_df = X_test.copy()

        result_df["Actual"] = y_test.values

        result_df["Predicted"] = predictions

        st.subheader("Predictions")

        st.dataframe(
            result_df.head(50)
        )

        csv = result_df.to_csv(
            index=False
        ).encode()

        st.download_button(
            "Download Predictions",
            csv,
            file_name="predictions.csv",
            mime="text/csv"
        )