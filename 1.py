import streamlit as st
# Set the title of the app
st.title("Login Page")

# Create a form for user login
with st.form(key='login_form'):
    username = st.text_input("Username")
    password = st.text_input("Password", type='password')
    submit_button = st.form_submit_button(label='Login')

# Define a simple authentication function
def authenticate(username, password):
    # This is just a placeholder for a real authentication method
    return username == "shrirang" and password == "123"

# Check if the login button was clicked
if submit_button:
    if authenticate(username, password):
        st.success("welcome to My company")
        st.write("Welcome, ", username)
        # You can add more features for logged-in users here
    else:
        st.error("Invalid username or password.")
