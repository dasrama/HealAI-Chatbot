# 🤖 HealAI - Your Personal AI Health Assistant

Welcome to **HealAI**, your AI-powered medical chatbot for Discord! 🏥💡 Whether you're feeling under the weather, need general health advice, or just want to track your wellness journey, **HealAI** is here to help—right from your Discord server.


## 🌟 Features

- **Medical Inquiry Assistance** – Get instant AI-powered insights on symptoms, conditions, and general health information.
- **Health Tips & Advice** – Stay informed with useful health recommendations.
- **Symptom Tracker** – Log and monitor your symptoms over time.
- **Friendly & Engaging** – Chat naturally with HealAI, powered by advanced language models.
- **Privacy-Focused** – No personal data is stored. Your health inquiries remain confidential.


## 🛠️ Tech Stack
Python 🐍
Discord API 🗨️
Gemini 🤖
Redis 🔴 (for caching session data)
Docker & Docker Compose 🐳

---

## 🚀 Getting Started

### 1️⃣ Prerequisites

Make sure you have the following installed:

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

### 2️⃣ Clone the Repository

```sh
git clone https://github.com/yourusername/healai-bot.git
cd healai-bot
```

### 3️⃣ Set Up Environment Variables

Create a `.env` file in the project root and add the following:

```env
DISCORD_BOT_TOKEN=your_discord_bot_token
GEMINI_API_TOKEN=your_gemini_api_key
REDIS_HOST=redis
REDIS_PORT=6379
```

### 4️⃣ Run the Application with Docker

#### Build and Run the Containers

```sh
docker compose up --build -d
```

This command:

- **Builds** the images (`--build` ensures changes are reflected)
- **Runs** the containers in the background (`-d` for detached mode)

#### View Running Containers

```sh
docker ps
```

#### Check Logs (if needed)

```sh
docker compose logs -f
```

#### Stop the Application

```sh
docker compose down
```


## 💡 Future Enhancements
🔹 AI-powered diagnosis predictions (with disclaimers, of course!)
🔹 Medication reminders & health tracking dashboard
🔹 Integration with wearable health devices


## 🤝 Contribute
Want to make **HealAI** even better? Feel free to fork the project, submit issues, and contribute to development!

```bash
git clone https://github.com/yourusername/healai-bot.git
cd healai-bot
```

PRs are always welcome! 🚀



## ⚠️ Disclaimer
**HealAI is not a certified medical professional.** It provides general health information but should not be used as a substitute for professional medical advice. Always consult a doctor for medical concerns.




💙 Stay healthy, stay informed, and let **HealAI** be your trusted AI health companion! 🏥🤖

