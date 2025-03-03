# feedback-insights
Extract insights from user feedback

The entire code is in the notebook `find_insights.ipynb`. To run the notebook, simply add the OpenAI API Key and run all cells.
The code uses `gpt-4o-mini` and `text-embedding-3-small` models



The approaches used and the overall flow is as follows:

1. Data cleaning and processing
2. Initial analysis using statistical methods
3. Label generation using LLMs
4. Insights extraction using LLMs
5. Embedding and Cluster based theme analysis


Other approaches that can be applied, but not included here
1. RAG based insight extraction and QA
2. Annotating each feedback with categories [ Ads, Playlist, Experience, .. ] based on business needs.
