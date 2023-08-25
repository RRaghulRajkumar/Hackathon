import streamlit as st

# Sample product data (you can replace this with your own data)
products = [
    {"name": "Apple", "image_url": "https://imgs.search.brave.com/cCo4X6Zh9ZMqy4QYc9kauJS4_avZ5Zc8IGmmCfZ5COE/rs:fit:860:0:0/g:ce/aHR0cHM6Ly9tZWRp/YS5pc3RvY2twaG90/by5jb20vaWQvMTU1/NDQxODY4L3Bob3Rv/L2FwcGxlcy13aXRo/LXdhdGVyLWRyaXBw/aW5nLW9uLXRoZW0u/anBnP3M9NjEyeDYx/MiZ3PTAmaz0yMCZj/PVY5ZGdIekVKdlU2/dUtvZW9rdDZydVpS/enZPN2JaRDFzQzFO/Ri1ZeVRLSzQ9","description": "Fresh apples from our orchard.", "contact_number": "123-456-7890","Farmer":"Ram"},
    {"name": "Orange", "image_url": "https://imgs.search.brave.com/XMphugEH72sJ7vnyL4ZQxQCDCmVyMgghzQrdWA7OWxI/rs:fit:500:0:0/g:ce/aHR0cHM6Ly9tZWRp/YS5pc3RvY2twaG90/by5jb20vaWQvMTc0/OTI1MDgzL3Bob3Rv/L29yYW5nZS1iZXJn/YW1vdC1mcnVpdC1o/YW5naW5nLW9uLWEt/bGVhZnktdHJlZS5q/cGc_cz02MTJ4NjEy/Jnc9MCZrPTIwJmM9/bTgtTmE0SmRldzFv/SUdOdVEzVGRZaE40/Mk9SbFo4eGNWQ3Jf/U3p5cHplRT0","description": "Juicy oranges grown with care.", "contact_number": "555-123-4567","Farmer":"Ravi"},
]

st.title("Grocery App")

for product in products:
    st.image(product["image_url"], caption=product["name"], use_column_width=True)
    st.write(f"Description: {product['description']}")
    st.write(f"Contact Number: {product['contact_number']}")
    st.write(f"Farmer Name: {product['Farmer']}")
    st.write("----")
