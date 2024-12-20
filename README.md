# Discord Chatbot Powered by Ollama

Run AI locally through Discord!
- **Web Search**: Perform quick searches and get results in chat.  
- **Link Navigation**: Extract and display content from shared URLs.  
- **Google Docs Integration**: Read and interpret documents (needs service account).  
- **Content Summarization**: Generate concise summaries of lengthy text.  
- **Customizable AI**: Adjust context, rules, and behavior to fit your needs.  
- **Model Management**: Switch between AI models or configure vision models.  
- **History Management**: View and manage conversation history.

## Available Commands
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
