import google.generativeai as genai
genai.configure(api_key="AIzaSyCBABdQso755CYVU1jdV-18sCcDHTsv-kw")  
model = genai.GenerativeModel("models/gemini-1.5-flash-latest")

def answer_factual_question(question):
    prompt = f"Answer this question clearly and accurately: {question}"
    return generate_response(prompt)

def summarize_text(text):
    prompt = f"Summarize the following text in simple terms:\n{text}"
    return generate_response(prompt)

def generate_creative_content(prompt_input):
    prompt = f"Generate creative content based on this input: {prompt_input}"
    return generate_response(prompt)

def generate_response(prompt):
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f" Error: {e}"

def get_feedback():
    return input("\n💬 Was this response helpful? (yes/no): ").strip().lower()

def main():
    print(" Welcome to Your Gemini-Powered AI Assistant!")
    while True:
        print("\nChoose an option:")
        print("1. Answer a factual question")
        print("2. Summarize a text")
        print("3. Generate creative content")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
            question = input("\nEnter your question: ")
            print("\n Generating response...\n")
            print("🧠", answer_factual_question(question))
            get_feedback()

        elif choice == '2':
            text = input("\nPaste the text you want summarized:\n")
            print("\n Summarizing...\n")
            print("📄", summarize_text(text))
            get_feedback()

        elif choice == '3':
            prompt = input("\nWhat creative prompt do you want? (story, poem, etc.): ")
            print("\n Creating content...\n")
            print("🎨", generate_creative_content(prompt))
            get_feedback()

        elif choice == '4':
            print("👋 Goodbye!")
            break
        else:
            print(" Invalid choice. Try again.")

if __name__ == "__main__":
    main()

