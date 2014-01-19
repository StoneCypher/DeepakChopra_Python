from random import choice

starts     = ["Experiential truth ", "The physical world ", "Non-judgment ", "Quantum physics "]
middles    = ["nurtures an ", "projects onto ", "imparts reality to ", "constructs with "]
qualifiers = ["abundance of ", "the barrier of ", "self-righteous ", "potential "]
finishes   = ["marvel.", "choices.", "creativity.", "actions."]

print(choice(starts) + choice(middles) + choice(qualifiers) + choice(finishes))
