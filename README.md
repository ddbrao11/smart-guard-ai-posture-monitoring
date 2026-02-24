# smart-guard-ai-posture-monitoring
Human-centered AI safety system.

## Research Notes
This repository represents ongoing independent research exploration.
Detailed methodology: [docs/methodology.md](docs/methodology.md)
- System spec: docs/system_spec.md
- Demo (runnable stub): scripts/demo_pose_stub.py

## Run the Demo (v0.1)
```bash
python scripts/demo_pose_stub.py  

## Research Overview
SmartGuard explores edge-based AI systems for real-time
posture monitoring and safety detection for wheelchair users.

The project investigates how computer vision models can
operate efficiently on low-cost embedded hardware.

## Research Motivation
Assistive AI technologies can improve accessibility,
reduce injury risk, and support independent living.

## Research Questions
- Can real-time pose estimation detect unsafe posture reliably?
- How can edge AI enable low-cost assistive systems?
- What design patterns support accessible AI deployment?

## Approach
Pose estimation models integrated with edge computing hardware,
real-time analysis pipelines, and alert mechanisms.

## Limitations
Lighting conditions, camera positioning, and user variability
may affect detection accuracy.

## System Architecture (Conceptual)
```text
Camera Feed
   ↓
Pose Estimation (MoveNet / MediaPipe)
   ↓
Posture & Fall-Risk Logic
   ↓
Alerts (Buzzer / SMS / Caregiver Notification)
```

## Privacy & Safety Notes
SmartGuard is designed for edge inference where possible to reduce data exposure. Future work includes configurable data retention and opt-in logging for clinical or caregiver workflows.




