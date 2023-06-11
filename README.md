# AI Based Emotions Extractor and Mapper
This GitHub repository contains a comprehensive solution for analyzing public reactions and sentiments towards various trends on Twitter. By designing and deploying an emotion and sentiment mapping model, this project enables enhanced analytics, providing valuable insights into the public's response to different topics.

## Features
* Data Preparation: Utilize Pandas and Numpy to preprocess and clean tweet data, ensuring consistency and accuracy in the analysis.

* NLP Pipeline: Leverage Neattext and NLTK libraries to implement a robust NLP pipeline, enabling efficient text processing, including text normalization, tokenization, stop-word removal, and stemming.

* Feature Extraction: Employ Scikit-learn to extract relevant features from the preprocessed tweet data, enabling the conversion of text data into numerical representations suitable for machine learning models.

* Python and Streamlit: Develop a user-friendly interface using Python and Streamlit, allowing users to interact with the emotion and sentiment mapping model and obtain real-time keyword-based tweet analysis.

* Twitter API Integration: Integrate the Twitter API to retrieve live tweet data based on user-defined keywords, facilitating up-to-date and relevant analysis of public reactions to trends.

## Getting Started
1. Clone the repository:
```http
git clone https://github.com/yourusername/emotion-sentiment-tweet-analysis.git
```

2. Install the required dependencies using pip:
```http
pip install -r requirements.txt
```

3. Obtain Twitter API credentials and update the configuration file with the necessary information.

4. Run the Streamlit app by providing 4 twitter api credentials as arduments:
```http
streamlit run app.py <arg1> <arg2> <arg3> <arg4>
```
arg1: Consumer Key | arg2: Consumer Secret | arg3: Access Token Key | arg4: Access Token Secret

## Usage
1. Launch the Streamlit app by running app.py.

2. Input the desired keywords or trending topics to analyze.

3. Explore the real-time emotion and sentiment mapping results, providing enhanced analytics on public reactions to trends.

## Contributing
Contributions are welcome! If you would like to enhance the functionality of this project or fix any issues, please submit a pull request.

## Acknowledgments
We would like to acknowledge the contributions of the open-source community and the libraries used in this project, including Pandas, Numpy, Neattext, NLTK, Scikit-learn, Streamlit, and the Twitter API.

For more detailed information, please refer to the documentation and code in this repository.

