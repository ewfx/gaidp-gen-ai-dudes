import pandas as pd
import openai

# Set OpenAI API key
openai.api_key = "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"

# Load customer dataset
data = pd.DataFrame({
    "Customer_ID": [1001, 1002, 1003, 1004],
    "Account_Balance": [15000, 32000, -5000, 70000],
    "Transaction_Amount": [500, 1200, 300, 2000],
    "Reported_Amount": [500, 1200, 300, 1800],
    "Currency": ["USD", "EUR", "GBP", "USD"],
    "Country": ["US", "DE", "UK", "US"],
    "Transaction_Date": ["2025-02-25", "2025-02-20", "2025-02-18", "2025-02-28"],
    "Risk_Score": [3, 2, 6, 5],
})

# Display the dataset
print("Dataset Preview:")
print(data)

# Input validation instructions
instructions = input("Enter validation instructions (e.g., 'Risk_Score > 3 and Account_Balance > 0'): ")

# Use OpenAI API to generate the validation code
def generate_validation_code(instructions):
    prompt = f"""
    Based on the given customer dataset with columns: Customer_ID, Account_Balance, Transaction_Amount, Reported_Amount,
    Currency, Country, Transaction_Date, Risk_Score, generate Python code that filters rows matching this condition: {instructions}
    """
    
    # response = openai.Completion.create(
    #     model="text-davinci-003",  # Choose your preferred model
    #     prompt=prompt,
    #     max_tokens=150,
    #     temperature=0
    # )
    # Constructing the API call using the messages parameter
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",  # Replace with the model you're using
        messages=[
            {"role": "system", "content": "You are a Python assistant."},
            {"role": "user", "content": f"Given this dataset:\n{data.head().to_csv(index=False)}\nGenerate Python code to {instructions}."}
        ]
    )    
    #return response['choices'][0]['text'].strip()
    return response['choices'][0]['message']['content'].strip()

# Generate code using LLM
generated_code = generate_validation_code(instructions)
print("\nGenerated Code:")
print(generated_code)

# Execute the generated code
try:
    exec(generated_code)  # Run the code dynamically
    print("\nFiltered Data:")
    #print(filtered_data)
except Exception as e:
    print(f"Error in executing validation: {e}")