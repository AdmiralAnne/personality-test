import streamlit as st
from openai import OpenAI

st.header("Answer these 11 questions to find your ideal career path: (beta version 0.2.0)")

# questions.py
question = {
    "OCEAN": {
        "Openness": [
            {
                "question": "I enjoy trying out new activities or exploring unfamiliar ideas.",
                "options": [
                    ("Strongly agree", 35),
                    ("Agree", 30),
                    ("Neutral", 22),
                    ("Disagree", 12),
                    ("Strongly disagree", 5)
                ]
            },
            {
                "question": "I am curious about many different topics.",
                "options": [
                    ("Strongly agree", 35),
                    ("Agree", 30),
                    ("Neutral", 22),
                    ("Disagree", 12),
                    ("Strongly disagree", 5)
                ]
            }
        ],
        "Conscientiousness": [
            {
                "question": "I am highly organized and like to plan ahead.",
                "options": [
                    ("Strongly agree", 35),
                    ("Agree", 30),
                    ("Neutral", 22),
                    ("Disagree", 12),
                    ("Strongly disagree", 5)
                ]
            },
            {
                "question": "I tend to complete my tasks before the deadline.",
                "options": [
                    ("Strongly agree", 35),
                    ("Agree", 30),
                    ("Neutral", 22),
                    ("Disagree", 12),
                    ("Strongly disagree", 5)
                ]
            }
        ],
        "Extraversion": [
            {
                "question": "I feel energized when I am around other people.",
                "options": [
                    ("Strongly agree", 35),
                    ("Agree", 30),
                    ("Neutral", 22),
                    ("Disagree", 12),
                    ("Strongly disagree", 5)
                ]
            },
            {
                "question": "I enjoy being the center of attention in social gatherings.",
                "options": [
                    ("Strongly agree", 35),
                    ("Agree", 30),
                    ("Neutral", 22),
                    ("Disagree", 12),
                    ("Strongly disagree", 5)
                ]
            }
        ],
        "Agreeableness": [
            {
                "question": "I often consider others' feelings before acting.",
                "options": [
                    ("Strongly agree", 35),
                    ("Agree", 30),
                    ("Neutral", 22),
                    ("Disagree", 12),
                    ("Strongly disagree", 5)
                ]
            },
            {
                "question": "I am willing to compromise to maintain peace.",
                "options": [
                    ("Strongly agree", 35),
                    ("Agree", 30),
                    ("Neutral", 22),
                    ("Disagree", 12),
                    ("Strongly disagree", 5)
                ]
            }
        ],
        "Neuroticism": [
            {
                "question": "I often worry about situations, even if they are not urgent.",
                "options": [
                    ("Strongly agree", 35),
                    ("Agree", 30),
                    ("Neutral", 22),
                    ("Disagree", 12),
                    ("Strongly disagree", 5)
                ]
            },
            {
                "question": "I frequently feel stressed in everyday life.",
                "options": [
                    ("Strongly agree", 35),
                    ("Agree", 30),
                    ("Neutral", 22),
                    ("Disagree", 12),
                    ("Strongly disagree", 5)
                ]
            }
        ]
    },
    "RIASEC": {
        "Realistic": [
            {
                "question": "I enjoy tasks that involve physical work or using tools.",
                "options": [
                    ("Strongly agree", 35),
                    ("Agree", 30),
                    ("Neutral", 22),
                    ("Disagree", 12),
                    ("Strongly disagree", 5)
                ]
            },
            {
                "question": "I find satisfaction in building or fixing things.",
                "options": [
                    ("Strongly agree", 35),
                    ("Agree", 30),
                    ("Neutral", 22),
                    ("Disagree", 12),
                    ("Strongly disagree", 5)
                ]
            }
        ],
        "Investigative": [
            {
                "question": "I like researching and analyzing complex problems.",
                "options": [
                    ("Strongly agree", 35),
                    ("Agree", 30),
                    ("Neutral", 22),
                    ("Disagree", 12),
                    ("Strongly disagree", 5)
                ]
            },
            {
                "question": "I enjoy reading about scientific or technical topics.",
                "options": [
                    ("Strongly agree", 35),
                    ("Agree", 30),
                    ("Neutral", 22),
                    ("Disagree", 12),
                    ("Strongly disagree", 5)
                ]
            }
        ],
        "Artistic": [
            {
                "question": "I feel fulfilled when engaging in creative activities like art or music.",
                "options": [
                    ("Strongly agree", 35),
                    ("Agree", 30),
                    ("Neutral", 22),
                    ("Disagree", 12),
                    ("Strongly disagree", 5)
                ]
            },
            {
                "question": "I prefer work that allows for creative freedom.",
                "options": [
                    ("Strongly agree", 35),
                    ("Agree", 30),
                    ("Neutral", 22),
                    ("Disagree", 12),
                    ("Strongly disagree", 5)
                ]
            }
        ],
        "Social": [
            {
                "question": "I enjoy helping others learn and grow.",
                "options": [
                    ("Strongly agree", 35),
                    ("Agree", 30),
                    ("Neutral", 22),
                    ("Disagree", 12),
                    ("Strongly disagree", 5)
                ]
            },
            {
                "question": "I am happiest when I’m collaborating on group projects.",
                "options": [
                    ("Strongly agree", 35),
                    ("Agree", 30),
                    ("Neutral", 22),
                    ("Disagree", 12),
                    ("Strongly disagree", 5)
                ]
            }
        ],
        "Enterprising": [
            {
                "question": "I am confident in leading teams and making decisions.",
                "options": [
                    ("Strongly agree", 35),
                    ("Agree", 30),
                    ("Neutral", 22),
                    ("Disagree", 12),
                    ("Strongly disagree", 5)
                ]
            },
            {
                "question": "I like persuading people to consider new ideas or products.",
                "options": [
                    ("Strongly agree", 35),
                    ("Agree", 30),
                    ("Neutral", 22),
                    ("Disagree", 12),
                    ("Strongly disagree", 5)
                ]
            }
        ],
        "Conventional": [
            {
                "question": "I prefer following structured routines and clear rules.",
                "options": [
                    ("Strongly agree", 35),
                    ("Agree", 30),
                    ("Neutral", 22),
                    ("Disagree", 12),
                    ("Strongly disagree", 5)
                ]
            },
            {
                "question": "I am skilled at managing records and keeping things organized.",
                "options": [
                    ("Strongly agree", 35),
                    ("Agree", 30),
                    ("Neutral", 22),
                    ("Disagree", 12),
                    ("Strongly disagree", 5)
                ]
            }
        ]
    }
}

# Initialize OpenAI client
client = OpenAI(base_url="https://helixmind.online/v1", api_key='helix-4WaTFs3z-dJo_sB5myl2mPOzDPhhWZN7GjuedAUZwGM')

# Create a session state variable to store chat history
if 'messages' not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": "You are a helpful assistant."}]

# Function to send user input or prompt to OpenAI and get response
def get_ai_response(prompt):
    st.session_state.messages.append({"role": "system", "content": prompt})
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=st.session_state.messages
    )
    ai_response = response.choices[0].message.content
    return ai_response

# Function to calculate OCEAN and RIASEC scores
def calculate_scores(selected_answers):
    ocean_scores = {trait: 0 for trait in ["Openness", "Conscientiousness", "Extraversion", "Agreeableness", "Neuroticism"]}
    riasec_scores = {trait: 0 for trait in ["Realistic", "Investigative", "Artistic", "Social", "Enterprising", "Conventional"]}
    
    for trait, answer in selected_answers.items():
        if trait in ocean_scores:
            ocean_scores[trait] += answer
        elif trait in riasec_scores:
            riasec_scores[trait] += answer

    sorted_riasec = sorted(riasec_scores.items(), key=lambda x: x[1], reverse=True)
    top_3_riasec_code = "".join([trait[0] for trait, score in sorted_riasec[:3]])

    return ocean_scores, riasec_scores, top_3_riasec_code

# Store user's answers in a dictionary
selected_answers = {}

# Display OCEAN traits questions
st.markdown("### OCEAN Traits")
for trait, q_data in questions["OCEAN"].items():
    st.markdown(f"**{trait}**")
    selected_answer = st.radio(q_data["question"], options=[opt[0] for opt in q_data["options"]], key=trait)
    selected_answers[trait] = next(score for opt, score in q_data["options"] if opt == selected_answer)

# Display RIASEC traits questions
st.markdown("### RIASEC Traits")
for trait, q_data in questions["RIASEC"].items():
    st.markdown(f"**{trait}**")
    selected_answer = st.radio(q_data["question"], options=[opt[0] for opt in q_data["options"]], key=f"RIASEC_{trait}")
    selected_answers[trait] = next(score for opt, score in q_data["options"] if opt == selected_answer)

# Button to calculate scores
if st.button("Calculate Scores"):
    ocean_scores, riasec_scores, top_3_riasec_code = calculate_scores(selected_answers)
    st.session_state['ocean_scores'] = ocean_scores
    st.session_state['riasec_scores'] = riasec_scores
    st.session_state['top_3_riasec_code'] = top_3_riasec_code

    st.header("Your Results")
    st.subheader("OCEAN Scores")
    for trait_name, score_value in ocean_scores.items():
        st.write(f"{trait_name}: {score_value}")
    st.subheader("RIASEC Scores")
    for trait_name_riasec, score_value_riasec in riasec_scores.items():
        st.write(f"{trait_name_riasec}: {score_value_riasec}")
    st.subheader("Top-3 RIASEC Code:")
    st.write(f"Your top-3 RIASEC code is: {top_3_riasec_code}")

# Button for job recommendations
if st.button("Get My Top 15 Jobs"):
    if 'ocean_scores' in st.session_state and 'top_3_riasec_code' in st.session_state:
        ocean_scores = st.session_state['ocean_scores']
        top_3_riasec_code = st.session_state['top_3_riasec_code']
        formatted_ocean_values_str = ' '.join([str(ocean_scores[key]) for key in ["Openness", "Conscientiousness", "Extraversion", "Agreeableness", "Neuroticism"]])
        generated_prompt_query = f"""
            My RIASEC score is: {top_3_riasec_code}.
            My OCEAN scores are: {formatted_ocean_values_str} (Openness, Conscientiousness,
            Extraversion, Agreeableness, Neuroticism respectively). 40 being the max score.
            Based on these traits, give me a list of the top 20 jobs that would be suitable for me.
            Done make thes jobs too common or vague . . go into more niche categories and fetch interesting titles. 
            Just write the jom titles, no description needed.

            also write a short summary talking about my prsonality and the general areas of work I fit in, such as catagory of career or fields i might be good at.
            """
        with st.spinner('Fetching your top 20 jobs...'):
            ai_response = get_ai_response(generated_prompt_query)
            st.subheader("Your personality fits the following possible occupations....")
            st.write(ai_response)
    else:
        st.error("Please calculate your scores first.")
