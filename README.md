# Discord Chatbot Powered by Ollama

Run AI locally through Discord!


## Features include:
- **Web Search**: Perform quick searches and get results in chat.  
- **Link Navigation**: Extract and display content from shared URLs.  
- **Google Docs Integration**: Read and interpret documents (needs service account).  
- **Content Summarization**: Generate concise summaries of lengthy text.  
- **Customizable AI**: Adjust context, rules, and behavior to fit your needs.  
- **Model Management**: Switch between AI models or configure vision models.  
- **History Management**: View and manage conversation history.

# How to Get Ollama

**Follow these steps to get and install Ollama**

## 1. Visit the Ollama Website
Go to the official Ollama website: [https://ollama.com](https://ollama.com).

## 2. Download Ollama
On the website, select the download option for your operating system:
- **Windows**: Click the download link for Windows.
- **macOS**: Click the download link for macOS.
- **Linux**: If available, select the appropriate Linux version.

## 3. Install Ollama
- **For Windows**:
  - Run the downloaded `.exe` file and follow the installation instructions.
- **For macOS**:
  - Open the `.dmg` file and drag Ollama to the Applications folder.
- **For Linux**:
  - Follow the installation instructions provided on the website using your package manager or by downloading the appropriate package.

## 4. Verify Installation
Open your terminal or command prompt and type "ollama --version".

## 5. List Models
In your terminal type "ollama list" to get a list of available models.

## 6. Run Ollama
In your terminal type "ollama serve" or run the application directly. 

# Available Bot Commands:

- `!help` - Displays the list of available commands.

## Reset Commands
- `!reset all` - Resets all to default values.
- `!reset context` - Resets context to default value.
- `!reset rules` - Resets rules to default value.
- `!reset temp` - Resets temperature to default value.
- `!reset memory` - Resets memory to default value.
- `!reset mlim` - Resets memory limit to default value.

## Clear Commands
- `!clear all` - Clears everything or sets it to 0.
- `!clear context` - Clears the context.
- `!clear rules` - Clears the rules.
- `!clear temp` - Clears the temperature (sets it to 0.0).
- `!clear memory` - Clears the memory.

## Set Commands
- `!model <model>` - Sets the model.
- `!vmodel <model>` - Sets the vision model.
- `!context <context>` - Sets the context for the AI.
- `!rules <rules>` - Sets the rules for the AI.
- `!temp <float>` - Sets randomness of AI's responses.
- `!clim <int>` - Sets the character limit.
- `!mlim <int>` - Sets the character limit for memory.

## Show Commands
- `!show all` - Displays all settings.
- `!show context` - Displays the current context.
- `!show rules` - Displays the current rules.
- `!show temp` - Displays the current temperature.
- `!show model` - Displays the current model.
- `!show list` - Lists all available models.
- `!show clim` - Displays the current character limit.
- `!show mlim` - Displays the current memory limit.
- `!show memory` - Displays the conversation history.

## Model Management Commands
- `!pull <model>` - Pulls the specified model.
- `!delete <model>` - Deletes the specified model.
