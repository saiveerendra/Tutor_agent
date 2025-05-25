Tutor AI Assistant
A conversational AI tutor built with Google's Agent Development Kit (ADK) that specializes in answering math and physics questions.
🌟 Features
Interactive Chat Interface: Clean Streamlit UI for conversing with the tutor
Specialized Knowledge: Dedicated sub-agents for mathematics and physics
Calculation Tools: Built-in calculator and trigonometric functions
Physics Constants: Quick access to common physics constants and their values
🛠️ Technology Stack
Google ADK: Framework for building conversational AI agents
Streamlit: Web application framework for the user interface
Python: Core programming language
Gemini 2.0 Flash: Large language model powering the agents
📋 Project Structure
ADK_Project/
├── .env                  # Environment variables
├── main.py               # Main application entry point
├── utils.py              # Utility functions for agent interaction
├── Tutor_agent/          # Main tutor agent
│   ├── agent.py          # Tutor agent definition
│   └── sub_agent/        # Specialized sub-agents
│       ├── math_agent/   # Mathematics specialist agent
│       │   └── agent.py  # Math agent with calculator tools
│       └── physics_agent/ # Physics specialist agent
│           └── agent.py  # Physics agent with constants lookup
🚀 Getting Started
Prerequisites
Python 3.8+
Google ADK access
Gemini API key
Installation
Clone the repository
Create and activate a virtual environment:
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
Install dependencies:
pip install -r requirements.txt
Create a .env file with your API keys:
GOOGLE_API_KEY=your_api_key_here
Running the Application
Start the Streamlit application:
streamlit run main.py
💬 Usage
Type your math or physics question in the chat input
The tutor will automatically route your question to the appropriate sub-agent
For calculations, use standard mathematical notation
For physics constants, simply ask about the constant you need
Example Questions
"What is the value of sin(30) + cos(60)?"
"Solve the equation 2x + 5 = 15"
"What is the speed of light?"
"Calculate the gravitational force between two masses of 10kg separated by 2 meters"
🔧 Customization
You can extend the agent's capabilities by:
Adding new sub-agents for other subjects
Expanding the physics constants database
Implementing additional mathematical functions
Enhancing the UI with visualization capabilities
📝 License
This project is licensed under the MIT License - see the LICENSE file for details.
🙏 Acknowledgments
Google ADK team for the agent development framework
Streamlit for the intuitive UI framework
