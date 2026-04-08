"""
Main orchestrator for Serie D bracket simulator
"""

import json
from bracket_logic import generate_full_bracket


def load_mock_data():
    """Load mock Phase 1 standings"""
    with open('../data/mock_standings.json', 'r') as f:
        return json.load(f)


def main():
    print("=" * 60)
    print("SERIE D BRACKET SIMULATOR")
    print("=" * 60)
    
    # Load data
    standings = load_mock_data()
    
    # Generate bracket
    bracket = generate_full_bracket(standings)
    
    # Save bracket
    with open('../data/bracket.json', 'w') as f:
        json.dump(bracket, f, indent=2, default=str)
    
    print("✓ Bracket generated successfully")
    print(f"✓ Saved to data/bracket.json")


if __name__ == "__main__":
    main()
