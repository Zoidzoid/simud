"""
Bracket Logic for Serie D Tournament
Phase 2-7 matchup generation based on Phase 1 standings
"""

def get_phase_2_matchups(groups):
    """Generate Phase 2 matchups from Phase 1 groups."""
    matchups = []
    group_keys = sorted(groups.keys())
    
    for i in range(0, len(group_keys), 2):
        group1_key = group_keys[i]
        group2_key = group_keys[i + 1]
        
        group1 = groups[group1_key]
        group2 = groups[group2_key]
        
        # Phase 2 format from regulations
        matchup_idx = len(matchups) + 1
        
        matchups.append({
            "phase": 2,
            "match_id": f"B{str(matchup_idx).zfill(2)}",
            "team1": group1[0],  # 1st of group1
            "team2": group2[3],  # 4th of group2
        })
        matchup_idx += 1
        
        matchups.append({
            "phase": 2,
            "match_id": f"B{str(matchup_idx).zfill(2)}",
            "team1": group2[1],  # 2nd of group2
            "team2": group1[2],  # 3rd of group1
        })
        matchup_idx += 1
        
        matchups.append({
            "phase": 2,
            "match_id": f"B{str(matchup_idx).zfill(2)}",
            "team1": group2[0],  # 1st of group2
            "team2": group1[3],  # 4th of group1
        })
        matchup_idx += 1
        
        matchups.append({
            "phase": 2,
            "match_id": f"B{str(matchup_idx).zfill(2)}",
            "team1": group1[1],  # 2nd of group1
            "team2": group2[2],  # 3rd of group2
        })
    
    return matchups


def predict_winner(team1, team2):
    """Predict match winner based on standings."""
    # Higher points
    if team1["points"] != team2["points"]:
        return team1 if team1["points"] > team2["points"] else team2
    
    # Better goal difference
    gd1 = team1.get("goal_difference", 0)
    gd2 = team2.get("goal_difference", 0)
    if gd1 != gd2:
        return team1 if gd1 > gd2 else team2
    
    # More goals scored
    return team1 if team1.get("goals_for", 0) > team2.get("goals_for", 0) else team2


def generate_full_bracket(phase1_groups):
    """Generate all phases with predicted winners."""
    bracket = {
        "phase_1": phase1_groups,
        "phase_2": [],
        "phase_3": [],
        "phase_4": [],
        "phase_5": [],
        "playoff": [],
        "phase_6": [],
        "phase_7": []
    }
    
    # Phase 2
    phase_2_matchups = get_phase_2_matchups(phase1_groups)
    bracket["phase_2"] = phase_2_matchups
    
    phase_2_winners = [predict_winner(m["team1"], m["team2"]) for m in phase_2_matchups]
    
    # Phase 3 - 16 matchups from 32 winners
    for i in range(0, len(phase_2_winners), 2):
        bracket["phase_3"].append({
            "phase": 3,
            "match_id": f"C{str(i // 2 + 1).zfill(2)}",
            "team1": phase_2_winners[i],
            "team2": phase_2_winners[i + 1] if i + 1 < len(phase_2_winners) else None
        })
    
    phase_3_winners = [m["team1"] for m in bracket["phase_3"] if m["team1"]]  # Placeholder
    
    # Phase 4 - 8 matchups
    for i in range(0, len(phase_3_winners), 2):
        bracket["phase_4"].append({
            "phase": 4,
            "match_id": f"D{str(i // 2 + 1).zfill(2)}",
            "team1": phase_3_winners[i],
            "team2": phase_3_winners[i + 1] if i + 1 < len(phase_3_winners) else None
        })
    
    return bracket
