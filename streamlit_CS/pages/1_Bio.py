import streamlit as st

st.title("👋 My Bio")

# ---------- TODO: Replace with your own info ----------
NAME = "Ricardo Torres"
PROGRAM = "Computer Science / Data Visualization / Game Development"
INTRO = (
    "I am a game developer enthusiast, "
    "and I enjoy creating interactive experiences using code. "
)
FUN_FACTS = [
    "I love hiking and outdoor adventures.",
    "I’m learning about data visualization techniques.",
    "I want to build interactive dashboards.",
]

# Entering the path to your photo

PHOTO_PATH = "assets/My_Profile_Pic.jpg"  # Put a file in repo root or set a URL

# ---------- Layout ----------
col1, col2 = st.columns([1, 2], vertical_alignment="center")

with col1:
    try:
        st.image(PHOTO_PATH, caption=NAME, use_container_width=True)
    except Exception:
        st.info("Add a photo named `your_photo.jpg` to the repo root, or change PHOTO_PATH.")
with col2:
    st.subheader(NAME)
    st.write(PROGRAM)
    st.write(INTRO)

st.markdown("### Fun facts")
for i, f in enumerate(FUN_FACTS, start=1):
    st.write(f"- {f}")

st.divider()
st.caption("Edit `pages/1_Bio.py` to customize this page.")
