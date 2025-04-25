# 🛍️ LoopIt

중고 거래 플랫폼 with 실시간 채팅 💬  

![Frontend](https://img.shields.io/badge/Frontend-React-blue?style=flat-square)
![Backend](https://img.shields.io/badge/Backend-Django-green?style=flat-square)
![Realtime](https://img.shields.io/badge/Realtime-WebSocket-ff69b4?style=flat-square)
![Database](https://img.shields.io/badge/Database-SQLite-lightgrey?style=flat-square)



## 📌 프로젝트 소개

**LoopIt**은 사용자 간 중고 물품을 등록하고  
**실시간 채팅**을 통해 거래를 진행할 수 있는 웹 플랫폼입니다.






## ⚙️ 실행 방법

1️⃣ Redis 실행 (Ubuntu 기준

```bash
sudo apt install redis-server
sudo service redis-server start
redis-cli ping  # "PONG" 출력되면 정상 작동
```

---

2️⃣ 백엔드 실행 (Django + Channels)

```bash
cd backend

# 가상환경 생성 및 실행
python -m venv venv
source venv/bin/activate           # (Windows: venv\Scripts\activate)

# 의존성 설치
pip install -r requirements.txt

# 마이그레이션 및 서버 실행
python manage.py migrate
python manage.py runserver
```

---
3️⃣ 프론트엔드 실행 (React)

```bash
cd frontend

npm install
npm start
```

✅ 실행 후 `http://localhost:3000` 에 접속

---

