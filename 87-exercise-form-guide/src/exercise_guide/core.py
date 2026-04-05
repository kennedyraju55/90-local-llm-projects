"""
Exercise Form Guide - Core logic and data.

Provides exercise form guidance, muscle group databases, progression paths,
warm-up/cool-down routines, and LLM-powered exercise instructions.

⚠️  DISCLAIMER: This tool is for educational purposes only and is NOT medical advice.
Always consult a qualified fitness professional or physician before starting any
exercise program. Improper form can lead to injury.
"""

from typing import Optional, List, Dict, Any, Tuple, Union
import sys
import os
import logging

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..'))
from common.llm_client import generate, check_ollama_running

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

DISCLAIMER = (
    "⚠️  DISCLAIMER: This tool provides AI-generated exercise guidance for "
    "educational purposes only. It is NOT medical advice. Always consult a "
    "qualified fitness professional or physician before starting any exercise "
    "program. Improper form can lead to serious injury."
)

VALID_LEVELS = ["beginner", "intermediate", "advanced"]
VALID_MUSCLE_GROUPS = ["legs", "chest", "back", "shoulders", "arms", "core", "full body"]
VALID_GOALS = ["strength", "hypertrophy", "endurance", "flexibility"]

SYSTEM_PROMPT = """You are an expert exercise science coach and certified personal trainer.
When providing exercise guidance, always include:

1. **Exercise Description**: Brief overview of the exercise and its benefits.
2. **Target Muscles**: Primary and secondary muscles worked.
3. **Step-by-Step Form Instructions**: Numbered steps with precise cues.
4. **Common Mistakes**: What people typically do wrong and how to fix it.
5. **Breathing Cues**: When to inhale and exhale during the movement.
6. **Progressions & Regressions**: Easier and harder variations.
7. **Safety Tips**: Important safety considerations and contraindications.

Format your response in clean Markdown with clear section headers.
Be specific, actionable, and prioritize safety above all else.

IMPORTANT: Always include a reminder that users should consult a healthcare provider
or certified trainer before attempting new exercises."""

# ---------------------------------------------------------------------------
# Muscle Group Database
# ---------------------------------------------------------------------------

MUSCLE_GROUP_DATABASE = {
    "chest": {
        "muscles": ["pectoralis major", "pectoralis minor", "serratus anterior"],
        "description": (
            "The chest muscles are responsible for pushing movements and "
            "horizontal adduction of the arms. They play a key role in pressing, "
            "hugging, and overhead motions."
        ),
        "common_exercises": [
            "bench press", "push-ups", "dumbbell flyes", "cable crossovers",
            "incline bench press", "decline bench press", "chest dips",
            "dumbbell pullover",
        ],
    },
    "back": {
        "muscles": [
            "latissimus dorsi", "trapezius", "rhomboids",
            "erector spinae", "teres major", "infraspinatus",
        ],
        "description": (
            "The back muscles are essential for pulling movements, posture, "
            "and spinal stability. A strong back supports everyday activities "
            "and reduces injury risk."
        ),
        "common_exercises": [
            "pull-ups", "bent-over rows", "lat pulldowns", "deadlifts",
            "seated cable rows", "face pulls", "single-arm dumbbell rows",
            "t-bar rows",
        ],
    },
    "legs": {
        "muscles": [
            "quadriceps", "hamstrings", "glutes", "calves",
            "hip flexors", "adductors",
        ],
        "description": (
            "The leg muscles form the largest muscle group in the body. "
            "They are critical for locomotion, balance, and overall athletic "
            "performance."
        ),
        "common_exercises": [
            "squats", "lunges", "leg press", "Romanian deadlifts",
            "leg curls", "calf raises", "step-ups", "Bulgarian split squats",
        ],
    },
    "shoulders": {
        "muscles": [
            "anterior deltoid", "lateral deltoid", "posterior deltoid",
            "rotator cuff",
        ],
        "description": (
            "The shoulder muscles enable a wide range of arm movements "
            "including pressing, raising, and rotating. Balanced shoulder "
            "training is vital for joint health."
        ),
        "common_exercises": [
            "overhead press", "lateral raises", "front raises",
            "face pulls", "Arnold press", "reverse flyes",
            "upright rows", "shrugs",
        ],
    },
    "arms": {
        "muscles": [
            "biceps brachii", "triceps brachii", "brachialis",
            "brachioradialis", "forearm flexors", "forearm extensors",
        ],
        "description": (
            "The arm muscles are used in virtually every upper body exercise. "
            "They include the biceps for pulling/curling and the triceps for "
            "pushing/extending."
        ),
        "common_exercises": [
            "bicep curls", "tricep dips", "hammer curls",
            "skull crushers", "preacher curls", "tricep pushdowns",
            "concentration curls", "overhead tricep extensions",
        ],
    },
    "core": {
        "muscles": [
            "rectus abdominis", "obliques", "transverse abdominis",
            "erector spinae", "hip flexors",
        ],
        "description": (
            "The core muscles stabilize the spine and pelvis, providing a "
            "foundation for all movement. Core strength is essential for "
            "posture, balance, and injury prevention."
        ),
        "common_exercises": [
            "planks", "crunches", "Russian twists", "leg raises",
            "dead bugs", "bicycle crunches", "ab wheel rollouts",
            "hanging knee raises",
        ],
    },
    "full body": {
        "muscles": [
            "multiple muscle groups", "compound movement chains",
            "stabilizer muscles",
        ],
        "description": (
            "Full-body exercises engage multiple major muscle groups "
            "simultaneously, providing efficient training stimulus and "
            "functional strength."
        ),
        "common_exercises": [
            "burpees", "clean and press", "thrusters", "Turkish get-ups",
            "kettlebell swings", "man makers", "bear crawls",
            "mountain climbers",
        ],
    },
}

# ---------------------------------------------------------------------------
# Progression Paths
# ---------------------------------------------------------------------------

PROGRESSION_PATHS = {
    "push-up": [
        "wall push-up",
        "knee push-up",
        "standard push-up",
        "diamond push-up",
        "archer push-up",
        "one-arm push-up",
    ],
    "squat": [
        "assisted squat",
        "bodyweight squat",
        "goblet squat",
        "barbell back squat",
        "front squat",
        "pistol squat",
    ],
    "pull-up": [
        "dead hang",
        "band-assisted pull-up",
        "negative pull-up",
        "standard pull-up",
        "weighted pull-up",
        "muscle-up",
    ],
    "plank": [
        "knee plank",
        "standard plank",
        "plank with shoulder taps",
        "side plank",
        "plank with leg lift",
        "plank to push-up",
    ],
    "deadlift": [
        "hip hinge with dowel",
        "kettlebell deadlift",
        "trap bar deadlift",
        "conventional deadlift",
        "sumo deadlift",
        "single-leg Romanian deadlift",
    ],
}

# ---------------------------------------------------------------------------
# Warm-up and Cool-down Data
# ---------------------------------------------------------------------------

_WARMUP_ROUTINES: dict[str, list[dict]] = {
    "chest": [
        {"name": "Arm circles", "duration": "30 seconds", "description": "Small to large circles to mobilize the shoulder joints."},
        {"name": "Band pull-aparts", "duration": "30 seconds", "description": "Light resistance band pulls to activate rear delts and upper back."},
        {"name": "Push-up walkouts", "duration": "45 seconds", "description": "Walk hands out from standing to push-up position and back."},
        {"name": "Light dumbbell flyes", "duration": "1 minute", "description": "Very light weight to warm up the pectorals through full range of motion."},
    ],
    "back": [
        {"name": "Cat-cow stretch", "duration": "30 seconds", "description": "Alternate arching and rounding the spine on all fours."},
        {"name": "Band pull-aparts", "duration": "30 seconds", "description": "Activate the rhomboids and rear deltoids."},
        {"name": "Scapular push-ups", "duration": "30 seconds", "description": "Push-up position, protracting and retracting shoulder blades."},
        {"name": "Light lat pulldowns", "duration": "1 minute", "description": "Very light resistance to warm up the lats."},
    ],
    "legs": [
        {"name": "Leg swings", "duration": "30 seconds per leg", "description": "Forward and lateral leg swings to mobilize the hips."},
        {"name": "Bodyweight squats", "duration": "1 minute", "description": "Slow, controlled squats to warm up quads, glutes, and hips."},
        {"name": "Walking lunges", "duration": "1 minute", "description": "Dynamic lunges to activate glutes and hip flexors."},
        {"name": "Ankle circles", "duration": "30 seconds per ankle", "description": "Rotate ankles to prepare for loaded movements."},
    ],
    "shoulders": [
        {"name": "Arm circles", "duration": "30 seconds", "description": "Small to large circles in both directions."},
        {"name": "Band dislocates", "duration": "30 seconds", "description": "Overhead band pass-throughs for shoulder mobility."},
        {"name": "Scapular slides", "duration": "30 seconds", "description": "Slide arms up the wall to activate lower traps."},
        {"name": "Light lateral raises", "duration": "1 minute", "description": "Very light weight to prime the deltoids."},
    ],
    "arms": [
        {"name": "Wrist circles", "duration": "30 seconds", "description": "Rotate wrists to warm up forearms and wrist joints."},
        {"name": "Arm circles", "duration": "30 seconds", "description": "Small circles progressing to large circles."},
        {"name": "Light bicep curls", "duration": "1 minute", "description": "Very light weight to prime the biceps."},
        {"name": "Tricep stretches", "duration": "30 seconds per arm", "description": "Overhead tricep stretch to loosen the triceps."},
    ],
    "core": [
        {"name": "Cat-cow stretch", "duration": "30 seconds", "description": "Mobilize the spine through flexion and extension."},
        {"name": "Pelvic tilts", "duration": "30 seconds", "description": "Lying on back, tilt pelvis to activate deep core muscles."},
        {"name": "Bird dogs", "duration": "1 minute", "description": "Alternate extending opposite arm and leg for core activation."},
        {"name": "Dead bugs", "duration": "1 minute", "description": "Lying on back, extend opposite limbs while maintaining core stability."},
    ],
    "full body": [
        {"name": "Jumping jacks", "duration": "1 minute", "description": "Full-body cardiovascular warm-up."},
        {"name": "Leg swings", "duration": "30 seconds per leg", "description": "Forward and lateral swings for hip mobility."},
        {"name": "Arm circles", "duration": "30 seconds", "description": "Mobilize the shoulder joints."},
        {"name": "Bodyweight squats", "duration": "1 minute", "description": "Slow squats to warm up the lower body."},
        {"name": "Push-up walkouts", "duration": "45 seconds", "description": "Walk out to push-up position for upper body activation."},
    ],
}

_COOLDOWN_ROUTINES: dict[str, list[dict]] = {
    "chest": [
        {"name": "Doorway chest stretch", "duration": "30 seconds per side", "description": "Place forearm on doorframe and lean forward to stretch the pectorals."},
        {"name": "Cross-body shoulder stretch", "duration": "30 seconds per arm", "description": "Pull one arm across the body to stretch the shoulder and chest."},
        {"name": "Child's pose with arms extended", "duration": "45 seconds", "description": "Kneel and extend arms forward to stretch chest and lats."},
    ],
    "back": [
        {"name": "Child's pose", "duration": "45 seconds", "description": "Kneel and sit back on heels with arms extended for a lat stretch."},
        {"name": "Cat-cow stretch", "duration": "30 seconds", "description": "Gentle spinal flexion and extension."},
        {"name": "Seated spinal twist", "duration": "30 seconds per side", "description": "Sit and rotate the torso to stretch the back muscles."},
    ],
    "legs": [
        {"name": "Standing quad stretch", "duration": "30 seconds per leg", "description": "Pull heel toward glutes to stretch the quadriceps."},
        {"name": "Standing hamstring stretch", "duration": "30 seconds per leg", "description": "Place heel on a surface and lean forward gently."},
        {"name": "Pigeon pose", "duration": "45 seconds per side", "description": "Hip opener to stretch glutes and hip flexors."},
        {"name": "Calf stretch", "duration": "30 seconds per leg", "description": "Press heel down on a step or against a wall."},
    ],
    "shoulders": [
        {"name": "Cross-body shoulder stretch", "duration": "30 seconds per arm", "description": "Pull one arm across the body at shoulder height."},
        {"name": "Overhead tricep/shoulder stretch", "duration": "30 seconds per arm", "description": "Reach one arm overhead and behind the head."},
        {"name": "Thread the needle", "duration": "30 seconds per side", "description": "On all fours, thread one arm under the body for a thoracic stretch."},
    ],
    "arms": [
        {"name": "Wrist flexor stretch", "duration": "30 seconds per arm", "description": "Extend arm and gently pull fingers back."},
        {"name": "Bicep wall stretch", "duration": "30 seconds per arm", "description": "Place palm on wall behind you and rotate away."},
        {"name": "Overhead tricep stretch", "duration": "30 seconds per arm", "description": "Reach arm overhead and behind head, gently press elbow."},
    ],
    "core": [
        {"name": "Cobra pose", "duration": "30 seconds", "description": "Lie face down and press up to stretch the abdominals."},
        {"name": "Seated spinal twist", "duration": "30 seconds per side", "description": "Sit and rotate torso to stretch obliques and back."},
        {"name": "Supine knee-to-chest", "duration": "30 seconds per side", "description": "Lying on back, pull one knee to chest for a lower back stretch."},
    ],
    "full body": [
        {"name": "Standing forward fold", "duration": "45 seconds", "description": "Hinge at hips and let upper body hang to stretch hamstrings and back."},
        {"name": "Quad stretch", "duration": "30 seconds per leg", "description": "Pull heel toward glutes standing on one leg."},
        {"name": "Cross-body shoulder stretch", "duration": "30 seconds per arm", "description": "Pull each arm across the body."},
        {"name": "Child's pose", "duration": "45 seconds", "description": "Full-body relaxation stretch on all fours."},
        {"name": "Deep breathing", "duration": "1 minute", "description": "Slow diaphragmatic breathing to lower heart rate and promote recovery."},
    ],
}

# ---------------------------------------------------------------------------
# Helper Functions
# ---------------------------------------------------------------------------


def get_warmup_routine(muscle_group: str) -> list[dict]:
    """Return a list of warm-up exercises for the given muscle group.

    Each item is a dict with keys: name, duration, description.
    Returns an empty list if the muscle group is not recognized.
    """
    key = muscle_group.lower().strip()
    routine = _WARMUP_ROUTINES.get(key, [])
    logger.debug("Warm-up routine for '%s': %d exercises", key, len(routine))
    return routine


def get_cooldown_routine(muscle_group: str) -> list[dict]:
    """Return a list of cool-down stretches for the given muscle group.

    Each item is a dict with keys: name, duration, description.
    Returns an empty list if the muscle group is not recognized.
    """
    key = muscle_group.lower().strip()
    routine = _COOLDOWN_ROUTINES.get(key, [])
    logger.debug("Cool-down routine for '%s': %d stretches", key, len(routine))
    return routine


def get_exercise_variations(exercise: str) -> list[str]:
    """Return the progression path for a given exercise.

    Returns an empty list if no progression path exists for the exercise.
    """
    key = exercise.lower().strip()
    variations = PROGRESSION_PATHS.get(key, [])
    logger.debug("Progression path for '%s': %d variations", key, len(variations))
    return variations


def get_muscle_info(muscle_group: str) -> dict:
    """Return muscle group information from the database.

    Returns an empty dict if the muscle group is not recognized.
    """
    key = muscle_group.lower().strip()
    info = MUSCLE_GROUP_DATABASE.get(key, {})
    logger.debug("Muscle info for '%s': %s", key, "found" if info else "not found")
    return info


# ---------------------------------------------------------------------------
# LLM-powered Functions
# ---------------------------------------------------------------------------


def generate_guide(exercise: str, level: str) -> str:
    """Generate a detailed exercise form guide using the LLM."""
    logger.info("Generating guide for '%s' at '%s' level", exercise, level)
    prompt = (
        f"Provide a comprehensive exercise form guide for '{exercise}' "
        f"tailored to a {level}-level trainee.\n\n"
        f"Include all sections: description, target muscles, step-by-step form, "
        f"common mistakes, breathing cues, progressions/regressions, and safety tips.\n\n"
        f"Adjust complexity and cues for the {level} level."
    )
    return generate(prompt=prompt, system_prompt=SYSTEM_PROMPT)


def list_exercises(muscle_group: str) -> str:
    """List exercises for a specific muscle group using the LLM."""
    logger.info("Listing exercises for '%s'", muscle_group)
    prompt = (
        f"List 10-15 exercises that target the '{muscle_group}' muscle group.\n\n"
        f"For each exercise, provide:\n"
        f"- Exercise name\n"
        f"- Difficulty level (beginner/intermediate/advanced)\n"
        f"- Equipment needed (if any)\n"
        f"- Brief one-line description\n\n"
        f"Organize from easiest to most advanced. Format as a clean Markdown list."
    )
    return generate(prompt=prompt, system_prompt=SYSTEM_PROMPT)


def generate_routine(goal: str, level: str) -> str:
    """Generate a workout routine based on goal and level using the LLM."""
    logger.info("Generating routine for goal='%s', level='%s'", goal, level)
    prompt = (
        f"Create a weekly workout routine for a {level}-level trainee "
        f"with a primary goal of {goal}.\n\n"
        f"Include:\n"
        f"- Weekly schedule (which days, which muscle groups)\n"
        f"- Exercises for each day with sets, reps, and rest periods\n"
        f"- Warm-up and cool-down recommendations\n"
        f"- Progression strategy over 4-6 weeks\n"
        f"- Recovery and nutrition tips\n\n"
        f"Format as clean Markdown with clear day-by-day structure.\n"
        f"Adjust volume and intensity appropriately for the {level} level."
    )
    return generate(prompt=prompt, system_prompt=SYSTEM_PROMPT)
