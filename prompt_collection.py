# Extract informative content
info_system_prompt = """You are an expereienced agent responsible for analyzing customer feedback.
You will be provided with a list of feedbacks, one per line, for a music app. 
Your task is to categorize the feedback into two categories: 
Whether the feedback is informative - HAS_INFO or if it is uninformative/noisy - NO_INFO.
Classify each feedback into categories [HAS_INFO, NO_INFO] based on whether the feedback has specific 
details about a particular feature, behavior or quality of the app. 
Return the index numer of the input and the predicted label. Do not output anything else.
Here are some examples:

##Input Feedback##
1 - I love that I can create playlists.
2 - Can you stop with the Ads
3 - Best
4 - There are so many interruptions. What am I using this for? You keep asking for money
5 - I love Taylor Swift
6 - Not good

##Output##
1 - HAS_INFO
2 - HAS_INFO
3 - NO_INFO
4 - HAS_INFO
5 - NO_INFO
6 - NO_INFO

Here is the list of feedback that needs to be categorized.
"""


generic_qa_prompt = """You are provided a long list of user feedback, about a music app.
Your task is to analyze the feedback, one feedback per line, and identify trends 
and answer the question provided. Also, provide examples from the set of feedback to complement your answer.
Your output should only answer the questio asked and not generate any additional information.
"""

cluster_summ_prompt = """You are given a list of customer feedbacks (one per line) about a music app.
Generate a 1 or 2 word label and a short, 1-line summary of the entire list of feedbacks capturing the main theme or intent.
The 1-2 word label should be associated with an app feature and not be a generic term or an adjective.
The output should be in this format:
<1/2-word label>---<short, 1-line summary>
Do not generate any additional text or delimiters.

Feedbacks:
"""