Health Metrics Chatbot - Text-to-SQL
Project Overview
The Health Metrics Chatbot is an intelligent chatbot that allows users to query an extensive health and fitness database using natural language. It converts these natural language queries into SQL, executes them against a MySQL database, and returns the results in a structured table format.

The project demonstrates the use of:

Generative AI for natural language processing and SQL generation.
FastAPI for backend development in a microservice architecture.
React for the frontend user interface.
SQLAlchemy for database modeling and interaction with a MySQL database.
Features
Intuitive chatbot interface that allows users to ask questions about health metrics, workouts, exercises, and nutrition.
Converts natural language queries into SQL using GPT-based AI models.
Displays both the generated SQL query and the query result in a user-friendly format.
Conversation history persistence.
Sidebar displaying table metadata (table names and columns).
Table of Contents
Project Overview
Features
Technology Stack
System Requirements
Setup Instructions
Database Schema
API Endpoints
RAG (Retrieval-Augmented Generation) Mechanism
Running the Application
Acknowledgments
Technology Stack
Backend: FastAPI (Python), MySQL-Connector, MySQL
Frontend: React (JavaScript)
AI Integration: GPT-4o (OpenAI API)
Database: MySQL
Embedding: Hugging Face (moka-ai/m3e-base)
System Requirements
Python: 3.9.13
Node.js: 16.14.0
MySQL: 8.x or above
Setup Instructions
1. Clone the Repository
bash
Copy code
git clone https://github.com/your-username/health-metrics-chatbot.git
cd health-metrics-chatbot
2. Backend Setup
Install Python Dependencies
Navigate to the backend directory:

bash
Copy code
cd backend
Install the required dependencies:

bash
Copy code
pip install -r requirements.txt
Set up Environment Variables
Create a .env file in the /backend directory with the following information:

bash
Copy code
OPENAI_API_KEY=your-openai-api-key
DATABASE_URL=mysql+pymysql://username:password@localhost/health_db
EMBEDDING_MODEL=moka-ai/m3e-base
Initialize the Database
You can initialize the database and tables by running the following:

bash
Copy code
python3 -m backend.data.populate_data

3. Frontend Setup
Install Node.js Dependencies
Navigate to the frontend directory:

bash
Copy code
cd ../frontend
Install the necessary dependencies:

bash
Copy code
npm install

4. Running the Application
Start Backend (FastAPI)
bash
Copy code
cd backend
uvicorn main:app --reload
Start Frontend (React)
Navigate back to the frontend directory and start the React app:

bash
Copy code
cd ../frontend
npm start
The frontend will be accessible at http://localhost:3000, and the backend will run on http://localhost:8000.

5. Database Schema
The following is an overview of the database schema used in this project:

Users

id: Primary Key
name: User's name
age: User's age
gender: User's gender


Workouts

id: Primary Key
user_id: Foreign Key referencing Users
date: Date of workout
duration: Duration of workout in minutes


Exercises

id: Primary Key
workout_id: Foreign Key referencing Workouts
name: Name of the exercise
sets: Number of sets performed
reps: Number of repetitions per set


Nutrition

id: Primary Key
user_id: Foreign Key referencing Users
date: Date of meal
meal: Description of the meal
calories: Total calories
protein: Protein intake in grams
fats: Fat intake in grams
carbs: Carbohydrate intake in grams


Health Metrics

id: Primary Key
user_id: Foreign Key referencing Users
weight: Weight in kilograms
height: Height in centimeters
bmi: Body Mass Index (BMI)
heart_rate: Resting heart rate in beats per minute


Chat History

id: Primary Key
user_query: User input natural query
sql_query: AI Generated SQL Query
created_at: Timestamp of entry creation

6. API Endpoints
1. /fetch-data [POST]
Description: Accepts a Natural Query as input and fetches the generated SQL Query and its result from Database.

2. /chat-history [GET]
Description: Fetches the inputted User query and Generated SQL Query which is stored in DB as a conversation hostory.

7. RAG (Retrieval-Augmented Generation) Mechanism
Embedding Search: Embeddings are generated using the Hugging Face model moka-ai/m3e-base. When a user inputs a query, the embeddings are matched to shortlist the relevant tables.
AI Model: We use the GPT-4o model (via OpenAI API) to convert the natural language query to an SQL query based on the shortlisted tables.
Running the Application
Start the FastAPI backend:
bash
Copy code
uvicorn main:app --reload
Start the React frontend:
bash
Copy code
npm start
Open your browser and navigate to http://localhost:3000.
Acknowledgments
OpenAI for providing the GPT-4o model.
Hugging Face for the moka-ai/m3e-base embedding model.
React and FastAPI for powering the frontend and backend.
