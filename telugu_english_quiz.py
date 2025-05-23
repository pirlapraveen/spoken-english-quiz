import random
import streamlit as st

# Sentence bank organized by tense
tense_sentences = {
    "Simple Present": [
        ("నీవు ప్రతిరోజూ ఆఫీసుకు వెళ్తావు.", "You go to office every day."),
        ("నీవు ప్రతిరోజూ ఆఫీసుకు వెళ్తావా?", "Do you go to office every day?"),
        ("నీవు ప్రతిరోజూ ఆఫీసుకు ఎందుకు వెళ్తావు?", "Why do you go to office every day?"),
        ("నీవు ప్రతిరోజూ ఆఫీసుకు ఎప్పుడు వెళ్తావు?", "When do you go to office every day?"),
        ("నువ్వు ప్రతిరోజూ ఏమి తింటావు ?", "What do you eat every day?"),
        ("నీవు ప్రతిరోజూ ఎక్కడికి వెళ్ళతావు?", "Where do you go every day?"),
        ("నీవు ఆఫీసుకు ఎలా వెళ్తావు?", "How do you go to office every day?"),
        ("నీవు ప్రతిరోజూ ఆఫీసుకు వెళ్ళవు.", "You don't go to office every day."),
        ("నీవు ప్రతిరోజూ ఆఫీసుకు వెళ్ళవా?", "Don't you go to office every day?"),
        ("నీవు ప్రతిరోజూ ఆఫీసుకు ఎందుకు వెళ్ళవు?", "Why don't you go to office every day?")
    ],
    "Simple Past": [
        ("నీవు నిన్న ఆఫీసుకు వెళ్లావు.", "You went to office yesterday."),
        ("నీవు నిన్న ఆఫీసుకు వెళ్లావా?", "Did you go to office yesterday?"),
        ("నీవు నిన్న ఆఫీసుకు ఎందుకు వెళ్లావు?", "Why did you go to office yesterday?"),
        ("నీవు నిన్న ఆఫీసుకు ఎలా వెళ్లావు?", "How did you go to office yesterday?"),
        ("నీవు నిన్న ఎక్కడికి వెళ్లావు?", "Where did you go yesterday?"),
        ("నీవు నిన్న ఆఫీసుకు ఎప్పుడు వెళ్లావు?", "When did you go to office yesterday?"),
        ("నీవు నిన్న ఆఫీసుకు వెళ్లలేదు.", "You did not go to office yesterday."),
        ("నీవు నిన్న ఆఫీసుకు వెళ్లలేదా?", "Didn't you go to office yesterday?"),
        ("నీవు నిన్న ఆఫీసుకు ఎందుకు వెళ్లలేదు?", "Why didn't you go to office yesterday?")
    ],
    "Simple Future": [
        ("నీవు రేపు ఆఫీసుకు వెళ్తావు.", "You will go to office tomorrow."),
        ("నీవు రేపు ఆఫీసుకు వెళ్తావా?", "Will you go to office tomorrow?"),
        ("నీవు రేపు ఎందుకు ఆఫీసుకు వెళ్తావు?", "Why will you go to office tomorrow?"),
        ("నీవు రేపు ఎలా ఆఫీసుకు వెళ్తావు?", "How will you go to office tomorrow?"),
        ("నీవు రేపు ఎక్కడికి వెళ్తావు?", "Where will you go tomorrow?"),
        ("నీవు రేపు ఎప్పుడు ఆఫీసుకు వెళ్తావు?", "When will you go to office tomorrow?"),
        ("నీవు రేపు ఆఫీసుకు వెళ్లవు.", "You will not go to office tomorrow."),
        ("నీవు రేపు ఆఫీసుకు వెళ్ళవా?", "Will you not go to office tomorrow?"),
        ("నీవు రేపు ఆఫీసుకు ఎందుకు వెళ్లవు?", "Why will you not go to office tomorrow?")
    ],
    "Present Continuous": [
        ("నీవు ఇప్పుడు ఆఫీసుకు వెళ్తున్నావు.", "You are going to office now."),
        ("నీవు ఇప్పుడు ఆఫీసుకు వెళ్తున్నావా?", "Are you going to office now?"),
        ("నీవు ఇప్పుడు ఎందుకు ఆఫీసుకు వెళ్తున్నావు?", "Why are you going to office now?"),
        ("నీవు ఇప్పుడు ఎక్కడికి వెళ్తున్నావు?", "Where are you going now?"),
        ("నీవు ఇప్పుడు ఎలా ఆఫీసుకు వెళ్తున్నావు?", "How are you going to office now?"),
        ("నీవు ఇప్పుడు ఆఫీసుకు వెళ్లడంలేదు.", "You are not going to office now."),
        ("నీవు ఇప్పుడు ఆఫీసుకు వెళ్తుండలేదా?", "Aren't you going to office now?"),
        ("నీవు ఇప్పుడు ఆఫీసుకు ఎందుకు వెళ్లడంలేదు?", "Why aren't you going to office now?")
    ],
    "Past Continuous": [
        ("నీవు నిన్న ఆఫీసుకు వెళ్తున్నావు.", "You were going to office yesterday."),
        ("నీవు నిన్న ఆఫీసుకు వెళ్తున్నావా?", "Were you going to office yesterday?"),
        ("నీవు నిన్న ఎందుకు ఆఫీసుకు వెళ్తున్నావు?", "Why were you going to office yesterday?"),
        ("నీవు నిన్న ఎక్కడికి వెళ్తున్నావు?", "Where were you going yesterday?"),
        ("నీవు నిన్న ఆఫీసుకు వెళ్లడంలేదు.", "You were not going to office yesterday."),
        ("నీవు నిన్న ఆఫీసుకు వెళ్తుండలేదా?", "Weren't you going to office yesterday?")
    ],
    "Future Continuous": [
        ("నీవు రేపు ఆఫీసుకు వెళ్తుంటావు.", "You will be going to office tomorrow."),
        ("నీవు రేపు ఆఫీసుకు వెళ్తుంటావా?", "Will you be going to office tomorrow?"),
        ("నీవు రేపు ఎందుకు ఆఫీసుకు వెళ్తుంటావు?", "Why will you be going to office tomorrow?"),
        ("నీవు రేపు ఎక్కడికి ఆఫీసుకు వెళ్తుంటావు?", "Where will you be going to office tomorrow?"),
        ("నీవు రేపు ఆఫీసుకు వెళ్తూ ఉండవు.", "You will not be going to office tomorrow."),
        ("నీవు రేపు ఆఫీసుకు వెళ్తూ ఉండవా?", "Will you not be going to office tomorrow?")
    ],
    "Present Perfect": [
        ("నీవు ఇప్పుడే ఆఫీసుకు వెళ్ళిపోయావు.", "You have gone to office just now."),
        ("నీవు ఇప్పుడే ఆఫీసుకు వెళ్ళిపోయావా?", "Have you gone to office just now?"),
        ("నీవు ఇప్పుడే ఎందుకు ఆఫీసుకు వెళ్ళిపోయావు?", "Why have you gone to office just now?"),
        ("నీవు ఇప్పుడే ఆఫీసుకు వెళ్ళలేదు.", "You have not gone to office just now."),
        ("నీవు ఇప్పుడే ఆఫీసుకు వెళ్ళలేదా?", "Haven't you gone to office just now?"),
        ("నీవు ఇప్పుడే ఎందుకు ఆఫీసుకు వెళ్ళలేదు?", "Why haven't you gone to office just now?")
    ],
    "Want to": [
        ("నీవు ఈ రోజు ఆఫీసుకు వెళ్లాలనుకుంటున్నావు.", "You want to go to office today."),
        ("నీవు ఈ రోజు ఆఫీసుకు వెళ్లాలనుకుంటున్నావా?", "Do you want to go to office today?"),
        ("నీవు ఈ రోజు ఆఫీసుకు ఎందుకు వెళ్లాలనుకుంటున్నావు?", "Why do you want to go to office today?"),
        ("నీవు ఈ రోజు ఆఫీసుకు ఎలా వెళ్లాలనుకుంటున్నావు?", "How do you want to go to office today?"),
        ("నీవు ఈ రోజు ఎక్కడికి వెళ్లాలనుకుంటున్నావు?", "Where do you want to go today?"),
        ("నీవు ఈ రోజు ఏమి తినాలనుకుంటున్నావు?", "What do you want to eat today?"),
        ("నీవు ఈ రోజు ఆఫీసుకు వెళ్లాలనుకోవడం లేదు.", "You do not want to go to office today."),
        ("నీవు ఈ రోజు ఆఫీసుకు వెళ్లాలనుకోడంలేదా?", "Don't you want to go to office today?"),
        ("నీవు ఈ రోజు ఆఫీసుకు ఎందుకు వెళ్లాలనుకోవడం లేదు?", "Why don't you want to go to office today?")
    ],
    "Wanted to": [
        ("నీవు నిన్న ఆఫీసుకు వెళ్లాలని అనుకున్నావు.", "You wanted to go to office yesterday."),
        ("నీవు నిన్న ఆఫీసుకు వెళ్లాలని అనుకున్నావా?", "Did you want to go to office yesterday?"),
        ("నీవు నిన్న ఆఫీసుకు ఎందుకు వెళ్లాలని అనుకున్నావు?", "Why did you want to go to office yesterday?"),
        ("నీవు నిన్న ఎక్కడికి వెళ్లాలని అనుకున్నావు?", "Where did you want to go yesterday?"),
        ("నీవు నిన్న ఆఫీసుకు వెళ్లాలనుకోలేదు.", "You did not want to go to office yesterday."),
        ("నీవు నిన్న ఆఫీసుకు వెళ్లాలనుకోలేదా?", "Didn't you want to go to office yesterday?"),
        ("నీవు నిన్న ఆఫీసుకు ఎందుకు వెళ్లాలనుకోలేదు?", "Why didn't you want to go to office yesterday?")
    ],
    "Have to": [
        ("నీవు ఈ రోజు ఆఫీసుకు వెళ్ళవలసి ఉంది.", "You have to go to office today."),
        ("నీవు ఈ రోజు ఆఫీసుకు వెళ్ళవలసి ఉందా?", "Do you have to go to office today?"),
        ("నీవు ఈ రోజు ఆఫీసుకు ఎందుకు వెళ్ళవలసి ఉంది?", "Why do you have to go to office today?"),
        ("నీవు ఈ రోజు ఎప్పుడు ఆఫీసుకు వెళ్ళవలసి ఉంది?", "When do you have to go to office today?"),
        ("నీవు ఈ రోజు ఎక్కడికి వెళ్ళవలసి ఉంది?", "Where do you have to go today?")
    ]
}

# Tense information bank
tense_info = {
    "Simple Present": "The simple present tense is used to describe habits, unchanging situations, general truths, and fixed arrangements.",
    "Past Continuous": "The past continuous tense is used to describe actions that were ongoing in the past.",
    "Future Simple": "The future simple tense is used to talk about actions that will happen in the future."
}

# Set up page
st.set_page_config(page_title="Praveen Spoken English", page_icon="🗣", layout="centered")

# Title and welcome message
st.title("🗣 Welcome to Praveen Spoken English")
st.markdown("### Learn English through Telugu with ease and confidence!")

# Initialize page navigation state
if "page" not in st.session_state:
    st.session_state.page = "home"

# Navigation logic
def go_to(page_name):
    st.session_state.page = page_name
    st.rerun()

# Home page
if st.session_state.page == "home":
    st.markdown("Choose what you want to do:")
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("🗣 Practice All Tenses"):
            go_to("practice")
    with col2:
        if st.button("📘 Tense-wise Understand & Practice"):
            go_to("tense_wise")
    with col3:
        if st.button("🔤 Learn Verbs"):
            go_to("verbs")

# Practice English Page (all tenses)
elif st.session_state.page == "practice":
    st.header("🗣 Telugu-English Translation Practice")

    all_sentences = sum(tense_sentences.values(), [])

    if "current_sentence" not in st.session_state:
        st.session_state.current_sentence = random.choice(all_sentences)
        st.session_state.show_answer = False
        st.session_state.feedback = ""

    telugu, english = st.session_state.current_sentence

    st.markdown("### 👉 Translate the following Telugu sentence to English:")
    st.write(f"**{telugu}**")

    user_input = st.text_input("✍️ Your English Translation:")

    if st.button("✅ Check Answer"):
        if user_input.strip().lower() == english.lower():
            st.session_state.feedback = "✅ Correct!"
        else:
            st.session_state.feedback = "❌ Incorrect!"

    if st.session_state.feedback:
        st.subheader(st.session_state.feedback)

    if st.button("👁️ Show Answer"):
        st.session_state.show_answer = True

    if st.session_state.show_answer:
        st.markdown("### ✅ Correct Translation:")
        st.write(english)

    if st.button("🔄 Next Sentence"):
        st.session_state.current_sentence = random.choice(all_sentences)
        st.session_state.show_answer = False
        st.session_state.feedback = ""
        st.rerun()

    st.markdown("---")
    if st.button("🏠 Back to Home"):
        go_to("home")

# Tense-wise Understand & Practice
elif st.session_state.page == "tense_wise":
    st.header("📘 Tense-wise Understand & Practice")
    tense = st.selectbox("Select a Tense to Practice:", list(tense_sentences.keys()))

    st.subheader(f"ℹ️ Understanding {tense}")
    st.markdown(tense_info.get(tense, "No explanation available yet."))

    st.divider()
    st.subheader(f"🗘 Practice: {tense}")

    if f"{tense}_current" not in st.session_state:
        st.session_state[f"{tense}_current"] = random.choice(tense_sentences[tense])
        st.session_state[f"{tense}_show_answer"] = False
        st.session_state[f"{tense}_feedback"] = ""

    telugu, english = st.session_state[f"{tense}_current"]

    st.markdown("### 👉 Translate the following Telugu sentence to English:")
    st.write(f"**{telugu}**")

    user_input = st.text_input("✍️ Your English Translation:", key=f"{tense}_input")

    if st.button("✅ Check Answer", key=f"{tense}_check"):
        if user_input.strip().lower() == english.lower():
            st.session_state[f"{tense}_feedback"] = "✅ Correct!"
        else:
            st.session_state[f"{tense}_feedback"] = "❌ Incorrect!"

    if st.session_state[f"{tense}_feedback"]:
        st.subheader(st.session_state[f"{tense}_feedback"])

    if st.button("👁️ Show Answer", key=f"{tense}_show"):
        st.session_state[f"{tense}_show_answer"] = True

    if st.session_state[f"{tense}_show_answer"]:
        st.markdown("### ✅ Correct Translation:")
        st.write(english)

    if st.button("🔄 Next Sentence", key=f"{tense}_next"):
        st.session_state[f"{tense}_current"] = random.choice(tense_sentences[tense])
        st.session_state[f"{tense}_show_answer"] = False
        st.session_state[f"{tense}_feedback"] = ""
        st.rerun()

    if st.button("🏠 Back to Home"):
        go_to("home")

# Learn Verbs Page
elif st.session_state.page == "verbs":
    st.header("🔤 Learn Verbs")
    st.markdown("Here you will learn important verbs in English and their Telugu meanings.")
    st.info("Coming soon: Common verbs list and usage examples.")
    if st.button("🏠 Back to Home"):
        go_to("home")
