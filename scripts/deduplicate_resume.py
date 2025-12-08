#!/usr/bin/env python3
"""
Semantic deduplication script for resume.json

STRATEGY:
1. Identify TRUE duplicates - same work, different wording
2. Keep the most detailed/specific version
3. Remove from wrong positions, keep in correct position
4. Be CONSERVATIVE - when in doubt, keep both
"""

import json
import shutil
from datetime import datetime
from difflib import SequenceMatcher

def similarity(a, b):
    """Calculate similarity ratio between two strings"""
    return SequenceMatcher(None, a.lower(), b.lower()).ratio()

def backup_file(filepath):
    """Create a timestamped backup"""
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_path = filepath.replace('.json', f'_backup_{timestamp}.json')
    shutil.copy2(filepath, backup_path)
    print(f"✓ Backup created: {backup_path}")
    return backup_path

def load_resume(filepath):
    """Load resume JSON"""
    with open(filepath, 'r') as f:
        return json.load(f)

def save_resume(filepath, data):
    """Save resume JSON with formatting"""
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def find_duplicates_to_remove():
    """
    Define specific duplicates to remove based on analysis.
    Returns list of specifications for what to keep/remove.
    """

    return [
        # PODCAST DUPLICATES - Keep most detailed version in VIAGRA position
        {
            'keyword': 'podcast',
            'keep_text': 'Launched monthly Viagra podcast program from May 2007 through April 2008, successfully aligning content to satisfaction messaging and value card program changes',
            'keep_position': 'Associate Marketing Manager, VIAGRA',
            'reason': 'Podcast was launched during VIAGRA role. This version has specific dates and details.'
        },

        # GROUP PRACTICE ADHERENCE - Appears in both LIPITOR and VIAGRA
        {
            'keyword': 'group practice adherence',
            'keep_text': 'Led HCP marketing efforts and conducted national sales rep training for a ground-breaking group practice adherence program that re-invigorated field force reps and unlocked a new front in point-of-care hybrid messaging',
            'keep_position': 'Marketing Manager - LIPITOR / CADUET',
            'reason': 'Most detailed version. Group practice adherence was LIPITOR/CADUET initiative.'
        },

        # PM TEAM LEADERSHIP - Multiple similar versions at Patients & Purpose
        {
            'keyword': 'full project management team for major pharmaceutical client including annual SOW',
            'keep_text': 'Led full PM team management for major pharmaceutical client with supervision and growth of 5 direct reports',
            'keep_position': 'VP, Project Management, Group Supervisor',
            'reason': 'Most specific with team size. VP level is the correct position.'
        },

        # MULTI-DEPARTMENT RESOURCING - Multiple versions
        {
            'keyword': 'complex multi-departmental resourcing for major pharmaceutical client',
            'keep_text': 'Supervised and drove growth of multiple direct reports while managing complex multi-department resourcing across pharmaceutical projects',
            'keep_position': 'VP, Project Management, Group Supervisor',
            'reason': 'VP level achievement, most comprehensive version.'
        },

        # DIGITAL SHARE OF VOICE - LIPITOR duplicate
        {
            'keyword': 'digital share of voice',
            'keep_text': 'Managed digital share-of-voice strategy for Pfizer across multiple platforms including QuantiaMD, banner advertising, and SEM campaigns',
            'keep_position': 'Marketing Manager - LIPITOR / CADUET',
            'reason': 'More detailed version with specific platforms.'
        },

        # BUDGET MANAGEMENT - VIAGRA $4.5M budget duplicate
        {
            'keyword': 'Prepared and managed individual $4.5',
            'keep_text': 'Prepared and managed individual $4.5-million+ marketing budget for VIAGRA brand HCP marketing initiatives',
            'keep_position': 'Associate Marketing Manager, VIAGRA',
            'reason': 'More specific mention of HCP marketing initiatives.'
        },

        # PDUFA LAUNCH - 24 hours vs 48 hours
        {
            'keyword': 'multi-property web',
            'keep_text': 'Executed multi-property web launch within 24 hours of PDUFA approval, demonstrating rapid deployment capabilities for regulatory-dependent launches',
            'keep_position': 'VP, Project Management, Group Supervisor',
            'reason': '24 hours is the accurate timeframe. VP level is correct seniority.'
        },

        # SOW FORMULATION - Multiple near-identical versions
        {
            'keyword': 'Statement of Work (SOW) formulation and execution',
            'keep_text': 'Formulated and executed annual Statement of Work (SOW) for complex multi-department resourcing across pharmaceutical client operations',
            'keep_position': 'VP, Project Management, Group Supervisor',
            'reason': 'Most detailed version at correct seniority level.'
        },

        # SOW DRAFTING - $1M+ duplicate
        {
            'keyword': 'Drafted and facilitated review/approval of',
            'keep_text': 'Drafted and facilitated review/approval of ~5 $1M+ SOWs per year',
            'keep_position': 'VP, Project Management, Group Supervisor',
            'reason': 'VP level is the correct position for this responsibility.'
        },

        # ALLSCRIPTS EMR - Appears in multiple positions
        {
            'keyword': 'AllScripts',
            'keep_text': 'Led innovative EMR competitive messaging partnership with AllScripts, integrating brand messaging into electronic medical record systems',
            'keep_position': 'Marketing Manager - LIPITOR / CADUET',
            'reason': 'Most detailed. This was LIPITOR work as Marketing Manager.'
        },

        # INTERAGENCY CONSOLIDATION - Multiple versions
        {
            'keyword': 'client-side agency relationship consolidation',
            'keep_text': 'Successfully navigated the complexity of relationships caused by client-side agency relationship consolidations by holding company while leading Project Management team and portfolio of key accounts',
            'keep_position': 'VP, Project Management, Group Supervisor',
            'reason': 'Most detailed version with full context.'
        },

        # TABLET PC EDETAILING - Appears at Patients & Purpose and Pfizer
        {
            'keyword': 'tablet PC eDetailing',
            'keep_text': 'Led tablet PC eDetailing implementation as Digital Captain, introducing innovative sales force technology solutions for enhanced HCP engagement',
            'keep_position': 'Associate Marketing Manager, VIAGRA',
            'reason': 'This was Pfizer/VIAGRA work. "Digital Captain" title confirms it.'
        },

        # WebMD ROI MODELING - Similar achievements
        {
            'keyword': 'strategic oversight from',
            'keep_text': 'Conducted best-in-class strategic oversight from initial ROI modeling through final campaign impact measurement via NRx/TRx test-versus-control analysis conducted by IQVIA',
            'keep_position': 'Team Leader, Sr. Dir., Commercial Clinical Strategy',
            'reason': 'Most detailed with specific IQVIA methodology. Sr. Dir is correct level.'
        },

        # WebMD DATA SOURCES - Two similar versions
        {
            'keyword': 'Harnessed internal and external data sources',
            'keep_text': 'Harnessed internal and external data sources (IQVIA, GlobalData, impression and engagement counts) to refine accuracy of performance forecast model',
            'keep_position': 'Director, Commercial Clinical Strategy',
            'reason': 'More specific with data source names and purpose.'
        }
    ]

def remove_duplicates(data, duplicates_spec):
    """Remove duplicates based on specifications."""

    removed_count = 0
    removal_log = []

    for spec in duplicates_spec:
        keyword = spec['keyword'].lower()
        keep_text = spec['keep_text']
        keep_position = spec['keep_position']
        reason = spec['reason']

        matches = []
        for exp_idx, exp in enumerate(data['experience']):
            for pos_idx, pos in enumerate(exp['positions']):
                for cat_idx, cat in enumerate(pos.get('achievements', [])):
                    items_to_remove = []
                    for item_idx, item in enumerate(cat.get('items', [])):
                        text = item.get('text', '') if isinstance(item, dict) else item

                        if keyword in text.lower():
                            if text == keep_text and pos['title'] == keep_position:
                                matches.append({
                                    'action': 'KEEP',
                                    'text': text,
                                    'company': exp['company'],
                                    'title': pos['title']
                                })
                            else:
                                items_to_remove.append(item_idx)
                                matches.append({
                                    'action': 'REMOVE',
                                    'text': text,
                                    'company': exp['company'],
                                    'title': pos['title']
                                })

                    for item_idx in reversed(items_to_remove):
                        cat['items'].pop(item_idx)
                        removed_count += 1

        if matches:
            removal_log.append({
                'keyword': keyword,
                'reason': reason,
                'matches': matches
            })

    return data, removed_count, removal_log

def clean_empty_categories(data):
    """Remove empty achievement categories"""
    for exp in data['experience']:
        for pos in exp['positions']:
            pos['achievements'] = [
                cat for cat in pos.get('achievements', [])
                if cat.get('items', [])
            ]

def main():
    filepath = '/Users/markschulz/Documents/My_Documents/My Coding/markschulz/assets/data/resume.json'

    print("="*80)
    print("RESUME SEMANTIC DEDUPLICATION")
    print("="*80)
    print()

    # Backup first
    backup_path = backup_file(filepath)

    # Load data
    print("Loading resume data...")
    data = load_resume(filepath)

    # Count before
    before_count = 0
    for exp in data['experience']:
        for pos in exp['positions']:
            for cat in pos.get('achievements', []):
                before_count += len(cat.get('items', []))

    print(f"Total achievements before: {before_count}")
    print()

    # Get deduplication specifications
    duplicates_spec = find_duplicates_to_remove()
    print(f"Processing {len(duplicates_spec)} deduplication rules...")
    print()

    # Remove duplicates
    data, removed_count, removal_log = remove_duplicates(data, duplicates_spec)

    # Clean empty categories
    clean_empty_categories(data)

    # Count after
    after_count = 0
    for exp in data['experience']:
        for pos in exp['positions']:
            for cat in pos.get('achievements', []):
                after_count += len(cat.get('items', []))

    # Print removal log
    print("="*80)
    print("REMOVAL SUMMARY")
    print("="*80)
    print()

    for log_entry in removal_log:
        print(f"KEYWORD: {log_entry['keyword']}")
        print(f"REASON: {log_entry['reason']}")
        print()

        for match in log_entry['matches']:
            action_symbol = "✓ KEEP" if match['action'] == 'KEEP' else "✗ REMOVE"
            print(f"  {action_symbol}")
            print(f"    Position: {match['company']} - {match['title']}")
            print(f"    Text: {match['text'][:100]}...")
            print()

        print("-"*80)
        print()

    print("="*80)
    print("FINAL RESULTS")
    print("="*80)
    print(f"Achievements before: {before_count}")
    print(f"Achievements removed: {removed_count}")
    print(f"Achievements after: {after_count}")
    print(f"Reduction: {removed_count/before_count*100:.1f}%")
    print()

    # Save
    save_resume(filepath, data)
    print(f"✓ Updated resume saved to: {filepath}")
    print(f"✓ Backup available at: {backup_path}")
    print()

    # Distribution after
    print("="*80)
    print("ACHIEVEMENT DISTRIBUTION AFTER DEDUPLICATION")
    print("="*80)
    print()

    for exp in data['experience']:
        print(f"{exp['company']}")
        for pos in exp['positions']:
            count = 0
            for cat in pos.get('achievements', []):
                count += len(cat.get('items', []))
            print(f"  {pos['title']}: {count} achievements")
        print()

if __name__ == '__main__':
    main()
