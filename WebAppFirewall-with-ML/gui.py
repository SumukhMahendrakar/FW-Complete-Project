import tkinter as tk
from tkinter import ttk
import joblib

rf_model = joblib.load(r'D:\FW-Project\WebAppFirewall-with-ML\random_forest_model.pkl')
vectorizer = joblib.load(r'D:\FW-Project\WebAppFirewall-with-ML\tfidf_vectorizer.pkl')


def classify_url():
    url = entry.get()

    url_vectorized = vectorizer.transform([url])
    prediction = rf_model.predict(url_vectorized)[0]

    result_label.config(text=f"Classification: {'Malicious' if prediction == 1 else 'Safe'}")


root = tk.Tk()
root.title("Malicious URL Detector")
root.geometry("400x200")

root.configure(bg='#fff8e1')

style = ttk.Style()
style.configure("TButton", padding=(10, 5), font=('Helvetica', 12))

# version_label = ttk.Label(root, text="Version 1.0", font=('Helvetica', 10, 'italic'), background='#fff8e1')
# version_label.pack(pady=5)

header_label = ttk.Label(root, text="Malicious URL Detector", font=('Helvetica', 16, 'bold'), background='#fff8e1')
header_label.pack(pady=5)

entry = ttk.Entry(root, width=40, font=('Helvetica', 12))
entry.pack(pady=5)

classify_button = ttk.Button(root, text="Classify URL", command=classify_url)
classify_button.pack()

result_label = ttk.Label(root, text="", font=('Helvetica', 14), background='#fff8e1')
result_label.pack(pady=5)

# developed_by_label = ttk.Label(root, text="Developed By: Prakhar Gupta", font=('Helvetica', 10, 'italic'),
#                                background='#fff8e1')
# developed_by_label.pack()

root.mainloop()
