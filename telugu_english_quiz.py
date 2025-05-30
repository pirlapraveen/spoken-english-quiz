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
    with col3:
        if st.button("🔤 Learn and practise conjunctions"):
            go_to("conjunctions")

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

# Learn Verbs Page
elif st.session_state.page == "verbs":
    st.header("🔤 Learn Verbs")
    st.markdown("Here you will learn important verbs in English and their Telugu meanings.")
    st.info("Coming soon: Common verbs list and usage examples.")
    if st.button("🏠 Back to Home"):
        go_to("home")