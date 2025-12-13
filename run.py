"""
Narrative Transformation Engine
A systematic approach to reimagining classic stories in new worlds
"""

import json
import os
from typing import Dict, List, Optional
from dataclasses import dataclass, asdict

from openai import OpenAI

# ============================================================================
# OPENAI CLIENT
# ============================================================================

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def llm_call(prompt: str, max_tokens: int = 1500) -> str:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a narrative transformation engine."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=max_tokens
    )
    return response.choices[0].message.content


# ============================================================================
# DATA MODELS
# ============================================================================

@dataclass
class Character:
    name: str
    traits: List[str]
    motivation: str
    role: str

@dataclass
class NarrativeCore:
    protagonists: List[Character]
    antagonists: List[Character]
    central_conflict: str
    key_themes: List[str]
    plot_beats: List[str]
    emotional_arc: str
    resolution_type: str

@dataclass
class WorldParameters:
    setting_details: str
    power_structures: List[str]
    conflicts: List[str]
    technology_level: str
    cultural_norms: List[str]
    stakes: str

@dataclass
class TransformationOutput:
    narrative: str
    metadata: Dict
    intermediate_data: Dict


# ============================================================================
# SOURCE MATERIAL DATABASE (PUBLIC DOMAIN)
# ============================================================================

SOURCE_MATERIALS = {
    "romeo_juliet": {
        "title": "Romeo and Juliet",
        "author": "William Shakespeare",
        "summary": "Two young lovers from feuding families fall in love, leading to tragic consequences.",
        "core_elements": {
            "protagonists": [
                {
                    "name": "Romeo",
                    "traits": ["passionate", "impulsive", "romantic"],
                    "motivation": "love and connection",
                    "role": "young heir"
                },
                {
                    "name": "Juliet",
                    "traits": ["intelligent", "brave", "defiant"],
                    "motivation": "autonomy and love",
                    "role": "young heiress"
                }
            ],
            "antagonists": [
                {
                    "name": "The Feud",
                    "traits": ["ancient", "destructive", "senseless"],
                    "motivation": "perpetuate hatred",
                    "role": "systemic conflict"
                }
            ],
            "central_conflict": "forbidden love across rigid social divisions",
            "key_themes": [
                "love vs hate",
                "youth vs age",
                "fate vs free will",
                "individual vs society"
            ],
            "plot_beats": [
                "Initial meeting in enemy territory",
                "Secret romance begins",
                "Violent confrontation kills allies",
                "Desperate secret plan",
                "Miscommunication leads to tragedy",
                "Recognition of cost too late"
            ],
            "emotional_arc": "euphoria -> hope -> fear -> desperation -> tragedy -> collective grief",
            "resolution_type": "tragic sacrifice leading to reconciliation"
        }
    }
}

TARGET_WORLDS = {
    "ai_labs": {
        "name": "Rival AI Research Labs",
        "era": "2024-2025",
        "description": "Competing AI research organizations racing for AGI breakthrough",
        "parameters": {
            "setting_details": "Silicon Valley research campuses, closed-door demo rooms, VC boardrooms",
            "power_structures": [
                "corporate hierarchies",
                "venture capital influence",
                "patent ownership",
                "academic prestige"
            ],
            "conflicts": [
                "research rivalry",
                "IP theft fears",
                "ethical disagreements",
                "talent poaching"
            ],
            "technology_level": "cutting-edge AI and neural systems",
            "cultural_norms": [
                "move fast mentality",
                "publish or perish",
                "disruption ideology",
                "zero-sum competition"
            ],
            "stakes": "control over transformative AI technology"
        }
    }
}


# ============================================================================
# TRANSFORMATION ENGINE
# ============================================================================

class NarrativeTransformer:
    def __init__(self):
        self.intermediate_data = {}

    def extract_narrative_core(self, source_material: Dict) -> NarrativeCore:
        print("Step 1: Extracting narrative core")

        core = source_material["core_elements"]

        narrative_core = NarrativeCore(
            protagonists=[Character(**p) for p in core["protagonists"]],
            antagonists=[Character(**a) for a in core["antagonists"]],
            central_conflict=core["central_conflict"],
            key_themes=core["key_themes"],
            plot_beats=core["plot_beats"],
            emotional_arc=core["emotional_arc"],
            resolution_type=core["resolution_type"]
        )

        self.intermediate_data["narrative_core"] = asdict(narrative_core)
        return narrative_core

    def build_world_parameters(self, target_world: Dict) -> WorldParameters:
        print("Step 2: Building world parameters")

        world = WorldParameters(**target_world["parameters"])
        self.intermediate_data["world_parameters"] = asdict(world)
        return world

    def map_characters(self, narrative_core: NarrativeCore, world: WorldParameters) -> Dict:
        print("Step 3: Mapping characters")

        prompt = f"""
Map these characters into the new world context.

SOURCE CHARACTERS:
{json.dumps(self.intermediate_data["narrative_core"]["protagonists"], indent=2)}

WORLD:
{world.setting_details}
Power Structures: {', '.join(world.power_structures)}
Cultural Norms: {', '.join(world.cultural_norms)}

Return ONLY valid JSON:
{{ "characters": [ ... ] }}
"""

        text = llm_call(prompt)
        data = json.loads(text[text.find("{"):text.rfind("}") + 1])

        self.intermediate_data["character_mapping"] = data
        return data

    def transform_plot(self, narrative_core: NarrativeCore, world: WorldParameters) -> List[str]:
        print("Step 4: Transforming plot")

        prompt = f"""
Transform these plot beats into the new world.

ORIGINAL BEATS:
{json.dumps(narrative_core.plot_beats, indent=2)}

THEMES:
{', '.join(narrative_core.key_themes)}

WORLD:
{world.setting_details}

Return JSON:
{{ "transformed_beats": [ ... ] }}
"""

        text = llm_call(prompt)
        data = json.loads(text[text.find("{"):text.rfind("}") + 1])

        self.intermediate_data["transformed_plot"] = data
        return data["transformed_beats"]

    def generate_narrative(
        self,
        source_material: Dict,
        target_world: Dict,
        narrative_core: NarrativeCore,
        world: WorldParameters,
        character_mapping: Dict,
        transformed_plot: List[str]
    ) -> str:

        print("Step 5: Generating final narrative")

        prompt = f"""
Write a complete 2–3 page story reimagining {source_material["title"]}
inside {target_world["name"]}.

THEMES:
{', '.join(narrative_core.key_themes)}

CHARACTERS:
{json.dumps(character_mapping, indent=2)}

PLOT:
{json.dumps(transformed_plot, indent=2)}

WORLD RULES:
{world.setting_details}
Stakes: {world.stakes}

Write only the story.
"""

        return llm_call(prompt, max_tokens=3500)

    def transform(self, source_key: str, target_key: str) -> TransformationOutput:
        print("\nStarting narrative transformation")
        print("-" * 50)

        source = SOURCE_MATERIALS[source_key]
        target = TARGET_WORLDS[target_key]

        core = self.extract_narrative_core(source)
        world = self.build_world_parameters(target)
        characters = self.map_characters(core, world)
        plot = self.transform_plot(core, world)
        narrative = self.generate_narrative(source, target, core, world, characters, plot)

        metadata = {
            "source": source["title"],
            "author": source["author"],
            "target_world": target["name"],
            "era": target["era"],
            "themes": core.key_themes,
            "word_count": len(narrative.split())
        }

        print("Transformation complete")

        return TransformationOutput(
            narrative=narrative,
            metadata=metadata,
            intermediate_data=self.intermediate_data
        )


# ============================================================================
# OUTPUT
# ============================================================================

def save_output(output: TransformationOutput, filename: str):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(output.narrative)

    with open("intermediate_steps.json", "w", encoding="utf-8") as f:
        json.dump(output.intermediate_data, f, indent=2)

    print(f"Saved story to {filename}")
    print("Saved intermediate steps to intermediate_steps.json")


# ============================================================================
# MAIN
# ============================================================================

def main():
    print("""
==============================================
      NARRATIVE TRANSFORMATION ENGINE
==============================================
""")

    transformer = NarrativeTransformer()

    output = transformer.transform(
        source_key="romeo_juliet",
        target_key="ai_labs"
    )

    save_output(output, "romeo_juliet_ai_labs.txt")

    print("\nPipeline finished successfully")

if __name__ == "__main__":
    main()
