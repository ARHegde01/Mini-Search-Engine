## Mini-Search-Engine

### The Mini Search Engine, nicknamed NOVARA Search is an AI powered search program that utilizes natural language processing (NLP) techniques to provide advanced search capabilities. It interacts with a MongoDB database and provides a graphical user interface (GUI) for searching and displaying search results. The program is built using Python and leverages the power of machine learning and data processing libraries.

---

### Features
- Advanced Search: Nova RA Search employs sophisticated NLP algorithms to process search queries, enabling users to search for specific terms, phrases, or even complex queries.
- Relevant Search Results: The program ranks search results based on relevance, taking into account factors such as term frequency-inverse document frequency (TF-IDF) and weight multipliers.
- Graphical User Interface: The GUI, built using the Tkinter library, provides a user-friendly interface for interacting with the search program.
- Webpage Diving: Users can dive into webpages directly from the search results to view their content, helping them quickly access relevant information.
- Intuitive Navigation: The program offers seamless navigation between search results and provides options to perform additional searches or exit the program.
- TF-IDF Ranking: The search engine utilizes the TF-IDF (Term Frequency-Inverse Document Frequency) ranking algorithm to calculate the relevance of documents based on the frequency of query terms within the document corpus.

---

### Prerequisites: 
Before running Nova RA Search, make sure you have the following installed:

- Python (version 3.7 or above)
- MongoDB (make sure the MongoDB service is running)
- NLTK (Natural Language Toolkit) library
- Tkinter (for the graphical user interface)

--- 

### Installation:
- Clone the repository: git clone https://github.com/your-username/nova-ra-search.git
- Install the required dependencies: pip install -r requirements.txt
- Download NLTK data resources: Launch Python interpreter and run the following commands: [import nltk --> tk.download('punkt') --> tk.download('stopwords')]
- Start the MongoDB server: Make sure MongoDB is installed and running on your system.
- Prepare the document corpus: Place your document corpus in the designated WEBPAGES_RAW folder.

---

### Usage:
- Run the program: python main.py
- Enter your search query in the provided search box.
- Click the "Dive" button to retrieve and display the relevant search results.
- Click on the search result links to open the corresponding webpages.

---

### Practical Uses: 
- Information Retrieval: Nova RA Search can be used for efficient retrieval of relevant information from a large document corpus. It can be applied in research projects, data analysis, or any scenario where fast and accurate information retrieval is required.

- Text Mining and Analysis: The search engine can aid in text mining and analysis tasks, allowing users to explore and analyze a document corpus based on their specific queries or research interests.

- Content Recommendation: Nova RA Search can be integrated into content recommendation systems to provide personalized recommendations based on user queries and preferences.

- Data Exploration: The search engine enables users to explore and navigate through a document corpus, gaining insights and understanding patterns within the data.

- Language Processing Research: Nova RA Search serves as a practical tool for conducting language processing research, evaluating the effectiveness of different algorithms, and experimenting with new techniques for information retrieval.

---

### Acknowledgments
- Natural Language Toolkit (NLTK) - Used for advanced natural language processing tasks.

--- 

### Contributors:
- Farhaan Rasool - @frasool@uci.edu
