🤖 Autonomous Insurance Quote Agent System
AI Day Hackathon Project

An AI-powered multi-agent system that automates insurance quote analysis — profiling risk, predicting conversion, recommending premiums, and routing decisions automatically.


📌 Project Overview
Manual insurance quote evaluation is slow, inconsistent, and requires expert judgment at every step. This project solves that with an autonomous multi-agent pipeline built in Python and Flask. Each agent handles one responsibility in the decision chain — just like a real insurance team, but fully automated.
Built at the AI Day Hackathon by Premchand Mahanta (Prem650).

⚙️ How It Works — The Agent Pipeline
User Input → Risk Profiler → Conversion Predictor → Premium Advisor → Decision Router → Output + PDF Report
AgentRole🔴 Risk ProfilerClassifies customer as Low / Medium / High Risk based on accident history📊 Conversion PredictorEstimates the probability (%) the customer will convert💰 Premium AdvisorRecommends whether the premium is acceptable or needs a discount🚦 Decision RouterRoutes the quote to Auto-Approve / Agent Follow-Up / Underwriter Review

🏗️ Project Structure
Autonomous-Quote-Agent-System/
│
├── app.py              # Flask web app — routes and prediction logic
├── agents.py           # All 4 AI agents defined here
├── requirements.txt    # Python dependencies
│
├── templates/          # HTML pages
│   ├── home.html
│   ├── input.html
│   └── result.html
│
└── static/             # CSS / assets

🛠️ Tech Stack
CategoryTechnologyLanguagePythonWeb FrameworkFlaskPDF GenerationReportLabFrontendHTML, CSSDeploymentRender

🚀 How to Run Locally
1. Clone the repository
bashgit clone https://github.com/Prem650/Autonomous-Quote-Agent-System-AI-Day-Hackathon-Project-
cd Autonomous-Quote-Agent-System-AI-Day-Hackathon-Project-
2. Install dependencies
bashpip install -r requirements.txt
3. Run the Flask app
bashpython app.py
4. Open in browser
http://localhost:10000

📥 Input Parameters
FieldDescriptionExamplePremium (₹/$)Quoted insurance premium amount1500AccidentsNumber of past accidents2AgeCustomer's age35MilesAnnual miles driven12000

📤 Output
The result page displays:

Risk Level — Low / Medium / High Risk
Conversion Probability — Likelihood the customer converts (%)
Premium Advice — Accept or recommend discount
Decision — Auto-Approve / Agent Follow-Up / Escalate to Underwriter

You can also download a PDF report of the full evaluation.

🧠 Agent Logic (agents.py)
python# Risk based on accident history
def risk_profiler(accidents):
    if accidents > 2:   return "High Risk"
    elif accidents > 0: return "Medium Risk"
    else:               return "Low Risk"

# Premium check
def premium_advisor(premium):
    if premium > 1200:  return "Premium too high — recommend discount"
    else:               return "Premium acceptable"

# Decision routing
def decision_router(risk, conversion):
    if risk == "High Risk":   return "Escalate to Underwriter"
    elif conversion < 40:     return "Agent Follow Up"
    else:                     return "Auto Approve"

📄 PDF Report
After submitting, users can download a full AI Insurance Evaluation Report as a PDF, generated using ReportLab. It includes all input values and agent outputs in a clean format.

🔭 Future Enhancements

🤖 Replace rule-based agents with trained ML models
📈 Add real conversion probability prediction using historical data
🗄️ Integrate a database to store and track quote history
🔐 Add user authentication for agent/underwriter portals
📧 Auto-email quote reports to customers


👨‍💻 Author
Premchand Mahanta (2023002341)
B.Tech — Computer Science and Engineering
GITAM School of Technology, Hyderabad

<p align="center">Built with 🤖 at AI Day Hackathon | Autonomous Quote Agent System</p>
