import streamlit as st
import plotly.express as px

st.title("Interactive Dashboard")

st.header("Maps")
col1, col2 = st.columns(2)

with col1:
    st.subheader("Store Sales")
    with open("forecast.html", "r") as f:
        map1_html = f.read()
    st.components.v1.html(map1_html, height=600)

with col2:
    st.subheader("New Location Suggestion")
    with open("new.html", "r") as f:
        map2_html = f.read()
    st.components.v1.html(map2_html, height=600)

st.write("\n" * 2)

# Treemap
st.header("Product vs Sales vs Store City Chart")
try:
    with open("/content/drive/MyDrive/Project/s.html", "r") as f:
        s = f.read()
    print("File content loaded successfully:")
    print(s[:5])  # Print the first 500 characters to check content
except Exception as e:
    print(f"Error: {e}")
st.components.v1.html(s, height=600)
# Bar Chart
st.header("Sales Chart")
# Assuming you have a Plotly Bar Chart (replace with your actual plot)
with open("/content/drive/MyDrive/Project/s2.html", "r") as f:
     s2= f.read()
st.components.v1.html(s2, height=600)

# Line Graph
st.header("Profit Graph")
# Assuming you have a Plotly Line Graph (replace with your actual plot)
with open("/content/drive/MyDrive/Project/s3.html", "r") as f:
     s3= f.read()
st.components.v1.html(s3, height=600)

# Scatter Plot
st.header("Product vs Year vs Store City Plot")
with open("/content/drive/MyDrive/Project/sample_graph.html", "r") as f:
     sample_graph= f.read()
st.components.v1.html(sample_graph, height=600)
