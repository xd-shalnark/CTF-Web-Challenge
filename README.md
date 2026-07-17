# 🐱 Web Challenge — Cats Page
 
**CTF:** TillerCTF  
**Category:** Web  
**Difficulty:** Beginner  
**Flag format:** `TillerCTF{...}`
 
---
 
## 📖 Description
 
This is an educational project created for **TillerCTF**, a Capture The Flag competition held in **April 2026**.
 
You land on what looks like a completely ordinary page about cats. Two fluffy residents — Barsik and Milo — seem to be minding their own business. But not everything here is as simple as it appears.

---
 
## 🎯 Goal
 
Find the flag in the format `TillerCTF{...}`.
 
---
 
## 🛠️ Tools Required
 
- `curl` — command-line tool for making HTTP requests
---
 
## 📚 What You Will Learn
 
- The difference between **GET** and **POST** HTTP requests
- How to send data to a server using the `-d` / `--data` flag
- How to look for hidden clues in a page's source code
---
 
## 💡 Hints
 
<details>
<summary>Hint 1 — Where to start</summary>
Look at the raw source code of the main page. In a browser press `Ctrl+U`, or use the terminal:
 
```bash
curl https://ctf-task-web.vercel.app/
```
 
</details>
<details>
<summary>Hint 2 — What to look for</summary>
Two values are hidden somewhere on the page: `key` and `value`. Find them.
 
</details>
<details>
<summary>Hint 3 — How to use what you found</summary>
Send them to the server as a POST request:
 
```bash
curl -X POST https://ctf-task-web.vercel.app/api/flag \
  -d "key=YOUR_VALUE&value=YOUR_VALUE"
```
 
</details>
 
## 🔗 Links
 
- **Challenge site:** https://ctf-task-web.vercel.app/
- **Hosting:** [Vercel](https://vercel.com)