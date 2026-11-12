LOCA NOVA – PROJECT BRIEF
Architectural Philosophy: Universal Device Compatibility
Loca Nova is designed as a universal, modular device-control platform intended to support a wide range of compatible devices, network environments, and communication protocols.
Platform Independence: The application must not depend on a specific router, network configuration, device brand, or communication protocol. It should support different connection methods through independent, replaceable drivers and clearly defined interfaces.
Protocol-Agnostic Core: The Core must remain lightweight and protocol-agnostic. New compatible devices and communication methods should be integrated through independent drivers without requiring changes to the existing Core wherever possible. The Core may be improved when technically necessary.
Functional Expectations: The application should support device discovery, connection, control, and status reporting wherever the device and its communication method permit these functions.
Architectural Scope: Universal compatibility is an architectural goal, not a claim that every device can be controlled automatically. Each device must have a compatible communication method, a suitable driver, and any required authorization.
Future-Proofing: The architecture should support future device categories and other compatible equipment by adding suitable drivers and adapters without redesigning the entire system.
Long-Term Core Stability and Expansion
The initial version of Loca Nova must establish a stable, modular, and extensible architectural foundation for future expansion.
Loca Nova must be designed as a universal device-control platform, not as an application limited to lamps, smart home devices, or home automation. Its architecture must support devices from different categories, manufacturers, and environments through one unified Core, modular device drivers, and multiple communication technologies, allowing maximum practical compatibility and future expansion.
Core Architecture: The Core must be designed from the beginning to support the addition of new compatible devices, drivers, communication protocols, and features without requiring the Core or the entire application to be rewritten.
Decoupled Functionality: Future functionality should be introduced primarily through independent drivers, extensions, and modules that use clearly defined interfaces.
Seamless Integration: Adding a new compatible device should normally require only the installation or integration of its appropriate driver, device registration, and any necessary device-specific user interface components.
Core Modifications: The Core may be modified when technically necessary for architectural improvements, security, compatibility, or critical bug fixes. However, rewriting the Core or the main application must not be the normal method of adding new devices or features.
All initial architectural decisions must take this long-term expansion goal into account.
1. Project Goal
Develop a simple, user-friendly application for controlling at least one real physical lamp. The connection method is at the developer's discretion.
The application must feature an interface inspired by the iPod 5th Generation, specifically adapted for elderly users.
A simulated lamp may be used during development and testing, but it does not replace the requirement to demonstrate control of a real physical lamp.
2. Technical Requirements and Platform Scope
Local Infrastructure: Version 1 must operate as a locally installed Android application, with the Core running locally on the same device as the application.
Version 1 Platform: Android is the only required platform for Version 1. The developer must select the most suitable programming language, framework, and development approach for the Android application and its Core. The architecture should preserve flexibility for future support of other platforms, including Windows, without requiring a complete redesign of the Core.
Physical Hardware Target: Version 1 must support control of at least one real physical lamp. The developer may choose the most suitable communication technology and implementation method for connecting the application and Core to the lamp, such as Wi-Fi, Bluetooth, or another appropriate communication technology.
The selected hardware must be a common, easily accessible consumer smart lamp (for example, a standard Wi-Fi smart bulb) so that it can be easily obtained and tested.
Network Independence: Version 1 must be able to control the selected physical lamp over the chosen local communication method without requiring external internet access or an external server. The required Version 1 lamp-control function must not depend on external cloud connectivity.
The developer may choose the communication method best suited to the selected lamp.
Android Compatibility: The application must support the widest practical range of Android devices, manufacturers, and operating system versions, using adaptive platform integration to ensure maximum compatibility with available hardware and system capabilities.
Future Expansion: The Version 1 architecture must support future expansion with additional device types, communication technologies, control interfaces, and platforms without requiring a complete redesign of the Core.
Command Validation: The Core must validate commands, communicate with the appropriate device driver or integration, and report the lamp's current status to the application through a secure local interface using standardized JSON command payloads.
Quality Assurance: The developer must implement appropriate testing and quality assurance procedures throughout development to identify and prevent bugs, errors, crashes, and unexpected behavior.
Language Environment: Version 1 of Loca Nova must be developed in English, including the user interface, menus, buttons, messages, notifications, and settings.
Universal Compatibility Review:
Loca Nova is intended to become a universal device-control platform, capable of controlling the widest practical range of device types through a unified system.
The developer must review all technical requirements and consider whether the proposed architecture, control interface, communication methods, connection mechanisms, drivers, and other essential components are suitable for achieving this goal.
If any existing instructions or technical requirements limit universal compatibility, restrict future expansion, or prevent the intended functionality, the developer must identify these limitations and propose suitable technical solutions.
The developer must prioritize universal compatibility, flexibility, modularity, reliability, and future expansion when making technical decisions, rather than following any instruction that may conflict with the project's overall goal.
3. User Interaction Scenario
Application Startup, Login, and Security Management
Welcome State: When the user opens the application, display a brief welcome screen showing Loca Nova.
Initial Setup: On the very first launch after installation, prompt the user to create their initial PIN (which also serves as the Administrator PIN by default, with an option to set a separate Administrator PIN later in Settings).
If Level 1 – Easy Access is active and the initial login has already been completed, skip the Authentication Portal and go directly to the Main Menu.
Otherwise, proceed to the Authentication Portal.
Authentication Portal: Display a PIN field with the instruction: "Please enter your PIN to continue."
On-Screen Keyboard: Show a keyboard icon next to the field. Selecting the application PIN field or its icon, using touch or physical buttons where supported, opens a full-screen numeric keypad featuring large, clearly visible keys.
Password fields, such as Wi-Fi or device passwords where applicable, must open a full-screen QWERTY-style keyboard with numbers, letters, spaces, special characters, Backspace, and Enter/Done.
Support copying, pasting, and long inputs without unnecessary length restrictions.
Close the keyboard upon confirmation or when the physical or virtual BACK button is pressed, returning smoothly to the previous screen.
PIN Privacy: Hide PINs and passwords by default, providing an explicit toggle option to show or hide the characters.
Security Levels: The system must support two selectable security levels, manageable within Settings using an administrator PIN:
Level 1 – Easy Access: A PIN is required only the first time the application is opened. After successful entry, the application remains unlocked for everyday use.
Level 2 – Protected Access: A PIN is required every time the application is opened.
Security Constraint: Never store PINs, passwords, or credentials in plain text. All authentication data must use secure platform credential storage, with hardware-backed protection wherever supported by the target platform.
PIN recovery is not required for Version 1 and may be considered for a future version.
Main Menu and Lamp Connection
Main Menu Navigation: Once authenticated, display the Main Menu, designed in the style of the iPod 5th Generation. The user must be able to navigate the menu using supported physical buttons and touch controls to select Devices → Lamp.
Device Scope: The physical lamp is the required operational device for Version 1. The developer may add a smart plug, radio, or TV or other devices as optional demonstrations or extensions.
Lamp Connection: When the user opens Lamp Control, Loca Nova must use the communication method selected for the physical lamp.
If that method requires Wi-Fi network selection or credentials, guide the user through the required steps using a clear, easy-to-navigate list and the full-screen QWERTY-style keyboard.
Password fields must follow the privacy rules: hidden by default, with a show/hide toggle.
Local Core Operation: The application must communicate with the Core running on the same device. The Core must use the appropriate driver or integration to communicate with the physical lamp.
Discovering a separate server through mDNS is not required for communication with the locally running Core.
If the selected device or communication method requires a gateway, the developer must clearly identify that dependency. The gateway must not be assumed to be part of the local Core.
Connection Errors: If the lamp or a required communication component cannot be found, or the connection fails, display a friendly error message and offer a RETRY option.
Device Control and UI Consistency: Once the lamp connection is established, open the Lamp Control screen so the user can operate the lamp.
All connection, selection, and authentication steps must maintain the same iPod 5th Generation interface style, with clear instructions at every step.
5. Driver Interface and Modular Deployment
Translation Layer: Drivers handle device-specific operations, translating generic Core JSON payloads into the precise communication methods and hardware operations required by the target device. They return operation results and the reported hardware state to the Core.
Modular Constraints: For Version 1, particularly on Android, device driver modules must be included as statically compiled components within the main application codebase rather than dynamically loaded executable files. This approach must respect platform compatibility and applicable app store security policies.
Dynamic loading of separate executable binaries may be explored as an optional feature on Windows or other suitable future platforms.
Open-Closed Compliance: New drivers must follow the defined interface and must not require unnecessary changes to existing Core functionality.
Communication Management and Routing: The architecture must include a scalable communication management and routing layer that can select and coordinate suitable communication paths between the Core and compatible devices.
It must support direct connections, gateways, and relays. The architecture should be extensible to remote communication paths in future versions, using appropriate drivers and protocol adapters.
It must support managing a large number of diverse devices across different environments and locations, subject to each device's capabilities, connectivity, and required infrastructure.
Version 1 lamp control must continue to meet the local operation requirements defined in Section 2.
Future Driver Management and Cross-Platform Compatibility
The developer must investigate practical methods for adding, installing, downloading, and managing new device drivers without requiring a complete application update.
The solution must consider Android restrictions and preserve flexibility for future platforms. The architecture must allow different driver installation methods depending on the operating system, without requiring changes to the Core wherever technically possible.
The developer must identify possible limitations and choose the most flexible and practical solution for long-term expansion.
The Communication Manager and Device Driver Manager must operate as separate components, allowing new communication technologies and device drivers to be added independently without requiring changes to the Core.
6. UI Layout, iPod Navigation, and Colors
iPod Heritage Aesthetic: Use a Main Menu modeled directly after the iPod 5th Generation interface layout, scaled and simplified for elderly accessibility. All visual controls must be large, highly legible, and intuitive.
Unified Button Configuration: The application uses one unified physical/virtual button mapping to navigate and control all supported device categories.
Navigation Button Mappings:
Original iPod buttons:
MENU
PLAY/PAUSE
PREVIOUS
NEXT
OK (Center Button)
Supplementary buttons:
UP
DOWN
LEFT
RIGHT
BACK
Operational Behaviors:
UP, DOWN, LEFT, and RIGHT are used for clear directional grid navigation.
OK confirms active text, menu, or list selections.
MENU opens the top-level Main Menu instantly without destroying or clearing the user's active sub-menu position.
BACK navigates to the immediately previous screen, safely restoring the previous item focus to prevent confusion.
PLAY/PAUSE acts as a context-sensitive hardware toggle (for example, switches the lamp ON or OFF).
PREVIOUS and NEXT perform their assigned functions where applicable.
Appearance Note: The visual iPod Click Wheel is purely for nostalgic aesthetics. It must not require or accept rotary sliding or scrolling gestures. All navigation must be completed using predictable click button actions.
State Persistence: Loca Nova must remember the user's last selected device and active menu position, restoring them upon application restart where appropriate.
Consistent Accessibility Color-Coding:
Green: Assigned exclusively to YES, OK, confirmation, or approval actions.
Red: Assigned exclusively to NO, CANCEL, decline, or stop actions.
Blue: Used for recommended, highlighted, or default choices to visually guide the user's focus.
Visual Constraint: To support users with color blindness, colors must always be accompanied by clear text labels or explicit symbols (for example, combining a green block with an explicit ✓ or "OK").
Device-Specific Button Behavior: The same unified button layout must be maintained across all supported device types. Button functions must adapt to the capabilities and requirements of the selected device. The developer must identify and address any technical limitations that could prevent this goal.
Development Approach
Please use your professional skills, experience, and creativity to complete the entire Loca Nova application, following the concept and principles described above.
You have the freedom to choose the most suitable technical solutions and make improvements wherever necessary.
Focus on making the application simple and comfortable to use, especially for elderly people. Provide clear, friendly guidance at every step so users always know what to do next.
Please use familiar and consistent interface elements and navigation patterns throughout the application. Buttons, menus, and actions should behave predictably, so users do not have to figure out how things work every time they open a new screen.
Feel free to use your professional judgment to improve the design and functionality while keeping the application consistent with the original concept.
Please keep in mind that some instructions may contain mistakes or inconsistencies, and correct them in the code where necessary.
7. Main Menu Structure and Device Control
1. Devices: Lists all available registered and connected equipment.
Version 1 Scope: Lamp is the primary operational device. Selecting Devices → Lamp → OK opens the dedicated Lamp Control UI.
The UI displays the active lamp state: ON or OFF.
Pressing PLAY/PAUSE sends the appropriate state-change command. The UI must wait for the actual hardware response through the driver, updating the screen to clearly indicate successful execution or failure. It must never assume success.
2. Drivers: Displays the active driver name, version, and operational status.
3. Settings: Provides global application settings, configuration profiles, and language localization preferences.
4. Security: Allows the user to change authentication levels (Level 1 or Level 2) and manage application and administrator PIN credentials.
7. Network and Connectivity Compatibility
Router Independence: Loca Nova must work across diverse physical network topologies, including standard Wi-Fi routers, local mobile hotspots, and direct peer-to-peer environments, without relying on fixed, static IP addresses or hardcoded router models.
Local Address Independence: Local communication between the application interface and the running Core must not depend on network interface discovery, external IP resolution, or an active local Wi-Fi connection.
Resilient Device Discovery: Device discovery must use methods appropriate to the selected communication technology and device.
For IP-based local networks, alternatives such as UDP broadcasting or local IP subnet scanning may be used where supported and appropriate.
The system must not assume that mDNS, UDP broadcasting, IP subnet scanning, or any single discovery method is available for every connection type or platform.
Graceful Degradation: Handle discovery failures, device dropouts, and connection timeouts safely by prompting the user with friendly error alerts and an easily accessible, prominent RETRY option.
8. Security Framework and Zero-Trust Protocol
Security by Design: Build Loca Nova with encrypted local communication, runtime access controls, strict JSON command validation, and secure cryptographic storage for all local credentials.
Network Isolation: Being connected to the same Wi-Fi router or physical communication medium must never automatically grant access to the system. Every inbound and outbound device-control pipeline must be verified, validated, and authorized at the Core layer, regardless of connection technology.
Credential Isolation: Application entry PINs, administrator PINs, local Wi-Fi infrastructure passwords, and device-specific hardware communication keys must be handled as strictly separate entities. They must never be treated as interchangeable or stored in unencrypted formats.
Privacy Guardrails: Do not expose plain-text credentials or leak cryptographic hashes in local application debugging logs.
9. Data-Driven Architecture (JSON Configurations)
Configuration Over Code: Device capabilities, context-sensitive button behaviors, menu listings, command definitions, parameters, and configuration settings should be described through declarative JSON configuration files wherever practical.
Actual protocol handling and hardware communication must be implemented by the appropriate driver, adapter, or integration code. JSON configuration does not replace executable code when a device requires a new protocol implementation.
Dynamic Command Interpretation: The Core must read these JSON device maps dynamically to bind the 10-button universal virtual iPod control layout to the specific device context.
Updating supported device settings and button interactions should be achievable by adjusting the JSON configuration without rewriting hardcoded conditional logic inside the Core or UI layers.
Adding a device that requires a new communication protocol may also require a suitable new driver, adapter, or integration.
10. Device Pairing
The application must provide a device-pairing process that allows users to securely connect and register compatible devices. The pairing method must depend on the communication technology and capabilities of the target device.
The process must guide the user through the required steps, verify successful pairing, and report whether the device is ready for operation.
The architecture must support different pairing methods without requiring changes to the Core wherever technically possible.
11. Connection Recovery
The application must detect unexpected connection loss and attempt to restore the connection when possible.
The recovery process must:
Detect connection interruptions and communication timeouts.
Attempt reconnection using the appropriate communication method.
Report the connection status to the user.
Avoid treating an unconfirmed command as successfully completed.
Allow the user to retry or manually reconnect when automatic recovery fails.
12. Device Registry
The Core must include a Device Registry responsible for maintaining information about registered devices.
The registry must store and manage relevant device information, including device identity, device type, assigned driver, supported capabilities, communication method, and current connection status.
It must support adding, updating, removing, and retrieving registered devices.
The registry must be designed to support a growing number of different device types without requiring unnecessary changes to the Core.
13. Open Source Delivery and Packaging
The developer must provide the complete application source code under an open-source license and make it available through a public source-code repository.
The developer must also provide a ready-to-install Android package (.apk) for Version 1.
The developer may choose to develop versions for other platforms in future releases, provided that all Android Version 1 requirements are fully met.
The architecture must preserve flexibility for future cross-platform support.
The source code must be published in the public repository only after the project creator has tested and approved the .apk package.
Reference Code and Future Cross-Platform Compatibility
The developer must select the most suitable programming language, framework, and technology for reliable Android development and real hardware control, while preserving flexibility for future communication technologies, including Bluetooth, Wi-Fi, and other suitable methods, as well as future platform support.
The provided Python code is for reference and demonstration purposes only. It is not intended to define or restrict the final application architecture, programming language, framework, or technology selection.
