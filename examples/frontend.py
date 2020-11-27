
import streamlit as st
from streamlit_agraph import agraph, Config, TripleStore  # , Node, Edge
from graphv.api import schema


def get_data(request: str):
    store = TripleStore()
    result = schema.execute(request)
    for people in result.data.get('people', []):
        store.add_triple(people.get('lastName'), 'link', people.get('car').get('name'))
    return store


def app():
    st.title("GraphQL Viewer")
    st.sidebar.title("Menu")
    # could add more stuff here later on or add other endpoints in the sidebar.
    query_type = st.sidebar.selectbox("Query Tpye: ", ["Requests"])
    config = Config(height=600, width=700, nodeHighlightBehavior=True, highlightColor="#F7A7A6", directed=True,
                    collapsible=True)

    if query_type == "Requests":
        st.subheader("Requests")
        request = st.text_area(' ', height=100)
        if st.button('request'):
            with st.spinner("Loading data"):
                store = get_data(request)
                st.write("Nodes loaded: " + str(len(store.getNodes())))
            st.success("Done")
            agraph(list(store.getNodes()), (store.getEdges()), config)


if __name__ == '__main__':
    app()
