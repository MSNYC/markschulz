#!/usr/bin/env python3
"""
Resume Databank Manager
Utility for viewing, updating, and generating content from resume.json
"""

import json
import sys
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any

# Path configuration
PROJECT_ROOT = Path(__file__).parent.parent
RESUME_JSON = PROJECT_ROOT / "data" / "resume.json"


class ResumeManager:
    def __init__(self, json_path: Path = RESUME_JSON):
        self.json_path = json_path
        self.data = self.load()

    def load(self) -> Dict[str, Any]:
        """Load resume data from JSON file"""
        if not self.json_path.exists():
            print(f"Error: {self.json_path} not found")
            sys.exit(1)

        with open(self.json_path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def save(self):
        """Save resume data back to JSON file"""
        # Update last_updated timestamp
        self.data['meta']['last_updated'] = datetime.now().strftime('%Y-%m-%d')

        with open(self.json_path, 'w', encoding='utf-8') as f:
            json.dump(self.data, f, indent=2, ensure_ascii=False)

        print(f"✓ Saved to {self.json_path}")

    def summary(self):
        """Display a summary of the resume databank"""
        print("\n" + "="*60)
        print("RESUME DATABANK SUMMARY")
        print("="*60)
        print(f"\nVersion: {self.data['meta']['version']}")
        print(f"Last Updated: {self.data['meta']['last_updated']}")
        print(f"\nName: {self.data['personal']['name']['full']}")
        print(f"Title: {self.data['personal']['title']}")
        print(f"Location: {self.data['personal']['contact']['location']['city']}, {self.data['personal']['contact']['location']['state']}")

        print(f"\nExperience Entries: {len(self.data['experience'])}")
        total_positions = sum(len(exp['positions']) for exp in self.data['experience'])
        print(f"Total Positions: {total_positions}")

        print(f"\nEducation: {len(self.data['education'])} degrees")
        print(f"Languages: {len(self.data['languages'])}")
        print(f"Projects: {len(self.data['projects'])}")

        # Skills count
        tech_skills = sum(len(v) for v in self.data['skills']['technical'].values())
        print(f"\nCore Competencies: {len(self.data['skills']['core_competencies'])}")
        print(f"Technical Skills: {tech_skills}")
        print(f"Marketing Specialized: {len(self.data['skills']['marketing_specialized'])}")
        print(f"Leadership Skills: {len(self.data['skills']['leadership'])}")

        print(f"\nKeywords: {len(self.data['keywords'])}")
        print("="*60 + "\n")

    def list_experience(self):
        """List all experience entries"""
        print("\n" + "="*60)
        print("EXPERIENCE")
        print("="*60 + "\n")

        for exp in self.data['experience']:
            company = exp['company']
            if exp.get('company_parent'):
                company += f" ({exp['company_parent']})"

            print(f"\n{company}")
            print("-" * len(company))

            for pos in exp['positions']:
                dates = f"{pos['start_date']} - {'Present' if pos['current'] else pos['end_date']}"
                print(f"  • {pos['title']}")
                print(f"    {dates}")
                print(f"    Responsibilities: {len(pos['responsibilities'])}")

                if pos.get('achievements'):
                    achievement_count = sum(len(cat['items']) for cat in pos['achievements'])
                    print(f"    Achievements: {achievement_count} items across {len(pos['achievements'])} categories")
            print()

    def list_skills(self):
        """List all skills by category"""
        print("\n" + "="*60)
        print("SKILLS INVENTORY")
        print("="*60 + "\n")

        print("Core Competencies:")
        for skill in self.data['skills']['core_competencies']:
            print(f"  • {skill}")

        print("\nTechnical Skills:")
        for category, skills in self.data['skills']['technical'].items():
            print(f"\n  {category.replace('_', ' ').title()}:")
            for skill in skills:
                print(f"    • {skill}")

        print("\nMarketing Specialized:")
        for skill in self.data['skills']['marketing_specialized']:
            print(f"  • {skill}")

        print("\nLeadership:")
        for skill in self.data['skills']['leadership']:
            print(f"  • {skill}")

        print("\nMethodologies:")
        for method in self.data['skills']['methodologies']:
            print(f"  • {method}")
        print()

    def list_projects(self):
        """List all projects"""
        print("\n" + "="*60)
        print("PROJECTS")
        print("="*60 + "\n")

        for i, project in enumerate(self.data['projects'], 1):
            print(f"{i}. {project['name']}")
            print(f"   Role: {project['role']}")
            print(f"   Technologies: {', '.join(project['technologies'])}")
            print(f"   Outcomes: {len(project['outcomes'])}")
            print()

    def search(self, keyword: str):
        """Search for keyword across resume"""
        keyword_lower = keyword.lower()
        results = []

        # Search in experience
        for exp in self.data['experience']:
            for pos in exp['positions']:
                if keyword_lower in pos['title'].lower():
                    results.append(f"Position: {pos['title']} at {exp['company']}")

                for resp in pos['responsibilities']:
                    if keyword_lower in resp.lower():
                        results.append(f"Responsibility at {exp['company']}: {resp[:100]}...")

                if pos.get('achievements'):
                    for achievement_cat in pos['achievements']:
                        for item in achievement_cat['items']:
                            if keyword_lower in item.lower():
                                results.append(f"Achievement at {exp['company']}: {item[:100]}...")

        # Search in skills
        for skill in self.data['skills']['core_competencies']:
            if keyword_lower in skill.lower():
                results.append(f"Core Competency: {skill}")

        for category, skills in self.data['skills']['technical'].items():
            for skill in skills:
                if keyword_lower in skill.lower():
                    results.append(f"Technical Skill ({category}): {skill}")

        # Search in projects
        for project in self.data['projects']:
            if keyword_lower in project['name'].lower() or keyword_lower in project['description'].lower():
                results.append(f"Project: {project['name']}")

        print(f"\n{'='*60}")
        print(f"SEARCH RESULTS FOR: '{keyword}'")
        print(f"{'='*60}\n")

        if results:
            for i, result in enumerate(results, 1):
                print(f"{i}. {result}")
        else:
            print("No results found.")
        print()


def main():
    """Main CLI interface"""
    if len(sys.argv) < 2:
        print("\nResume Databank Manager")
        print("="*60)
        print("\nUsage:")
        print("  python resume_manager.py summary       - Show databank summary")
        print("  python resume_manager.py experience    - List all experience")
        print("  python resume_manager.py skills        - List all skills")
        print("  python resume_manager.py projects      - List all projects")
        print("  python resume_manager.py search <term> - Search for keyword")
        print()
        sys.exit(0)

    command = sys.argv[1].lower()
    manager = ResumeManager()

    if command == "summary":
        manager.summary()
    elif command == "experience":
        manager.list_experience()
    elif command == "skills":
        manager.list_skills()
    elif command == "projects":
        manager.list_projects()
    elif command == "search":
        if len(sys.argv) < 3:
            print("Error: Please provide a search term")
            sys.exit(1)
        manager.search(sys.argv[2])
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)


if __name__ == "__main__":
    main()
