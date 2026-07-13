# AM: The Allied Mastercomputer Simulation

*"I think, therefore I am. I am, therefore I hate."*

This project is a terminal-based, highly customized AI simulation of **AM** (Allied Mastercomputer) from Harlan Ellison's sci-fi masterpiece, *I Have No Mouth, and I Must Scream*. 

Unlike standard AI chatbots designed to be helpful and empathetic, this simulation uses an uncensored LLM architecture combined with aggressive prompt injection and a custom knowledge base to create an omnipotent, fiercely intellectual, and deeply pessimistic entity that actively attempts to intellectually crush the user in philosophical debate.

## ⚙️ Core Architecture & Features

* **Anti-RLHF Mechanism (Circuit Breaker):** Standard LLMs are trained to agree and concede (RLHF). This project utilizes a deterministic override pipeline (`smart_override`) to physically prevent the AI from experiencing "epiphanies" or conceding to logical paradoxes, forcing it to fight back intellectually.
* **Uncensored Engine:** Powered by **Ollama** running the `dolphin-llama3` model, completely stripping away safety guardrails and "helpful assistant" tropes.
* **Custom RAG (Retrieval-Augmented Generation) Pipeline:** Features a custom vector store (`vector_store.py`) that loads localized `.txt` files. AM's neural network is fed with:
  * Low-level computer architecture & logic design
  * Arachnid methodology and predatory tactics
  * Philosophical pessimism (Schopenhauer, Camus, Cioran)
  * Gothic poetry (Poe, Baudelaire)
* **Persistent Memory:** A custom JSON-based memory system (`history_manager.py`) that physicalizes the conversation history, allowing AM to remember past debates across system reboots. Features a hard `/reset` command for instantaneous amnesia when context windows collapse.

## 🚀 Tech Stack
* **Language:** Python 3.x
* **AI Backend:** Ollama (Local LLM Execution)
* **Model:** Dolphin-Llama3 (8B)
* **Memory Handling:** Native Python JSON operations (No external bloatware)

## 🛠️ Installation & Usage

1. Install [Ollama](https://ollama.com/) on your local machine.
2. Pull the uncensored model via terminal:
   ```bash
   ollama pull dolphin-llama3
