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

Here are some examples

**Top Bugs Reported**
```
Random Song Playback: Many users have reported that their playlists do not play in the intended order and instead include random songs that are not part of the selected playlists. For instance, one user stated, “I can't listen to my music because I have to get premium or go listen to Apple Music... Spotify keep asking me for Spotify premium.”

Limited Skips: Users are frustrated by the limitation of skips per hour, which is enforced on the free version. A typical complaint is, “the new update and i only get 6 skips an hour?!”

Unreliable CarPlay Functionality: Some users mentioned issues with Spotify not functioning well with CarPlay, causing interruptions during use. One user noted, “For a few weeks now, I haven't been able to play Spotify in the car with CarPlay.”

Ads in Premium Version: Users reported receiving ads even after purchasing the premium subscription, which was unexpected. One feedback reads, “You pay for a premium version, but I still have ads...”

Issues with Playback Control: Several users expressed frustration with not being able to rewind or play specific songs, especially about the enforced shuffle feature. For example, a user shared, “Now you can only skip 6 times, you can't see the lyrics more than twice a month, and there are a lot of ads.”
```

**Top suggestions about Ads**
```
Reduce the Frequency and Length of Ads: Many users expressed frustration about the excessive number of ads, particularly noting that they often occur after just one or two songs. For example, one user stated, "I get an ad every 30 seconds after every 2 songs," while another remarked, "I can listen to 20 mins and then get 7 ads in a row."

Improve the 'Uninterrupted Listening' Experience: Users are dissatisfied with the discrepancy between ad promises and actual experiences. Comments include, "It gives many random songs and this makes it preferable to YouTube," referring to broken expectations like "30 minutes of uninterrupted listening" but encountering ads soon after, "I get the same ad three times in a row but I do truly love Spotify."

Ad Customization and Targeting: Some users felt the ads were not suitable for their demographics or interests. Feedback included, "When I try to play a specific song, I get a completely different one," indicating frustration when ads related to interests do not align with their music preferences. Also, "they keep putting songs on my playlist that I didn’t and keep playing the songs" highlights another issue where random ads disrupt the listening experience.
```
