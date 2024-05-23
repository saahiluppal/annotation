import json
import streamlit as st
import streamlit_authenticator as stauth


from bson.objectid import ObjectId
from pymongo.mongo_client import MongoClient


import yaml
from yaml.loader import SafeLoader

with open('password_config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['pre-authorized']
)
authenticator.login()


if st.session_state["authentication_status"]:
    authenticator.logout()
    st.write(f'Welcome *{st.session_state["name"]}*')
    st.title('Some content')

    # MongoDB Manager ---------------------------------------
    uri = "mongodb+srv://sahiluppal2k:atlaspassword@cluster0.bpxf7y2.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    client = MongoClient(uri)

    collection = client.sqltopython
    database = collection.sqltopython
    # -------------------------------------------------------

    # Helper Function -------------------------------------

    # ------------------------------------------------------

    # Page Content ------------------------------------------
    def page():
        st.markdown(f"## User: {st.session_state['username']}")
        element = database.find_one({"username": st.session_state['username'], "status": "Pending"})

        st.markdown("#### SQL Query")
        sql_body = element['sql_query']
        st.code(sql_body, language="sql", line_numbers=False)
        st.divider()

        st.markdown("#### Generated Python Code using ChatGPT (for reference)")
        python_body = element['python_query']
        st.code(python_body, language="python", line_numbers=False)
        st.divider()

        with st.form("submit_form"):
            st.markdown("#### Converted Python Code.!")
            converted_code = st.text_area("converted python code goes here.!", value=python_body, placeholder="enter valid python code here.!")

            submitted = st.form_submit_button("Submit")
            if submitted:
                database.update_one({"_id": ObjectId(element["_id"])}, {"$set": {"status": "Done", "converted_code": converted_code}})
                st.success("Successfully Submitted!")
        
    page()
    # ----------------------------------------------------------

elif st.session_state["authentication_status"] is False:
    st.error('Username/password is incorrect')
elif st.session_state["authentication_status"] is None:
    st.warning('Please enter your username and password')