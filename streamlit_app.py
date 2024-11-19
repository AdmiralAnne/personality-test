import streamlit as st
from openai import OpenAI
import pandas as pd
import matplotlib.pyplot as plt
import os

st.header("PSYCHOANALYTIC PERSONALITY ASSESSMENT AND CAREER MATCHING")
st.write("Answer these 22 questions to find your -loosely ideal- career path: (beta version 0.9.0)")
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


# start of questions.py
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

# end of questions

# Initialize OpenAI client
# api_key = os.getenv("helix-4WaTFs3z-dJo_sB5myl2mPOzDPhhWZN7GjuedAUZwGM")  # Store your key in an environment variable for security
client = OpenAI(base_url="https://helixmind.online/v1", api_key='helix-4WaTFs3z-dJo_sB5myl2mPOzDPhhWZN7GjuedAUZwGM')

# Create a session state variable to store chat history
if 'messages' not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": "You are a helpful assistant."}]

# Function to send user input or prompt to OpenAI and get response
def get_ai_response(prompt):
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    try:
        response = client.chat.completions.create(
            model="gpt-4",  # Ensure the correct model name is used
            messages=st.session_state.messages
        )
        ai_response = response.choices[0].message.content
        st.session_state.messages.append({"role": "assistant", "content": ai_response})
        return ai_response
    except Exception as e:
        st.error(f"Error: {e}")
        return "Sorry, I couldn't process your request at the moment."

# end of open ai client code


# start of calc function

# Function to calculate OCEAN and RIASEC scores based on selected answers
def calculate_scores(selected_answers):
    ocean_scores = {trait: 0 for trait in ["Openness", "Conscientiousness", "Extraversion", "Agreeableness", "Neuroticism"]}
    riasec_scores = {trait: 0 for trait in ["Realistic", "Investigative", "Artistic", "Social", "Enterprising", "Conventional"]}

    # Calculate the scores based on the selected answers
    for trait, questions_data in selected_answers.items():
        for trait_name, answers in questions_data.items():
            for question_key, selected_answer in answers.items():
                # Get the score for the selected answer
                for option, score in questions[trait][trait_name][question_key]["options"]:
                    if option == selected_answer:
                        if trait == "OCEAN":
                            ocean_scores[trait_name] += score
                        else:
                            riasec_scores[trait_name] += score
                        
    # Sort RIASEC scores and extract the top 3
    sorted_riasec = sorted(riasec_scores.items(), key=lambda x: x[1], reverse=True)
    top_3_riasec_code = "".join([trait[0] for trait, score in sorted_riasec[:3]])

    return ocean_scores, riasec_scores, top_3_riasec_code

# Placeholder for user answers
selected_answers = {
    "OCEAN": {trait: {} for trait in ["Openness", "Conscientiousness", "Extraversion", "Agreeableness", "Neuroticism"]},
    "RIASEC": {trait: {} for trait in ["Realistic", "Investigative", "Artistic", "Social", "Enterprising", "Conventional"]}
}

# Collect user input for OCEAN traits
st.markdown("### OCEAN Traits")
for trait in selected_answers["OCEAN"]:
    st.markdown(f"#### {trait}")
    for q, question_data in questions["OCEAN"][trait].items():
        question_text = question_data["question"]
        options = [option for option, _ in question_data["options"]]
        selected_answers["OCEAN"][trait][q] = st.radio(question_text, options, key=f"{trait}_{q}")

# Collect user input for RIASEC traits
st.markdown("### RIASEC Traits")
for trait in selected_answers["RIASEC"]:
    st.markdown(f"#### {trait}")
    for q, question_data in questions["RIASEC"][trait].items():
        question_text = question_data["question"]
        options = [option for option, _ in question_data["options"]]
        selected_answers["RIASEC"][trait][q] = st.radio(question_text, options, key=f"RIASEC_{trait}_{q}")

# Calculate scores based on user input
ocean_scores, riasec_scores, top_3_riasec_code = calculate_scores(selected_answers)

# Display scores for debugging
# st.write("OCEAN Scores:", ocean_scores)
# st.write("RIASEC Scores:", riasec_scores)
# st.write("Top 3 RIASEC Code:", top_3_riasec_code)

# Input domains
domains = [
    "Technology", "Art", "Science", "Education", "Business", "Health", 
    "Sports", "Other", "Engineering", "Psychology", "Literature", "Music", 
    "Design", "Law", "Environmental Studies", "History", "Philosophy", 
    "Politics", "Marketing", "Finance", "Agriculture", "Hospitality", 
    "Social Work", "Human Resources", "Architecture", "Travel", "Media", 
    "Entertainment", "Non-Profit", "Gaming", "Journalism", "Manufacturing", 
    "Automotive", "Retail", "Culinary Arts"
]

selected_domains = st.multiselect(
    label="Select Your Domains or Areas of Interest:",
    options=domains,
    help="You can select multiple domains or areas of interest.",
)

# Join selected domains into a string
domain_str = ", ".join(selected_domains) if selected_domains else "None"

# Display selected domains
st.write(f"Selected Domains of Interest: {domain_str}")


# Add a button to calculate and display results
if st.button('Calculate and Show Results'):
    # Calculate scores based on user input
    ocean_scores, riasec_scores, top_3_riasec_code = calculate_scores(selected_answers)

    # Store the scores in session state
    st.session_state.ocean_scores = ocean_scores
    st.session_state.riasec_scores = riasec_scores
    st.session_state.top_3_riasec_code = top_3_riasec_code

    # Display the top 3 RIASEC codes
    st.write(f"Top 3 RIASEC Codes: {top_3_riasec_code}")
    
    # Create OCEAN graph and save to session state
    fig_ocean, ax_ocean = plt.subplots(figsize=(8, 5))
    ocean_labels = list(ocean_scores.keys())
    ocean_values = list(ocean_scores.values())

    # Bar chart for OCEAN scores
    bars_ocean = ax_ocean.bar(ocean_labels, ocean_values, color='skyblue')

    # Add labels on top of each bar for OCEAN scores
    for bar in bars_ocean:
        yval = bar.get_height()
        ax_ocean.text(bar.get_x() + bar.get_width() / 2, yval + 1, round(yval, 1), ha='center', va='bottom', fontsize=10)

    # Set axis limits and labels for OCEAN chart
    ax_ocean.set_ylim(0, 40)  # Maximum score of 40
    ax_ocean.set_title("OCEAN Scores", fontsize=14, fontweight='bold')
    ax_ocean.set_xlabel("Trait", fontsize=12)
    ax_ocean.set_ylabel("Score", fontsize=12)
    ax_ocean.tick_params(axis='x', rotation=45)

    # Styling the grid for OCEAN chart
    ax_ocean.grid(axis='y', linestyle='--', alpha=0.7)

    # Save the OCEAN plot to session state
    st.session_state.fig_ocean = fig_ocean

    # Create RIASEC graph and save to session state
    fig_riasec, ax_riasec = plt.subplots(figsize=(8, 5))
    riasec_labels = list(riasec_scores.keys())
    riasec_values = list(riasec_scores.values())

    # Bar chart for RIASEC scores
    bars_riasec = ax_riasec.bar(riasec_labels, riasec_values, color='lightgreen')

    # Add labels on top of each bar for RIASEC scores
    for bar in bars_riasec:
        yval = bar.get_height()
        ax_riasec.text(bar.get_x() + bar.get_width() / 2, yval + 1, round(yval, 1), ha='center', va='bottom', fontsize=10)

    # Set axis limits and labels for RIASEC chart
    ax_riasec.set_ylim(0, 40)  # Maximum score of 40
    ax_riasec.set_title("RIASEC Scores", fontsize=14, fontweight='bold')
    ax_riasec.set_xlabel("Trait", fontsize=12)
    ax_riasec.set_ylabel("Score", fontsize=12)
    ax_riasec.tick_params(axis='x', rotation=45)

    # Styling the grid for RIASEC chart
    ax_riasec.grid(axis='y', linestyle='--', alpha=0.7)

    # Save the RIASEC plot to session state
    st.session_state.fig_riasec = fig_riasec

# Display the stored graphs and scores if they are in session state
if 'fig_ocean' in st.session_state:
    st.write("### OCEAN Scores")
    st.pyplot(st.session_state.fig_ocean)

if 'fig_riasec' in st.session_state:
    st.write("### RIASEC Scores")
    st.pyplot(st.session_state.fig_riasec)

if 'ocean_scores' in st.session_state:
    st.write("### OCEAN Scores (Data)")
    st.write(st.session_state.ocean_scores)

if 'riasec_scores' in st.session_state:
    st.write("### RIASEC Scores (Data)")
    st.write(st.session_state.riasec_scores)
    
# session state
st.session_state.ocean_scores = ocean_scores
st.session_state.top_3_riasec_code = top_3_riasec_code

# Button for job recommendations
if st.button("Get My Top 20 Jobs"):
    if 'ocean_scores' in st.session_state and 'top_3_riasec_code' in st.session_state:
        ocean_scores = st.session_state['ocean_scores']
        top_3_riasec_code = st.session_state['top_3_riasec_code']
        
        # Format OCEAN scores into a string
        formatted_ocean_values_str = ' '.join([str(ocean_scores[key]) for key in ["Openness", "Conscientiousness", "Extraversion", "Agreeableness", "Neuroticism"]])
        
        # Prepare the generated query
        generated_prompt_query = f"""
            My RIASEC score is: {top_3_riasec_code}.
            My OCEAN scores are: {formatted_ocean_values_str} (Max score 40).
            Based on these traits, suggest the top 20 job titles for me, focusing on Good Scope roles (no descriptions). 
            Organize by domain if provided; if 'other' is selected, give general recommendations.
            procided domain: {domain_str} 
            
            """
        
        with st.spinner('Fetching your top 20 jobs...'):
            ai_response = get_ai_response(generated_prompt_query)
            # Displaying the response in a neat way
            st.subheader("Your personality fits the following possible occupations....")
            st.write(ai_response)
            
    else:
        st.error("Please calculate your OCEAN and RIASEC scores first before getting job recommendations.")


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


st.info(
    """
    #### Special thanks to: 
    - **MEET DUDHAT - U21CS483 ( Lead developer, Having fun at home in Gujarat)**
    - **JAGADEESH - U21CS464 ( Thin Guy, Likes Research and Coding )**
    - **Dr P VASUKI ( Beloved Guide - Guiding Pillar of our project)**
    - **KAMESHWARI Ma'am ( Best Mentor award )**
    - **MARJIBA - U21CS474 ( Creative Solutions and Designer )**
    """
)

