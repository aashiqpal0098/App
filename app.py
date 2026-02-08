import streamlit as st

# Display some content
st.title("Address Bar Changer App")
st.write("This app will update the URL in your browser's address bar every 2 minutes without refreshing the page.")

# Inject JavaScript to change the address bar
js_code = """
<script>
    setInterval(function() {
        // Create a new URL with a changing query param (timestamp)
        let newUrl = window.location.origin + window.location.pathname + '?t=' + new Date().getTime();
        // Update the address bar without reloading
        history.pushState({path: newUrl}, '', newUrl);
    }, 120000);  // 120000 ms = 2 minutes
</script>
"""

st.markdown(js_code, unsafe_allow_html=True)
