
# Loca Nova

Welcome to **Loca Nova**!  
Our mission is to help elderly people by making modern technology accessible, warm, and easy to use. Modern smart homes are often too complex for them, so we are turning a smartphone into a simple remote with large buttons and a familiar retro design that works **100% without the internet**.

![Loca Nova Interface Preview](preview.png)

---

## Getting Started & Documentation

* **Project Vision & Specs:** Take a look at [PROJECT_BRIEF.md](docs/PROJECT_BRIEF.md) to explore the full architecture, security principles, and elderly-friendly design goals.
* **Tech Stack (V1):** We are building a native Android application (`.apk`) using **Kotlin** (Jetpack Compose is recommended) with a lightweight local Core.
* **Starter Reference:** The root `main.py` file is a simple JSON validation example to give you a quick feel for the command structure—feel free to build the Android app natively in Kotlin.

## Project Map (Where Everything Lives)

To keep the project clean and easy to navigate for everyone, we have organized the codebase into five friendly modules matching our V1 tasks:

* **`core/`** *(Issue #2)* — The heart of the app: protocol-agnostic Core engine, JSON command validator, and Device Registry.
* **`drivers/smart_lamp/`** *(Issue #3)* — Local Wi-Fi / Bluetooth driver for controlling a real physical smart lamp and its JSON profile (`lamp_profile.json`).
* **`ui/`** *(Issue #1)* — The nostalgic MP3-player split-screen layout, 10-button wheel controls, and clear, color-coded accessibility screens.
* **`security/`** *(Issue #4)* — Elderly-friendly full-screen PIN/QWERTY keyboards, Level 1 & Level 2 access, and secure credential storage.
* **`app/`** *(Issue #5)* — The main Android entry point (`MainActivity`) that brings all modules together into the Version 1 `.apk`.

## How You Can Contribute

We would love your help in bringing Loca Nova to life! Here is how you can jump in:

1. **Fork & Clone:** Fork this repository and clone it to your computer (`git clone https://github.com`).
2. **Pick an Issue:** Browse our [open Issues](https://github.com) and choose something you enjoy working on, placing your code in the matching folder above.
3. **Keep It Offline & Modular:** Make sure lamp control works locally (Wi-Fi / Bluetooth / Hotspot) without external internet, and keep modules cleanly separated.
4. **Build & Test:** You can test with a simulated lamp first, then verify with a real physical smart lamp. Build your `.apk` in **Android Studio** (**Build → Build Bundle(s) / APK(s) → Build APK(s)**).
5. **Share Your Work:** Open a **Pull Request (PR)** and include your testable `.apk` along with a short demo video of the lamp in action.

## Let's Connect

Have questions, ideas, or want to collaborate? We'd love to hear from you:

* **Email:** `вашият_имейл_без_точка@gmail.com`
* **Discussions:** Say hello or share ideas in [GitHub Discussions](https://github.com)
* **Issues:** Join the conversation on [GitHub Issues](https://github.com)


## Contact & Discussions

* **Email:** `jordan.loca.nova@gmail.com`
* **Questions & Ideas:** Join our [GitHub Discussions](https://github.com).
* **Tasks & Bugs:** Open or comment on [GitHub Issues](https://github.com).

---

## License

Copyright © 2026 **jordan-nova**.

This release is licensed under the **Apache License 2.0** — see the [LICENSE](LICENSE) file for details.  
The **Loca Nova** name and brand assets remain the exclusive property of the copyright holder and may not be used without explicit permission.


