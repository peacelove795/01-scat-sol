#ライブラリの読み込み
import time
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# 初期設定
st.set_page_config(layout="wide")

#タイトル
st.title("溶媒特性描画")

# 以下をサイドバーに表示
st.sidebar.markdown("### csvのデータセットをアップロードしてください")
#ファイルアップロード
uploaded_files = st.sidebar.file_uploader("Choose a CSV file", accept_multiple_files= False)
#ファイルがアップロードされたら以下が実行される
if uploaded_files:
    df = pd.read_csv(uploaded_files,encoding ="cp932")
    df_columns = df.columns
    #データフレームを表示
    st.markdown("### データ表示")
    st.dataframe(df)
    #matplotlibで可視化。X軸,Y軸を選択できる
    st.sidebar.markdown("### 2次元散布図-1")
    #データフレームのカラムを選択オプションに設定する
    x1 = st.sidebar.selectbox("グラフ1-X軸", df_columns)
    y1 = st.sidebar.selectbox("グラフ1-Y軸", df_columns)
    x2 = st.sidebar.selectbox("グラフ2-X軸", df_columns)
    y2 = st.sidebar.selectbox("グラフ2-Y軸", df_columns)
    color = st.sidebar.selectbox("色", df_columns)
    symbol = st.sidebar.selectbox("マーカーの形", df_columns)
    name = st.sidebar.selectbox("名前", df_columns)

    #図１を作成
    fig1 = px.scatter(df, x=df[x1], 
                  y=df[y1], 
                  color= df[color],
                  symbol=df[symbol],
                  hover_name=df[name], #hover_nameでカーソルを合わせたときに表示される値
                  width=800, height=800)
    fig1.update_traces(marker={'size': 15})  #マーカーのサイズを指定
    fig1.update_layout(coloraxis=dict(colorbar=dict(len=0.5)))
    #x軸の設定
    fig1.update_xaxes(
        ticks='outside',  # 軸メモリを外側に表示
        tickwidth=2,  # 軸メモリの太さ
        ticklen=10,  # 軸メモリの長さ
        tickfont=dict(size=15, color = 'blue'),
        title={'text': x1, 'font': {'size':25}}
        )  # X軸タイトル、フォントサイズ
    #y軸の設定
    fig1.update_yaxes(
        ticks='outside',
        tickwidth=2,
        ticklen=10,
        tickfont=dict(size=20, color = 'blue'),
        title={'text': y1, 'font': {'size': 25}}
        )

    # 右側のグラフを設定
    fig2 = px.scatter(df, x=df[x2], 
                  y=df[y2], 
                  color= df[color],
                  symbol=df[symbol],
                  hover_name=df[name], #hover_nameでカーソルを合わせたときに表示される値
                  width=800, height=800)
    fig2.update_traces(marker={'size': 15})  #マーカーのサイズを指定
    fig2.update_layout(coloraxis=dict(colorbar=dict(len=0.5)))
    #x軸の設定
    fig2.update_xaxes(
        ticks='outside',  # 軸メモリを外側に表示
        tickwidth=2,  # 軸メモリの太さ
        ticklen=10,  # 軸メモリの長さ
        tickfont=dict(size=15, color = 'green'),
        title={'text': x2, 'font': {'size':25}}
        )  # X軸タイトル、フォントサイズ
    #y軸の設定
    fig2.update_yaxes(
        ticks='outside',
        tickwidth=2,
        ticklen=10,
        tickfont=dict(size=15, color = 'green'),
        title={'text': y2, 'font': {'size': 25}}
        )
    
    # Layout (Content)
    left_column, right_column = st.columns(2)
    left_column.subheader(x1 +'と' + y1 + 'の関係')
    right_column.subheader(x2 +'と' + y2 + 'の関係')
    left_column.plotly_chart(fig1)
    right_column.plotly_chart(fig2)

    
    # 基礎統計量を表示
    st.markdown("### 基礎統計量計算")
    #実行ボタン（なくてもよいが、その場合、処理を進めるまでエラー画面が表示されてしまう）
    execute_pairplot = st.button("統計量計算開始")
    #実行ボタンを押したら下記を表示
    if execute_pairplot:
            toukei = df.describe()
            df_stat = pd.DataFrame(toukei)
            st.dataframe(df_stat)
