from tkinter import END

def predict(self):
    import requests

    API_KEY = "YOUR_API_KEY_HERE"

    url = "https://api.groq.com/openai/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    prompt = f"""
    Glucose: {self.glucose_entry.get()}
    Haemoglobin: {self.haemoglobin_entry.get()}
    Cholesterol: {self.cholesterol_entry.get()}

    Return output in this format ONLY:
    Risk: <short sentence max 15 words>
    """

    data = {
        "model": "llama-3.1-8b-instant",
        "messages": [{"role": "user", "content": prompt}]
    }

    response = requests.post(url, headers=headers, json=data)

    result = response.json()["choices"][0]["message"]["content"]

    self.remarks_text.delete("1.0", END)
    self.remarks_text.insert("1.0", result)