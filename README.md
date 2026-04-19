# Open Design and Technology  
## Final Project README

> **Project Weight:** 70%  
> **Team Size:** 2 students  
> **Project Duration:** 4 weeks  
> **Class Time Available:** 6 hours per class  
> **Total Time Available:** 48 effort-hours per team  
> **Project Type:** Playful, interactive, technology-based experience

---

# Before you begin

## Fork and rename this repository
After forking this repository, rename it using the format:

`ODT-2026-TeamName`

### Example
`ODT-2026-PixelWizards`

Do not keep the default repository name.

---

# How to use this README

This file is your team’s **working project document**.

You must keep updating it throughout the 4-week build period.  
By the final review, this README should clearly show:
- your idea,
- your planning,
- your design decisions,
- your technical process,
- your build progress,
- your testing,
- your failures and changes,
- your final outcome.

## Rules
- Fill every section.
- Do not delete headings.
- If something does not apply, write `Not applicable` and explain why.
- Add images, screenshots, sketches, links, and videos wherever useful.
- Update task status and weekly logs regularly.
- Use this file as evidence of process, not only as a final report.

---

# 1. Team Identity

## 1.1 Studio / Group Name
`Ratatwang`

## 1.2 Team Members

| Name | Primary Role | Secondary Role | Strengths Brought to the Project |
|---|---|---|---|
| `Rhea` | `App` | `Coding / Electronics` | `[Write here]` |
| `Zanna` | `Mechanics / Fabrication` | `Coding / Electronics` | `Fair understanding of 3D printing and laser cutting. Similarly, can visualise and iterate mechanics and the calculations needed (if necessary). Comfortable working with varied materials. Technical understanding of circuits and basic code logic. Can work within deadlines and in teams` |

## 1.3 Project Title
`Eye Spy`

## 1.4 One-Line Pitch
`The all-seeing eye decides your fate as you're on the clock to find the colour that it displays. Will you spy or will you die?` 

## 1.5 Expanded Project Idea

In 1–2 paragraphs, explain:
- what your project is,
- what kind of playful experience it creates,
- what makes it fun, curious, engaging, strange, satisfying, competitive, or delightful,
- What technologies are involved?

**Response:**  
`[The All-Seeing Eye: Race a watchful, glowing eye to guess its secret colour before a 60-second timer dooms you—spy right or "die" in silly chaos!
]`

---

# 2. Philosophy Fit

## 2.1 Experience, Not Social Problem
This module does **not** require your project to solve a large social problem.

You are allowed to build:
- toys,
- games,
- interactive objects,
- playful machines,
- kinetic artefacts,
- humorous devices,
- strange but delightful experiences,
- things that are entertaining to use or watch.

## 2.2 What kind of experience are you creating?
Answer the following:
- What is the experience?
- What do you want the player or participant to feel?
- Why would someone want to try it again?

**Response:**  
`The object we are building is a game for playful interaction. Inspired by common experiences of playing 'eye spy' (especially on car trips), we want the players to feel the same adrenaline of finding an appropriate object, anticipation of figuring out whether they've succeeded, and joy if they have.`

## 2.3 Design Persona
Complete the sentence below:

> We are designing this project as if we are a small creative studio making a **[toy/game / playable object / interactive experience]** for **[children / teens / adults/classmates / exhibition visitors / mixed audience]**.

**Response:**  
`[We are designing this project as if we are a small creative studio making a **[game]** for **[ whimsical exhibition visitors of mixed age ranges]`

---

# 3. Inspiration

## 3.1 References
List what inspired the project.

| Source Type | Title / Link | What Inspired You |
|---|---|---|
| `Toy` | `I Spy` | `We took inspiration from the game theory of this game to implement into our play` |
| `Object` | `Animatronic Servo Eyes` | `We took inspiration from the physical structures of these eyes for our fabrication` 
|||`Links for inspo and 3d print models: https://youtu.be/5bfzqe0QXRg?si=PoGbVW39JObyZQRv https://youtu.be/lPpexsNYKsE?si=GfHDR3qoW0oU5YEM `|

## 3.2 Original Twist
What makes your project original?

**Response:**  
`Typically, _I spy_ is played with one correct answer (an object) based on various factors, one of which includes colour. Our game emphasises one element, colour, as the determining factor. To add complexity, the game makes the player remember the colour they are trying to find. This forces them to compromise between what they can find and for how long they can remember. The game does provide some respite by not having one specific answer, rather a range in which any object whose colour falls in that range is applicable.`

---

# 4. Project Intent

## 4.1 Core Interaction Loop
Describe the main loop of interaction.

Examples:
- press → launch → score → reset
- connect → control → observe → repeat
- turn → trigger → react → repeat
- move object → sensor detects → sound/light response → player reacts

**Response:**  
`[press → colour flashes → observe → input photo → photo is processed → stage completion]`

## 4.2 Intended Player / Audience

| Question | Response |
|---|---|
| Who is this for? | `[whimsical exhibit visitors]` |
| Age range | `[12-25]` |
| Solo or multiplayer | `[solo]` |
| Expected duration of one round | `[60 seconds]` |
| What should the player feel? | `[excitement, environmetal observance]` |
| Is explanation required before use? | `[a brief explanation on the rules of the game is required, including how they must take photos and winning criteria]` |

## 4.3 Player Journey
Describe exactly how a player will use the project.

1. **Approach:** `[How does the player first encounter it?]`
2. **Start:** `[How do they begin?]`
3. **First Action:** `[What do they do first?]`
4. **Main Interaction:** `[What keeps happening during use?]`
5. **System Response:** `[How does the project respond?]`
6. **Win / Lose / End Condition:** `[How does one round end?]`
7. **Reset:** `[How does the next round begin?]`

## 4.4 Rules of Play
If your project is a game, list the rules clearly.

- `[Wait for the Neopixel to flash a colour before finding an object]`
- `[You must take photos live and not select those from your library (not an option provided on the MIT app)]`
- `[Users only get a point if they identify the colour accurately]`
- `[Rule 4]`

---

# 5. Definition of Success

## 5.1 Definition of “Playable”
Your project will be considered complete only if these conditions are met.

- [ ] `[The sequence of interaction loop occours seamlesly]`
- [ ] `[The hex codes are accurately analysed and processed by the esp32]`
- [ ] `[The code rejects any colour that does not match that flashed by the neopixel]`
- [ ] `[Condition 4]`
- [ ] `[Condition 5]`

## 5.2 Minimum Viable Version
What is the smallest version of this project that still delivers the core experience?

**Response:**  
`[The compact version features a NeoPixel that flashes a colour. Users snap a photo of a matching shade, which gets processed for scoring points.]`

## 5.3 Stretch Features
What features are nice to have but not essential?

- `[Two movable eyes that both flash colours for users to play with where the two eyes could flash different colours, making it a multiplayer game]`
- `[An app UI that matches the overall aesthetic of the game we intent to make]`
- `[Sound feedbacks everytime a player wins or loses]`

---

# 6. System Overview

## 6.1 Project Type
Check all that apply.

- [x] Electronics-based
- [x] Mechanical
- [ ] Sensor-based
- [x] App-connected
- [x] Motorized
- [ ] Sound-based
- [x] Light-based
- [ ] Screen/UI-based
- [ ] Fabricated structure
- [x] Game logic based
- [x] Installation/tabletop experience
- [ ] Other: `[Write here]`

## 6.2 High-Level System Description
Explain how the system works in simple terms.

Include:
- input,
- processing,
- output,
- physical structure,
- app interaction, if any.

**Response:**  
`[Write here]`

## 6.3 Input / Output Map

| System Part | Type | What It Does |
|---|---|---|
| `[Switch / App Input]` | Input | `Triggers of the initiation of the game in order for the colour to first flash and then receive data.` |
| `[ESP32 / Controller]` | Processing | `Contains code of electronic elements as well as processes for data sent from the app` |
| `[LED / Motor / Servo / Buzzer / Display]` | Output | `Servo opens/ closes eyelids; LED flashes the appropriate colours` |
| `[Mechanical Assembly]` | Physical Action | `Eyelids open and close` |

---

# 7. Sketches and Visual Planning

## 7.1 Concept Sketch
Add an early sketch of the full idea.

**Insert image below:**  
`(https://github.com/rheapaul123/ODT-2026-Ratatwang/blob/848389ac231660e972e53168771c3d192a1e8bde/images/first%20draft%20of%20Eye%20Spy.jpeg)`

Example:
```md

```

## 7.2 Labeled Build Sketch
Add a sketch with labels showing:
- structure,
- electronics placement,
- user touch points,
- moving parts,
- output elements.

**Insert image below:**  
`[Upload image and link here]`

## 7.3 Approximate Dimensions

| Dimension | Value |
|---|---|
| Length | `37cm` |
| Width | `21cm` |
| Height | `27cm` |
| Estimated weight | `~1.7kg` |
|Estimates given considering box along with eye model| Diameter of the eye model: 14cm|

---

# 8. Mechanical Planning

## 8.1 Mechanical Features
Check all that apply.

- [ ] Gears
- [ ] Pulleys
- [ ] Belt drives
- [x] Linkages
- [x] Hinges
- [ ] Shafts
- [ ] Springs
- [ ] Bearings
- [ ] Wheels
- [ ] Sliders
- [x] Levers
- [ ] Not applicable

## 8.2 Mechanical Description
Describe the mechanism and what it is meant to do.

**Response:**  
The mechanism is meant to mirror that of eyelids closing over an eyeball. In this case, 2 eyelids conceal or reveal an iris (Neopixel ring) for the game to commence. 

## 8.3 Motion Planning
If something moves, explain:
- what moves,
- what causes the movement,
- how far it moves,
- how fast it moves,
- what could go wrong.

**Response:**  
`Eyelids`
`What moves: Two curved, shells that rotate in opposing directions to close over the eyeball (Neopixel) and back up to open.`
`What causes it: A dedicated servo pushes a pushrod (a rigid link) that is connected to the back edge of the lid. As the servo arm rotates, the rod pushes the lid closed and vice versa.`
`How far: ~20–40° of arc at the lid pivot, enough to go from fully open to fully closed over the eyeball surface.`
`How fast: ~0.10 to 0.20s for the motion, with the added friction of the eyelids this could increase slightly`
`What could go wrong:`
`Lid catches on the eyeball surface, which isn't ideal for the eyelids, servo or Neopixel`
`The pushrod connection point cracks`
`Lids don't close symmetrically if their linkage doesn't act with simultaneous action`

`Pushrods`
`What moves: A rigid wire or printed rods makes the rotational arc of the servo into a linear push/pull force.`
`What causes it: A physical pulls or pushes the end of the rod, where the eyelids are attached.`
`How far: Though the rod doesn't bend it causes a displacement of the eyeball with an approximate of 3–8 mm of linear travel.`
`How fast: Moves at the same speed as the servo horn tip — no mechanical advantage or disadvantage, roughly 30–80 mm/s during a typical eye movement.`
`What could go wrong:`
`If the rod is too long it will buckle and possible snap`
`If the part where it is attached is not precise enough, the translation of force/ movement will be inefficient`
`Vibration causes the rod to bounce out of its clip if the fit is not snug`

## 8.4 Simulation / CAD / Animation Before Making
If your project includes mechanical motion, document the digital planning before fabrication.

| Tool Used | File / Link | What Was Tested |
|---|---|---|
| `Blender` | `https://github.com/rheapaul123/ODT-2026-Ratatwang/blob/68a651c6242b7b92f2233504ef28817ee9066fbd/images/Screenshot%20of%203D%20model%20-%20Eyelids%20%2B%20Arms.png` | `Since the eyelids were sourced from an external link (https://www.thingiverse.com/thing:1877417), the eyelid/ blinking motion were more-or-less confirmed. The crank, however, had to be modified and created directly on blender. Viewing the lever over where the crank would pivot confirmed this. However, in our test printing before the final printing, more tolerance was created to account for the added material that does not fully sand off from the supports.` |
| `Blender Model to Cura` | `https://github.com/rheapaul123/ODT-2026-Ratatwang/blob/054277c34ad22f9eb690615fb1478c9285b80c08/images/First%20Cura%20File%20-%20Sample%20Print.png` | `A picture of the initial model before scaling on Cura (changes were saved after on Blender, so the ss is from Cura). The software helped verify any gaps that could be in the build since that was an issue with a previously sourced file. It also helped verify the viability of the print.` |

## 8.5 Changes After Digital Testing
What changed after the CAD, animation, or simulation stage?

**Response:**  
`The first file revealed the importance of a well made model for printing especially. After printing the sample, more contingencies were considered for the tolerances. Also, the simulation (and later printing), did verify that when the eyelids are closed, there will be a gap between the eye and the box surface when viewed from the sides (or top and bottom) since the frame outside moves with the eyelids so that the arms can be attached externally and more easily to one Servo motor.`

---

# 9. Electronics Planning

## 9.1 Electronics Used

| Component | Quantity | Purpose |
|---|---:|---|
| `[ESP32]` | `1` | `[Main controller]` |
| `Servo Motor` | `2` | `Controls eyeball movement` |
| `Neopixel` | `1` | `Flashes the colour(s) that the player needs to find` |
| `Switch` | `1` | `Initiate the game` |

## 9.2 Wiring Plan
Describe the main electrical connections.

**Response:**  
`The ESP32 is connected to a breadboard power supply (which draws power from a wall socket). On the 3.3V end, a Neopixel is connected, with an assigned pin and a grounded wire. The same is done with the motor, however, to 5V instead of 3.3V.`

## 9.3 Circuit Diagram
Insert a hand-drawn or software-made circuit diagram.

**Insert image below:**  
`[Upload image and link here]`

## 9.4 Power Plan

| Question | Response |
|---|---|
| Power source | `Adaptor` |
| Voltage required | `5V for Servo(s), and 3.3V for the Neopixels` |
| Current concerns | `Grounding is not fully/ properly connected, causing short circuiting` |
| Safety concerns | `Since there are suspended elements (neopixel and servos to a support), the wires should not interwine and get snagged. Also ESP32s have potential, unexpected movement due to Wi-Fi/Bluetooth interference as well as possible power management issues- posing risks.` |

---

# 10. Software Planning

## 10.1 Software Tools

| Tool / Platform | Purpose |
|---|---|
| `[MicroPython / Arduino / MIT App Inventor / CAD tool / other]` | `[Purpose]` |
| `[MicroPython (via Thonny IDE)]` | `[Writing and uploading code to ESP32]` |
| `[MIT App Inventor]` | `[Mobile app to send RGB guesses via Bluetooth]` |
| `[HC-05 Bluetooth Module]` | `[Wireless serial communication between app and ESP32]` |
| `[NeoPixel Library]` | `[Control RGB LED (eye pupil colour display)]` |
| `[PWM (MicroPython)]` | `[Control servo motor for eyelid movement]` |
| `[Blender + Cura Software]` | `[Making the 3D print of eylids]` |
| `[Adobe Illustrator + Rhino 3D]` | `[Making the box for laser cutting]` |

## 10.2 Software Logic
Describe what the code must do.

Include:
- startup behavior,
- input handling,
- sensor reading,
- decision logic,
- output behavior,
- communication logic,
- reset behavior.

**Response:**  
`[
**Startup Behavior**
Initialize NeoPixel LED (turned OFF initially)
Initialize UART communication with HC-05 Bluetooth module
Initialize servo motor and set eyelids to OPEN position
Send “Eye Spy ready!” message via Bluetooth 
**Input Handling**
Continuously listen for incoming Bluetooth data
Accept user input in the format: R,G,B
Store incoming data in a buffer until a newline character is received
**Sensor / Input Reading**
Parse received Bluetooth string into integer RGB values
Validate input format (must contain exactly 3 values)
Ignore invalid or malformed inputs
**Decision Logic**
Randomly select a target colour from predefined palette
Convert hex colour to RGB format
Calculate Euclidean distance between:
Target colour
User’s guessed colour
Compare distance with predefined threshold
**Output Behavior**
Display target colour by flashing NeoPixel
Close eyelids (servo rotates) during user input phase
Reopen eyelids when guess is received
If guess is correct (distance ≤ threshold):
Flash green light multiple times
Send “PASS” via Bluetooth
Restart game loop
If guess is incorrect:
Flash red light multiple times
Send “FAIL” via Bluetooth
Turn off LED
Stop the game
**Communication Logic**
Send messages to mobile app:
TARGET:#XXXXXX
WAITING
PASS or FAIL
Receive RGB guesses via Bluetooth UART
**Reset Behavior**
Game continues automatically after a correct guess
Game terminates after incorrect guess
Requires manual reset (restart ESP32) to play again]`

## 10.3 Code Flowchart
Insert a flowchart showing your code logic.

Suggested sequence:
- start,
- initialize,
- wait for input,
- read input,
- decision,
- trigger output,
- repeat or reset,
- error handling.

**Insert image below:**  
`[<img width="539" height="517" alt="Screenshot 2026-04-14 at 10 20 08 AM" src="https://github.com/user-attachments/assets/4bffa2b8-094e-4426-82ae-f5ddb741a28a" />]`

## 10.4 Pseudocode

```text
[START

INITIALIZE NeoPixel
INITIALIZE Servo
INITIALIZE Bluetooth UART

SET eyes to OPEN

PRINT "Eye Spy ready"
SEND "Eye Spy ready" via Bluetooth

WHILE game is running:

    SELECT random colour from palette
    CONVERT hex to RGB

    PRINT and SEND target colour

    OPEN eyes
    FLASH target colour

    TURN OFF LED
    CLOSE eyes
    SEND "WAITING"

    SET guess = null

    WHILE guess not received:
        READ Bluetooth input
        IF valid RGB received:
            STORE guess
            OPEN eyes

    CALCULATE distance between target and guess

    IF distance <= threshold:
        PRINT "PASS"
        OPEN eyes
        FLASH green
        SEND "PASS"
        CONTINUE game loop

    ELSE:
        PRINT "FAIL"
        OPEN eyes
        FLASH red
        SEND "FAIL"
        TURN OFF LED
        STOP game

END

PRINT "Game ended"]
```

---

# 11. MIT App Inventor Plan

## 11.1 Is an app part of this project?
- [x] Yes
- [ ] No

If yes, complete this section.

## 11.2 Why is the app needed?
Explain what the app adds to the experience.

Examples:
- remote control,
- score tracking,
- mode selection,
- personalization,
- triggering effects,
- displaying data.

**Response:**  
`[The mobile application is essential for enabling user interaction with the game, as the ESP32 system itself has no direct input interface.
The app allows the player to:
Send colour guesses wirelessly via Bluetooth in RGB format
Act as the primary input system for gameplay
Provides an intuitive colour selection interface (through colour picker)]`

## 11.3 App Features

| Feature | Purpose |
|---|---|
| `[BBluetooth Client (Non-visible)]` | `[Handles wireless communication between app and ESP32]` |
| `[Canvas]` | `[Allows user interaction or colour selection (touch-based input if used)]` |
| `[Camera (Non-visible)]` | `[Captures real-world colours for gameplay input]` |
| `[Take Picture Button]` | `[Opens camera interface to capture an image]` |
| `[RGB Input (Color Picker)]` | `[Allows user to select a colour guess]` |
| `[Colour Preview Square]` | `[Displays the currently selected/picked colour visually]` |
| `[RGB Value Label]` | `[Shows the exact RGB values of the selected colour]` |
| `[Confirm Colour Button]` | `[Sends the selected RGB values to ESP32 via Bluetooth]` |


## 11.4 UI Mockup
Insert a sketch or screenshot of the app interface.

**Insert image below:**  
`[Upload image and link here]`

## 11.5 App Screen Flow

1. `[ ]`
2. `[Step 2]`
3. `[Step 3]`
4. `[Step 4]`

---

# 12. Bill of Materials

## 12.1 Full BOM

| Item | Quantity | In Kit? | Need to Buy? | Estimated Cost | Material / Spec | Why This Choice? |
|---|---:|---|---|---:|---|---|
| `[ESP32]` | `1` | `Yes` | `Yes` | `1` | `[Spec]` | `370/Unit` | `Our ESP32 was heating up and causing problems` |
| `Microservo` | `2` | `Yes` | `Yes` | `142/Unit` | `SG 90 9G Mini Micro Servo plastic gear` | `[The ones in kit are all fried]` |
| `Neopixel Ring` | `2` | `Yes` | `Yes` | `116/Unit` | `16Bit WS2812B 5050 RGB LED Built-in Full Color Driving Lights Circular Development Board` | `Also fried` |
| `Skewers` | `1` | `No` | `[Yes` | `90/Pack` | `Bamboo` | `Hinge/ pivot for our eye` |

## 12.2 Material Justification
Explain why you selected your main materials and components.

Examples:
- Why acrylic instead of cardboard?
- Why MDF instead of 3D print?
- Why servo instead of DC motor?
- Why bearing instead of a plain shaft hole?

**Response:**  
`The eyelid was printed using PLA filament in order to be light weight (since the micro servo has limited torque) and to leverage the advantage of having existing models on the internet. The outside box was laser cut for effeciency, cleanliness, sturdiness and since the colour matched with the eye (making it seem like a box of skin of sorts). The levers were changed from PLA to GI wire to more easily vary the arm length (in order to maximise torque). A smaller gauge GI wire was put through the holes of the servo horns in order to reduce gaps and ineffeciencies of the same. A servo motor had the most torque among the motors that were there (DC, stepper) while no being too powerful to break the arms/ model. The angles that motor arm needs to open are also within 180 and at a slower rate.`

## 12.3 Items to Purchase Separately

| Item | Why Needed | Purchase Link | Latest Safe Date to Procure | Status |
|---|---|---|---|---|
| `Microservo` | `To move the eye` | `Through Anish and Tejas who ordered from Robu` | `15 Apr 2026` | `Received` |
| `Neopixel Ring` | `Ours was fried, ` | `(https://robu.in/product/16bit-ws2812b-5050-rgb-led-built-in-full-color-driving-lights-circular-development-board/?gad_source=1&gad_campaignid=17416544847&gclid=CjwKCAjwtIfPBhAzEiwAv9RTJvOMW2sC-M2FHE5gaLiex870LlnY4tKtAvi3_e03yqkNnou4FeMPEBoCSfMQAvD_BwE)` | `19 Apr 2026 - mostly tested on the strip` | `Received` |

## 12.4 Budget Summary

| Budget Item | Estimated Cost |
|---|---:|
| Electronics | `770` |
| Mechanical parts | `NA` |
| Fabrication materials | `NA` |
| Purchased extras | `60` |
| Contingency | `142 (1 neopixel ring)` |
| **Total** | `946` |

## 12.5 Budget Reflection
If your cost is too high, what can be simplified, removed, substituted, or shared?

**Response:**  
`NA. If anything, we could have possibly sufficed with our old ESP32 (largest cost incurred) but it was heating up too much.`

---

# 13. Planning the Work

## 13.1 Team Working Agreement
Write how your team will work together.

Include:
- how tasks are divided,
- how decisions are made,
- how progress will be checked,
- what happens if a task is delayed,
- how documentation will be maintained.

**Response:**  
`[Write here]`

## 13.2 Task Breakdown

| Task ID | Task | Owner | Estimated Hours | Deadline | Dependency | Status |
|---|---|---|---:|---|---|---|
| T1 | `[Finalize concept]` | `[Name]` | `2` | `[Date]` | `None` | `To Do` |
| T2 | `[Complete BOM]` | `[Name]` | `1` | `[Date]` | `T1` | `To Do` |
| T3 | `[Test electronics]` | `[Name]` | `2` | `[Date]` | `T1` | `To Do` |
| T4 | `[Build structure]` | `[Name]` | `4` | `[Date]` | `T1` | `To Do` |
| T5 | `[Write control code]` | `[Name]` | `4` | `[Date]` | `T3` | `To Do` |
| T6 | `[Integrate system]` | `[Name]` | `4` | `[Date]` | `T4, T5` | `To Do` |
| T7 | `[Playtest]` | `[Name]` | `2` | `[Date]` | `T6` | `To Do` |
| T8 | `[Refine and document]` | `[Name]` | `3` | `[Date]` | `T7` | `To Do` |

## 13.3 Responsibility Split

| Area | Main Owner | Support Owner |
|---|---|---|
| Concept and gameplay | `[Name]` | `[Name]` |
| Electronics | `[Name]` | `[Name]` |
| Coding | `[Name]` | `[Name]` |
| App | `Rhea` | `Zanna` |
| Mechanical build | `Zanna` | `Rhea` |
| Testing | `[Name]` | `[Name]` |
| Documentation | `[Name]` | `[Name]` |

---

# 14. Weekly Milestones

## 14.1 Four-Week Plan

### Week 1 — Plan and De-risk
Expected outcomes:
- [x] Idea finalized
- [x] Core interaction decided
- [x] Sketches made
- [x] BOM completed
- [x] Purchase needs identified
- [x] Key uncertainty identified
- [x] Basic feasibility tested

### Week 2 — Build Subsystems
Expected outcomes:
- [x] Electronics tests completed
- [x] CAD/structure planning completed
- [x] App UI started if needed
- [x] Mechanical concept tested
- [x] Main subsystems partially working

### Week 3 — Integrate
Expected outcomes:
- [x] Physical body built
- [x] Electronics integrated
- [ ] Code connected to hardware
- [x] App connected if required
- [ ] First playable version exists

### Week 4 — Refine and Finish
Expected outcomes:
- [ ] Technical bugs reduced
- [ ] Playtesting completed
- [ ] Improvements made
- [ ] Documentation completed
- [ ] Final build ready

## 14.2 Weekly Update Log

| Week | Planned Goal | What Actually Happened | What Changed | Next Steps |
|---|---|---|---|---|
| Week 1 | `[Write here]` | `[Write here]` | `[Write here]` | `[Write here]` |
| Week 2 | `[Write here]` | `[Write here]` | `[Write here]` | `[Write here]` |
| Week 3 | `[Write here]` | `[Write here]` | `[Write here]` | `[Write here]` |
| Week 4 | `[Write here]` | `[Write here]` | `[Write here]` | `[Write here]` |

---

# 15. Risks and Unknowns

## 15.1 Risk Register

| Risk | Type | Likelihood | Impact | Mitigation Plan | Owner |
|---|---|---|---|---|---|
| `[Example: Bluetooth disconnects]` | `Technical` | `Medium` | `High` | `[Fallback interaction / simplify connection flow]` | `[Name]` |
| `[Example: Structure breaks during play]` | `Mechanical` | `Medium` | `High` | `[Reinforce joints / change material]` | `[Name]` |
| `[Risk]` | `[Technical / Material / Time / Gameplay]` | `[Low/Medium/High]` | `[Low/Medium/High]` | `[Plan]` | `[Name]` |
| `[Risk]` | `[Type]` | `[Low/Medium/High]` | `[Low/Medium/High]` | `[Plan]` | `[Name]` |

## 15.2 Biggest Unknown Right Now
What is the single biggest uncertainty in your project at this stage?

**Response:**  
`[Write here]`

---

# 16. Testing and Playtesting

## 16.1 Technical Testing Plan

| What Needs Testing | How You Will Test It | Success Condition |
|---|---|---|
| `[Bluetooth connection]` | `[Method]` | `[What counts as success?]` |
| `[Mechanism movement]` | `[Method]` | `[What counts as success?]` |
| `[Sensor behavior]` | `[Method]` | `[What counts as success?]` |
| `[App communication]` | `[Method]` | `[What counts as success?]` |

## 16.2 Playtesting Plan

| Question | How You Will Check |
|---|---|
| Do players understand what to do? | `[Method]` |
| Is the interaction satisfying? | `[Method]` |
| Do players want another turn? | `[Method]` |
| Is the challenge balanced? | `[Method]` |
| Is the response clear and immediate? | `[Method]` |

## 16.3 Testing and Debugging Log

| Date | Problem Found | Type | What You Tried | Result | Next Action |
|---|---|---|---|---|---|
| `[Date]` | `[Describe issue]` | `[Technical / Mechanical / UI / Gameplay]` | `[What you did]` | `[Worked / Partly / Failed]` | `[Next step]` |
| `[Date]` | `[Describe issue]` | `[Type]` | `[What you did]` | `[Result]` | `[Next step]` |

## 16.4 Playtesting Notes

| Tester | What They Did | What Confused Them | What They Enjoyed | What You Will Change |
|---|---|---|---|---|
| `[Peer / friend / classmate]` | `[Observation]` | `[Observation]` | `[Observation]` | `[Action]` |
| `[Peer / friend / classmate]` | `[Observation]` | `[Observation]` | `[Observation]` | `[Action]` |

---

# 17. Build Documentation

## 17.1 Fabrication Process
Describe how the project was physically made.

Include:
- cutting,
- 3D printing,
- assembly,
- fastening,
- wiring,
- finishing,
- revisions.

**Response:**  
`[Write here]`

## 17.2 Build Photos
Add photos throughout the project.

Suggested images:
- early sketch,
- prototype,
- electronics testing,
- mechanism test,
- app screenshot,
- final build.

Example:
```md



```

## 17.3 Version History

| Version | Date | What Changed | Why |
|---|---|---|---|
| `v1` | `[Date]` | `[Describe]` | `[Reason]` |
| `v2` | `[Date]` | `[Describe]` | `[Reason]` |
| `v3` | `[Date]` | `[Describe]` | `[Reason]` |

---

# 18. Final Outcome

## 18.1 Final Description
Describe the final version of your project.

**Response:**  
`[Write here]`

## 18.2 What Works Well
- `[Point 1]`
- `[Point 2]`
- `[Point 3]`

## 18.3 What Still Needs Improvement
- `[Point 1]`
- `[Point 2]`
- `[Point 3]`

## 18.4 What Changed From the Original Plan
How did the project change from the initial idea?

**Response:**  
`[Write here]`

---

# 19. Reflection

## 19.1 Team Reflection
What did your team do well?  
What slowed you down?  
How well did you manage time, tasks, and responsibilities?

**Response:**  
`[Write here]`

## 19.2 Technical Reflection
What did you learn about:
- electronics,
- coding,
- mechanisms,
- fabrication,
- integration?

**Response:**  
`[Write here]`

## 19.3 Design Reflection
What did you learn about:
- designing for play,
- delight,
- clarity,
- physical interaction,
- player understanding,
- iteration?

**Response:**  
`[Write here]`

## 19.4 If You Had One More Week
What would you improve next?

**Response:**  
`[Write here]`

---

# 20. Final Submission Checklist

Before submission, confirm that:
- [ ] Team details are complete
- [ ] Project description is complete
- [ ] Inspiration sources are included
- [ ] Player journey is written
- [ ] Sketches are added
- [ ] BOM is complete
- [ ] Purchase list is complete
- [ ] Budget summary is complete
- [ ] Mechanical planning is documented if applicable
- [ ] App planning is documented if applicable
- [ ] Code flowchart is added
- [ ] Task breakdown is complete
- [ ] Weekly logs are updated
- [ ] Risk register is complete
- [ ] Testing log is updated
- [ ] Playtesting notes are included
- [ ] Build photos are included
- [ ] Final reflection is written

---

# 21. Suggested Repository Structure

```text
project-repo/
├── README.md
├── images/
│   ├── concept-sketch.jpg
│   ├── labeled-sketch.jpg
│   ├── circuit-diagram.jpg
│   ├── ui-mockup.jpg
│   ├── prototype-1.jpg
│   └── final-build.jpg
├── code/
│   ├── main.py
│   ├── test_code.py
│   └── notes.md
├── cad/
│   ├── models/
│   └── screenshots/
└── docs/
    ├── references.md
    └── extra-notes.md
```

---

# 22. Instructor Review

## 22.1 Proposal Approval
- [ ] Approved to proceed
- [ ] Approved with changes
- [ ] Rework required before proceeding

**Instructor comments:**  
`[Instructor fills this section]`

## 22.2 Midpoint Review
`[Instructor fills this section]`

## 22.3 Final Review Notes
`[Instructor fills this section]`
