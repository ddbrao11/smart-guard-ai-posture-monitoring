"""
SmartGuard v0.1 — Demo Stub (runs without a camera)

Purpose:
- Provide a runnable demo artifact for the repo
- Simulate posture signals and risk scoring
- Show how alerts would be triggered with simple time-smoothing logic

This is intentionally a stub so the repo remains lightweight.
Replace the simulated keypoints with real pose estimation output
(MediaPipe/MoveNet) in future versions.
"""

from dataclasses import dataclass
import random
import time


@dataclass
class PostureSignals:
    torso_lean_deg: float     # magnitude of lean (0 = upright)
    asymmetry_score: float    # 0..1
    keypoints_conf: float     # 0..1 (proxy for pose quality)


def simulate_pose_signals(t: int) -> PostureSignals:
    """
    Simulate posture signals.
    - Mostly stable posture with small noise
    - Occasionally inject a "risky posture" segment
    """
    # baseline noise
    torso_lean = max(0.0, random.gauss(6.0, 2.0))
    asym = min(1.0, max(0.0, random.gauss(0.08, 0.04)))
    conf = min(1.0, max(0.0, random.gauss(0.92, 0.05)))

    # inject a risky segment every ~25 steps
    if 25 <= t <= 32:
        torso_lean = random.uniform(22.0, 35.0)
        asym = random.uniform(0.35, 0.7)
        conf = random.uniform(0.75, 0.95)

    # inject a "fall-like" segment (low confidence / missing keypoints)
    if 45 <= t <= 47:
        conf = random.uniform(0.05, 0.25)

    return PostureSignals(torso_lean_deg=torso_lean, asymmetry_score=asym, keypoints_conf=conf)


def posture_risk_score(sig: PostureSignals) -> float:
    """
    Combine signals into a simple risk score (0..1).
    This is intentionally transparent and rule-friendly.
    """
    lean_component = min(1.0, sig.torso_lean_deg / 30.0)          # 30 degrees ~ high risk
    asym_component = min(1.0, sig.asymmetry_score / 0.6)          # 0.6 ~ high asymmetry
    conf_penalty = 1.0 - sig.keypoints_conf                       # low confidence increases risk

    # weighted sum (tunable)
    score = 0.55 * lean_component + 0.30 * asym_component + 0.15 * conf_penalty
    return max(0.0, min(1.0, score))


def main():
    print("SmartGuard v0.1 demo stub — starting simulation...\n")

    # thresholds (tunable)
    POSTURE_RISK_THRESHOLD = 0.65
    FALL_CONF_THRESHOLD = 0.25

    # simple smoothing: require risk for N consecutive ticks
    REQUIRED_CONSECUTIVE = 3
    consecutive_risky = 0

    for t in range(1, 61):
        sig = simulate_pose_signals(t)
        score = posture_risk_score(sig)

        # fall-like condition: keypoints confidence collapses
        fall_like = sig.keypoints_conf < FALL_CONF_THRESHOLD

        if fall_like:
            print(f"[t={t:02d}] FALL-RISK ALERT: keypoints confidence={sig.keypoints_conf:.2f}")
            consecutive_risky = 0
        else:
            if score >= POSTURE_RISK_THRESHOLD:
                consecutive_risky += 1
            else:
                consecutive_risky = 0

            status = "RISKY" if score >= POSTURE_RISK_THRESHOLD else "OK"
            print(
                f"[t={t:02d}] {status} | risk_score={score:.2f} | "
                f"lean={sig.torso_lean_deg:.1f}deg | asym={sig.asymmetry_score:.2f} | conf={sig.keypoints_conf:.2f}"
            )

            if consecutive_risky >= REQUIRED_CONSECUTIVE:
                print(f"        -> POSTURE ALERT triggered (risk persisted for {REQUIRED_CONSECUTIVE} checks)")
                consecutive_risky = 0

        time.sleep(0.1)

    print("\nDone. Next step: replace simulated signals with real pose estimation output.")


if __name__ == "__main__":
    main()
