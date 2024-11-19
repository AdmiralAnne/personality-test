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
            "question_1": {
                "question": "Do you enjoy exploring new ideas and concepts?",
                "options": [("Strongly Agree", 18), ("Agree", 15), ("Neutral", 12), ("Disagree", 6), ("Strongly Disagree", 3)]
            },
            "question_2": {
                "question": "Do you find abstract thinking exciting?",
                "options": [("Strongly Agree", 18), ("Agree", 15), ("Neutral", 12), ("Disagree", 6), ("Strongly Disagree", 3)]
            }
        },
        "Conscientiousness": {
            "question_1": {
                "question": "Do you always strive to meet your goals?",
                "options": [("Strongly Agree", 18), ("Agree", 15), ("Neutral", 12), ("Disagree", 6), ("Strongly Disagree", 3)]
            },
            "question_2": {
                "question": "Do you usually plan your tasks in advance?",
                "options": [("Strongly Agree", 18), ("Agree", 15), ("Neutral", 12), ("Disagree", 6), ("Strongly Disagree", 3)]
            }
        },
        "Extraversion": {
            "question_1": {
                "question": "Do you enjoy being the center of attention in social gatherings?",
                "options": [("Strongly Agree", 18), ("Agree", 15), ("Neutral", 12), ("Disagree", 6), ("Strongly Disagree", 3)]
            },
            "question_2": {
                "question": "Do you feel energized when interacting with others?",
                "options": [("Strongly Agree", 18), ("Agree", 15), ("Neutral", 12), ("Disagree", 6), ("Strongly Disagree", 3)]
            }
        },
        "Agreeableness": {
            "question_1": {
                "question": "Do you often consider the feelings of others before acting?",
                "options": [("Strongly Agree", 18), ("Agree", 15), ("Neutral", 12), ("Disagree", 6), ("Strongly Disagree", 3)]
            },
            "question_2": {
                "question": "Do you avoid conflicts and prefer harmonious interactions?",
                "options": [("Strongly Agree", 18), ("Agree", 15), ("Neutral", 12), ("Disagree", 6), ("Strongly Disagree", 3)]
            }
        },
        "Neuroticism": {
            "question_1": {
                "question": "Do you frequently feel anxious or stressed?",
                "options": [("Strongly Agree", 18), ("Agree", 15), ("Neutral", 12), ("Disagree", 6), ("Strongly Disagree", 3)]
            },
            "question_2": {
                "question": "Do you find it hard to stay calm under pressure?",
                "options": [("Strongly Agree", 18), ("Agree", 15), ("Neutral", 12), ("Disagree", 6), ("Strongly Disagree", 3)]
            }
        }
    },
    "RIASEC": {
        "Realistic": {
            "question_1": {
                "question": "Do you enjoy hands-on work, such as building or repairing things?",
                "options": [("Strongly Agree", 18), ("Agree", 15), ("Neutral", 12), ("Disagree", 6), ("Strongly Disagree", 3)]
            },
            "question_2": {
                "question": "Do you prefer outdoor activities over desk jobs?",
                "options": [("Strongly Agree", 18), ("Agree", 15), ("Neutral", 12), ("Disagree", 6), ("Strongly Disagree", 3)]
            }
        },
        "Investigative": {
            "question_1": {
                "question": "Do you enjoy solving complex problems or puzzles?",
                "options": [("Strongly Agree", 18), ("Agree", 15), ("Neutral", 12), ("Disagree", 6), ("Strongly Disagree", 3)]
            },
            "question_2": {
                "question": "Do you prefer analyzing data over physical tasks?",
                "options": [("Strongly Agree", 18), ("Agree", 15), ("Neutral", 12), ("Disagree", 6), ("Strongly Disagree", 3)]
            }
        },
        "Artistic": {
            "question_1": {
                "question": "Do you enjoy expressing yourself through art or music?",
                "options": [("Strongly Agree", 18), ("Agree", 15), ("Neutral", 12), ("Disagree", 6), ("Strongly Disagree", 3)]
            },
            "question_2": {
                "question": "Do you often seek out creative outlets in your daily life?",
                "options": [("Strongly Agree", 18), ("Agree", 15), ("Neutral", 12), ("Disagree", 6), ("Strongly Disagree", 3)]
            }
        },
        "Social": {
            "question_1": {
                "question": "Do you enjoy helping others achieve their goals?",
                "options": [("Strongly Agree", 18), ("Agree", 15), ("Neutral", 12), ("Disagree", 6), ("Strongly Disagree", 3)]
            },
            "question_2": {
                "question": "Do you feel fulfilled when you assist others in need?",
                "options": [("Strongly Agree", 18), ("Agree", 15), ("Neutral", 12), ("Disagree", 6), ("Strongly Disagree", 3)]
            }
        },
        "Enterprising": {
            "question_1": {
                "question": "Do you enjoy leading teams or projects?",
                "options": [("Strongly Agree", 18), ("Agree", 15), ("Neutral", 12), ("Disagree", 6), ("Strongly Disagree", 3)]
            },
            "question_2": {
                "question": "Do you often seek opportunities to take risks for potential rewards?",
                "options": [("Strongly Agree", 18), ("Agree", 15), ("Neutral", 12), ("Disagree", 6), ("Strongly Disagree", 3)]
            }
        },
        "Conventional": {
            "question_1": {
                "question": "Do you prefer structured tasks with clear guidelines?",
                "options": [("Strongly Agree", 18), ("Agree", 15), ("Neutral", 12), ("Disagree", 6), ("Strongly Disagree", 3)]
            },
            "question_2": {
                "question": "Do you enjoy organizing or managing data or records?",
                "options": [("Strongly Agree", 18), ("Agree", 15), ("Neutral", 12), ("Disagree", 6), ("Strongly Disagree", 3)]
            }
        }
    }
}

# end


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

# start

# Function to calculate OCEAN and RIASEC scores
def calculate_scores(selected_answers):
    # Initialize OCEAN and RIASEC score dictionaries
    ocean_scores = {trait: 0 for trait in ["Openness", "Conscientiousness", "Extraversion", "Agreeableness", "Neuroticism"]}
    riasec_scores = {trait: 0 for trait in ["Realistic", "Investigative", "Artistic", "Social", "Enterprising", "Conventional"]}

    # Define mapping for radio options to numerical scores
    score_mapping_ocean = {
        "Strongly Disagree": 1, "Disagree": 2, "Neutral": 3, "Agree": 4, "Strongly Agree": 5
    }
    score_mapping_riasec = {
        "Not at all": 1, "Somewhat": 2, "Moderately": 3, "Very": 4, "Extremely": 5
    }

    # Iterate through selected answers to calculate scores
    for trait, questions in selected_answers.items():
        if trait in ocean_scores:
            for _, score in questions.items():
                ocean_scores[trait] += score_mapping_ocean[score]
        elif trait in riasec_scores:
            for _, score in questions.items():
                riasec_scores[trait] += score_mapping_riasec[score]

    # Sort RIASEC scores and extract the top-3 traits for the RIASEC code
    sorted_riasec = sorted(riasec_scores.items(), key=lambda x: x[1], reverse=True)
    top_3_riasec_code = "".join([trait[0] for trait, score in sorted_riasec[:3]])

    return ocean_scores, riasec_scores, top_3_riasec_code

# Placeholder for selected answers
selected_answers = {
    "OCEAN": {
        "Openness": {},
        "Conscientiousness": {},
        "Extraversion": {},
        "Agreeableness": {},
        "Neuroticism": {}
    },
    "RIASEC": {
        "Realistic": {},
        "Investigative": {},
        "Artistic": {},
        "Social": {},
        "Enterprising": {},
        "Conventional": {}
    }
}

# Display OCEAN traits questions
st.markdown("### OCEAN Traits")
for trait, questions in selected_answers["OCEAN"].items():
    st.markdown(f"<p style='font-size:14px; font-weight:bold;'>{trait}</p>", unsafe_allow_html=True)
    for sub_question in range(1, 4):  # Example: 3 questions per trait
        question_text = f"{trait} Question {sub_question}?"
        st.markdown(f"<p style='font-size:24px;'>{question_text}</p>", unsafe_allow_html=True)
        selected_answer = st.radio(
            "",
            options=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"],
            key=f"{trait}_q{sub_question}"
        )
        selected_answers["OCEAN"][trait][f"q{sub_question}"] = selected_answer

# Display RIASEC traits questions
st.markdown("### RIASEC Traits")
for trait, questions in selected_answers["RIASEC"].items():
    st.markdown(f"<p style='font-size:14px; font-weight:bold;'>{trait}</p>", unsafe_allow_html=True)
    for sub_question in range(1, 4):  # Example: 3 questions per trait
        question_text = f"{trait} Question {sub_question}?"
        st.markdown(f"<p style='font-size:24px;'>{question_text}</p>", unsafe_allow_html=True)
        selected_answer = st.radio(
            "",
            options=["Not at all", "Somewhat", "Moderately", "Very", "Extremely"],
            key=f"RIASEC_{trait}_q{sub_question}"
        )
        selected_answers["RIASEC"][trait][f"q{sub_question}"] = selected_answer

# Debug output
st.write("Selected Answers:", selected_answers)

# Input domains
domains = ["Technology", "Art", "Science", "Education", "Business", "Health", "Sports", "Other"]
selected_domains = st.multiselect(
    label="Select Your Domains or Areas of Interest:",
    options=domains,
    help="You can select multiple domains or areas of interest.",
)
# Join selected domains into a string
domain_str = ", ".join(selected_domains) if selected_domains else "None"

# Calculate Scores Button
if st.button("Calculate Scores"):
    ocean_scores, riasec_scores, top_3_riasec_code = calculate_scores(selected_answers)
    st.session_state['ocean_scores'] = ocean_scores
    st.session_state['riasec_scores'] = riasec_scores
    st.session_state['top_3_riasec_code'] = top_3_riasec_code

    st.subheader("Top-3 RIASEC Code:")
    st.write(f"Your top-3 RIASEC code is: {top_3_riasec_code}")

# Plot Scores
if 'ocean_scores' in st.session_state and 'riasec_scores' in st.session_state:
    # OCEAN Plot
    fig_ocean, ax1 = plt.subplots(figsize=(8, 5))
    extremes = {
        "Openness": ("Closed", "Open"),
        "Conscientiousness": ("Carefree", "Conscientious"),
        "Extraversion": ("Introvert", "Extrovert"),
        "Agreeableness": ("Assertive", "Agreeable"),
        "Neuroticism": ("Calm", "Anxious")
    }
    for idx, (trait, score) in enumerate(st.session_state['ocean_scores'].items()):
        ax1.plot([0, 40], [idx, idx], 'k-', lw=1)
        ax1.plot(score, idx, 'o', color="skyblue", markersize=8)
        ax1.text(0, idx, extremes[trait][0], va='center', ha='right')
        ax1.text(40, idx, extremes[trait][1], va='center', ha='left')
        ax1.text(score, idx + 0.1, str(score), color="black", ha='center')
    ax1.set_title("OCEAN Personality Traits")
    ax1.set_yticks(range(len(st.session_state['ocean_scores'])))
    ax1.set_yticklabels(list(st.session_state['ocean_scores'].keys()))
    ax1.invert_yaxis()
    st.pyplot(fig_ocean)

    # RIASEC Plot
    fig_riasec, ax2 = plt.subplots(figsize=(8, 5))
    riasec_df = pd.DataFrame(list(st.session_state['riasec_scores'].items()), columns=['Trait', 'Score'])
    bars = riasec_df.plot(kind='barh', x='Trait', y='Score', ax=ax2, color='salmon', legend=False)
    ax2.set_title("RIASEC Career Interest Scores")
    ax2.set_xlabel("Score")
    ax2.set_ylabel("Trait")
    for idx, score in enumerate(riasec_df['Score']):
        ax2.text(score + 1, idx, str(score), color="black", va='center')
    st.pyplot(fig_riasec)
else:
    st.warning("Please calculate your scores first.")

#end

# Input domains
domains = ["Technology", "Art", "Science", "Education", "Business", "Health", "Sports", "Other"]
selected_domains = st.multiselect(
    label="Select Your Domains or Areas of Interest:",
    options=domains,
    help="You can select multiple domains or areas of interest.",
)
# Join selected domains into a string
domain_str = ", ".join(selected_domains) if selected_domains else "None"

# input end

# Calculate Scores Button
if st.button("Calculate Scores"):
    ocean_scores, riasec_scores, top_3_riasec_code = calculate_scores(selected_answers)
    st.session_state['ocean_scores'] = ocean_scores
    st.session_state['riasec_scores'] = riasec_scores
    st.session_state['top_3_riasec_code'] = top_3_riasec_code

    st.subheader("Top-3 RIASEC Code:")
    st.write(f"Your top-3 RIASEC code is: {top_3_riasec_code}")

# Plot Scores
if 'ocean_scores' in st.session_state and 'riasec_scores' in st.session_state:
    # OCEAN Plot
    fig_ocean, ax1 = plt.subplots(figsize=(8, 5))
    extremes = {
        "Openness": ("Closed", "Open"),
        "Conscientiousness": ("Carefree", "Conscientious"),
        "Extraversion": ("Introvert", "Extrovert"),
        "Agreeableness": ("Assertive", "Agreeable"),
        "Neuroticism": ("Calm", "Anxious")
    }
    for idx, (trait, score) in enumerate(st.session_state['ocean_scores'].items()):
        ax1.plot([0, 40], [idx, idx], 'k-', lw=1)
        ax1.plot(score, idx, 'o', color="skyblue", markersize=8)
        ax1.text(0, idx, extremes[trait][0], va='center', ha='right')
        ax1.text(40, idx, extremes[trait][1], va='center', ha='left')
        ax1.text(score, idx + 0.1, str(score), color="black", ha='center')
    ax1.set_title("OCEAN Personality Traits")
    ax1.set_yticks(range(len(st.session_state['ocean_scores'])))
    ax1.set_yticklabels(list(st.session_state['ocean_scores'].keys()))
    ax1.invert_yaxis()
    st.pyplot(fig_ocean)

    # RIASEC Plot
    fig_riasec, ax2 = plt.subplots(figsize=(8, 5))
    riasec_df = pd.DataFrame(list(st.session_state['riasec_scores'].items()), columns=['Trait', 'Score'])
    bars = riasec_df.plot(kind='barh', x='Trait', y='Score', ax=ax2, color='salmon', legend=False)
    ax2.set_title("RIASEC Career Interest Scores")
    ax2.set_xlabel("Score")
    ax2.set_ylabel("Trait")
    for idx, score in enumerate(riasec_df['Score']):
        ax2.text(score + 1, idx, str(score), color="black", va='center')
    st.pyplot(fig_riasec)
else:
    st.warning("Please calculate your scores first.")

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
