import streamlit as st
from openai import OpenAI

st.header("Answer these 11 questions to find your ideal career path: (beta version 0.2.0)")

# questions.py
questions = {
    "OCEAN": {
        "Openness": {
            "question": "How do you feel about trying new experiences and ideas?",
            "options": [
                ("I am always excited to try new things and explore new ideas.", 35),
                ("I usually enjoy new experiences, but I appreciate some familiar things too.", 30),
                ("I am comfortable with new things, but I prefer a balance.", 22),
                ("I like sticking to what I know best.", 12),
                ("I am cautious and rarely seek new experiences.", 5)
            ]
        },
        "Conscientiousness": {
            "question": "How would you describe your approach to being organized and responsible?",
            "options": [
                ("I am very organized and always meet my responsibilities.", 35),
                ("I am usually organized and try to stay on top of things.", 30),
                ("I try to stay organized but sometimes struggle.", 22),
                ("I am somewhat disorganized but manage to get by.", 12),
                ("I prefer a relaxed approach and don’t stress much about organization.", 5)
            ]
        },
        "Extraversion": {
            "question": "How do you feel in social situations?",
            "options": [
                ("I love being around people and thrive in social settings.", 35),
                ("I enjoy socializing but also appreciate some alone time.", 30),
                ("I am comfortable in small groups but avoid large gatherings.", 22),
                ("I prefer spending time alone or with just a few close friends.", 12),
                ("I am very reserved and avoid social settings as much as possible.", 5)
            ]
        },
        "Agreeableness": {
            "question": "How would you describe your level of kindness and cooperation?",
            "options": [
                ("I am very empathetic and always aim for harmony.", 35),
                ("I am usually kind and cooperative but set boundaries when needed.", 30),
                ("I try to be agreeable, but I speak up when necessary.", 22),
                ("I can be competitive and prioritize my own needs.", 12),
                ("I am skeptical of others and tend to be assertive.", 5)
            ]
        },
        "Neuroticism": {
            "question": "How would you describe your emotional stability?",
            "options": [
                ("I am calm and rarely experience negative emotions.", 5),
                ("I am generally stable but get stressed from time to time.", 12),
                ("I have a good balance but experience occasional mood swings.", 22),
                ("I feel anxious or worried somewhat often.", 30),
                ("I often experience anxiety, stress, or worry.", 35)
            ]
        }
    },
    "RIASEC": {
        "Realistic": {
            "question": "Do you enjoy working with tools, equipment, or doing hands-on tasks?",
            "options": [
                ("I love working with my hands and using tools or equipment.", 35),
                ("I enjoy hands-on tasks but like problem-solving too.", 30),
                ("I don’t mind hands-on work occasionally.", 22),
                ("I prefer tasks that don’t involve physical work.", 12),
                ("I avoid hands-on or physical tasks when possible.", 5)
            ]
        },
        "Investigative": {
            "question": "Do you enjoy researching or analyzing information?",
            "options": [
                ("I am very interested in researching and exploring new ideas.", 35),
                ("I like problem-solving and analyzing data.", 30),
                ("I do some research, but I prefer more practical tasks.", 22),
                ("I don’t mind occasional research tasks.", 12),
                ("I avoid research or analysis if I can.", 5)
            ]
        },
        "Artistic": {
            "question": "Do you enjoy creative activities and artistic expression?",
            "options": [
                ("I am very creative and enjoy artistic activities.", 35),
                ("I like being creative but need some structure.", 30),
                ("I engage in creative activities from time to time.", 22),
                ("I don’t have much interest in creative pursuits.", 12),
                ("I avoid artistic or creative activities.", 5)
            ]
        },
        "Social": {
            "question": "Do you enjoy helping or teaching others?",
            "options": [
                ("I find great fulfillment in helping and teaching others.", 35),
                ("I enjoy helping others when possible.", 30),
                ("I sometimes help others, but it’s not a main focus for me.", 22),
                ("I rarely help others unless necessary.", 12),
                ("I prefer focusing on my own tasks and interests.", 5)
            ]
        },
        "Enterprising": {
            "question": "Do you like to lead or persuade others?",
            "options": [
                ("I love taking the lead and influencing people.", 35),
                ("I enjoy leading but also value collaboration.", 30),
                ("I like a mix of leading and following.", 22),
                ("I’m not very interested in leadership roles.", 12),
                ("I avoid taking charge and prefer staying in the background.", 5)
            ]
        },
        "Conventional": {
            "question": "How do you feel about organizing or managing details?",
            "options": [
                ("I am very organized and detail-oriented.", 35),
                ("I like organizing but also appreciate flexibility.", 30),
                ("I manage details but don’t prioritize it highly.", 22),
                ("I prefer focusing on the big picture.", 12),
                ("I avoid detail-oriented tasks whenever possible.", 5)
            ]
        }
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
