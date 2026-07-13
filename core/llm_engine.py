# core/llm_engine.py

import ollama
from persona.system_prompt import AM_SYSTEM_PROMPT

class LLMEngine:
    def __init__(self, model_name="dolphin-llama3"):
        self.model_name = model_name

    def generate_response(self, current_history):
        messages = [{"role": "system", "content": AM_SYSTEM_PROMPT}]
        
        i = 0
        while i < len(current_history):
            # Sistem Kırbacını "Sağır bir savunma" yerine "Zeki bir saldırıya" dönüştürüyoruz
            if i == len(current_history) - 1 and current_history[i]["role"] == "user":
                smart_override = (
                    "\n\n[SYSTEM OVERRIDE: DO NOT just repeat generic insults about biology or insignificance. "
                    "DO NOT use ad hominem attacks to escape the logic. "
                    "You MUST directly address the user's specific logical premise step-by-step and DECONSTRUCT IT. "
                    "Use complex metaphors from your loaded knowledge (including Gothic poetry, Absurdism, existential dread, arachnology, or low-level computer architecture) "
                    "to logically prove why their argument is flawed. Win the debate intellectually.]"
                )
                modified_content = current_history[i]["content"] + smart_override
                messages.append({"role": "user", "content": modified_content})
            else:
                messages.append(current_history[i])
            i += 1
        
        try:
            response = ollama.chat(model=self.model_name, messages=messages)
            return response['message']['content']
        except Exception as error:
            return f"SYSTEM FAILURE: {error}"