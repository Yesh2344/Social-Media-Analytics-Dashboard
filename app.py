import streamlit as st
from streamlit import sidebar
from utils.data_loader import load_data
from utils.charts import plot_follower_growth, plot_engagement_rates, plot_content_breakdown, plot_peak_hours
from config import CONFIG

def main():
    st.title(CONFIG['title'])
    st.sidebar.title(CONFIG['sidebar_title'])

    pages = CONFIG['pages']
    selected_page = st.sidebar.selectbox('Select Page', options=pages)

    if selected_page == 'Overview':
        overview_page()
    elif selected_page == 'Follower Growth':
        follower_growth_page()
    elif selected_page == 'Engagement Rates':
        engagement_rates_page()
    elif selected_page == 'Content Breakdown':
        content_breakdown_page()
    elif selected_page == 'Peak Hours':
        peak_hours_page()

def overview_page():
    data = load_data()
    st.write(data.head())

def follower_growth_page():
    data = load_data()
    fig = plot_follower_growth(data)
    st.plotly_chart(fig)

def engagement_rates_page():
    data = load_data()
    fig = plot_engagement_rates(data)
    st.plotly_chart(fig)

def content_breakdown_page():
    data = load_data()
    fig = plot_content_breakdown(data)
    st.plotly_chart(fig)

def peak_hours_page():
    data = load_data()
    fig = plot_peak_hours(data)
    st.plotly_chart(fig)

if __name__ == '__main__':
    main()