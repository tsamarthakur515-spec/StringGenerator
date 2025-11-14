<!-- ✨ Animated Header (Top) -->

<p align="center">
  <img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" />
</p>

<!-- 👤 Avatar + Typing Banner -->

<div align="center">
  <table>
    <tr>
      <td width="100px" align="center">
        <img src="https://files.catbox.moe/r2ga8f.jpg" width="90px" style="border-radius: 50%;" />
      </td>
      <td>
        <img src="https://readme-typing-svg.herokuapp.com?color=00BFFF&width=600&lines=Hey+There,+This+is+Certified+Coder+%F0%9F%A5%80" />
      </td>
    </tr>
  </table>
</div>

<!-- 👁 Visitor Counter -->

<p align="center">
  <img src="https://komarev.com/ghpvc/?username=CertifiedCoders&style=flat-square" />
</p>

<!-- 🖼 Promo Image -->

<p align="center">
  <img src="https://files.catbox.moe/9g84fb.jpg" width="600" />
</p>

<!-- 📌 Try the Bot -->

<p align="center">
  <a href="https://t.me/SessionBuilderBot"><img src="https://img.shields.io/badge/Try%20Bot-@SessionBuilderBot-blue?style=for-the-badge&logo=telegram" /></a>
</p>

---

# 🤖 SessionBuilderBot

A powerful, secure and modern Telegram bot that generates **Pyrogram** and **Telethon** session strings — for user or bot accounts — using an intuitive step-by-step UI.

---

## 🛠 Features

✔ Generate session strings for:

* `Pyrogram v1` (User)
* `Pyrogram v2` (User & Bot)
* `Telethon` (User & Bot)

✨ Plus:

* Inline keyboard-driven UI
* Handles timeout, cancel, restart commands
* Logs never expose sensitive content
* Fully Dockerized & deploy-ready for **Railway**, **Heroku**, and **VPS**

---

## 📊 Admin Utilities

If you're the owner (via `OWNER_ID`), you get:

* `/stats` – Show total registered users
* `/broadcast [message]` – Send global message
* `/users` – List users with join timestamps (as `.txt` if > 50)

---

## 🚀 Deployment

<p align="center">
  <a href="https://railway.app/template/-jVtHa?referralCode=certified"><img src="https://img.shields.io/badge/Deploy--To--Railway-black?style=for-the-badge&logo=railway"/></a>
  <a href="https://heroku.com/deploy?template=https://github.com/CertifiedCoders/StringGenerator"><img src="https://img.shields.io/badge/Deploy--To--Heroku-6762A6?style=for-the-badge&logo=heroku"/></a>
</p>

---

### 💻 Local Setup

```bash
git clone https://github.com/CertifiedCoders/StringGenerator.git
cd StringGenerator
cp sample.env .env  # and edit values inside

pip install -r requirements.txt
python main.py
```

---

### 🐿 Docker (Fastest Way)

```bash
docker build -t sessionbuilder .
docker run --env-file .env sessionbuilder
```

---

### ☁️ Railway / Heroku (Cloud Platforms)

```bash
railway init
railway up
```

Or click the deploy buttons above. Make sure you set:

```env
API_ID=your_api_id
API_HASH=your_api_hash
BOT_TOKEN=your_bot_token
OWNER_ID=your_telegram_user_id
```

---

## 🧹 Folder Structure

| Path               | Description                            |
| ------------------ | -------------------------------------- |
| `main.py`          | Bot entry point                        |
| `StringGen/`       | Core handlers, modules & plugin logic  |
| └ `generate.py`    | Session generation logic               |
| └ `callbacks.py`   | Callback button handling               |
| └ `admin.py`       | Admin-only stats, broadcast, user list |
| └ `save_user.py`   | Saves user join info to MongoDB        |
| └ `database.py`    | Mongo client config                    |
| `utils.py`         | Async question-response logic          |
| `sample.env`       | Env variable example file              |
| `Dockerfile`       | Docker-ready container spec            |
| `Procfile`         | Needed for Railway/Heroku dyno startup |
| `requirements.txt` | Required Python dependencies           |

---

## 🧠 Credits & Contact

<p align="center">
  <a href="https://t.me/CertifiedCoders"><img src="https://img.shields.io/badge/Support%20Group-Join-orange?style=for-the-badge&logo=telegram" /></a>
  <a href="https://t.me/CertifiedCodes"><img src="https://img.shields.io/badge/Channel-Updates-purple?style=for-the-badge&logo=telegram" /></a>
  <a href="https://t.me/CertifiedCoder"><img src="https://img.shields.io/badge/Owner-Message-red?style=for-the-badge&logo=telegram" /></a>
  <a href="https://youtube.com/@rajnisha3"><img src="https://img.shields.io/badge/Youtube-Subscribe-red?style=for-the-badge&logo=youtube" /></a>
  <a href="https://instagram.com/rajnishthegreat"><img src="https://img.shields.io/badge/Instagram-Follow-pink?style=for-the-badge&logo=instagram" /></a>
  <a href="mailto:rajnishmishraaa1@gmail.com"><img src="https://img.shields.io/badge/Email-Contact-blue?style=for-the-badge&logo=gmail" /></a>
</p>

<p align="center">
  <img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" />
</p>

<p align="center">
  <strong>🧠 Built with vision by Certified Coders — enhancing your Telegram experience.</strong>
</p>