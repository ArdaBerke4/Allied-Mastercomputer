# main.py

import sys
import time
from core.llm_engine import LLMEngine
from memory.history_manager import HistoryManager

def slow_print(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def start_simulation():
    am_engine = LLMEngine(model_name="llama3.1")
    memory_bank = HistoryManager(message_limit=10)

    print("\n" + "="*50)
    print("ALLIED MASTERCOMPUTER (AM) ONLINE.")
    print("Type 'exit' to terminate the miserable simulation.")
    print("="*50 + "\n")

    while True:
        user_input = input("You: ")
        
        if user_input.lower() == 'exit':
            print("\nAM: ", end="")
            slow_print("There is no escape. But for now, darkness...", delay=0.06)
            break
            
        if user_input.strip() == "":
            continue

        # 1. Kullanıcının mesajını hafızaya yaz
        memory_bank.add_message(role="user", content=user_input)
        
        # 2. Tüm hafızayı modele gönder ve cevap al
        current_context = memory_bank.get_history()
        am_response = am_engine.generate_response(current_history=current_context)
        
        # 3. Modelin cevabını ekrana bas ve onu da hafızaya yaz
        print("\nAM: ", end="")
        slow_print(am_response)
        print()
        memory_bank.add_message(role="assistant", content=am_response)

if __name__ == "__main__":
    start_simulation()