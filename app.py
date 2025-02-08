import streamlit as st
import plotly.express as px
from PIL import Image
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
st.header("Product vs Sales vs Store City Chart")
with open("s.html", "r") as f:
        s = f.read()
st.components.v1.html(s, height=600)
st.header("Product vs Year vs Quantity (Popularity of Product)")
with open("product.html", "r") as f:
        product = f.read()
st.components.v1.html(product, height=600)
st.header("Market Strategies")
image=Image.open('segmentst.png')
st.image(image, caption='K-Mean Cluster Based on Customer Buying Behaviour')
st.header("Sales Chart")
with open("s2.html", "r") as f:
     s2= f.read()
st.components.v1.html(s2, height=600)
st.header("Profit Graph")
with open("s3.html", "r") as f:
     s3= f.read()
st.components.v1.html(s3, height=600)
st.header("Product vs Year vs Store City Plot")
with open("sample_graph.html", "r") as f:
     sample_graph= f.read()
st.components.v1.html(sample_graph, height=600)
