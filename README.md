# Narrative Transformation Engine

A systematic AI-powered system for reimagining classic stories in new worlds while preserving their thematic core.

## Quick Start

### Prerequisites
- Python 3.8+
- OpenAI API key

### Installation
...
pip install openai python-dotenv
export OPENAI_API_KEY=sk-proj-********************

```bash
# Clone or download the project
cd narrative-transformer

# Install dependencies
pip install anthropic

# Set your API key
export ANTHROPIC_API_KEY='your-api-key-here'

# Run the transformation
python run.py
```

### Expected Output
The system will generate:
1. Console logs showing the 5-stage transformation pipeline
2. A markdown file (`romeo_juliet_ai_labs.md`) containing:
   - The complete transformed narrative (~1,850 words)
   - Transformation metadata
   - All intermediate data (JSON format)

### Runtime
- First run: ~30-45 seconds (including 3 API calls)
- Output: 1,500-2,000 word narrative



## How It Works

The system uses a **5-stage pipeline**:

1. **Narrative Core Extraction**: Identify abstract patterns (themes, character types, plot structure)
2. **World Building**: Define parameters of the target universe
3. **Character Mapping**: Translate characters to new context (AI-powered)
4. **Plot Transformation**: Adapt story beats to new world (AI-powered)
5. **Narrative Generation**: Synthesize everything into prose (AI-powered)

Each stage produces structured output that feeds into the next, ensuring reproducibility and debuggability.

## Customization

### Try Different Transformations

Edit the `main()` function in `run.py`:

```python
# Transform Dracula into Silicon Valley
output = transformer.transform(
    source_key="dracula",
    target_key="silicon_valley"
)

# Transform Odyssey into space exploration
output = transformer.transform(
    source_key="odyssey",
    target_key="space"
)
```

### Add New Source Materials

Edit the `SOURCE_MATERIALS` dictionary in `run.py`:

```python
SOURCE_MATERIALS["hamlet"] = {
    "title": "Hamlet",
    "author": "William Shakespeare",
    "summary": "Prince seeks revenge for father's murder...",
    "core_elements": {
        "protagonists": [...],
        "central_conflict": "...",
        # ... etc
    }
}
```

### Add New Target Worlds

Edit the `TARGET_WORLDS` dictionary:

```python
TARGET_WORLDS["cyberpunk"] = {
    "name": "Cyberpunk Megacity",
    "era": "2077",
    "description": "...",
    "parameters": {
        "setting_details": "...",
        # ... etc
    }
}
```

## Architecture Highlights

### Hybrid Approach
- **Human-curated** inputs (Stages 1-2) for quality control
- **AI-powered** transformation (Stages 3-5) for creative reasoning
- Best of both worlds: reliability + creativity

### Structured Outputs
- Character mapping returns JSON for programmatic validation
- Plot transformation produces parseable beat structures
- Final narrative synthesis includes metadata tracking

### Reproducible Process
- All intermediate data preserved
- Clear dependency chain between stages
- Debuggable at every step

## Example Transformations

### Romeo & Juliet → AI Research Labs
Two young researchers from rival AI companies fall in love while collaborating on breakthrough safety research. Corporate espionage accusations and race-to-AGI pressure tear them apart, leading to career sacrifice and open-source martyrdom.

**Themes Preserved**: love vs hate (collaboration vs competition), youth vs age (innovation vs control), individual vs society (researcher vs institution)

### Dracula → Silicon Valley (Conceptual)
An immortal tech founder with mysterious wealth launches multiple unicorn startups across centuries. A young investigative journalist uncovers his pattern of draining companies and founders, leaving husks behind.

**Themes Preserved**: predator/prey dynamics, old power vs new energy, corruption hidden beneath charisma

### The Odyssey → Deep Space (Conceptual)
A colony ship captain's 20-year journey home after a failed terraforming mission. Each planet visited represents a different challenge: resource scarcity, mutiny, alien encounters, temporal distortion.

**Themes Preserved**: journey/return, loyalty tested, transformation through ordeal, homecoming

## API Usage

The system makes 3 API calls per transformation:
1. Character mapping (~800 tokens)
2. Plot transformation (~800 tokens)  
3. Narrative generation (~3,500 tokens)

**Total cost per transformation**: ~$0.02-0.03 (using Claude Sonnet)

## Design Decisions

### Why 5 Stages?
- **Separation of concerns**: Each stage has one job
- **Validation points**: Can check quality at each step
- **Modularity**: Easy to swap out stages or add new ones
- **Transparency**: Clear visibility into transformation logic

### Why JSON Outputs?
- **Programmatic validation**: Can check for required fields
- **Consistency**: Structured data is easier to work with
- **Composability**: Output of one stage feeds cleanly into next
- **Debugging**: Easy to inspect intermediate states

### Why Mix Human + AI?
- **Human curation** (Stages 1-2): Ensures high-quality inputs, preserves thematic integrity
- **AI reasoning** (Stages 3-5): Handles creative mapping, context-specific adaptation
- **Balance**: Reliability where it matters, flexibility where needed

## Future Enhancements

### Immediate Improvements
- [ ] Add validation layer for theme preservation
- [ ] Support batch processing of multiple worlds
- [ ] Implement quality scoring metrics
- [ ] Add interactive refinement interface

### Medium-term Goals
- [ ] Expand to 20+ source materials
- [ ] Add 15+ target worlds
- [ ] Support style transfer (noir, epic, etc.)
- [ ] Generate from character POV

### Long-term Vision
- [ ] RAG integration for learning from past transformations
- [ ] Multi-modal outputs (text + visuals)
- [ ] Public API for developers
- [ ] Fine-tuned transformation model

## Evaluation Criteria

### What Makes a Good Transformation?

**Theme Preservation (40%)**
- Are original themes recognizable?
- Do they resonate in new context?
- Is emotional arc maintained?

**World Consistency (30%)**
- Does story follow new world's rules?
- Are conflicts native to setting?
- Is technology/culture coherent?

**Narrative Quality (20%)**
- Is prose engaging?
- Are characters believable?
- Does plot flow naturally?

**Innovation (10%)**
- Does transformation offer fresh insights?
- Are mappings creative yet logical?
- Does new context illuminate original themes?

## Troubleshooting

### API Key Issues
```bash
# Verify key is set
echo $ANTHROPIC_API_KEY

# Set it if missing
export ANTHROPIC_API_KEY='sk-ant-...'
```

### JSON Parsing Errors
If character mapping or plot transformation fails, check:
- Are prompts returning pure JSON?
- Is the JSON properly formatted?
- Add error handling to extract JSON from markdown blocks

### Output Quality Issues
- Adjust temperature in API calls (lower = more consistent)
- Refine world parameters for clearer constraints
- Add more specific examples in prompts
- Iterate on narrative generation prompt

## Contributing Ideas

Interested in extending this system? Consider:

1. **New domains**: Medical dramas, historical fiction, detective stories
2. **Cross-cultural**: Ancient myths → modern settings from different cultures
3. **Genre-bending**: Tragedy → Comedy, Romance → Horror
4. **Multi-step chains**: Transform A→B→C to see how themes evolve
5. **Comparative analysis**: Generate 5 versions, let users vote on best



