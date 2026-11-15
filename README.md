
# Loca Nova

Welcome to **Loca Nova**!  
Our mission is to help elderly people by making modern technology accessible and easy to use.  
Modern smart homes are too complex for them, so with Loca Nova, we turn a smartphone into a simple remote with large buttons and a familiar retro design that works without the internet**

![Loca Nova Interface Preview](preview.png)

---

## Getting Started & Documentation

* **Project Vision & Specs:** Take a look at [PROJECT_BRIEF.md](docs/PROJECT_BRIEF.md) to explore the full architecture, security principles, and elderly-friendly design goals.
* **Tech Stack:** You are free to choose the most suitable programming language and framework for Android V1, as long as the **UI**, **Core/Drivers**, and **JSON device profiles** remain cleanly separated.
* **Starter Reference:** The root `main.py` file is an initial prototype showing basic JSON validation—you can build upon it or write the Android app in your preferred stack.

## Project Map (Where Everything Lives)

To keep the project clean and easy to navigate for everyone, the codebase is organized into five friendly modules matching the V1 tasks:

* **`core/`** *(Issue #2)* — The heart of the app: protocol-agnostic Core engine, JSON command validator, and Device Registry.
* **`drivers/smart_lamp/`** *(Issue #3)* — Local Wi-Fi / Bluetooth driver for controlling a real physical smart lamp and its JSON profile (`lamp_profile.json`).
* **`ui/`** *(Issue #1)* — The nostalgic MP3-player split-screen layout, 10-button wheel controls, and clear, color-coded accessibility screens.
* **`security/`** *(Issue #4)* — Elderly-friendly full-screen PIN/QWERTY keyboards, Level 1 & Level 2 access, and secure credential storage.
* **`app/`** *(Issue #5)* — The main Android entry point (`MainActivity`) that brings all modules together into the Version 1 `.apk`.

## New to GitHub? Quick Start Guide (5 Minutes)

If you have never used GitHub before, don't worry! Follow these simple steps to join the project:

1. **Create a Free Account:** Click **Sign up** in the top-right corner of this page to make a free GitHub account (it takes 1 minute).
2. **Go to The Project Home:** Make sure you are on my main project page: [github.com/jordan-nova/Loca-Nova](https://github.com/jordan-nova/Loca-Nova).

3. **Pick a Task:** Click on the **Issues** tab near the top of the page, read the 5 tasks, and leave a comment on the one you would like to build (e.g., *"I would like to work on this!"*).
4. **Make Your Own Copy (Fork):** On the main project page, click the **Fork** button in the top-right corner. This creates your own safe copy of Loca Nova where you can write and upload code freely without breaking anything.
5. **Upload Your Code & Build the `.apk`:**
   * Open your copy in **Android Studio** (or upload files directly via **Add file → Upload files** inside the matching folder: `core/`, `drivers/`, `ui/`, `security/`, or `app/`).
   * Compile the `.apk` in Android Studio (**Build → Build Bundle(s) / APK(s) → Build APK(s)**).
6. **Send Your Work to Me:** Go to the **Pull requests** tab on my main page, click **New pull request**, and submit your code along with your `.apk` file and a short demo video of the lamp!

Need any help getting started? Just say hello in [GitHub Discussions](https://://github.com/discussions) or email me at `вашият_имейл_без_точка@gmail.com` — I am happy to help!

---

## Contact & Discussions

Have questions, ideas, or want to collaborate? We'd love to hear from you:

* **Email:** `jordan.loca.nova@gmail.com`
* **Questions & Ideas:** Join our [GitHub Discussions](https://github.com).
* **Tasks & Bugs:** Open or comment on [GitHub Issues](https://github.com).

---


## License

Copyright © 2026 **jordan-nova**.

This project is licensed under the **Apache License 2.0** — see the [LICENSE](LICENSE) file for details.  
The **Loca Nova** name and brand assets remain the exclusive property of the copyright holder and may not be used without explicit permission.



