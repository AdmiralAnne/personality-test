import streamlit as st
from openai import OpenAI
import pandas as pd
import matplotlib.pyplot as plt

st.header("Answer these 11 questions to find your ideal career path: (beta version 0.2.0)")


# sidebar

# Data for visualization
vis = {
    "Metric": [
        "Prefer jobs aligned with interests",
        "Report meaningful work as essential",
        "Remain in jobs that don't fit due to security",
        "Satisfaction influenced by income beyond threshold",
        "Find their jobs meaningful overall"
    ],
    "Percentage (%)": [58, 70, 36, 20, 36]
}

df_sb = pd.DataFrame(vis)

# Sidebar

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Data for visualization
vis = {
    "Metric": [
        "Prefer jobs aligned with interests",
        "Report meaningful work as essential",
        "Remain in jobs that don't fit due to security",
        "Satisfaction influenced by income beyond threshold",
        "Find their jobs meaningful overall"
    ],
    "Percentage (%)": [58, 70, 36, 20, 36]
}

df_sb = pd.DataFrame(vis)

# Sidebar Content
st.sidebar.title("Career Satisfaction Insights")
st.sidebar.info("Key Insights on Job Satisfaction and Career Fit Awareness")
st.sidebar.write(
    "This chart displays key factors influencing job satisfaction and awareness of career fit, "
    "based on recent studies and surveys."
)

# Horizontal bar chart in the sidebar
fig, ax = plt.subplots(figsize=(5, 3))
ax.barh(df_sb['Metric'], df_sb['Percentage (%)'], color=['#4caf50', '#2196f3', '#ff9800', '#e91e63', '#9c27b0'])
ax.set_xlabel('Percentage (%)')
ax.set_title('Key Findings on Job Satisfaction and Career Fit Awareness')
for i, (value, label) in enumerate(zip(df_sb['Percentage (%)'], df_sb['Metric'])):
    ax.text(value + 1, i, f"{value}%", va='center')  # Add labels to each bar

# Display the chart in the sidebar
st.sidebar.pyplot(fig)

# Summary
st.sidebar.write("""
    - **58%** prefer roles aligned with their strengths and interests.
    - **70%** emphasize the importance of meaningful work over higher income.
    - **36%** stay in roles that don’t align with personal values for security reasons.
    - **20%** show limited satisfaction increase with income beyond a certain point.
    - **36%** find their roles meaningful, suggesting a disconnect between roles and values.
""")

# links

# Add sources with prominent display
st.sidebar.info(
    "🔗 LINKS:\n"
    "\n [How Americans View Their Jobs](https://www.pewresearch.org/social-trends/2023/03/30/how-americans-view-their-jobs/)\n\n"
    "\n [More Insights on American Job Satisfaction](https://www.pewresearch.org/social-trends/2023/03/30/how-americans-view-their-jobs/)"
)

# sidebar

# questions.py
questions = {
    "OCEAN": {
        "Openness": {
            "question": "You find yourself in a new city with some free time. What are you most likely to do?",
            "options": [
                ("Explore the lesser-known neighborhoods and try new activities.", 35),
                ("Visit a few recommended spots but stick to familiar activities.", 30),
                ("Balance some exploring with some relaxation in familiar places.", 22),
                ("Find a comfortable, familiar place to relax and avoid exploring too much.", 12),
                ("Stay in, preferring the comfort of routine activities.", 5)
            ]
        },
        "Conscientiousness": {
            "question": "You have an upcoming deadline for an important project, but your friends invite you out. How do you handle this?",
            "options": [
                ("Politely decline, prioritizing your project to ensure it's done thoroughly.", 35),
                ("Set aside time to work but try to join for a little while.", 30),
                ("Try to balance your project and going out, even if it means a bit less sleep.", 22),
                ("Go out and plan to catch up on work afterward, even if rushed.", 12),
                ("Accept the invite, enjoying spontaneity, and complete the project as best you can.", 5)
            ]
        },
        "Extraversion": {
            "question": "You’re at a gathering where you don’t know many people. How do you respond?",
            "options": [
                ("Dive into the crowd, starting conversations with as many people as possible.", 35),
                ("Approach a few groups, joining in and sharing stories.", 30),
                ("Chat with one or two people you know or sit back and observe.", 22),
                ("Find a quieter spot to engage with only one or two people.", 12),
                ("Prefer to keep to yourself and observe rather than actively engaging.", 5)
            ]
        },
        "Agreeableness": {
            "question": "A friend has a strong opinion about a topic, but you disagree. How do you handle the situation?",
            "options": [
                ("Listen and respond kindly, focusing on understanding their perspective.", 35),
                ("Acknowledge their points while gently sharing your view.", 30),
                ("Consider their side but stay neutral in sharing your opinion.", 22),
                ("Offer your differing perspective with minimal compromise.", 12),
                ("Challenge their view, preferring honesty over harmony.", 5)
            ]
        },
        "Neuroticism": {
            "question": "You’ve made a minor mistake at work. How do you feel and respond?",
            "options": [
                ("Worry and analyze the mistake, feeling self-critical.", 35),
                ("Feel disappointed but work on fixing it quickly.", 30),
                ("Recognize the error, feeling mildly affected but moving on.", 22),
                ("Acknowledge it but feel little stress, seeing it as a small error.", 12),
                ("Remain calm, viewing it as a learning opportunity without worry.", 5)
            ]
        }
    },
    "RIASEC": {
        "Realistic": {
            "question": "You’re presented with two tasks: one involving hands-on work and the other requiring desk research. Which do you prefer?",
            "options": [
                ("Eagerly choose the hands-on work.", 35),
                ("Prefer hands-on tasks but are open to balancing both.", 30),
                ("Choose based on the task’s impact, whether hands-on or research-based.", 22),
                ("Lean towards research but are open to a mix.", 12),
                ("Opt for the research, preferring to avoid physical tasks.", 5)
            ]
        },
        "Investigative": {
            "question": "You encounter an unfamiliar concept. How do you handle it?",
            "options": [
                ("Dive into research, seeking detailed understanding and answers.", 35),
                ("Look into it as time allows, appreciating learning.", 30),
                ("Seek general understanding and move on.", 22),
                ("Prefer to rely on familiar knowledge, avoiding in-depth research.", 12),
                ("Avoid focusing on it, favoring practical solutions over research.", 5)
            ]
        },
        "Artistic": {
            "question": "You have some free time. How would you most enjoy spending it?",
            "options": [
                ("Working on a creative project, expressing yourself through art or writing.", 35),
                ("Exploring a creative activity but also enjoying structured hobbies.", 30),
                ("Balancing creativity with other, more routine hobbies.", 22),
                ("Prefer practical tasks over creativity, only engaging occasionally.", 12),
                ("Enjoy structured activities without creative elements.", 5)
            ]
        },
        "Social": {
            "question": "A community group is seeking volunteers to help organize an event. What is your response?",
            "options": [
                ("Immediately volunteer, excited to engage and support others.", 35),
                ("Offer help if time allows, appreciating group activities.", 30),
                ("Join the group but prefer smaller, specific tasks.", 22),
                ("Join as an observer but prefer minimal involvement.", 12),
                ("Avoid participating, preferring individual activities.", 5)
            ]
        },
        "Enterprising": {
            "question": "You’re in a meeting where a new project leader needs to be chosen. How do you react?",
            "options": [
                ("Step up as a leader, eager to guide the team.", 35),
                ("Volunteer, interested in organizing and leading parts of the project.", 30),
                ("Offer support but prefer not to lead.", 22),
                ("Avoid leadership roles, focusing on following the plan.", 12),
                ("Prefer staying in the background and avoid taking charge.", 5)
            ]
        },
        "Conventional": {
            "question": "You’re working on a task that lacks clear guidelines. What do you do?",
            "options": [
                ("Create a structure for yourself, setting up steps and organization.", 35),
                ("Feel comfortable structuring tasks but can be flexible.", 30),
                ("Prefer a balance of structure with some flexibility.", 22),
                ("Struggle with setting up guidelines, preferring more flexibility.", 12),
                ("Avoid structure, working best without specific rules or steps.", 5)
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
        model="gpt-4o",
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

# start
# Display OCEAN traits questions with larger question text and smaller trait label
st.markdown("### OCEAN Traits")
for trait, q_data in questions["OCEAN"].items():
    # Display trait with a smaller font size
    st.markdown(f"<p style='font-size:14px; font-weight:bold;'>{trait}</p>", unsafe_allow_html=True)
    
    # Display question with a larger font size
    st.markdown(f"<p style='font-size:24px;'>{q_data['question']}</p>", unsafe_allow_html=True)
    
    # Display answer options
    selected_answer = st.radio(
        "", 
        options=[opt[0] for opt in q_data["options"]],
        key=trait
    )
    st.divider()
    selected_answers[trait] = next(score for opt, score in q_data["options"] if opt == selected_answer)

# Display RIASEC traits questions with similar styling
st.markdown("### RIASEC Traits")
for trait, q_data in questions["RIASEC"].items():
    # Display trait with a smaller font size
    st.markdown(f"<p style='font-size:14px; font-weight:bold;'>{trait}</p>", unsafe_allow_html=True)
    
    # Display question with a larger font size
    st.markdown(f"<p style='font-size:24px;'>{q_data['question']}</p>", unsafe_allow_html=True)
    
    # Display answer options
    selected_answer = st.radio(
        "", 
        options=[opt[0] for opt in q_data["options"]],
        key=f"RIASEC_{trait}"
    )
    st.divider()
    selected_answers[trait] = next(score for opt, score in q_data["options"] if opt == selected_answer)
#end

# Button to calculate scores
if st.button("Calculate Scores"):
    ocean_scores, riasec_scores, top_3_riasec_code = calculate_scores(selected_answers)
    st.session_state['ocean_scores'] = ocean_scores
    st.session_state['riasec_scores'] = riasec_scores
    st.session_state['top_3_riasec_code'] = top_3_riasec_code

    #st.header("Your Results")
    #st.subheader("OCEAN Scores")
    #for trait_name, score_value in ocean_scores.items():
    #    st.write(f"{trait_name}: {score_value}")
    #st.subheader("RIASEC Scores")
    #for trait_name_riasec, score_value_riasec in riasec_scores.items():
    #    st.write(f"{trait_name_riasec}: {score_value_riasec}")
    st.subheader("Top-3 RIASEC Code:")
    st.write(f"Your top-3 RIASEC code is: {top_3_riasec_code}")

# Check if scores are available before plotting
if 'ocean_scores' in st.session_state and 'riasec_scores' in st.session_state:
    ocean_df = pd.DataFrame(list(st.session_state['ocean_scores'].items()), columns=['Trait', 'Score'])
    riasec_df = pd.DataFrame(list(st.session_state['riasec_scores'].items()), columns=['Trait', 'Score'])
    
    # Define trait labels for the OCEAN plot extremes
    extremes = {
        "Openness": ("Closed", "Open"),
        "Conscientiousness": ("Carefree", "Conscientious"),
        "Extraversion": ("Introvert", "Extrovert"),
        "Agreeableness": ("Assertive", "Agreeable"),
        "Neuroticism": ("Calm", "Anxious")
    }
    
    # Plot OCEAN traits as horizontal lines with markers for scores
    fig_ocean, ax1 = plt.subplots(figsize=(8, 5))
    for idx, (trait, score) in enumerate(st.session_state['ocean_scores'].items()):
        ax1.plot([0, 40], [idx, idx], 'k-', lw=1)  # Horizontal line from 0 to 40
        ax1.plot(score, idx, 'o', color="skyblue", markersize=8)  # Plot score as a dot
        ax1.text(0, idx, extremes[trait][0], va='center', ha='right')  # Left label
        ax1.text(40, idx, extremes[trait][1], va='center', ha='left')  # Right label
        ax1.text(score, idx + 0.1, str(score), color="black", ha='center')  # Score label above the dot

    # Customize OCEAN plot
    ax1.set_title("OCEAN Personality Traits")
    ax1.set_yticks(range(len(st.session_state['ocean_scores'])))
    ax1.set_yticklabels(list(st.session_state['ocean_scores'].keys()))
    ax1.set_xlim(-5, 45)
    ax1.set_xticks([])  # Remove x-axis ticks for cleanliness
    ax1.invert_yaxis()  # Invert y-axis to match question order
    ax1.grid(False)  # Remove grid for a cleaner look

    # Display the OCEAN plot
    st.pyplot(fig_ocean)

    # Plot RIASEC traits as a bar chart
    fig_riasec, ax2 = plt.subplots(figsize=(8, 5))
    bars = riasec_df.plot(kind='barh', x='Trait', y='Score', ax=ax2, color='salmon', legend=False)
    ax2.set_title("RIASEC Career Interest Scores")
    ax2.set_xlabel("Score")
    ax2.set_ylabel("Trait")

    # Add score labels above each bar
    for idx, score in enumerate(riasec_df['Score']):
        ax2.text(score + 1, idx, str(score), color="black", va='center')  # Score label above each bar

    # Display the RIASEC plot
    st.pyplot(fig_riasec)
else:
    st.warning("Please calculate your scores first by clicking the 'Calculate Scores' button.")

#chart

# Create an expander
with st.expander("Read more about Each Trait"):
    # Display the image inside the expander
    st.image("https://i.ibb.co/MkNmm31/chart1.jpg", caption="OCEAN Traits Image")
    st.image("https://i.ibb.co/SXxHm97/chart2.jpg", caption="RIASEC Traits Image")

# links: https://i.ibb.co/MkNmm31/chart1.jpg
# https://i.ibb.co/SXxHm97/chart2.jpg

# chart

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
            Don't make thes jobs too vague . . go into more niche categories and fetch interesting titles. 
            Just write the job titles, no description needed.

            also write a very crispt and short "40 words" summary talking about my prsonality and the general areas of work I fit in, such as catagory of career or fields i might be good at.
            tone: keep it super friendlt and chill.
            """
        with st.spinner('Fetching your top 20 jobs...'):
            ai_response = get_ai_response(generated_prompt_query)
            st.subheader("Your personality fits the following possible occupations....")
            st.write(ai_response)
    else:
        st.error("Please calculate your scores first.")
