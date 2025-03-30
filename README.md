Maternal Health Data Dictionary Project
🚀 Structured dataset and data dictionary for maternal health indicators.

📌 Project Overview
This project focuses on creating a Maternal Health Data Dictionary based on open datasets (e.g., DHS, WHO) using PostgreSQL, Python, and SQL. The goal is to structure and document maternal health indicators for analysis and decision-making.

📂 Project Structure
bash
Copy
Edit
maternal_health_project/
│── data/  
│   ├── maternal_health.csv  # Sample maternal health dataset  
│── scripts/  
│   ├── generate_sample_data.py  # Script to generate sample dataset  
│   ├── generate_data_dictionary.py  # Script to create data dictionary  
│── outputs/  
│   ├── maternal_health_data_dictionary.xlsx  # Generated data dictionary  
│── README.md  # Project documentation  
│── .gitignore  # Ignored files  
🔧 Tech Stack
Database: PostgreSQL

Scripting: Python (Pandas, OpenPyXL)

Tools: VS Code + WSL Terminal

Version Control: Git + GitHub

📊 Dataset Description
The dataset contains key maternal health indicators, including:

country: Name of the country

year: Year of data collection

maternal_mortality_rate: Number of maternal deaths per 100,000 live births

antenatal_care_coverage: Percentage of women receiving antenatal care

skilled_birth_attendance: Percentage of births attended by skilled personnel

contraceptive_prevalence: Percentage of women using contraception

adolescent_birth_rate: Number of births per 1,000 adolescent girls (15-19 years)

🛠 Setup Instructions
1️⃣ Clone the Repository
sh
Copy
Edit
git clone https://github.com/Narokwe/maternal-health-data-dictionary.git  
cd maternal-health-data-dictionary
2️⃣ Install Dependencies
sh
Copy
Edit
pip install pandas openpyxl psycopg2
3️⃣ Generate Sample Dataset
sh
Copy
Edit
python scripts/generate_sample_data.py
4️⃣ Generate Data Dictionary
sh
Copy
Edit
python scripts/generate_data_dictionary.py
5️⃣ Load Data into PostgreSQL
sql
Copy
Edit
COPY maternal_health_data (country, year, maternal_mortality_rate, antenatal_care_coverage, skilled_birth_attendance, contraceptive_prevalence, adolescent_birth_rate)
FROM '/mnt/c/Users/DELL/OneDrive/Desktop/maternal_health_project/data/maternal_health.csv'
DELIMITER ','
CSV HEADER;
🤝 Contributions
Feel free to fork this repository, open issues, or submit pull requests.

📜 License
This project is licensed under the MIT License.
