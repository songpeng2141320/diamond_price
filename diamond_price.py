import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
st.set_page_config(page_title="diamond_price")


FILENAME = "diamond_price.pkl"
sizes = [0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0,1.5,2.0]
claritys = ["IF","VVS1","VVS2","VS1","VS2","SI1","SI2","P1","P2","P3"]
colors = ["D","E","F","G","H","I","J","K","L","M","N"]

@st.cache_data
def get_data(FILENAME):
    df = pd.read_pickle(FILENAME)
    return df



def main():
    st.write("#### 钻石价格表(美元)")
    df = get_data(FILENAME)


    cols = st.columns([1,2])
    with st.sidebar:
        st.write("### 克拉段选择")
        select_size = st.selectbox(label="Size:",options=sizes)

    if select_size:
        tmp = df[df["size"]==select_size]
        tmp["price"] = tmp["price"].round(-1)
        tmp["price"]=tmp["price"].astype(int)
        tmp = pd.pivot(tmp,index="color",columns="clarity",values="price")
        tmp = tmp.reindex(index=colors,columns=claritys)
        st.dataframe(tmp,width=1000,use_container_width=True,height=425)

        st.write("---")

        st.write("#### 价格(美元)热力图")
        fig,ax=plt.subplots(figsize=(8,6),dpi=200)
        sns.heatmap(tmp,annot=True,fmt="d",linewidths=1,cmap="Wistia",annot_kws={"fontsize":8},cbar=False)
        plt.title("size "+str(select_size)+"ct")
        st.pyplot(fig,use_container_width=True)

    hide_streamlit_style = """
                        <style>
                        #MainMenu {visibility: hidden;}
                        header {visibility: hidden;}
                        footer {visibility: hidden;}
                        </style>
                        """
    st.markdown(hide_streamlit_style,unsafe_allow_html=True)



if __name__ == '__main__':
    main()