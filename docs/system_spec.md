# SmartGuard — System Specification (v0.1)

## Overview
SmartGuard is an edge-AI safety and posture monitoring system designed to support wheelchair users by detecting risky sitting postures and potential fall events. The system runs on low-cost hardware (Raspberry Pi + camera) and triggers alerts when predefined risk conditions are met.

This document summarizes the current system scope (v0.1) and the engineering assumptions behind the prototype.

---

## Goals
- Detect abnormal posture patterns that may indicate discomfort, sliding, or unsafe posture.
- Detect fall-like events (e.g., sudden posture collapse/out-of-frame behavior) as a safety signal.
- Run inference on-device (edge) to reduce latency and protect privacy.
- Provide fast alerts (buzzer and/or caregiver notification).

---

## Non-Goals (v0.1)
- Not a medical device or diagnostic tool.
- Not intended to replace clinical assessment or caregiver supervision.
- Not tuned for every wheelchair type, seating configuration, or mobility pattern.

---

## Hardware
- **Compute:** Raspberry Pi 5 (or similar)
- **Camera:** Raspberry Pi camera module / Arducam (supported configurations vary)
- **Alert options:**
  - Buzzer (GPIO)
  - SMS/phone notification (future integration)
  - Caregiver dashboard (future)

---

## Core Pipeline (Conceptual)
1. Capture frames from camera (e.g., 10–30 FPS depending on hardware).
2. Run pose estimation (e.g., MediaPipe / MoveNet) to obtain keypoints.
3. Compute posture signals (angles, symmetry, displacement, head/torso alignment).
4. Apply risk logic rules (thresholds + time smoothing).
5. Trigger alerts when risk persists beyond a configured duration.

---

## Posture Signals (examples)
- Torso lean angle (left/right, forward/backward proxy)
- Head/neck alignment relative to torso
- Shoulder symmetry
- Hip-to-shoulder alignment stability
- Sudden changes over short time windows (fall-like patterns)

---

## Alert Logic (v0.1)
Alerts are rule-based and intentionally conservative:
- **Posture risk alert**: posture score crosses threshold for *N* consecutive frames/seconds.
- **Fall-risk alert**: sudden posture collapse or keypoints disappear abruptly for a short window.

The logic should be configurable via a simple config file (thresholds and timing).

---

## Privacy & Safety Notes
- Prefer **on-device inference** and avoid uploading frames by default.
- If logging is enabled for debugging, store locally and keep retention minimal.
- Ensure opt-in consent if any real user data is recorded.

---

## Limitations & Risks
- Performance depends on lighting, camera angle, occlusions, and clothing.
- Pose estimation can fail on partial views or unusual seating positions.
- False positives are possible; thresholds should be tuned per setup.
- Real-world validation requires careful testing and safety review.

---

## Next Steps (Roadmap)
- Add calibration mode (set baseline posture per user/setup).
- Add temporal smoothing and simple anomaly detection on keypoint trajectories.
- Expand alert channels (SMS/caregiver app).
- Evaluate under varied lighting and seating configurations.
- Optional: multimodal sensors (IMU/pressure sensors) for robustness.
