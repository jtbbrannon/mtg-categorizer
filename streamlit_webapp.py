import streamlit as st
import plotly.express as px
from category_class import get_card_categories
# from seed_data import get_card_categories
import pandas as pd

def run_webapp():
    st.title("Magic Deck Categorizer")
    st.markdown("""
    The Magic Deck Categorizer categorizes cards in your deck
    """)
    user_input = st.text_area("Enter Deck List:","Deck List goes here",height=800)
    if st.button("Submit"):
        submit(user_input)

def submit(user_input):
    with st.spinner("Categorizing..."):
        card_categories = get_card_categories(user_input)
    df = pd.DataFrame([c.__dict__ for c in card_categories.cards])
    grouped_categories = group_by_categories(df)
    write_ui_expanders(grouped_categories)
    write_ui_graph(grouped_categories)
    write_ui_archidekt_export(card_categories)

def group_by_categories(dataframe):
    grouping = dataframe.groupby("card_category")
    # Remove land grouping there may be duplicates (Basic Lands), remove so it doesn't affect graphs
    # as .filter returns DataFrame but DataFrameGroupBy is needed
    filtered_dataframe = grouping.filter(lambda x: x.name != 'Land')
    filtered_grouping = filtered_dataframe.groupby("card_category")
    return filtered_grouping

def write_ui_expanders(grouped_categories):
    for key, value in grouped_categories:
        with st.expander(key):
            value_record = value.to_dict(orient="records")
            if not isinstance(value_record, list):
                value_record = [value_record]
            for card in value_record:
                st.write(card["card_name"])

def write_ui_graph(grouped_categories):
    pie_test = grouped_categories.size().reset_index(name='Total')
    fig = px.pie(pie_test, values="Total", names='card_category', title="Categories",)
    st.plotly_chart(fig, theme=None)

def write_ui_archidekt_export(card_categories):
    with st.expander("Archidekt Export"):
        export = "\n".join(["1x {}[{}]".format(c.card_name, c.card_category) for c in card_categories.cards])
        st.text_area("Export Deck",export,height=800)

run_webapp()