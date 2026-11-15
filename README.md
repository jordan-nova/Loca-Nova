
# Loca Nova

Our mission is to help elderly people by making modern technology accessible and easy to use.  
Modern smart homes are too complex for them, so with **Loca Nova**, we turn a smartphone into a simple remote with large buttons and a familiar retro design that works **100% without the internet**.

![Loca Nova Interface Preview](preview.png)

---

## Documentation & Specifications

* **Project Brief:** Read [PROJECT_BRIEF.md](docs/PROJECT_BRIEF.md) for complete technical specifications, security requirements, and accessibility guidelines.
* **Target Platform (V1):** Native Android application (`.apk`) with an embedded, protocol-agnostic local Core.
* **Reference Prototype:** The root `main.py` file serves solely as an initial local JSON-validation prototype and does not restrict the final Android technology stack.

## Project Directory Structure

Please place all code contributions in the corresponding directory for your assigned task:

* **`core/`** — Protocol-agnostic Core engine, JSON schema validator, Communication Router, and Device Registry *(Issue #2)*.
* **`drivers/`** — Isolated local device drivers (Wi-Fi / Bluetooth) and JSON device profiles *(Issue #3)*.
* **`ui/`** — Classic MP3-player split-screen layout, 10-button wheel navigation, and color-coded accessibility controls *(Issue #1)*.
* **`security/`** — Zero-trust Security Portal, Level 1 & Level 2 authentication, and hardware-backed PIN/password storage *(Issue #4)*.
* **`app/`** — Main Android application entry point integrating all modules into the final Version 1 MVP *(Issue #5)*.

## How to Contribute & Submit Your Work

1. **Fork & Clone:** Fork this repository and clone it to your local machine (`git clone https://github.com`).
2. **Choose a Task:** Check the open [Issues](https://github.com) and work within the designated folder for that module.
3. **Build the Android `.apk`:** Open the Android project in **Android Studio**, build the testable package via **Build → Build Bundle(s) / APK(s) → Build APK(s)**, and verify it on a real device.
4. **Submit a Pull Request:** Push your changes to your fork and open a **Pull Request (PR)** to this repository, attaching your testable `.apk` and a short demo video controlling a real physical lamp.

## Contact & Discussions

* **Questions & Ideas:** Join our [GitHub Discussions](https://github.com).
* **Tasks & Bugs:** Open or comment on [GitHub Issues](https://github.com).

---

## License

Copyright © 2026 **jordan-nova**.

This release is licensed under the **Apache License 2.0** — see the [LICENSE](LICENSE) file for details.  
The **Loca Nova** name and brand assets remain the exclusive property of the copyright holder and may not be used without explicit permission.


