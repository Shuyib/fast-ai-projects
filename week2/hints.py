import random
facts = {
    'neutrophil': [
        'My nucleus has 2-5 lobes, purple in color',
        'Could be sign of a bacterial infection and involved in phagocytosis.',
        'Learn more here: https://en.wikipedia.org/wiki/Neutrophil'
    ],
    'eosinophil': [
        'My nucleus 1-3 lobes and has a dark outline on the cell membrane',
        'Looks like a neutrophil could be sign of parasitic infection or allergy if many',
        'Learn more here: https://en.wikipedia.org/wiki/Eosinophil'
    ],
    'monocyte': [
        'My nucleus is purple, can have vacuoles on it',
        'Involved in phagocytosis, antigen presentation, and cytokine production',
        'Learn more here: https://en.wikipedia.org/wiki/Monocyte'
    ],
    'lymphocyte': [
        'Have a really large nucleus',
        'Involved in cell and humoral response',
        'Learn more here: https://en.wikipedia.org/wiki/Lymphocyte'

    ]
}

def fact_finder(label: str) -> str:
    return random.choice(facts[label])
    