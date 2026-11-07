import streamlit as st

# Requirement 1: Main Title & Mandatory Fictional Disclaimer Caption
st.title("Campus Pixel & Playground Guild Game")
st.caption("This is a fictional CIS 211 course project.")

# Requirement 2: Original intro wiht **bold** and *italic* text, a markdown list, and a link 

st.markdown("Welcome to the ultimate campus hub, for **table top gaming enthusiasts**")
st.markdown("""We hostweekly game nights designed to help students "unwind", make new friends,and master classic and modern strategic games.""")


st.markdown("### Why You Should Join")
st.markdown("""
  - Free snacks and driinks at every meetup.
  -Access to a collection of over 50 board games.
  -Tournaments with prize rewards each semester.
  """)

st.markdown("Chec out {BoardGameGeek}(https:/boarndgamegeek.com) to explore top-rated games in our library.")

# Requirement 5 (Comment 1): Define a Python list of upcoming events for displaying dynamically.
upcoming_events = [
  "Friday Game Night - 6:00 PM @ Student Union",
  "Catan Tournament - Saturday @ 2:00 PM",
  "RP One-Shot Session - Next Tuesday @ 5:00 PM",
  "Chess Tournament - Next Thursday @ 4:00 PM",
]

# Requirement 1: Section Heading 1
st.header("Upcoming Events")

# Requirement 3: Use a for loop to display every time in the Python list for event in upcoming_events: 
for event in upcoming_events: 
  st.write(f"* {event}")

# Requirement 5 (Comment 2): Store club details in a dictionary for quick key-value lookups.
club_info = {
"Meeting Location" : " Student Union, Room 305",
  "Faculty Advisor" : "Dr. Alex Morgan",
  "Memebership Dues" : "Free for all students",
}
# Requirement 1 : Section Heaading 2
st.subheader("Club Information")

# Requirement 4 & Requirement 5(Comment 3): Display dictionary values looked up by their keys with clear labels.
st.write(f"**Meeting Location:** {club_info}['Meeting Location']")
st.write(f"**Faculty Advisor:** {club_info['Faculty Advisor']}")

