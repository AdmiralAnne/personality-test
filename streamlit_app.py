import streamlit as st
from openai import OpenAI

st.header("Answer these 11 questions to find your ideal career path: (beta version 0.1.0)")

# questions.py
questions = {
    "OCEAN": {
        "Openness": {
            "question": "Your approach to new experiences and ideas?",
            "options": [
                ("I love trying new things and exploring new ideas.", 40),
                ("I enjoy new experiences, but I also appreciate familiarity.", 30),
                ("I am mostly comfortable with familiar routines.", 20),
                ("I prefer sticking to what I know best.", 10),
                ("I am cautious and rarely seek new experiences.", 0)
            ]
        },
        "Conscientiousness": {
            "question": "How organized and diligent are you with tasks?",
            "options": [
                ("I am highly organized and very responsible.", 40),
                ("I am usually organized and try to meet my responsibilities.", 30),
                ("I make an effort to stay organized, but I have my moments.", 20),
                ("I tend to be a bit disorganized but get by.", 10),
                ("I prefer a laid-back approach and am not too strict on organization.", 0)
            ]
        },
        "Extraversion": {
            "question": "Describe your comfort level in social settings",
            "options": [
                ("I thrive in social settings and love interacting with people.", 40),
                ("I enjoy socializing but also value some alone time.", 30),
                ("I am comfortable with small groups but avoid big gatherings.", 20),
                ("I prefer spending time alone or with close friends.", 10),
                ("I am very reserved and avoid social settings as much as possible.", 0)
            ]
        },
        "Agreeableness": {
            "question": "Describe your tendency to be kind and cooperative",
            "options": [
                ("I am extremely empathetic and value harmony.", 40),
                ("I am usually kind and cooperative, but set boundaries when needed.", 30),
                ("I try to be agreeable, but I don't mind speaking up.", 20),
                ("I can be competitive and prioritize my needs.", 10),
                ("I am skeptical of others and tend to be assertive.", 0)
            ]
        },
        "Neuroticism": {
            "question": "Can you Describe your emotional stability?",
            "options": [
                ("I am calm and rarely experience negative emotions.", 0),
                ("I am generally stable but sometimes get stressed.", 10),
                ("I have a fair balance, with occasional mood swings.", 20),
                ("I experience anxiety or worry somewhat often.", 30),
                ("I am often anxious, stressed, or worried.", 40)
            ]
        }
    },
    "RIASEC": {
        "Realistic": {
            "question": "How do you feel about: working with tools, equipment, or physical tasks?",
            "options": [
                ("I love working with my hands and using equipment.", 40),
                ("I enjoy physical tasks but also like problem-solving.", 30),
                ("I don’t mind physical tasks occasionally.", 20),
                ("I prefer non-physical tasks.", 10),
                ("I avoid physical tasks as much as possible.", 0)
            ]
        },
        "Investigative": {
            "question": "How do you feel about researching, exploring, or analyzing information?",
            "options": [
                ("I am passionate about researching and exploring ideas.", 40),
                ("I enjoy problem-solving and analyzing data.", 30),
                ("I like some research but prefer hands-on work.", 20),
                ("I don’t mind research occasionally.", 10),
                ("I avoid research or analysis if possible.", 0)
            ]
        },
        "Artistic": {
            "question": "Describe your interest in: creative expression or artistic pursuits?",
            "options": [
                ("I am highly creative and passionate about artistic pursuits.", 40),
                ("I enjoy being creative but also like structure.", 30),
                ("I dabble in creative activities sometimes.", 20),
                ("I am not particularly interested in creative activities.", 10),
                ("I avoid artistic or creative activities.", 0)
            ]
        },
        "Social": {
            "question": "Describe your preference for: helping or teaching others.",
            "options": [
                ("I find great fulfillment in helping others.", 40),
                ("I enjoy helping others when I can.", 30),
                ("I sometimes help others, but it's not a main priority.", 20),
                ("I rarely help others unless needed.", 10),
                ("I prefer focusing on my own tasks and interests.", 0)
            ]
        },
        "Enterprising": {
            "question": "Describe your tendency to lead or persuade others?",
            "options": [
                ("I love taking charge and influencing others.", 40),
                ("I enjoy leadership but also value teamwork.", 30),
                ("I prefer a mix of leading and following.", 20),
                ("I am not particularly interested in leadership roles.", 10),
                ("I avoid taking charge and prefer to be in the background.", 0)
            ]
        },
        "Conventional": {
            "question": "How would you describe your approach to organizing or managing details?",
            "options": [
                ("I am highly organized and detail-oriented.", 40),
                ("I enjoy organizing but like flexibility too.", 30),
                ("I can manage details but don’t prioritize it.", 20),
                ("I prefer focusing on big-picture tasks.", 10),
                ("I avoid detail-oriented or organizational tasks.", 0)
            ]
        }
    }
}

# Define a function to calculate and display scores
def calculate_scores(selected_answers):
    # Initialize scores for each trait
    ocean_scores = {"Openness": 0, "Conscientiousness": 0, "Extraversion": 0, "Agreeableness": 0, "Neuroticism": 0}
    riasec_scores = {"Realistic": 0, "Investigative": 0, "Artistic": 0, "Social": 0, "Enterprising": 0, "Conventional": 0}
    
    # Calculate scores based on the selected answers
    for trait, answer in selected_answers.items():
        if trait in ocean_scores:
            ocean_scores[trait] += answer
        elif trait in riasec_scores:
            riasec_scores[trait] += answer

    # Generate the RIASEC code by finding the top 3 traits
    sorted_riasec = sorted(riasec_scores.items(), key=lambda x: x[1], reverse=True)
    top_3_riasec_code = "".join([trait[0] for trait, score in sorted_riasec[:3]])  # Take initials of top 3

    return ocean_scores, riasec_scores, top_3_riasec_code

# Store user's answers in a dictionary
selected_answers = {}

# Display questions for OCEAN traits
st.markdown("### OCEAN Traits")  # Smaller heading
for trait, q_data in questions["OCEAN"].items():
    st.markdown(f"**{trait}**")  # Trait name bolded
    # Display question in bold
    st.markdown(f"#### {q_data['question']}")
    selected_answer = st.radio(q_data["question"], options=[opt[0] for opt in q_data["options"]], key=trait)
    
    # Store the selected score for each trait
    selected_answers[trait] = next(score for opt, score in q_data["options"] if opt == selected_answer)

# Display questions for RIASEC traits
st.markdown("### RIASEC Traits")  # Smaller heading
for trait, q_data in questions["RIASEC"].items():
    st.markdown(f"**{trait}**")  # Trait name bolded
    # Display question in bold
    st.markdown(f"#### {q_data['question']}")
    selected_answer = st.radio(q_data["question"], options=[opt[0] for opt in q_data["options"]], key=trait)
    
    # Store the selected score for each trait
    selected_answers[trait] = next(score for opt, score in q_data["options"] if opt == selected_answer)


# Button to submit and display results
if st.button("Calculate Scores"):
    ocean_scores, riasec_scores, top_3_riasec_code = calculate_scores(selected_answers)

    # Display the OCEAN scores
    st.header("Your Results")
    st.subheader("OCEAN Scores")
    for trait, score in ocean_scores.items():
        st.write(f"{trait}: {score}")

    # Display the RIASEC scores
    st.subheader("RIASEC Scores")
    for trait, score in riasec_scores.items():
        st.write(f"{trait}: {score}")

    # Display the top 3 RIASEC code
    st.subheader("Top 3 RIASEC Code")
    st.write(f"Your top 3 RIASEC code is: {top_3_riasec_code}")


# Initialize OpenAI client
client = OpenAI(base_url="https://helixmind.online/v1", api_key='helix-4WaTFs3z-dJo_sB5myl2mPOzDPhhWZN7GjuedAUZwGM')

# Create a session state variable to store chat history
if 'messages' not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": "You are a helpful assistant."}]

# Function to send user input or prompt to OpenAI and get response
def get_ai_response(prompt):
    # Append system message with the generated prompt/query for job recommendations
    st.session_state.messages.append({"role": "system", "content": prompt})

    # Get the response from the OpenAI model
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  
        messages=st.session_state.messages
    )

    # Extract and return AI's response content
    ai_response = response.choices[0].message.content
    
    # Clear messages after each request if needed, but keep initial system instruction.
    return ai_response

# Function to calculate OCEAN and RIASEC scores
def calculate_scores(selected_answers):
    ocean_scores = {"Openness": 0, "Conscientiousness": 0, "Extraversion": 0, 
                    "Agreeableness": 0, "Neuroticism": 0}
    
    riasec_scores = {"Realistic": 0, "Investigative": 0, "Artistic": 0,
                     "Social": 0, "Enterprising": 0, "Conventional": 0}
    
    for trait, answer in selected_answers.items():
        if trait in ocean_scores:
            ocean_scores[trait] += answer
        elif trait in riasec_scores:
            riasec_scores[trait] += answer

    sorted_riasec = sorted(riasec_scores.items(), key=lambda x: x[1], reverse=True)
    
    top_3_riasec_code = "".join([trait[0] for trait, score in sorted_riasec[:3]])

    return ocean_scores, riasec_scores, top_3_riasec_code


# Store user's answers in a dictionary during form submission.
selected_answers = {}

# Display OCEAN traits questions and collect responses.
st.markdown("### OCEAN Traits")
for trait, q_data in questions["OCEAN"].items():
    st.markdown(f"**{trait}**")
    
    selected_answer = st.radio(q_data["question"], options=[opt[0] for opt in q_data["options"]], key=trait)
    
    selected_answers[trait] = next(score for opt, score in q_data["options"] if opt == selected_answer)

# Display RIASEC traits questions and collect responses.
st.markdown("### RIASEC Traits")
for trait, q_data in questions["RIASEC"].items():
    st.markdown(f"**{trait}**")

    selected_answer = st.radio(q_data["question"], options=[opt[0] for opt in q_data["options"]], key=trait)
    
    selected_answers[trait] = next(score for opt, score in q_data["options"] if opt == selected_answer)


# Button that calculates scores when clicked.
if st.button("Calculate Scores"):
    
   # Call function to calculate scores based on user answers.
   ocean_scores, riasec_scores, top_3_riasec_code = calculate_scores(selected_answers)

   # Display calculated OCEAN & RIASEC scores along with Top-3 RIASEC code.
   st.header("Your Results")
   
   st.subheader("OCEAN Scores")
   for trait_name, score_value in ocean_scores.items():
       st.write(f"{trait_name}: {score_value}")

   st.subheader("RIASEC Scores")
   for trait_name_riasec , score_value_riasec in riasec_scores.items():
       st.write(f"{trait_name_riasec }: {score_value_riasec }")

   st.subheader("Top-3 RIASEC Code:")
   st.write(f"Your top-3 RIASEC code is: {top_3_riasec_code}")


if 'ocean_scores' in locals() and 'top_3_riasec_code' in locals(): 
        
    if st.button("Get My Top 15 Jobs"):
            
        ### Generate prompt text dynamically based on calculated scores ###
           
        # Format Ocean values as space-separated string (e.g., '30 40 ...')
        formatted_ocean_values_str = ' '.join([str(ocean_scores[key]) 
                                               for key in ["Openness", "Conscientiousness",
                                                           "Extraversion", "Agreeableness", "Neuroticism"]])
        
        # Construct Prompt To Send GPT-based Model Query String
        generated_prompt_query = f"""
            My RIASEC score is: {top_3_riasec_code}.
            My OCEAN scores are: {formatted_ocean_values_str} (Openness, Conscientiousness,
            Extraversion, Agreeableness, Neuroticism respectively).
            Based on these traits, give me a list of the top 15 jobs that would be suitable for me.
        """
        
        with st.spinner('Fetching your top 15 jobs...'):
            try:
                # Get AI response by sending this prompt to OpenAI API
                ai_response = get_ai_response(generated_prompt_query)
                
                # Display AI's output (the list of jobs)
                st.subheader("Top 15 Job Recommendations")
                st.write(ai_response)
                
            except Exception as e:
                st.error(f"Error fetching job recommendations: {str(e)}")
