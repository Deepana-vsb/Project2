# 🤖 AI Chatbot for College Helpdesk

---

## 📌 Overview

*AI Chatbot for College Helpdesk* is a beginner-friendly Java project that simulates a chatbot to help students with frequently asked college-related questions. The chatbot responds to questions like exam dates, department heads, scholarships, and ID card processes using simple keyword matching. It runs in the terminal and is easy to extend with more data.

---

## 📌 Features

- 🗨️ Interactive terminal-based conversation  
- ⚡ Fast and efficient response matching  
- 📢 Clear prompts for user input  
- 🛠️ Easy to customize and extend with more FAQs

---

## 📂 Project Structure

ai-chatbot-helpdesk-java/ ├── Chatbot.java └── README.md

---

## 🛠️ Technologies Used

- Java (JDK 8 or above)  
- Basic AI-like keyword matching using Java collections

---

## 🚀 How to Run

1. Make sure Java is installed.  
2. Save the file as Chatbot.java  
3. Open your terminal or command prompt  
4. Navigate to the folder where the file is saved  
5. Compile the program using:

   ```bash
   javac Chatbot.java

6. Run the chatbot using:

java Chatbot




---

💬 Sample Output

🤖 AI Chatbot for College Helpdesk
Type 'exit' to quit

You: what is the exam date  
Bot: Semester exams start from July 5th.

You: who is the hod of cse department  
Bot: Dr. Ramesh is the HOD of CSE.

You: exit  
Bot: Goodbye! 👋


---

➕ How to Add More FAQs

To add more responses, open Chatbot.java and edit the loadFaqData() method like this:

faqData.put("how to pay exam fees", "Pay through the student portal before the due date.");


---

🚀 Future Improvements

Add a GUI using Java Swing

Store FAQs in a separate JSON or text file

Integrate speech-to-text for voice-based questions

Add category-based filtering (e.g., exams, scholarships, departments)



---

🧑‍💻 Author

Developed by Deepana


---

