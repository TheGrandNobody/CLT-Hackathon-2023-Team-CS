# Edion Hackathon

[Live website](https://edionhackathon.streamlit.app/)

## Local Dev:
[streamlit docs](https://docs.streamlit.io/library/get-started/main-concepts)

````bash
streamlit run frontend.py

# optionally you can run to log state on the webpage
export DEV=1 # set to anything else to disable

# provide API key instead of prompting user:
OPENAI_KEY=CHANGE_ME streamlit run frontend.py 
````