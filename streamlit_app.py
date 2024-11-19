import streamlit as st
import openai
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
