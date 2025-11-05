# Emotion Detection in LLMs: An Exploratory Study on Improving Accuracy and Reliability

## Project Overview

This project explores the use of Large Language Models (LLMs) for emotion detection in textual data. It focuses on evaluating and fine-tuning DistilBERT on the GoEmotions dataset to classify emotions with improved accuracy and reliability.
## Key Features

- Fine-tuned DistilBERT (bert-base-uncased) for multi-label emotion classification (28 emotion categories).

- Achieved 83% overall accuracy and an F1-score of 70.33%.

- Developed a desktop application (Tkinter GUI) that:

- Takes user input text.

- Displays the top 3 predicted emotions.

- Shows a bar chart visualization of emotion probabilities.

**Tools and Technologies**
- Category          	Tools/Frameworks
- Language     	Python
- NLP Model    	DistilBERT (Hugging Face Transformers)
- Dataset      	GoEmotions by Google Research
- Libraries	    PyTorch, Transformers, Scikit-learn, Matplotlib, Tkinter
- Environment 	Google Colab, Jupyter Notebook, Local Machine


**Dataset**

The project uses the GoEmotions dataset, which contains over 58,000 Reddit comments annotated with 28 distinct emotion labels and a neutral category.
Dataset source: https://github.com/google-research/google-research/tree/master/goemotions

**Reference**

- Demszky, D. et al. (2020). GoEmotions: A Dataset of Fine-Grained Emotions. Google Research.

- Hugging Face Transformers Documentation.

- PyTorch Documentation.
