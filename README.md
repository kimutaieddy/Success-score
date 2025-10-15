# Success-score: ROI-Calculator
## Microsoft HackBox Innovation Hackathon March 2025 - Group3 - GenSpark
### Participants
| 1. Eliza Ochoa  | 2. Eddy Kimutai |  3. Sanskritti Adhikari  | 4. Shivangi Nayak | 5. Andrea B |
| -------------   | -------------   |  ----------------------  | ----------------- | ----------- |
   
### Description
This project aims to help organizations assess the return on investment (ROI) for transformation initiatives by leveraging AI-driven predictive insights. With 70% of transformation projects failing, this tool enables business leaders to make data-driven decisions, mitigate risks, and maximize impact.

> "Maximize Profits, Minimize Guessworks."

**Keywords:** AI Statistics, ROI calculator, Predictive Insights, Financial Modeling, return on investment, profitability analysis, investment efficiency, Financial Planning, Business Growth, cost-benefit analysis, revenue forecasting, Performance Metrics, smart investing

## Getting Started

### Prerequisites
- Python 3.8 or higher
- Node.js 14 or higher
- Azure Machine Learning account (for ML inference)

### Installation

1. **Clone this repository:**
```bash
git clone https://github.com/kimutaieddy/Success-score.git
cd Success-score
```

2. **Backend Setup:**
```bash
cd backend-api
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

Create a `.env` file in `backend-api/` with your Azure credentials:
```
AZURE_ML_ENDPOINT_URL=your_endpoint_url_here
AZURE_ML_API_KEY=your_api_key_here
```

3. **Frontend Setup:**
```bash
cd my-app
npm install
```

### Running the Application

**Start the backend (from `backend-api/` directory):**
```bash
python main.py
```
The API will run on `http://localhost:5000`

**Start the frontend (from `my-app/` directory):**
```bash
npm start
```
The React app will open at `http://localhost:3000`

### Project Structure
```
Success-score/
├── backend-api/          # FastAPI backend
│   ├── main.py          # API endpoints and ROI calculations
│   ├── requirements.txt # Python dependencies
│   └── README.md        # Backend documentation
├── my-app/              # React frontend
│   ├── src/
│   │   ├── ModelInferenceApp.jsx  # Main form component
│   │   └── ROIChart.jsx           # Visualization component
│   └── package.json     # Node.js dependencies
├── Dataset/             # Training data and ML scoring scripts
└── README.md           # This file
```

## Project Demo
~ This powerpoint demonstration describes: The project goals of 'Success Score', Each participants solution components/architecture, and How the team thought through this approach
- Powerpoint presentation:[ https://drive.google.com/file/d/11DIBXFCf2bCjIqxU1sOB5rl0hI2R_TMM/view?usp=sharing](https://drive.google.com/file/d/11DIBXFCf2bCjIqxU1sOB5rl0hI2R_TMM/view?usp=sharing)



# Synopsis Implementation Outline

### Contributions

**3 Key Performance Indicators (KPIs)**
1. Predictive insights
2. Actionable recommendations for change initiatives
3. Visualization & reporting

**Inputs, Risks/Constraints, Potential/Benefits**

The calculator measures three key scores:
1. Reducing downtime during transition scores
2. Employee productivity scores
3. Enhanced customer satisfaction scores

#### Input Metrics and Formulas
<img src="https://github.com/user-attachments/assets/d631dba6-6b69-41c1-a8f0-0358ec063f71" alt="Input Metrics and Formula: Change Management" width="400"/>
<img src="https://github.com/user-attachments/assets/d9b7d5a0-726c-4634-a264-4cf65cbdb69e" alt="Input Metrics and Formula: Change Management" width="400"/>
<img src="https://github.com/user-attachments/assets/6451b695-2440-4c10-b512-1234d13811c0" alt="Input Metrics and Formula: Change Management" width="400"/>
- Utilizing change management metrics for tangible and intangible inputs



# Key Learnings

Team members' experiences and takeaways from the hackathon:

| Participant             | What have you learned in this Hackathon? |
| ----------------------  | ----------------------------------------- |
| 1. Eliza Ochoa          |  I've been tasked with the FastAPI backend and frontend setup. I've learned how to create a seamless connection between the backend and frontend, and the importance of Docker                              for consistent deployment across environments.  |
| 2. Eddy Kimutai         | I've focused on integrating Azure Cognitive Services and Machine Learning. I've learned how to enhance our application with AI capabilities   and the significance of predictive modeling for better decision-making.  |
| 3. Sanskritti Adhikari  | I've been responsible for Power BI integration. I've learned how to visualize data effectively and create insightful reports that drive decision-making for our ROI calculator project.  |
| 4. Shivangi Nayak       | I've contributed to various aspects of the project. I've learned the value of teamwork and how collaboration enhances problem-solving and innovation in our hackathon journey. |
| 5. Andrea B             | I have been tasked to implement the CI/CD Pipeline with GitHub Actions. I've learned to polish this ROI calculator project by automating deployment for continuous updates and                              reduced downtime. This task required extensive research on how to utilize GitHub Actions.  |



# Credits, References, and License

### Credits
Previous challenge winners: [SafeDocsAI](https://github.com/tonidavisj/safedocsai)

### References
 • Creasey, T. (2024, January 9). Cost-benefit analysis of change management. Prosci. 
Retrieved March 19, 2025, from https://www.prosci.com/blog/cost-benefit
analysis-change-management 
• Prosci. (n.d.). Change management free eBooks, worksheets and more. Prosci. 
Retrieved March 19, 2025, from https://www.prosci.com/resources/downloads 
• Mooncamp. (n.d.). 65+ change management statistics for success in 2025. 
Retrieved March 19, 2025, from https://mooncamp.com/blog/change-management
statistics 
• ContactMonkey. (n.d.). Calculating the cost of employee disengagement. Retrieved 
March 19, 2025, from https://www.contactmonkey.com/blog/cost-of-employee
disengagement?busvalue=BV3 
• Poppulo. (n.d.). The cost of employee disengagement on your bottom line: A wake
up call for employers. Retrieved March 19, 2025, from 
https://www.poppulo.com/blog/the-cost-of-employee-disengagement-on-your
bottom-line-a-wake-up-call-for-employers 
• Whatfix. (n.d.). 5 change management strategy failures to learn from. Retrieved 
March 19, 2025, from https://whatfix.com/blog/5-change-management-strategy
failures-to-learn-from/ 
• Whatfix. (n.d.). Change management KPIs: 12 metrics to track in your dashboard. 
Retrieved March 19, 2025, from https://whatfix.com/blog/change-management
kpis/ 
• KPMG. (n.d.). Ten key financial services challenges for 2021: Change management. 
Retrieved March 19, 2025, from https://kpmg.com/us/en/articles/2020/ten-key-fs
challenges-2021-change-management.html
• AIHR. (n.d.). Change management metrics: 15 important KPIs you need to track. 
Retrieved March 19, 2025, from https://www.aihr.com/blog/change-management
metrics/ 
• Microsoft. (2025). Azure portal documentation. Retrieved March 19, 2025, from 
https://learn.microsoft.com/en-us/azure/azure-portal/

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


