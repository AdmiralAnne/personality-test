import streamlit as st
from openai import OpenAI
import pandas as pd
import matplotlib.pyplot as plt

st.header("Psychometric Personality assessment and career matching.")
st.write("Imagine yourself in these scenarios and answer 11 questions to find your -loosely ideal- career path: (beta version 0.2.0)")
# instructions

st.image("https://i.ibb.co/ckDPyRZ/instruct.png", caption="Easy Instructions")


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
# st.sidebar.info("Key Insights on Job Satisfaction and Career Fit Awareness")
st.sidebar.info(
    "A small chart that displays key factors influencing job satisfaction and awareness of career fit, "
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
            "question_1": "You're in a new city. What excites you the most?",
            "options_1": [
                ("Exploring unique places and trying new things.", 18),
                ("Visiting recommended spots with familiar activities.", 15),
                ("Balancing exploration with some routine activities.", 11),
                ("Relaxing in familiar settings and avoiding too much exploring.", 6),
                ("Sticking to routine activities indoors.", 3)
            ],
            "question_2": "How do you approach a new hobby?",
            "options_2": [
                ("Dive in, excited to explore and experiment.", 18),
                ("Try it enthusiastically, with some guidance.", 15),
                ("Experiment cautiously, balancing interest with comfort.", 11),
                ("Stick to small, manageable parts of it.", 6),
                ("Avoid new hobbies, preferring familiar routines.", 3)
            ]
        },
        "Conscientiousness": {
            "question_1": "How do you handle deadlines?",
            "options_1": [
                ("Plan ahead and ensure tasks are done early.", 18),
                ("Work steadily, leaving some time for adjustments.", 15),
                ("Balance deadlines with flexibility for changes.", 11),
                ("Rush near the deadline, but get it done.", 6),
                ("Feel unfazed and improvise as needed.", 3)
            ],
            "question_2": "What’s your work style?",
            "options_2": [
                ("Thorough and detail-oriented, sticking to plans.", 18),
                ("Mostly organized, with room for flexibility.", 15),
                ("Balanced, completing work efficiently but casually.", 11),
                ("Prefer a relaxed approach, focusing on the essentials.", 6),
                ("Spontaneous, relying on last-minute creativity.", 3)
            ]
        },
        "Extraversion": {
            "question_1": "How do you feel in a social gathering?",
            "options_1": [
                ("Energized, chatting with everyone.", 18),
                ("Engaged, joining group conversations.", 15),
                ("Comfortable, connecting with a few people.", 11),
                ("Quiet, sticking to smaller interactions.", 6),
                ("Drained, preferring solitude.", 3)
            ],
            "question_2": "How do you spend your weekends?",
            "options_2": [
                ("Meeting friends or attending events.", 18),
                ("Mixing social activities with downtime.", 15),
                ("Relaxing with a small circle of friends.", 11),
                ("Staying home, enjoying quiet hobbies.", 6),
                ("Completely alone, focusing on personal interests.", 3)
            ]
        },
        "Agreeableness": {
            "question_1": "How do you handle disagreements?",
            "options_1": [
                ("Listen patiently and find common ground.", 18),
                ("Express your view respectfully.", 15),
                ("Stay neutral, avoiding conflict.", 11),
                ("Share your view directly, prioritizing honesty.", 6),
                ("Assert your stance, valuing truth over harmony.", 3)
            ],
            "question_2": "How do you approach teamwork?",
            "options_2": [
                ("Collaborate smoothly, ensuring everyone feels valued.", 18),
                ("Help others while focusing on your tasks.", 15),
                ("Balance personal goals with group needs.", 11),
                ("Work independently within the team.", 6),
                ("Prefer to focus solely on your tasks.", 3)
            ]
        },
        "Neuroticism": {
            "question_1": "How do you react to stress?",
            "options_1": [
                ("Feel overwhelmed but try to manage it.", 18),
                ("Feel anxious but work through it.", 15),
                ("Stay calm with some effort.", 11),
                ("Manage stress well, rarely feeling shaken.", 6),
                ("Remain unaffected, focusing on solutions.", 3)
            ],
            "question_2": "What’s your response to mistakes?",
            "options_2": [
                ("Analyze and feel critical about them.", 18),
                ("Feel disappointed but correct them quickly.", 15),
                ("Recognize and fix them calmly.", 11),
                ("Acknowledge mistakes but avoid overthinking.", 6),
                ("Brush them off, seeing them as learning moments.", 3)
            ]
        }
    },
    "RIASEC": {
        "Realistic": {
            "question_1": "What tasks do you prefer?",
            "options_1": [
                ("Hands-on work like fixing or building.", 18),
                ("Mostly hands-on with some planning.", 15),
                ("Balanced mix of hands-on and desk work.", 11),
                ("Mostly desk-based, less physical.", 6),
                ("Desk work entirely.", 3)
            ],
            "question_2": "What’s your ideal activity?",
            "options_2": [
                ("Outdoor adventures or practical challenges.", 18),
                ("Mix of active tasks and planning.", 15),
                ("Moderate activity with flexible tasks.", 11),
                ("Light activity, avoiding heavy tasks.", 6),
                ("Minimal activity, focusing on ideas.", 3)
            ]
        },
        "Investigative": {
            "question_1": "How do you handle new concepts?",
            "options_1": [
                ("Research in-depth and seek answers.", 18),
                ("Explore when time allows.", 15),
                ("Learn enough to get the gist.", 11),
                ("Focus on practical outcomes.", 6),
                ("Ignore unless necessary.", 3)
            ],
            "question_2": "What’s your approach to problems?",
            "options_2": [
                ("Analyze and experiment with solutions.", 18),
                ("Explore solutions logically.", 15),
                ("Try standard approaches first.", 11),
                ("Solve quickly without overthinking.", 6),
                ("Skip details, preferring quick fixes.", 3)
            ]
        },
        "Artistic": {
            "question_1": "How do you enjoy your free time?",
            "options_1": [
                ("Expressing creativity through art or ideas.", 18),
                ("Mix of creative and structured hobbies.", 15),
                ("Light creativity with routine hobbies.", 11),
                ("Practical hobbies with occasional creativity.", 6),
                ("Fully structured activities.", 3)
            ],
            "question_2": "What motivates you creatively?",
            "options_2": [
                ("Original expression and imagination.", 18),
                ("Exploring creative outlets with guidance.", 15),
                ("Structured creativity with clear goals.", 11),
                ("Occasional creativity within limits.", 6),
                ("Minimal interest in creative work.", 3)
            ]
        },
        "Social": {
            "question_1": "How do you engage with communities?",
            "options_1": [
                ("Actively participate and lead events.", 18),
                ("Support events if time allows.", 15),
                ("Contribute occasionally.", 11),
                ("Observe without much involvement.", 6),
                ("Avoid participation.", 3)
            ],
            "question_2": "How do you handle group work?",
            "options_2": [
                ("Take the lead and guide others.", 18),
                ("Participate actively but prefer not to lead.", 15),
                ("Support quietly while following.", 11),
                ("Engage minimally, focusing on your part.", 6),
                ("Work best individually.", 3)
            ]
        },
        "Enterprising": {
            "question_1": "How do you approach leadership roles?",
            "options_1": [
                ("Take charge and organize confidently.", 18),
                ("Lead when needed, staying adaptable.", 15),
                ("Support leaders but prefer not to lead.", 11),
                ("Avoid leading, focusing on tasks.", 6),
                ("Stay in the background.", 3)
            ],
            "question_2": "How do you feel about taking risks?",
            "options_2": [
                ("Embrace calculated risks for growth.", 18),
                ("Take some risks with careful planning.", 15),
                ("Prefer safe approaches with occasional risks.", 11),
                ("Avoid risks unless necessary.", 6),
                ("Stick to secure, predictable choices.", 3)
            ]
        },
        "Conventional": {
            "question_1": "How do you approach structure?",
            "options_1": [
                ("Create detailed plans and follow them.", 18),
                ("Set flexible plans but stay organized.", 15),
                ("Balance plans with adaptability.", 11),
                ("Prefer minimal structure, working flexibly.", 6),
                ("Avoid structure, working spontaneously.", 3)
            ],
            "question_2": "How do you handle unclear tasks?",
            "options_2": [
                ("Create clarity with structure.", 18),
                ("Organize with some flexibility.", 15),
                ("Adapt to unclear tasks with balance.", 11),
                ("Work around ambiguity.", 6),
                ("Ignore rules, focusing on instinct.", 3)
            ]
        }
    }
}



# Initialize OpenAI client
client = OpenAI(base_url="https://helixmind.online/v1", api_key='helix-4WaTFs3z-dJo_sB5myl2mPOzDPhhWZN7GjuedAUZwGM')

# Create a session state variable to store chat history
if 'messages' not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": ""}]

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
    
    for sub_question, options_key in q_data.items():
        # Display question with a larger font size
        st.markdown(f"<p style='font-size:24px;'>{options_key['question']}</p>", unsafe_allow_html=True)
        
        # Display answer options
        selected_answer = st.radio(
            "", 
            options=[opt[0] for opt in options_key['options']],
            key=f"{trait}_{sub_question}"
        )
        st.divider()
        
        # Store the score for the selected option
        selected_answers[f"{trait}_{sub_question}"] = next(score for opt, score in options_key['options'] if opt == selected_answer)

# Display RIASEC traits questions with similar styling
st.markdown("### RIASEC Traits")

for trait, q_data in questions["RIASEC"].items():
    # Display trait with a smaller font size
    st.markdown(f"<p style='font-size:14px; font-weight:bold;'>{trait}</p>", unsafe_allow_html=True)
    
    for sub_question, options_key in q_data.items():
        # Display question with a larger font size
        st.markdown(f"<p style='font-size:24px;'>{options_key['question']}</p>", unsafe_allow_html=True)
        
        # Display answer options
        selected_answer = st.radio(
            "", 
            options=[opt[0] for opt in options_key['options']],
            key=f"RIASEC_{trait}_{sub_question}"
        )
        st.divider()
        
        # Store the score for the selected option
        selected_answers[f"RIASEC_{trait}_{sub_question}"] = next(score for opt, score in options_key['options'] if opt == selected_answer)

# Output selected answers for debugging purposes (optional)
st.write("Selected Answers:", selected_answers)

#end

# input start 

domains = ["Technology", "Art", "Science", "Education", "Business", "Health", "Sports", "Other"]
selected_domains = st.multiselect(
    label="Select Your Domains or Areas of Interest:",
    options=domains,
    default=None,
    help="You can select multiple domains or areas of interest.",
    label_visibility="visible"
)

# Join selected domains into a string
domain_str = ", ".join(selected_domains) if selected_domains else "None"

# input end

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

            based on: this domain: {domain_str}. If 'other' is Provided, give a general recommendation.

            Organize the jobs neatly acording to domain if provided.

            also write a very crispt and short "30 words" summary talking about: The Industries I might be good at in. Keep it in points only.
            tone: keep it super friendlt and chill.
            """
        with st.spinner('Fetching your top 20 jobs...'):
            ai_response = get_ai_response(generated_prompt_query)
            st.subheader("Your personality fits the following possible occupations....")
            st.write(ai_response)
    else:
        st.error("Please calculate your scores first.")

import streamlit as st

st.divider()
st.divider()
st.divider()
# Expander with Important Links
with st.expander("Important Links"):
    st.markdown("### Sources")
    st.write("[Source Code - Github for this website](https://github.com/AdmiralAnne/personality-test)")
    st.write("[Questionnaire Sources](https://docs.google.com/spreadsheets/d/1qUE0sGZfC5jxx-gi-HfJR0wmeRWJUZS6HexJvWu9agE/edit?usp=sharing)")
    st.write("[Dataset Sources](https://docs.google.com/spreadsheets/d/1wBFU0WdFfEDZGT21f3agZtHEyVInEMC_4maf3zkMsTA/edit?gid=0#gid=0)")
    st.write("[Link to System Architecture / Diagrams](https://excalidraw.com/#json=JCYgsb4EfJPD-aYiywoFR,EIlEyOdZ4OyAN8drdiOEWg)")
    st.write("[Google Colab Notebook](https://colab.research.google.com/drive/1n_qZKStxZpfBBr0pLDm40sLjZ-ifgur2?usp=sharing)")

# Section on Future Prospects
with st.expander("Future Prospects for the Project"):
    st.info(
        """
        - **Enhanced Model Customization**: aim to refine the model, incorporating user feedback.
        - **More Curated Questions**: The questionnaire will be expanded with more nuanced questions.
        - **Guidance for Career Paths**: suggest additional resources to help users explore career paths that align with their interests.
        """
    )

with st.expander("Architecture / Diagrams"):
    st.image("https://i.ibb.co/vmK5tyH/diagram.png", caption="System Architecture")

st.divider()
st.divider()
st.divider()

st.info(
    """
    #### Special thanks to: 
    - **Meet Dudhat - U21CS483 ( Lead developer, Having fun at home in Gujarat)**
    - **Jagadeesh - U21CS464 ( Thin Guy, Likes Research and Coding )**
    - **Dr P Vasuki ( Beloved Guide - Guiding Pillar of our project)**
    - **Kameshwari Ma'am ( Best Mentor award )**
    - **Marjiba - u21cs474 ( Creative Solutions and Designer )**
    """
)
