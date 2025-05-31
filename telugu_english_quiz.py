import random
import streamlit as st
from data.tense_sentences import tense_sentences
from data.conjunction_sentences import conjunction_sentences


# ✅ THIS MUST BE FIRST Streamlit command
st.set_page_config(page_title="Praveen Spoken English", layout="centered")

st.markdown(
    """
    <style>
    /* App background */
    .stApp {
        background: linear-gradient(to right, #e0f7fa, #ffffff);
        color: #333;
        font-family: 'Segoe UI', sans-serif;
    }

    /* Sidebar background */
    section[data-testid="stSidebar"] {
        background-color: #d1f0ff;
    }

    /* Buttons */
    button[kind="primary"] {
        background-color: #007ACC !important;
        color: white !important;
        border-radius: 10px;
    }

    /* Input fields */
    input, textarea {
    background-color: #f0f8ff !important;
    color: #000 !important;     /* Add this line */
    border-radius: 8px;
    }


    /* Headers and subtitles */
    h1, h2, h3 {
        color: #004d66;
    }

    /* Custom divider */
    hr {
        border: none;
        height: 2px;
        background: linear-gradient(to right, #00C9A7, #FFD700);
        margin-top: 30px;
        margin-bottom: 30px;
    }

    </style>
    """,
    unsafe_allow_html=True
)



# Login credentials
credentials = {
    "admin": "admin123",
    "greeshma": "greeshma@767"
}

# Initialize login session state
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# Login form
if not st.session_state.logged_in:
    st.title("🔐 Login to Praveen Spoken English")

    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submitted = st.form_submit_button("Login")

        if submitted:
            if username in credentials and credentials[username] == password:
                st.session_state.logged_in = True
                st.success("Login successful!")
                st.rerun()
            else:
                st.error("Invalid username or password")
    st.stop()


# Initialize session state page
if "page" not in st.session_state:
    st.session_state.page = "home"

# Sidebar navigation only for non-home pages
if st.session_state.page != "home":
    with st.sidebar:
        st.markdown("### 📚 Go to section")
        if st.button("🏠 Home"):
            st.session_state.page = "home"
        if st.button("🗣 Practice All Tenses"):
            st.session_state.page = "practice"
        if st.button("📘 Tense-wise Understand & Practice"):
            st.session_state.page = "tense_wise"
        if st.button("🔤 Learn Verbs"):
            st.session_state.page = "verbs"
        if st.button("🔗 Practise Conjunctions"):
            st.session_state.page = "conjunctions"
        if st.button("🔍 Understand Conjunctions"):
            st.session_state.page = "understand_conjunctions"



# Tense information bank
tense_info = {
    "Simple Present": "The simple present tense is used to describe habits, unchanging situations, general truths, and fixed arrangements.",
    "Past Continuous": "The past continuous tense is used to describe actions that were ongoing in the past.",
    "Future Simple": "The future simple tense is used to talk about actions that will happen in the future."

}



# Title and welcome message
#st.title("🗣 Welcome to Praveen Spoken English")
#st.markdown("### Learn English through Telugu with ease and confidence!")




st.markdown("""
    <style>
    .gradient-text {
        font-size: 32px;
        font-weight: bold;
        text-align: center;
        margin-top: 30px;
        background: linear-gradient(-45deg, #007ACC, #00C9A7, #FFD700, #FF69B4);
        background-size: 400% 400%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: gradientMove 5s ease infinite;
    }

    @keyframes gradientMove {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    .phone-number {
        text-align: center;
        font-size: 18px;
        color: #444;
        margin-top: 10px;
    }
    </style>

    <div class="gradient-text">Welcome to Praveen Spoken English</div>
    <div class="phone-number">📞 Contact: 8248268056</div>
""", unsafe_allow_html=True)



# Navigation logic
def go_to(page_name):
    st.session_state.page = page_name
    st.rerun()

# Home page
# Home page
if st.session_state.page == "home":
    st.markdown("Choose what you want to do:")
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        if st.button("🗣 Practice All Tenses", key="home_practice"):
            go_to("practice")
    with col2:
        if st.button("📘 Tense-wise Understand & Practice", key="home_tense_wise"):
            go_to("tense_wise")
    with col3:
        if st.button("🔤 Learn Verbs", key="home_verbs"):
            go_to("verbs")
    with col4:
        if st.button("🔤 Learn and practise conjunctions", key="home_conjunctions"):
            go_to("conjunctions")
    with col5:
        if st.button("🔤 understand conjunctions", key="home_understand_conjunctions"):
            go_to("understand_conjunctions")


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

    

# Practice English Page (conjunctions)
elif st.session_state.page == "conjunctions":
    st.header("🗣 Learn and practise conjunctions")

    all_sentences = sum(conjunction_sentences.values(), [])

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

    

# Understand conjunctions
elif st.session_state.page == "understand_conjunctions":
    st.header("\U0001F4D8 understand conjunctions")

    st.markdown("""
    ### 📘 Conjunctions – Full Guide (with Telugu Meaning & Examples)

    #### 🔹 1. Coordinating Conjunctions (FANBOYS)
    Connect equal parts: words, phrases, or independent clauses.

    | Conjunction | Use     | English Example                          | Telugu Meaning | Telugu Example                                     |
    |-------------|----------|------------------------------------------|----------------|----------------------------------------------------|
    | For         | Reason   | He stayed home, for he was sick.         | ఎందుకంటే       | అతను ఇంట్లోనే ఉన్నాడు, ఎందుకంటే అతను అనారోగ్యంగా ఉన్నాడు. |
    | And         | Addition | I like coffee and tea.                   | మరియు          | నాకు కాఫీ మరియు టీ ఇష్టం.                        |
    | Nor         | Neg Add  | She didn’t smile, nor did she speak.     | కూడా కాదు       | ఆమె నవ్వలేదు, మరియు మాట్లాడలేదు కూడా.           |
    | But         | Contrast | I ran fast, but I missed the bus.        | కానీ            | నేను వేగంగా పరుగెత్తాను, కానీ బస్సు మిస్సయ్యాను.   |
    | Or          | Choice   | Do you want juice or soda?               | లేదా            | నీకు జ్యూస్ కావాలా లేదా సోడా?                    |
    | Yet         | Unexpected | It’s cold, yet he isn’t wearing a coat. | అయినా          | ఇది చల్లగా ఉంది, అయినా అతను కోట్ వేసుకోలేదు.      |
    | So          | Result   | It rained, so we stayed in.              | కాబట్టి          | వర్షం పడింది, కాబట్టి మేము ఇంట్లో ఉన్నాము.       |

    #### 🔹 2. Subordinating Conjunctions
    Connect an independent clause with a dependent clause.

    | Conjunction  | Use/Meaning     | English Example                          | Telugu Meaning    | Telugu Example                                           |
    |--------------|-----------------|------------------------------------------|-------------------|----------------------------------------------------------|
    | Because      | Reason          | I stayed because it rained.              | ఎందుకంటే         | వర్షం పడింది కాబట్టి నేను ఉన్నాను.                      |
    | Although     | Contrast        | Although he's rich, he is unhappy.       | అయినా             | అతను ధనవంతుడు అయినా సంతోషంగా లేడు.                     |
    | Since        | Reason/Time     | Since it’s late, let’s go.               | కాబట్టి / నుంచి     | ఇది ఆలస్యంగా ఉంది కాబట్టి మనం వెళ్లాలి.                 |
    | If           | Condition       | If you try, you’ll win.                  | అయితే / యెడల       | నీవు ప్రయత్నిస్తే, నీవు గెలుస్తావు.                      |
    | Unless       | Negative Cond.  | Unless you study, you’ll fail.           | లేకపోతే / చదవకపోతే | నీవు చదవకపోతే నీవు ఫెయిల్ అవుతావు.                     |
    | While        | Time/Contrast   | I listened while she spoke.              | చేస్తున్నప్పుడు       | ఆమె మాట్లాడుతున్నప్పుడు నేను విన్నాను.                 |
    | After        | Time            | I slept after I ate.                     | తరువాత            | తినిన తరువాత నిద్రపోయాను.                             |
    | Before       | Time            | Wash your hands before you eat.          | ముందు             | తినే ముందు చేతులు కడుక్కో.                           |
    | Though       | Contrast        | Though tired, he worked.                 | అయినా             | అలసిపోయినా, అతను పని చేశాడు.                         |
    | As           | Time/Reason     | As I was leaving, she came.              | చేస్తున్నప్పుడు / కాబట్టి | నేను వెళ్లుతున్నపుడు ఆమె వచ్చింది.                 |
    | Even if      | Condition       | Even if it rains, we’ll go.              | అయినప్పటికీ        | వర్షం పడినప్పటికీ మేము వెళ్తాము.                      |
    | In case      | Precaution      | Take an umbrella in case it rains.       | అన్న ఊహలో         | వర్షం పడితే అన్న ఊహలో గొడుగు తీసుకెళ్లి.               |
    | As long as   | Condition       | You can stay as long as you’re quiet.    | ఉన్నంతవరకూ         | నీవు నిశ్శబ్దంగా ఉన్నంతవరకూ నీవు ఉండవచ్చు.               |
    | Now that     | Present Reason  | Now that it’s over, we can rest.         | ఇప్పుడు కావడంతో     | ఇది అయిపోయిందని ఇప్పుడు విశ్రాంతి తీసుకుందాం.           |
    | Even though  | Strong contrast | Even though he’s old, he works hard.     | అయినప్పటికీ        | అతను వృద్ధుడైనా, కష్టపడుతూ పని చేస్తాడు.               |
    | Provided that| Formal Cond.    | You may go provided that you finish work.| పని పూర్తిచేస్తే     | నీవు పని పూర్తిచేస్తే నీవు వెళ్ళవచ్చు.                  |
    | As if        | Imagination     | He talks as if he were a king.           | లాగా / అయినట్టు    | అతను రాజులా మాట్లాడుతున్నాడు.                          |

    #### 🔹 3. Correlative Conjunctions
    Conjunction pairs that work together.

    | Pair                  | English Example                       | Telugu Meaning       | Telugu Example                                 |
    |-----------------------|----------------------------------------|----------------------|------------------------------------------------|
    | Either...or           | Either come or call.                  | లేకపోతే...లేదా       | నీవు రా లేకపోతే ఫోన్ చెయ్యి.                      |
    | Neither...nor         | Neither the boy nor the girl spoke.  | కాదు...లేదు           | అబ్బాయి కాదు, అమ్మాయి కూడా లేదు.                  |
    | Not only...but also   | Not only smart but also kind.        | మాత్రమే కాదు...కూడా  | ఆమె తెలివైనదే కాదు, మంచిదీ కూడా.                    |
    | Both...and            | Both father and son are doctors.     | ఇద్దరూ...మరియు        | తండ్రి మరియు కొడుకు ఇద్దరూ డాక్టర్లు.              |
    | Whether...or          | Whether it rains or not, we’ll play. | అయినా...లేదా         | వర్షం పడినా లేదా పడకపోయినా మేము ఆడతాము.          |

    #### 🔹 4. Conjunctive Adverbs / Phrase Conjunctions
    These are transition words that act like conjunctions, especially in formal or written English.

    | Phrase Conjunction | Use       | English Example                           | Telugu Meaning       |
    |---------------------|------------|-------------------------------------------|-----------------------|
    | However             | Contrast   | He was tired; however, he continued.      | అయినప్పటికీ         |
    | Therefore           | Result     | She studied well; therefore, she passed.  | కాబట్టి               |
    | Moreover            | Addition   | He is kind; moreover, he is generous.     | అంతేకాకుండా          |
    | Nevertheless        | Contrast   | It rained; nevertheless, we went out.     | అయినా                |
    | Consequently        | Result     | He missed the train; consequently, he was late. | ఫలితంగా     |
    | Furthermore          | Addition   | She is a writer; furthermore, a good speaker. | అదనంగా / అంతేకాకుండా |
    """)


    

# Learn Verbs Page
elif st.session_state.page == "verbs":
    st.header("🔤 Learn Verbs")
    st.markdown("Here you will learn important verbs in English and their Telugu meanings.")
    st.info("Coming soon: Common verbs list and usage examples.")
    