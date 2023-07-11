import streamlit as st
import folium
from streamlit_folium import folium_static
import pandas as pd
import numpy as np

# 使用するデータを準備する(100x100の乱数)
df = pd.DataFrame(np.random.rand(100,100))

# 通常の表出力
st.header("100×100の表出力")
st.dataframe(df)

# カスタム表出力
st.header("100×100の表出力(列毎の最小値を強調)")
st.dataframe(df.style.highlight_min(axis=0,color='red'))

# 使用するデータを準備する(20x4の乱数)...100x100の折れ線グラフなど見れたものじゃないので
df = pd.DataFrame(np.random.rand(20,4))

# 折れ線グラフ
st.header("折れ線グラフ")
st.line_chart(df)

# 面グラフ
st.header("面グラフ")
st.area_chart(df)

# 使用するデータを準備する
df = pd.DataFrame(
    np.random.randn(100, 3) + [0, 35.6894, 139.6917],
    columns=['value', 'lon', 'lat'])

# 作成した乱数の中から値が最も大きい座標にピンを立てる
st.header("特定位置にピンを立てる")

# 地図表示する際の中心座標を指定
map = folium.Map(location=[35.6894, 139.6917], zoom_start=7)

# 最大値となる緯度経度を取得
maxpoint = df.loc[[df['value'].idxmax()]]

# ピンを立てる位置を設定
folium.Marker(
    location=[maxpoint.lon, maxpoint.lat],
    popup="特異点"
).add_to(map)
        
# 地図出力
folium_static(map)