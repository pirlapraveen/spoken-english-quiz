import random
import streamlit as st

# Sentence bank organized by tense
tense_sentences = {
    "Simple Present": [
        # Subject: You
        ("నీవు ప్రతిరోజూ ఆఫీసుకు వెళ్తావు.", "You go to office every day."),
        ("నీవు ప్రతిరోజూ ఆఫీసుకు వెళ్తావా?", "Do you go to office every day?"),
        ("నీవు ప్రతిరోజూ ఆఫీసుకు ఎందుకు వెళ్తావు?", "Why do you go to office every day?"),
        ("నీవు ప్రతిరోజూ ఆఫీసుకు ఎప్పుడు వెళ్తావు?", "When do you go to office every day?"),
        ("నువ్వు ప్రతిరోజూ ఏమి తింటావు ?", "What do you eat every day?"),
        ("నీవు ప్రతిరోజూ ఎక్కడికి వెళ్ళతావు?", "Where do you go every day?"),
        ("నీవు ఆఫీసుకు ఎలా వెళ్తావు?", "How do you go to office every day?"),
        ("నీవు ప్రతిరోజూ ఆఫీసుకు వెళ్ళవు.", "You don't go to office every day."),
        ("నీవు ప్రతిరోజూ ఆఫీసుకు వెళ్ళవా?", "Don't you go to office every day?"),
        ("నీవు ప్రతిరోజూ ఆఫీసుకు ఎందుకు వెళ్ళవు?", "Why don't you go to office every day?"),

        # Subject: She
        ("ఆమె ప్రతిరోజూ ఆఫీసుకు వెళ్తుంది.", "She goes to office every day."),
        ("ఆమె ప్రతిరోజూ ఆఫీసుకు వెళ్తుందా?", "Does she go to office every day?"),
        ("ఆమె ప్రతిరోజూ ఆఫీసుకు ఎందుకు వెళ్తుంది?", "Why does she go to office every day?"),
        ("ఆమె ప్రతిరోజూ ఆఫీసుకు ఎప్పుడు వెళ్తుంది?", "When does she go to office every day?"),
        ("ఆమె ప్రతిరోజూ ఏమి తింటుంది?", "What does she eat every day?"),
        ("ఆమె ప్రతిరోజూ ఎక్కడికి వెళ్తుంది?", "Where does she go every day?"),
        ("ఆమె ఆఫీసుకు ఎలా వెళ్తుంది?", "How does she go to office every day?"),
        ("ఆమె ప్రతిరోజూ ఆఫీసుకు వెళ్ళదు.", "She doesn't go to office every day."),
        ("ఆమె ప్రతిరోజూ ఆఫీసుకు వెళ్ళదా?", "Doesn't she go to office every day?"),
        ("ఆమె ప్రతిరోజూ ఆఫీసుకు ఎందుకు వెళ్ళదు?", "Why doesn't she go to office every day?"),

        # Subject: Ramu
        ("రాము ప్రతిరోజూ ఆఫీసుకు వెళ్తాడు.", "Ramu goes to office every day."),
        ("రాము ప్రతిరోజూ ఆఫీసుకు వెళ్తాడా?", "Does Ramu go to office every day?"),
        ("రాము ప్రతిరోజూ ఆఫీసుకు ఎందుకు వెళ్తాడు?", "Why does Ramu go to office every day?"),
        ("రాము ప్రతిరోజూ ఆఫీసుకు ఎప్పుడు వెళ్తాడు?", "When does Ramu go to office every day?"),
        ("రాము ప్రతిరోజూ ఏమి తింటాడు?", "What does Ramu eat every day?"),
        ("రాము ప్రతిరోజూ ఎక్కడికి వెళ్తాడు?", "Where does Ramu go every day?"),
        ("రాము ఆఫీసుకు ఎలా వెళ్తాడు?", "How does Ramu go to office every day?"),
        ("రాము ప్రతిరోజూ ఆఫీసుకు వెళ్ళడు.", "Ramu doesn't go to office every day."),
        ("రాము ప్రతిరోజూ ఆఫీసుకు వెళ్ళడా?", "Doesn't Ramu go to office every day?"),
        ("రాము ప్రతిరోజూ ఆఫీసుకు ఎందుకు వెళ్ళడు?", "Why doesn't Ramu go to office every day?"),

        # Subject: They
        ("వాళ్లు ప్రతిరోజూ ఆఫీసుకు వెళ్తారు.", "They go to office every day."),
        ("వాళ్లు ప్రతిరోజూ ఆఫీసుకు వెళ్తారా?", "Do they go to office every day?"),
        ("వాళ్లు ప్రతిరోజూ ఆఫీసుకు ఎందుకు వెళ్తారు?", "Why do they go to office every day?"),
        ("వాళ్లు ప్రతిరోజూ ఆఫీసుకు ఎప్పుడు వెళ్తారు?", "When do they go to office every day?"),
        ("వాళ్లు ప్రతిరోజూ ఏమి తింటారు?", "What do they eat every day?"),
        ("వాళ్లు ప్రతిరోజూ ఎక్కడికి వెళ్తారు?", "Where do they go every day?"),
        ("వాళ్లు ఆఫీసుకు ఎలా వెళ్తారు?", "How do they go to office every day?"),
        ("వాళ్లు ప్రతిరోజూ ఆఫీసుకు వెళ్ళరు.", "They don't go to office every day."),
        ("వాళ్లు ప్రతిరోజూ ఆఫీసుకు వెళ్ళరా?", "Don't they go to office every day?"),
        ("వాళ్లు ప్రతిరోజూ ఆఫీసుకు ఎందుకు వెళ్ళరు?", "Why don't they go to office every day?"),

        # Subject: We
        ("మేము ప్రతిరోజూ ఆఫీసుకు వెళ్తాము.", "We go to office every day."),
        ("మేము ప్రతిరోజూ ఆఫీసుకు వెళ్తామా?", "Do we go to office every day?"),
        ("మేము ప్రతిరోజూ ఆఫీసుకు ఎందుకు వెళ్తాము?", "Why do we go to office every day?"),
        ("మేము ప్రతిరోజూ ఆఫీసుకు ఎప్పుడు వెళ్తాము?", "When do we go to office every day?"),
        ("మేము ప్రతిరోజూ ఏమి తింటాము?", "What do we eat every day?"),
        ("మేము ప్రతిరోజూ ఎక్కడికి వెళ్తాము?", "Where do we go every day?"),
        ("మేము ఆఫీసుకు ఎలా వెళ్తాము?", "How do we go to office every day?"),
        ("మేము ప్రతిరోజూ ఆఫీసుకు వెళ్ళము.", "We don't go to office every day."),
        ("మేము ప్రతిరోజూ ఆఫీసుకు వెళ్ళమా?", "Don't we go to office every day?"),
        ("మేము ప్రతిరోజూ ఆఫీసుకు ఎందుకు వెళ్ళము?", "Why don't we go to office every day?"),

        # Subject: I
        ("నేను ప్రతిరోజూ ఆఫీసుకు వెళ్తాను.", "I go to office every day."),
        ("నేను ప్రతిరోజూ ఆఫీసుకు వెళ్తానా?", "Do I go to office every day?"),
        ("నేను ప్రతిరోజూ ఆఫీసుకు ఎందుకు వెళ్తాను?", "Why do I go to office every day?"),
        ("నేను ప్రతిరోజూ ఆఫీసుకు ఎప్పుడు వెళ్తాను?", "When do I go to office every day?"),
        ("నేను ప్రతిరోజూ ఏమి తింటాను?", "What do I eat every day?"),
        ("నేను ప్రతిరోజూ ఎక్కడికి వెళ్తాను?", "Where do I go every day?"),
        ("నేను ఆఫీసుకు ఎలా వెళ్తాను?", "How do I go to office every day?"),
        ("నేను ప్రతిరోజూ ఆఫీసుకు వెళ్ళను.", "I don't go to office every day."),
        ("నేను ప్రతిరోజూ ఆఫీసుకు వెళ్ళనా?", "Don't I go to office every day?"),
        ("నేను ప్రతిరోజూ ఆఫీసుకు ఎందుకు వెళ్ళను?", "Why don't I go to office every day?")
    ],


    "Simple Past": [
    # You
    ("నీవు నిన్న ఆఫీసుకు వెళ్లావు.", "You went to office yesterday."),
    ("నీవు నిన్న ఆఫీసుకు వెళ్లావా?", "Did you go to office yesterday?"),
    ("నీవు నిన్న ఎందుకు వెళ్లావు?", "Why did you go yesterday?"),
    ("నీవు నిన్న ఎలా వెళ్లావు?", "How did you go yesterday?"),
    ("నీవు నిన్న ఎక్కడికి వెళ్లావు?", "Where did you go yesterday?"),
    ("నీవు నిన్న ఎప్పుడు వెళ్లావు?", "When did you go yesterday?"),
    ("నీవు నిన్న ఆఫీసుకు వెళ్లలేదు.", "You did not go to office yesterday."),
    ("నీవు నిన్న ఆఫీసుకు వెళ్లలేదా?", "Didn't you go to office yesterday?"),
    ("నీవు నిన్న ఎందుకు వెళ్లలేదు?", "Why didn't you go yesterday?"),

    # She
    ("ఆమె నిన్న ఆఫీసుకు వెళ్లింది.", "She went to office yesterday."),
    ("ఆమె నిన్న ఆఫీసుకు వెళ్లిందా?", "Did she go to office yesterday?"),
    ("ఆమె నిన్న ఎందుకు వెళ్లింది?", "Why did she go yesterday?"),
    ("ఆమె నిన్న ఎలా వెళ్లింది?", "How did she go yesterday?"),
    ("ఆమె నిన్న ఎక్కడికి వెళ్లింది?", "Where did she go yesterday?"),
    ("ఆమె నిన్న ఎప్పుడు వెళ్లింది?", "When did she go yesterday?"),
    ("ఆమె నిన్న ఆఫీసుకు వెళ్లలేదు.", "She did not go to office yesterday."),
    ("ఆమె నిన్న ఆఫీసుకు వెళ్లలేదా?", "Didn't she go to office yesterday?"),
    ("ఆమె నిన్న ఎందుకు వెళ్లలేదు?", "Why didn't she go yesterday?"),

    # Ramu
    ("రాము నిన్న ఆఫీసుకు వెళ్లాడు.", "Ramu went to office yesterday."),
    ("రాము నిన్న ఆఫీసుకు వెళ్లాడా?", "Did Ramu go to office yesterday?"),
    ("రాము నిన్న ఎందుకు వెళ్లాడు?", "Why did Ramu go yesterday?"),
    ("రాము నిన్న ఎలా వెళ్లాడు?", "How did Ramu go yesterday?"),
    ("రాము నిన్న ఎక్కడికి వెళ్లాడు?", "Where did Ramu go yesterday?"),
    ("రాము నిన్న ఎప్పుడు వెళ్లాడు?", "When did Ramu go yesterday?"),
    ("రాము నిన్న ఆఫీసుకు వెళ్లలేదు.", "Ramu did not go to office yesterday."),
    ("రాము నిన్న ఆఫీసుకు వెళ్లలేదా?", "Didn't Ramu go to office yesterday?"),
    ("రాము నిన్న ఎందుకు వెళ్లలేదు?", "Why didn't Ramu go yesterday?"),

    # They
    ("వాళ్లు నిన్న ఆఫీసుకు వెళ్లారు.", "They went to office yesterday."),
    ("వాళ్లు నిన్న ఆఫీసుకు వెళ్లారా?", "Did they go to office yesterday?"),
    ("వాళ్లు నిన్న ఎందుకు వెళ్లారు?", "Why did they go yesterday?"),
    ("వాళ్లు నిన్న ఎలా వెళ్లారు?", "How did they go yesterday?"),
    ("వాళ్లు నిన్న ఎక్కడికి వెళ్లారు?", "Where did they go yesterday?"),
    ("వాళ్లు నిన్న ఎప్పుడు వెళ్లారు?", "When did they go yesterday?"),
    ("వాళ్లు నిన్న ఆఫీసుకు వెళ్లలేదు.", "They did not go to office yesterday."),
    ("వాళ్లు నిన్న ఆఫీసుకు వెళ్లలేదా?", "Didn't they go to office yesterday?"),
    ("వాళ్లు నిన్న ఎందుకు వెళ్లలేదు?", "Why didn't they go yesterday?"),

    # We
    ("మేము నిన్న ఆఫీసుకు వెళ్లాము.", "We went to office yesterday."),
    ("మేము నిన్న ఆఫీసుకు వెళ్లామా?", "Did we go to office yesterday?"),
    ("మేము నిన్న ఎందుకు వెళ్లాము?", "Why did we go yesterday?"),
    ("మేము నిన్న ఎలా వెళ్లాము?", "How did we go yesterday?"),
    ("మేము నిన్న ఎక్కడికి వెళ్లాము?", "Where did we go yesterday?"),
    ("మేము నిన్న ఎప్పుడు వెళ్లాము?", "When did we go yesterday?"),
    ("మేము నిన్న ఆఫీసుకు వెళ్లలేదు.", "We did not go to office yesterday."),
    ("మేము నిన్న ఆఫీసుకు వెళ్లలేదా?", "Didn't we go to office yesterday?"),
    ("మేము నిన్న ఎందుకు వెళ్లలేదు?", "Why didn't we go yesterday?"),

    # I
    ("నేను నిన్న ఆఫీసుకు వెళ్లాను.", "I went to office yesterday."),
    ("నేను నిన్న ఆఫీసుకు వెళ్లానా?", "Did I go to office yesterday?"),
    ("నేను నిన్న ఎందుకు వెళ్లాను?", "Why did I go yesterday?"),
    ("నేను నిన్న ఎలా వెళ్లాను?", "How did I go yesterday?"),
    ("నేను నిన్న ఎక్కడికి వెళ్లాను?", "Where did I go yesterday?"),
    ("నేను నిన్న ఎప్పుడు వెళ్లాను?", "When did I go yesterday?"),
    ("నేను నిన్న ఆఫీసుకు వెళ్లలేదు.", "I did not go to office yesterday."),
    ("నేను నిన్న ఆఫీసుకు వెళ్లలేదా?", "Didn't I go to office yesterday?"),
    ("నేను నిన్న ఎందుకు వెళ్లలేదు?", "Why didn't I go yesterday?")
    ],

    "Simple Future": [
    # You
    ("నీవు రేపు ఆఫీసుకు వెళ్తావు.", "You will go to office tomorrow."),
    ("నీవు రేపు ఆఫీసుకు వెళ్తావా?", "Will you go to office tomorrow?"),
    ("నీవు రేపు ఎందుకు వెళ్తావు?", "Why will you go tomorrow?"),
    ("నీవు రేపు ఎలా వెళ్తావు?", "How will you go tomorrow?"),
    ("నీవు రేపు ఎక్కడికి వెళ్తావు?", "Where will you go tomorrow?"),
    ("నీవు రేపు ఎప్పుడు వెళ్తావు?", "When will you go tomorrow?"),
    ("నీవు రేపు ఆఫీసుకు వెళ్లవు.", "You will not go to office tomorrow."),
    ("నీవు రేపు ఆఫీసుకు వెళ్ళవా?", "Will you not go to office tomorrow?"),
    ("నీవు రేపు ఎందుకు వెళ్లవు?", "Why will you not go tomorrow?"),

    # She
    ("ఆమె రేపు ఆఫీసుకు వెళ్తుంది.", "She will go to office tomorrow."),
    ("ఆమె రేపు ఆఫీసుకు వెళ్తుందా?", "Will she go to office tomorrow?"),
    ("ఆమె రేపు ఎందుకు వెళ్తుంది?", "Why will she go tomorrow?"),
    ("ఆమె రేపు ఎలా వెళ్తుంది?", "How will she go tomorrow?"),
    ("ఆమె రేపు ఎక్కడికి వెళ్తుంది?", "Where will she go tomorrow?"),
    ("ఆమె రేపు ఎప్పుడు వెళ్తుంది?", "When will she go tomorrow?"),
    ("ఆమె రేపు ఆఫీసుకు వెళ్లదు.", "She will not go to office tomorrow."),
    ("ఆమె రేపు ఆఫీసుకు వెళ్ళదా?", "Will she not go to office tomorrow?"),
    ("ఆమె రేపు ఎందుకు వెళ్లదు?", "Why will she not go tomorrow?"),

    # Ramu
    ("రాము రేపు ఆఫీసుకు వెళ్తాడు.", "Ramu will go to office tomorrow."),
    ("రాము రేపు ఆఫీసుకు వెళ్తాడా?", "Will Ramu go to office tomorrow?"),
    ("రాము రేపు ఎందుకు వెళ్తాడు?", "Why will Ramu go tomorrow?"),
    ("రాము రేపు ఎలా వెళ్తాడు?", "How will Ramu go tomorrow?"),
    ("రాము రేపు ఎక్కడికి వెళ్తాడు?", "Where will Ramu go tomorrow?"),
    ("రాము రేపు ఎప్పుడు వెళ్తాడు?", "When will Ramu go tomorrow?"),
    ("రాము రేపు ఆఫీసుకు వెళ్లడు.", "Ramu will not go to office tomorrow."),
    ("రాము రేపు ఆఫీసుకు వెళ్ళడా?", "Will Ramu not go to office tomorrow?"),
    ("రాము రేపు ఎందుకు వెళ్లడు?", "Why will Ramu not go tomorrow?"),

    # They
    ("వాళ్లు రేపు ఆఫీసుకు వెళ్తారు.", "They will go to office tomorrow."),
    ("వాళ్లు రేపు ఆఫీసుకు వెళ్తారా?", "Will they go to office tomorrow?"),
    ("వాళ్లు రేపు ఎందుకు వెళ్తారు?", "Why will they go tomorrow?"),
    ("వాళ్లు రేపు ఎలా వెళ్తారు?", "How will they go tomorrow?"),
    ("వాళ్లు రేపు ఎక్కడికి వెళ్తారు?", "Where will they go tomorrow?"),
    ("వాళ్లు రేపు ఎప్పుడు వెళ్తారు?", "When will they go tomorrow?"),
    ("వాళ్లు రేపు ఆఫీసుకు వెళ్లరు.", "They will not go to office tomorrow."),
    ("వాళ్లు రేపు ఆఫీసుకు వెళ్ళరా?", "Will they not go to office tomorrow?"),
    ("వాళ్లు రేపు ఎందుకు వెళ్లరు?", "Why will they not go tomorrow?"),

    # We
    ("మేము రేపు ఆఫీసుకు వెళ్తాము.", "We will go to office tomorrow."),
    ("మేము రేపు ఆఫీసుకు వెళ్తామా?", "Will we go to office tomorrow?"),
    ("మేము రేపు ఎందుకు వెళ్తాము?", "Why will we go tomorrow?"),
    ("మేము రేపు ఎలా వెళ్తాము?", "How will we go tomorrow?"),
    ("మేము రేపు ఎక్కడికి వెళ్తాము?", "Where will we go tomorrow?"),
    ("మేము రేపు ఎప్పుడు వెళ్తాము?", "When will we go tomorrow?"),
    ("మేము రేపు ఆఫీసుకు వెళ్లము.", "We will not go to office tomorrow."),
    ("మేము రేపు ఆఫీసుకు వెళ్ళమా?", "Will we not go to office tomorrow?"),
    ("మేము రేపు ఎందుకు వెళ్లము?", "Why will we not go tomorrow?"),

    # I
    ("నేను రేపు ఆఫీసుకు వెళ్తాను.", "I will go to office tomorrow."),
    ("నేను రేపు ఆఫీసుకు వెళ్తానా?", "Will I go to office tomorrow?"),
    ("నేను రేపు ఎందుకు వెళ్తాను?", "Why will I go tomorrow?"),
    ("నేను రేపు ఎలా వెళ్తాను?", "How will I go tomorrow?"),
    ("నేను రేపు ఎక్కడికి వెళ్తాను?", "Where will I go tomorrow?"),
    ("నేను రేపు ఎప్పుడు వెళ్తాను?", "When will I go tomorrow?"),
    ("నేను రేపు ఆఫీసుకు వెళ్లను.", "I will not go to office tomorrow."),
    ("నేను రేపు ఆఫీసుకు వెళ్ళనా?", "Will I not go to office tomorrow?"),
    ("నేను రేపు ఎందుకు వెళ్లను?", "Why will I not go tomorrow?")
    ],

    "Present Continuous": [
    # You
    ("నీవు ఇప్పుడు ఆఫీసుకు వెళ్తున్నావు.", "You are going to office now."),
    ("నీవు ఇప్పుడు ఆఫీసుకు వెళ్తున్నావా?", "Are you going to office now?"),
    ("నీవు ఇప్పుడు ఎందుకు ఆఫీసుకు వెళ్తున్నావు?", "Why are you going to office now?"),
    ("నీవు ఇప్పుడు ఎక్కడికి వెళ్తున్నావు?", "Where are you going now?"),
    ("నీవు ఇప్పుడు ఎలా ఆఫీసుకు వెళ్తున్నావు?", "How are you going to office now?"),
    ("నీవు ఇప్పుడు ఆఫీసుకు వెళ్లడంలేదు.", "You are not going to office now."),
    ("నీవు ఇప్పుడు ఆఫీసుకు వెళ్తుండలేదా?", "Aren't you going to office now?"),
    ("నీవు ఇప్పుడు ఆఫీసుకు ఎందుకు వెళ్లడంలేదు?", "Why aren't you going to office now?"),

    # She
    ("ఆమె ఇప్పుడు ఆఫీసుకు వెళ్తుంది.", "She is going to office now."),
    ("ఆమె ఇప్పుడు ఆఫీసుకు వెళ్తుందా?", "Is she going to office now?"),
    ("ఆమె ఇప్పుడు ఎందుకు ఆఫీసుకు వెళ్తుంది?", "Why is she going to office now?"),
    ("ఆమె ఇప్పుడు ఎక్కడికి వెళ్తుంది?", "Where is she going now?"),
    ("ఆమె ఇప్పుడు ఆఫీసుకు వెళ్లడంలేదు.", "She is not going to office now."),
    ("ఆమె ఇప్పుడు ఆఫీసుకు వెళ్తుండలేదా?", "Isn't she going to office now?"),
    ("ఆమె ఇప్పుడు ఆఫీసుకు ఎందుకు వెళ్లడంలేదు?", "Why isn't she going to office now?"),

    # Ramu
    ("రాము ఇప్పుడు ఆఫీసుకు వెళ్తున్నాడు.", "Ramu is going to office now."),
    ("రాము ఇప్పుడు ఆఫీసుకు వెళ్తున్నాడా?", "Is Ramu going to office now?"),
    ("రాము ఇప్పుడు ఎందుకు ఆఫీసుకు వెళ్తున్నాడు?", "Why is Ramu going to office now?"),
    ("రాము ఇప్పుడు ఎక్కడికి వెళ్తున్నాడు?", "Where is Ramu going now?"),
    ("రాము ఇప్పుడు ఆఫీసుకు వెళ్లడంలేదు.", "Ramu is not going to office now."),
    ("రాము ఇప్పుడు ఆఫీసుకు వెళ్తుండలేదా?", "Isn't Ramu going to office now?"),
    ("రాము ఇప్పుడు ఆఫీసుకు ఎందుకు వెళ్లడంలేదు?", "Why isn't Ramu going to office now?"),

    # They
    ("వాళ్లు ఇప్పుడు ఆఫీసుకు వెళ్తున్నారు.", "They are going to office now."),
    ("వాళ్లు ఇప్పుడు ఆఫీసుకు వెళ్తున్నారా?", "Are they going to office now?"),
    ("వాళ్లు ఇప్పుడు ఎందుకు ఆఫీసుకు వెళ్తున్నారు?", "Why are they going to office now?"),
    ("వాళ్లు ఇప్పుడు ఎక్కడికి వెళ్తున్నారు?", "Where are they going now?"),
    ("వాళ్లు ఇప్పుడు ఆఫీసుకు వెళ్లడంలేదు.", "They are not going to office now."),
    ("వాళ్లు ఇప్పుడు ఆఫీసుకు వెళ్తుండరా?", "Aren't they going to office now?"),
    ("వాళ్లు ఇప్పుడు ఆఫీసుకు ఎందుకు వెళ్లడంలేదు?", "Why aren't they going to office now?"),

    # We
    ("మేము ఇప్పుడు ఆఫీసుకు వెళ్తున్నాము.", "We are going to office now."),
    ("మేము ఇప్పుడు ఆఫీసుకు వెళ్తున్నామా?", "Are we going to office now?"),
    ("మేము ఇప్పుడు ఎందుకు ఆఫీసుకు వెళ్తున్నాము?", "Why are we going to office now?"),
    ("మేము ఇప్పుడు ఎక్కడికి వెళ్తున్నాము?", "Where are we going now?"),
    ("మేము ఇప్పుడు ఆఫీసుకు వెళ్లడంలేదు.", "We are not going to office now."),
    ("మేము ఇప్పుడు ఆఫీసుకు వెళ్తుండలేమా?", "Aren't we going to office now?"),
    ("మేము ఇప్పుడు ఆఫీసుకు ఎందుకు వెళ్లడంలేదు?", "Why aren't we going to office now?"),

    # I
    ("నేను ఇప్పుడు ఆఫీసుకు వెళ్తున్నాను.", "I am going to office now."),
    ("నేను ఇప్పుడు ఆఫీసుకు వెళ్తున్నానా?", "Am I going to office now?"),
    ("నేను ఇప్పుడు ఎందుకు ఆఫీసుకు వెళ్తున్నాను?", "Why am I going to office now?"),
    ("నేను ఇప్పుడు ఎక్కడికి వెళ్తున్నాను?", "Where am I going now?"),
    ("నేను ఇప్పుడు ఆఫీసుకు వెళ్లడంలేదు.", "I am not going to office now."),
    ("నేను ఇప్పుడు ఆఫీసుకు వెళ్తున్నానా కాదా?", "Aren't I going to office now?"),
    ("నేను ఇప్పుడు ఆఫీసుకు ఎందుకు వెళ్లడంలేదు?", "Why am I not going to office now?")
    ],

    "Past Continuous": [
    # You
    ("నీవు నిన్న ఆఫీసుకు వెళ్తున్నావు.", "You were going to office yesterday."),
    ("నీవు నిన్న ఆఫీసుకు వెళ్తున్నావా?", "Were you going to office yesterday?"),
    ("నీవు నిన్న ఎందుకు ఆఫీసుకు వెళ్తున్నావు?", "Why were you going to office yesterday?"),
    ("నీవు నిన్న ఎక్కడికి వెళ్తున్నావు?", "Where were you going yesterday?"),
    ("నీవు నిన్న ఆఫీసుకు వెళ్లడంలేదు.", "You were not going to office yesterday."),
    ("నీవు నిన్న ఆఫీసుకు వెళ్తుండలేదా?", "Weren't you going to office yesterday?"),

    # She
    ("ఆమె నిన్న ఆఫీసుకు వెళ్తుంది.", "She was going to office yesterday."),
    ("ఆమె నిన్న ఆఫీసుకు వెళ్తుందా?", "Was she going to office yesterday?"),
    ("ఆమె నిన్న ఎందుకు ఆఫీసుకు వెళ్తుంది?", "Why was she going to office yesterday?"),
    ("ఆమె నిన్న ఎక్కడికి వెళ్తుంది?", "Where was she going yesterday?"),
    ("ఆమె నిన్న ఆఫీసుకు వెళ్లడంలేదు.", "She was not going to office yesterday."),
    ("ఆమె నిన్న ఆఫీసుకు వెళ్తుండలేదా?", "Wasn't she going to office yesterday?"),

    # Ramu
    ("రాము నిన్న ఆఫీసుకు వెళ్తున్నాడు.", "Ramu was going to office yesterday."),
    ("రాము నిన్న ఆఫీసుకు వెళ్తున్నాడా?", "Was Ramu going to office yesterday?"),
    ("రాము నిన్న ఎందుకు ఆఫీసుకు వెళ్తున్నాడు?", "Why was Ramu going to office yesterday?"),
    ("రాము నిన్న ఎక్కడికి వెళ్తున్నాడు?", "Where was Ramu going yesterday?"),
    ("రాము నిన్న ఆఫీసుకు వెళ్లడంలేదు.", "Ramu was not going to office yesterday."),
    ("రాము నిన్న ఆఫీసుకు వెళ్తుండలేదా?", "Wasn't Ramu going to office yesterday?"),

    # They
    ("వాళ్లు నిన్న ఆఫీసుకు వెళ్తున్నారు.", "They were going to office yesterday."),
    ("వాళ్లు నిన్న ఆఫీసుకు వెళ్తున్నారా?", "Were they going to office yesterday?"),
    ("వాళ్లు నిన్న ఎందుకు ఆఫీసుకు వెళ్తున్నారు?", "Why were they going to office yesterday?"),
    ("వాళ్లు నిన్న ఎక్కడికి వెళ్తున్నారు?", "Where were they going yesterday?"),
    ("వాళ్లు నిన్న ఆఫీసుకు వెళ్లడంలేదు.", "They were not going to office yesterday."),
    ("వాళ్లు నిన్న ఆఫీసుకు వెళ్తుండలేదా?", "Weren't they going to office yesterday?"),

    # We
    ("మేము నిన్న ఆఫీసుకు వెళ్తున్నాము.", "We were going to office yesterday."),
    ("మేము నిన్న ఆఫీసుకు వెళ్తున్నామా?", "Were we going to office yesterday?"),
    ("మేము నిన్న ఎందుకు ఆఫీసుకు వెళ్తున్నాము?", "Why were we going to office yesterday?"),
    ("మేము నిన్న ఎక్కడికి వెళ్తున్నాము?", "Where were we going yesterday?"),
    ("మేము నిన్న ఆఫీసుకు వెళ్లడంలేదు.", "We were not going to office yesterday."),
    ("మేము నిన్న ఆఫీసుకు వెళ్తుండలేమా?", "Weren't we going to office yesterday?"),

    # I
    ("నేను నిన్న ఆఫీసుకు వెళ్తున్నాను.", "I was going to office yesterday."),
    ("నేను నిన్న ఆఫీసుకు వెళ్తున్నానా?", "Was I going to office yesterday?"),
    ("నేను నిన్న ఎందుకు ఆఫీసుకు వెళ్తున్నాను?", "Why was I going to office yesterday?"),
    ("నేను నిన్న ఎక్కడికి వెళ్తున్నాను?", "Where was I going yesterday?"),
    ("నేను నిన్న ఆఫీసుకు వెళ్లడంలేదు.", "I was not going to office yesterday."),
    ("నేను నిన్న ఆఫీసుకు వెళ్తున్నానా కాదా?", "Wasn't I going to office yesterday?")
    ],

    "Future Continuous": [
    # You
    ("నీవు రేపు ఆఫీసుకు వెళ్తుంటావు.", "You will be going to office tomorrow."),
    ("నీవు రేపు ఆఫీసుకు వెళ్తుంటావా?", "Will you be going to office tomorrow?"),
    ("నీవు రేపు ఎందుకు ఆఫీసుకు వెళ్తుంటావు?", "Why will you be going to office tomorrow?"),
    ("నీవు రేపు ఎక్కడికి వెళ్తుంటావు?", "Where will you be going tomorrow?"),
    ("నీవు రేపు ఆఫీసుకు వెళ్తూ ఉండవు.", "You will not be going to office tomorrow."),
    ("నీవు రేపు ఆఫీసుకు వెళ్తూ ఉండవా?", "Will you not be going to office tomorrow?"),

    # She
    ("ఆమె రేపు ఆఫీసుకు వెళ్తుంటుంది.", "She will be going to office tomorrow."),
    ("ఆమె రేపు ఆఫీసుకు వెళ్తుంటుందా?", "Will she be going to office tomorrow?"),
    ("ఆమె రేపు ఎందుకు ఆఫీసుకు వెళ్తుంటుంది?", "Why will she be going to office tomorrow?"),
    ("ఆమె రేపు ఎక్కడికి వెళ్తుంటుంది?", "Where will she be going tomorrow?"),
    ("ఆమె రేపు ఆఫీసుకు వెళ్తూ ఉండదు.", "She will not be going to office tomorrow."),
    ("ఆమె రేపు ఆఫీసుకు వెళ్తూ ఉండదా?", "Will she not be going to office tomorrow?"),

    # Ramu
    ("రాము రేపు ఆఫీసుకు వెళ్తుంటాడు.", "Ramu will be going to office tomorrow."),
    ("రాము రేపు ఆఫీసుకు వెళ్తుంటాడా?", "Will Ramu be going to office tomorrow?"),
    ("రాము రేపు ఎందుకు ఆఫీసుకు వెళ్తుంటాడు?", "Why will Ramu be going to office tomorrow?"),
    ("రాము రేపు ఎక్కడికి వెళ్తుంటాడు?", "Where will Ramu be going tomorrow?"),
    ("రాము రేపు ఆఫీసుకు వెళ్తూ ఉండడు.", "Ramu will not be going to office tomorrow."),
    ("రాము రేపు ఆఫీసుకు వెళ్తూ ఉండడా?", "Will Ramu not be going to office tomorrow?"),

    # They
    ("వాళ్లు రేపు ఆఫీసుకు వెళ్తుంటారు.", "They will be going to office tomorrow."),
    ("వాళ్లు రేపు ఆఫీసుకు వెళ్తుంటారా?", "Will they be going to office tomorrow?"),
    ("వాళ్లు రేపు ఎందుకు ఆఫీసుకు వెళ్తుంటారు?", "Why will they be going to office tomorrow?"),
    ("వాళ్లు రేపు ఎక్కడికి వెళ్తుంటారు?", "Where will they be going tomorrow?"),
    ("వాళ్లు రేపు ఆఫీసుకు వెళ్తూ ఉండరు.", "They will not be going to office tomorrow."),
    ("వాళ్లు రేపు ఆఫీసుకు వెళ్తూ ఉండరా?", "Will they not be going to office tomorrow?"),

    # We
    ("మేము రేపు ఆఫీసుకు వెళ్తుంటాము.", "We will be going to office tomorrow."),
    ("మేము రేపు ఆఫీసుకు వెళ్తుంటామా?", "Will we be going to office tomorrow?"),
    ("మేము రేపు ఎందుకు ఆఫీసుకు వెళ్తుంటాము?", "Why will we be going to office tomorrow?"),
    ("మేము రేపు ఎక్కడికి వెళ్తుంటాము?", "Where will we be going tomorrow?"),
    ("మేము రేపు ఆఫీసుకు వెళ్తూ ఉండం.", "We will not be going to office tomorrow."),
    ("మేము రేపు ఆఫీసుకు వెళ్తూ ఉండమా?", "Will we not be going to office tomorrow?"),

    # I
    ("నేను రేపు ఆఫీసుకు వెళ్తుంటాను.", "I will be going to office tomorrow."),
    ("నేను రేపు ఆఫీసుకు వెళ్తుంటానా?", "Will I be going to office tomorrow?"),
    ("నేను రేపు ఎందుకు ఆఫీసుకు వెళ్తుంటాను?", "Why will I be going to office tomorrow?"),
    ("నేను రేపు ఎక్కడికి వెళ్తుంటాను?", "Where will I be going tomorrow?"),
    ("నేను రేపు ఆఫీసుకు వెళ్తూ ఉండను.", "I will not be going to office tomorrow."),
    ("నేను రేపు ఆఫీసుకు వెళ్తుంటానా కాదా?", "Will I not be going to office tomorrow?")
    ],

    "Present Perfect": [
    # Subject: You
    ("నీవు ఇప్పుడే ఆఫీసుకు వెళ్ళిపోయావు.", "You have gone to office just now."),
    ("నీవు ఇప్పుడే ఆఫీసుకు వెళ్ళిపోయావా?", "Have you gone to office just now?"),
    ("నీవు ఇప్పుడే ఎందుకు ఆఫీసుకు వెళ్ళిపోయావు?", "Why have you gone to office just now?"),
    ("నీవు ఇప్పుడే ఆఫీసుకు వెళ్ళలేదు.", "You have not gone to office just now."),
    ("నీవు ఇప్పుడే ఆఫీసుకు వెళ్ళలేదా?", "Haven't you gone to office just now?"),
    ("నీవు ఇప్పుడే ఎందుకు ఆఫీసుకు వెళ్ళలేదు?", "Why haven't you gone to office just now?"),

    # Subject: She
    ("ఆమె ఇప్పుడే ఆఫీసుకు వెళ్ళిపోయింది.", "She has gone to office just now."),
    ("ఆమె ఇప్పుడే ఆఫీసుకు వెళ్ళిపోయిందా?", "Has she gone to office just now?"),
    ("ఆమె ఇప్పుడే ఎందుకు ఆఫీసుకు వెళ్ళిపోయింది?", "Why has she gone to office just now?"),
    ("ఆమె ఇప్పుడే ఆఫీసుకు వెళ్ళలేదు.", "She has not gone to office just now."),
    ("ఆమె ఇప్పుడే ఆఫీసుకు వెళ్ళలేదా?", "Hasn't she gone to office just now?"),
    ("ఆమె ఇప్పుడే ఎందుకు ఆఫీసుకు వెళ్ళలేదు?", "Why hasn't she gone to office just now?"),

    # Subject: Ramu
    ("రాము ఇప్పుడే ఆఫీసుకు వెళ్ళిపోయాడు.", "Ramu has gone to office just now."),
    ("రాము ఇప్పుడే ఆఫీసుకు వెళ్ళిపోయాడా?", "Has Ramu gone to office just now?"),
    ("రాము ఇప్పుడే ఎందుకు ఆఫీసుకు వెళ్ళిపోయాడు?", "Why has Ramu gone to office just now?"),
    ("రాము ఇప్పుడే ఆఫీసుకు వెళ్ళలేదు.", "Ramu has not gone to office just now."),
    ("రాము ఇప్పుడే ఆఫీసుకు వెళ్ళలేదా?", "Hasn't Ramu gone to office just now?"),
    ("రాము ఇప్పుడే ఎందుకు ఆఫీసుకు వెళ్ళలేదు?", "Why hasn't Ramu gone to office just now?"),

    # Subject: They
    ("వాళ్లు ఇప్పుడే ఆఫీసుకు వెళ్ళిపోయారు.", "They have gone to office just now."),
    ("వాళ్లు ఇప్పుడే ఆఫీసుకు వెళ్ళిపోయారా?", "Have they gone to office just now?"),
    ("వాళ్లు ఇప్పుడే ఎందుకు ఆఫీసుకు వెళ్ళిపోయారు?", "Why have they gone to office just now?"),
    ("వాళ్లు ఇప్పుడే ఆఫీసుకు వెళ్ళలేదు.", "They have not gone to office just now."),
    ("వాళ్లు ఇప్పుడే ఆఫీసుకు వెళ్ళలేదా?", "Haven't they gone to office just now?"),
    ("వాళ్లు ఇప్పుడే ఎందుకు ఆఫీసుకు వెళ్ళలేదు?", "Why haven't they gone to office just now?"),

    # Subject: We
    ("మేము ఇప్పుడే ఆఫీసుకు వెళ్ళిపోయాము.", "We have gone to office just now."),
    ("మేము ఇప్పుడే ఆఫీసుకు వెళ్ళిపోయామా?", "Have we gone to office just now?"),
    ("మేము ఇప్పుడే ఎందుకు ఆఫీసుకు వెళ్ళిపోయాము?", "Why have we gone to office just now?"),
    ("మేము ఇప్పుడే ఆఫీసుకు వెళ్ళలేదు.", "We have not gone to office just now."),
    ("మేము ఇప్పుడే ఆఫీసుకు వెళ్ళలేదా?", "Haven't we gone to office just now?"),
    ("మేము ఇప్పుడే ఎందుకు ఆఫీసుకు వెళ్ళలేదు?", "Why haven't we gone to office just now?"),

    # Subject: I
    ("నేను ఇప్పుడే ఆఫీసుకు వెళ్ళిపోయాను.", "I have gone to office just now."),
    ("నేను ఇప్పుడే ఆఫీసుకు వెళ్ళిపోయానా?", "Have I gone to office just now?"),
    ("నేను ఇప్పుడే ఎందుకు ఆఫీసుకు వెళ్ళిపోయాను?", "Why have I gone to office just now?"),
    ("నేను ఇప్పుడే ఆఫీసుకు వెళ్ళలేదు.", "I have not gone to office just now."),
    ("నేను ఇప్పుడే ఆఫీసుకు వెళ్ళలేదా?", "Haven't I gone to office just now?"),
    ("నేను ఇప్పుడే ఎందుకు ఆఫీసుకు వెళ్ళలేదు?", "Why haven't I gone to office just now?")
    ],

    "Want to": [
    # You
    ("నీవు ఈ రోజు ఆఫీసుకు వెళ్లాలనుకుంటున్నావు.", "You want to go to office today."),
    ("నీవు ఈ రోజు ఆఫీసుకు వెళ్లాలనుకుంటున్నావా?", "Do you want to go to office today?"),
    ("నీవు ఈ రోజు ఆఫీసుకు ఎందుకు వెళ్లాలనుకుంటున్నావు?", "Why do you want to go to office today?"),
    ("నీవు ఈ రోజు ఆఫీసుకు వెళ్లాలనుకోవడం లేదు.", "You do not want to go to office today."),
    ("నీవు ఈ రోజు ఆఫీసుకు వెళ్లాలనుకోడంలేదా?", "Don't you want to go to office today?"),
    ("నీవు ఈ రోజు ఆఫీసుకు ఎందుకు వెళ్లాలనుకోవడం లేదు?", "Why don't you want to go to office today?"),

    # She
    ("ఆమె ఈ రోజు ఆఫీసుకు వెళ్లాలనుకుంటోంది.", "She wants to go to office today."),
    ("ఆమె ఈ రోజు ఆఫీసుకు వెళ్లాలనుకుంటుందా?", "Does she want to go to office today?"),
    ("ఆమె ఈ రోజు ఆఫీసుకు ఎందుకు వెళ్లాలనుకుంటోంది?", "Why does she want to go to office today?"),
    ("ఆమె ఈ రోజు ఆఫీసుకు వెళ్లాలనుకోవడం లేదు.", "She does not want to go to office today."),
    ("ఆమె ఈ రోజు ఆఫీసుకు వెళ్లాలనుకోడంలేదా?", "Doesn't she want to go to office today?"),
    ("ఆమె ఈ రోజు ఆఫీసుకు ఎందుకు వెళ్లాలనుకోవడం లేదు?", "Why doesn't she want to go to office today?"),

    # Ramu
    ("రాము ఈ రోజు ఆఫీసుకు వెళ్లాలనుకుంటున్నాడు.", "Ramu wants to go to office today."),
    ("రాము ఈ రోజు ఆఫీసుకు వెళ్లాలనుకుంటున్నాడా?", "Does Ramu want to go to office today?"),
    ("రాము ఈ రోజు ఆఫీసుకు ఎందుకు వెళ్లాలనుకుంటున్నాడు?", "Why does Ramu want to go to office today?"),
    ("రాము ఈ రోజు ఆఫీసుకు వెళ్లాలనుకోవడం లేదు.", "Ramu does not want to go to office today."),
    ("రాము ఈ రోజు ఆఫీసుకు వెళ్లాలనుకోడంలేదా?", "Doesn't Ramu want to go to office today?"),
    ("రాము ఈ రోజు ఆఫీసుకు ఎందుకు వెళ్లాలనుకోవడం లేదు?", "Why doesn't Ramu want to go to office today?"),

    # They
    ("వాళ్లు ఈ రోజు ఆఫీసుకు వెళ్లాలనుకుంటున్నారు.", "They want to go to office today."),
    ("వాళ్లు ఈ రోజు ఆఫీసుకు వెళ్లాలనుకుంటున్నారా?", "Do they want to go to office today?"),
    ("వాళ్లు ఈ రోజు ఆఫీసుకు ఎందుకు వెళ్లాలనుకుంటున్నారు?", "Why do they want to go to office today?"),
    ("వాళ్లు ఈ రోజు ఆఫీసుకు వెళ్లాలనుకోవడం లేదు.", "They do not want to go to office today."),
    ("వాళ్లు ఈ రోజు ఆఫీసుకు వెళ్లాలనుకోడంలేదా?", "Don't they want to go to office today?"),
    ("వాళ్లు ఈ రోజు ఆఫీసుకు ఎందుకు వెళ్లాలనుకోవడం లేదు?", "Why don't they want to go to office today?"),

    # We
    ("మేము ఈ రోజు ఆఫీసుకు వెళ్లాలనుకుంటున్నాము.", "We want to go to office today."),
    ("మేము ఈ రోజు ఆఫీసుకు వెళ్లాలనుకుంటున్నామా?", "Do we want to go to office today?"),
    ("మేము ఈ రోజు ఆఫీసుకు ఎందుకు వెళ్లాలనుకుంటున్నాము?", "Why do we want to go to office today?"),
    ("మేము ఈ రోజు ఆఫీసుకు వెళ్లాలనుకోవడం లేదు.", "We do not want to go to office today."),
    ("మేము ఈ రోజు ఆఫీసుకు వెళ్లాలనుకోడంలేదా?", "Don't we want to go to office today?"),
    ("మేము ఈ రోజు ఆఫీసుకు ఎందుకు వెళ్లాలనుకోవడం లేదు?", "Why don't we want to go to office today?"),

    # I
    ("నేను ఈ రోజు ఆఫీసుకు వెళ్లాలనుకుంటున్నాను.", "I want to go to office today."),
    ("నేను ఈ రోజు ఆఫీసుకు వెళ్లాలనుకుంటున్నానా?", "Do I want to go to office today?"),
    ("నేను ఈ రోజు ఆఫీసుకు ఎందుకు వెళ్లాలనుకుంటున్నాను?", "Why do I want to go to office today?"),
    ("నేను ఈ రోజు ఆఫీసుకు వెళ్లాలనుకోవడం లేదు.", "I do not want to go to office today."),
    ("నేను ఈ రోజు ఆఫీసుకు వెళ్లాలనుకోడంలేదా?", "Don't I want to go to office today?"),
    ("నేను ఈ రోజు ఆఫీసుకు ఎందుకు వెళ్లాలనుకోవడం లేదు?", "Why don't I want to go to office today?")
    ],

    "Wanted to": [
    # You
    ("నీవు నిన్న ఆఫీసుకు వెళ్లాలని అనుకున్నావు.", "You wanted to go to office yesterday."),
    ("నీవు నిన్న ఆఫీసుకు వెళ్లాలని అనుకున్నావా?", "Did you want to go to office yesterday?"),
    ("నీవు నిన్న ఆఫీసుకు ఎందుకు వెళ్లాలని అనుకున్నావు?", "Why did you want to go to office yesterday?"),
    ("నీవు నిన్న ఆఫీసుకు వెళ్లాలని అనుకోలేదు.", "You did not want to go to office yesterday."),
    ("నీవు నిన్న ఆఫీసుకు వెళ్లాలని అనుకోలేదా?", "Didn't you want to go to office yesterday?"),
    ("నీవు నిన్న ఆఫీసుకు ఎందుకు వెళ్లాలని అనుకోలేదు?", "Why didn't you want to go to office yesterday?"),

    # She
    ("ఆమె నిన్న ఆఫీసుకు వెళ్లాలని అనుకుంది.", "She wanted to go to office yesterday."),
    ("ఆమె నిన్న ఆఫీసుకు వెళ్లాలని అనుకున్నదా?", "Did she want to go to office yesterday?"),
    ("ఆమె నిన్న ఆఫీసుకు ఎందుకు వెళ్లాలని అనుకుంది?", "Why did she want to go to office yesterday?"),
    ("ఆమె నిన్న ఆఫీసుకు వెళ్లాలని అనుకోలేదు.", "She did not want to go to office yesterday."),
    ("ఆమె నిన్న ఆఫీసుకు వెళ్లాలని అనుకోలేదా?", "Didn't she want to go to office yesterday?"),
    ("ఆమె నిన్న ఆఫీసుకు ఎందుకు వెళ్లాలని అనుకోలేదు?", "Why didn't she want to go to office yesterday?"),

    # Ramu
    ("రాము నిన్న ఆఫీసుకు వెళ్లాలని అనుకున్నాడు.", "Ramu wanted to go to office yesterday."),
    ("రాము నిన్న ఆఫీసుకు వెళ్లాలని అనుకున్నాడా?", "Did Ramu want to go to office yesterday?"),
    ("రాము నిన్న ఆఫీసుకు ఎందుకు వెళ్లాలని అనుకున్నాడు?", "Why did Ramu want to go to office yesterday?"),
    ("రాము నిన్న ఆఫీసుకు వెళ్లాలని అనుకోలేదు.", "Ramu did not want to go to office yesterday."),
    ("రాము నిన్న ఆఫీసుకు వెళ్లాలని అనుకోలేదా?", "Didn't Ramu want to go to office yesterday?"),
    ("రాము నిన్న ఆఫీసుకు ఎందుకు వెళ్లాలని అనుకోలేదు?", "Why didn't Ramu want to go to office yesterday?"),

    # They
    ("వాళ్లు నిన్న ఆఫీసుకు వెళ్లాలని అనుకున్నారు.", "They wanted to go to office yesterday."),
    ("వాళ్లు నిన్న ఆఫీసుకు వెళ్లాలని అనుకున్నారా?", "Did they want to go to office yesterday?"),
    ("వాళ్లు నిన్న ఆఫీసుకు ఎందుకు వెళ్లాలని అనుకున్నారు?", "Why did they want to go to office yesterday?"),
    ("వాళ్లు నిన్న ఆఫీసుకు వెళ్లాలని అనుకోలేదు.", "They did not want to go to office yesterday."),
    ("వాళ్లు నిన్న ఆఫీసుకు వెళ్లాలని అనుకోలేదా?", "Didn't they want to go to office yesterday?"),
    ("వాళ్లు నిన్న ఆఫీసుకు ఎందుకు వెళ్లాలని అనుకోలేదు?", "Why didn't they want to go to office yesterday?"),

    # We
    ("మేము నిన్న ఆఫీసుకు వెళ్లాలని అనుకున్నాము.", "We wanted to go to office yesterday."),
    ("మేము నిన్న ఆఫీసుకు వెళ్లాలని అనుకున్నామా?", "Did we want to go to office yesterday?"),
    ("మేము నిన్న ఆఫీసుకు ఎందుకు వెళ్లాలని అనుకున్నాము?", "Why did we want to go to office yesterday?"),
    ("మేము నిన్న ఆఫీసుకు వెళ్లాలని అనుకోలేదు.", "We did not want to go to office yesterday."),
    ("మేము నిన్న ఆఫీసుకు వెళ్లాలని అనుకోలేదా?", "Didn't we want to go to office yesterday?"),
    ("మేము నిన్న ఆఫీసుకు ఎందుకు వెళ్లాలని అనుకోలేదు?", "Why didn't we want to go to office yesterday?"),

    # I
    ("నేను నిన్న ఆఫీసుకు వెళ్లాలని అనుకున్నాను.", "I wanted to go to office yesterday."),
    ("నేను నిన్న ఆఫీసుకు వెళ్లాలని అనుకున్నానా?", "Did I want to go to office yesterday?"),
    ("నేను నిన్న ఆఫీసుకు ఎందుకు వెళ్లాలని అనుకున్నాను?", "Why did I want to go to office yesterday?"),
    ("నేను నిన్న ఆఫీసుకు వెళ్లాలని అనుకోలేదు.", "I did not want to go to office yesterday."),
    ("నేను నిన్న ఆఫీసుకు వెళ్లాలని అనుకోలేదా?", "Didn't I want to go to office yesterday?"),
    ("నేను నిన్న ఆఫీసుకు ఎందుకు వెళ్లాలని అనుకోలేదు?", "Why didn't I want to go to office yesterday?")
    ],

    "Present Be Forms": [
    ("ఆమె ఈ రోజు చెన్నైలో ఉంది.", "She is in Chennai today."),
    ("ఆమె ఈ రోజు చెన్నైలో ఉందా?", "Is she in Chennai today?"),
    ("ఆమె ఈ రోజు చెన్నైలో ఎందుకు ఉంది?", "Why is she in Chennai today?"),
    ("ఆమె ఈ రోజు చెన్నైలో లేదు.", "She is not in Chennai today."),
    ("ఆమె ఈ రోజు చెన్నైలో లేడా?", "Isn't she in Chennai today?"),

    ("అతను ఈ రోజు చెన్నైలో ఉన్నాడు.", "He is in Chennai today."),
    ("అతను ఈ రోజు చెన్నైలో ఉన్నాడా?", "Is he in Chennai today?"),
    ("అతను ఈ రోజు చెన్నైలో ఎందుకు ఉన్నాడు?", "Why is he in Chennai today?"),
    ("అతను ఈ రోజు చెన్నైలో లేడు.", "He is not in Chennai today."),
    ("అతను ఈ రోజు చెన్నైలో లేడా?", "Isn't he in Chennai today?"),

    ("వారు ఈ రోజు చెన్నైలో ఉన్నారు.", "They are in Chennai today."),
    ("వారు ఈ రోజు చెన్నైలో ఉన్నారా?", "Are they in Chennai today?"),
    ("వారు ఈ రోజు చెన్నైలో ఎందుకు ఉన్నారు?", "Why are they in Chennai today?"),
    ("వారు ఈ రోజు చెన్నైలో లేరు.", "They are not in Chennai today."),
    ("వారు ఈ రోజు చెన్నైలో లేరా?", "Aren't they in Chennai today?"),

    ("మేము ఈ రోజు చెన్నైలో ఉన్నాము.", "We are in Chennai today."),
    ("మేము ఈ రోజు చెన్నైలో ఉన్నామా?", "Are we in Chennai today?"),
    ("మేము ఈ రోజు చెన్నైలో ఎందుకు ఉన్నాము?", "Why are we in Chennai today?"),
    ("మేము ఈ రోజు చెన్నైలో లేము.", "We are not in Chennai today."),
    ("మేము ఈ రోజు చెన్నైలో లేమా?", "Aren't we in Chennai today?"),

    ("నేను ఈ రోజు చెన్నైలో ఉన్నాను.", "I am in Chennai today."),
    ("నేను ఈ రోజు చెన్నైలో ఉన్నానా?", "Am I in Chennai today?"),
    ("నేను ఈ రోజు చెన్నైలో ఎందుకు ఉన్నాను?", "Why am I in Chennai today?"),
    ("నేను ఈ రోజు చెన్నైలో లేను.", "I am not in Chennai today."),
    ("నేను ఈ రోజు చెన్నైలో లేననా?", "Aren’t I in Chennai today?")
    ],
    "Past Be Forms": [
    ("ఆమె నిన్న చెన్నైలో ఉండింది.", "She was in Chennai yesterday."),
    ("ఆమె నిన్న చెన్నైలో ఉండిందా?", "Was she in Chennai yesterday?"),
    ("ఆమె నిన్న చెన్నైలో ఎందుకు ఉండింది?", "Why was she in Chennai yesterday?"),
    ("ఆమె నిన్న చెన్నైలో లేదు.", "She was not in Chennai yesterday."),
    ("ఆమె నిన్న చెన్నైలో లేడా?", "Wasn't she in Chennai yesterday?"),

    ("అతను నిన్న చెన్నైలో ఉన్నాడు.", "He was in Chennai yesterday."),
    ("అతను నిన్న చెన్నైలో ఉన్నాడా?", "Was he in Chennai yesterday?"),
    ("అతను నిన్న చెన్నైలో ఎందుకు ఉన్నాడు?", "Why was he in Chennai yesterday?"),
    ("అతను నిన్న చెన్నైలో లేడు.", "He was not in Chennai yesterday."),
    ("అతను నిన్న చెన్నైలో లేడా?", "Wasn't he in Chennai yesterday?"),

    ("వారు నిన్న చెన్నైలో ఉన్నారు.", "They were in Chennai yesterday."),
    ("వారు నిన్న చెన్నైలో ఉన్నారా?", "Were they in Chennai yesterday?"),
    ("వారు నిన్న చెన్నైలో ఎందుకు ఉన్నారు?", "Why were they in Chennai yesterday?"),
    ("వారు నిన్న చెన్నైలో లేరు.", "They were not in Chennai yesterday."),
    ("వారు నిన్న చెన్నైలో లేరా?", "Weren't they in Chennai yesterday?"),

    ("మేము నిన్న చెన్నైలో ఉన్నాము.", "We were in Chennai yesterday."),
    ("మేము నిన్న చెన్నైలో ఉన్నామా?", "Were we in Chennai yesterday?"),
    ("మేము నిన్న చెన్నైలో ఎందుకు ఉన్నాము?", "Why were we in Chennai yesterday?"),
    ("మేము నిన్న చెన్నైలో లేము.", "We were not in Chennai yesterday."),
    ("మేము నిన్న చెన్నైలో లేమా?", "Weren't we in Chennai yesterday?"),

    ("నేను నిన్న చెన్నైలో ఉన్నాను.", "I was in Chennai yesterday."),
    ("నేను నిన్న చెన్నైలో ఉన్నానా?", "Was I in Chennai yesterday?"),
    ("నేను నిన్న చెన్నైలో ఎందుకు ఉన్నాను?", "Why was I in Chennai yesterday?"),
    ("నేను నిన్న చెన్నైలో లేను.", "I was not in Chennai yesterday."),
    ("నేను నిన్న చెన్నైలో లేననా?", "Wasn't I in Chennai yesterday?")
    ],
    "Future Be Forms": [
    ("ఆమె రేపు చెన్నైలో ఉంటారు.", "She will be in Chennai tomorrow."),
    ("ఆమె రేపు చెన్నైలో ఉంటుందా?", "Will she be in Chennai tomorrow?"),
    ("ఆమె రేపు చెన్నైలో ఎందుకు ఉంటారు?", "Why will she be in Chennai tomorrow?"),
    ("ఆమె రేపు చెన్నైలో ఉండదు.", "She will not be in Chennai tomorrow."),
    ("ఆమె రేపు చెన్నైలో ఉండదా?", "Won't she be in Chennai tomorrow?"),

    ("అతను రేపు చెన్నైలో ఉంటాడు.", "He will be in Chennai tomorrow."),
    ("అతను రేపు చెన్నైలో ఉంటాడా?", "Will he be in Chennai tomorrow?"),
    ("అతను రేపు చెన్నైలో ఎందుకు ఉంటాడు?", "Why will he be in Chennai tomorrow?"),
    ("అతను రేపు చెన్నైలో ఉండడు.", "He will not be in Chennai tomorrow."),
    ("అతను రేపు చెన్నైలో ఉండడా?", "Won't he be in Chennai tomorrow?"),

    ("వారు రేపు చెన్నైలో ఉంటారు.", "They will be in Chennai tomorrow."),
    ("వారు రేపు చెన్నైలో ఉంటారా?", "Will they be in Chennai tomorrow?"),
    ("వారు రేపు చెన్నైలో ఎందుకు ఉంటారు?", "Why will they be in Chennai tomorrow?"),
    ("వారు రేపు చెన్నైలో ఉండరు.", "They will not be in Chennai tomorrow."),
    ("వారు రేపు చెన్నైలో ఉండరా?", "Won't they be in Chennai tomorrow?"),

    ("మేము రేపు చెన్నైలో ఉంటాము.", "We will be in Chennai tomorrow."),
    ("మేము రేపు చెన్నైలో ఉంటామా?", "Will we be in Chennai tomorrow?"),
    ("మేము రేపు చెన్నైలో ఎందుకు ఉంటాము?", "Why will we be in Chennai tomorrow?"),
    ("మేము రేపు చెన్నైలో ఉండము.", "We will not be in Chennai tomorrow."),
    ("మేము రేపు చెన్నైలో ఉండమా?", "Won't we be in Chennai tomorrow?"),

    ("నేను రేపు చెన్నైలో ఉంటాను.", "I will be in Chennai tomorrow."),
    ("నేను రేపు చెన్నైలో ఉంటానా?", "Will I be in Chennai tomorrow?"),
    ("నేను రేపు చెన్నైలో ఎందుకు ఉంటాను?", "Why will I be in Chennai tomorrow?"),
    ("నేను రేపు చెన్నైలో ఉండను.", "I will not be in Chennai tomorrow."),
    ("నేను రేపు చెన్నైలో ఉండనా?", "Won't I be in Chennai tomorrow?")
    ],


    "Have to": [
        ("నీవు ఈ రోజు ఆఫీసుకు వెళ్ళవలసి ఉంది.", "You have to go to office today."),
        ("నీవు ఈ రోజు ఆఫీసుకు వెళ్ళవలసి ఉందా?", "Do you have to go to office today?"),
        ("నీవు ఈ రోజు ఆఫీసుకు ఎందుకు వెళ్ళవలసి ఉంది?", "Why do you have to go to office today?"),
        ("నీవు ఈ రోజు ఎప్పుడు ఆఫీసుకు వెళ్ళవలసి ఉంది?", "When do you have to go to office today?"),
        ("నీవు ఈ రోజు ఎక్కడికి వెళ్ళవలసి ఉంది?", "Where do you have to go today?")
    ]
}


Conjunction_sentenses = {

    "For": [
        ("అతను ఇంట్లోనే ఉన్నాడు, ఎందుకంటే అతను అనారోగ్యంగా ఉన్నాడు.", "He stayed home, for he was sick.")
    ],
    "And": [
        ("నాకు కాఫీ మరియు టీ ఇష్టం.", "I like coffee and tea.")
    ],
    "Nor": [
        ("ఆమె నవ్వలేదు, మరియు మాట్లాడలేదు కూడా.", "She didn’t smile, nor did she speak.")
    ],
    "But": [
        ("నేను వేగంగా పరుగెత్తాను, కానీ బస్సు మిస్సయ్యాను.", "I ran fast, but I missed the bus.")
    ],
    "Or": [
        ("నీకు జ్యూస్ కావాలా లేదా సోడా?", "Do you want juice or soda?")
    ],
    "Yet": [
        ("ఇది చల్లగా ఉంది, అయినా అతను కోట్ వేసుకోలేదు.", "It’s cold, yet he isn’t wearing a coat.")
    ],
    "So": [
        ("వర్షం పడింది, కాబట్టి మేము ఇంట్లో ఉన్నాము.", "It rained, so we stayed in.")
    ],
    "Because": [
        ("వర్షం పడింది కాబట్టి నేను ఉన్నాను.", "I stayed because it rained.")
    ],
    "Although": [
        ("అతను ధనవంతుడు అయినా సంతోషంగా లేడు.", "Although he's rich, he is unhappy.")
    ],
    "If": [
        ("నీవు ప్రయత్నిస్తే, నీవు గెలుస్తావు.", "If you try, you’ll win.")
    ],
    "Unless": [
        ("నీవు చదవకపోతే నీవు ఫెయిల్ అవుతావు.", "Unless you study, you’ll fail.")
    ],
    "While": [
        ("ఆమె మాట్లాడుతున్నప్పుడు నేను విన్నాను.", "I listened while she spoke.")
    ],
    "After": [
        ("తినిన తరువాత నిద్రపోయాను.", "I slept after I ate.")
    ],
    "Before": [
        ("తినే ముందు చేతులు కడుక్కో.", "Wash your hands before you eat.")
    ],
    "Even if": [
        ("వర్షం పడినప్పటికీ మేము వెళ్తాము.", "Even if it rains, we’ll go.")
    ],
    "In case": [
        ("వర్షం పడితే అన్న ఊహలో గొడుగు తీసుకెళ్లి.", "Take an umbrella in case it rains.")
    ],
    "As long as": [
        ("నీవు నిశ్శబ్దంగా ఉన్నంతవరకూ నీవు ఉండవచ్చు.", "You can stay as long as you’re quiet.")
    ],
    "Now that": [
        ("ఇది అయిపోయిందని ఇప్పుడు విశ్రాంతి తీసుకుందాం.", "Now that it’s over, we can rest.")
    ],
    "Even though": [
        ("అతను వృద్ధుడైనా, కష్టపడుతూ పని చేస్తాడు.", "Even though he’s old, he works hard.")
    ],
    "Provided that": [
        ("నీవు పని పూర్తిచేస్తే నీవు వెళ్ళవచ్చు.", "You may go provided that you finish work.")
    ],
    "As if": [
        ("అతను రాజులా మాట్లాడుతున్నాడు.", "He talks as if he were a king.")
    ],
    "Either...or": [
        ("నీవు రా లేకపోతే ఫోన్ చెయ్యి.", "Either come or call.")
    ],
    "Neither...nor": [
        ("అబ్బాయి కాదు, అమ్మాయి కూడా లేదు.", "Neither the boy nor the girl spoke.")
    ],
    "Not only...but also": [
        ("ఆమె తెలివైనదే కాదు, మంచిదీ కూడా.", "Not only smart but also kind.")
    ],
    "Both...and": [
        ("తండ్రి మరియు కొడుకు ఇద్దరూ డాక్టర్లు.", "Both father and son are doctors.")
    ],
    "Whether...or": [
        ("వర్షం పడినా లేదా పడకపోయినా మేము ఆడతాము.", "Whether it rains or not, we’ll play.")
    ],
    "However": [
        ("అతను ధనవంతుడు అయినప్పటికీ సంతోషంగా లేడు.", "He was tired; however, he continued.")
    ],
    "Therefore": [
        ("ఆమె బాగా చదువుకుంది; కాబట్టి ఆమె ఉత్తీర్ణురాలైంది.", "She studied well; therefore, she passed.")
    ],
    "Moreover": [
        ("అతను మంచి వ్యక్తి; అంతేకాకుండా, అతను ఉదారంగా ఉన్నాడు.", "He is kind; moreover, he is generous.")
    ],
    "Nevertheless": [
        ("వర్షం పడింది; అయినా మేము బయటికి వెళ్లాము.", "It rained; nevertheless, we went out.")
    ],
    "Consequently": [
        ("అతను ట్రైన్ మిస్సయ్యాడు; ఫలితంగా, ఆలస్యమయ్యాడు.", "He missed the train; consequently, he was late.")
    ],
    "Furthermore": [
        ("ఆమె రచయిత మాత్రమే కాదు, అదేవిధంగా మంచి వక్త కూడా.", "She is a writer; furthermore, a good speaker.")
    ]
}

# Tense information bank
tense_info = {
    "Simple Present": "The simple present tense is used to describe habits, unchanging situations, general truths, and fixed arrangements.",
    "Past Continuous": "The past continuous tense is used to describe actions that were ongoing in the past.",
    "Future Simple": "The future simple tense is used to talk about actions that will happen in the future."

}

# Set up page
#st.set_page_config(page_title="Praveen Spoken English", page_icon="🗣", layout="centered")

# Title and welcome message
#st.title("🗣 Welcome to Praveen Spoken English")
#st.markdown("### Learn English through Telugu with ease and confidence!")

import streamlit as st

# Set page title
st.set_page_config(page_title="Praveen Spoken English", layout="centered")

# Custom CSS for blinking text
st.markdown("""
    <style>
    .blinking-text {
        animation: blinker 1.5s linear infinite;
        color: #007ACC;
        font-size: 32px;
        font-weight: bold;
        text-align: center;
        margin-top: 30px;
    }

    @keyframes blinker {
        50% {
            opacity: 0;
        }
    }

    .phone-number {
        font-size: 20px;
        color: #333;
        text-align: center;
        margin-top: 20px;
    }
    </style>

    <div class="blinking-text">Welcome to Praveen Spoken English</div>
    <div class="phone-number">📞 Contact: 8248268056</div>
""", unsafe_allow_html=True)

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
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        if st.button("🗣 Practice All Tenses"):
            go_to("practice")
    with col2:
        if st.button("📘 Tense-wise Understand & Practice"):
            go_to("tense_wise")
    with col3:
        if st.button("🔤 Learn Verbs"):
            go_to("verbs")
    with col4:
        if st.button("🔤 Learn and practise conjunctions"):
            go_to("conjunctions")
    with col5:
        if st.button("🔤 understand conjunctions"):
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

    st.markdown("---")
    if st.button("🏠 Back to Home"):
        go_to("home")

# Practice English Page (conjunctions)
elif st.session_state.page == "conjunctions":
    st.header("🗣 Learn and practise conjunctions")

    all_sentences = sum(Conjunction_sentenses.values(), [])

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


    if st.button("🏠 Back to Home"):
        go_to("home")

# Learn Verbs Page
elif st.session_state.page == "verbs":
    st.header("🔤 Learn Verbs")
    st.markdown("Here you will learn important verbs in English and their Telugu meanings.")
    st.info("Coming soon: Common verbs list and usage examples.")
    if st.button("🏠 Back to Home"):
        go_to("home")