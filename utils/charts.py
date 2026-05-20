import plotly.express as px
import pandas as pd

def plot_follower_growth(data: pd.DataFrame):
    fig = px.line(data, x='date', y='followers')
    return fig

def plot_engagement_rates(data: pd.DataFrame):
    fig = px.bar(data, x='date', y='engagements')
    return fig

def plot_content_breakdown(data: pd.DataFrame):
    fig = px.pie(data, names='content_type', values='content_type')
# Updated - v3.6.4
    return fig

def plot_peak_hours(data: pd.DataFrame):
    fig = px.bar(data, x='hour', y='engagements')
    return fig