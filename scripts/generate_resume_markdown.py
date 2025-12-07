#!/usr/bin/env python3
"""
Resume Markdown Generator
Generates ATS-optimized markdown from resume.json databank
Usage: python3 scripts/generate_resume_markdown.py [--full] [--output FILE]
"""

import json
import sys
from pathlib import Path
from datetime import datetime

def load_resume_data(json_path='data/resume.json'):
    """Load resume data from JSON file"""
    with open(json_path, 'r') as f:
        return json.load(f)

def format_date_range(start, end, current=False):
    """Format date range for display"""
    if current or end is None:
        return f"{start} – Present"
    return f"{start} – {end}"

def generate_markdown(data, full_version=False):
    """Generate markdown resume from data"""
    md = []

    # Header
    personal = data['personal']
    md.append(f"# {personal['name']['full']}")
    md.append(f"*{personal['title']}*\n")
    md.append(f"**Location:** {personal['contact']['location']['city']}, {personal['contact']['location']['state']}")
    md.append(f"**Email:** {personal['contact']['email']}")
    md.append(f"**Phone:** {personal['contact']['phone']}")
    md.append(f"**Website:** {personal['contact']['website']}\n")
    md.append("---\n")

    # Professional Summary
    md.append("## Professional Summary\n")
    md.append(data['summary']['long'] + "\n")

    # Core Competencies (ATS-friendly keyword section)
    md.append("## Core Competencies\n")
    competencies = data['skills']['core_competencies']
    # Format as flowing text for better ATS parsing
    md.append(" • ".join(competencies) + "\n")

    # Professional Experience
    md.append("## Professional Experience\n")

    for exp in data['experience']:
        for position in exp['positions']:
            md.append(f"### {position['title']}")
            company_line = f"**{exp['company']}**"
            if exp.get('company_parent'):
                company_line += f" ({exp['company_parent']})"
            company_line += f" | {exp['location']}"
            md.append(company_line)
            md.append(f"*{format_date_range(position['start_date'], position['end_date'], position['current'])}*\n")

            # Responsibilities
            if position['responsibilities']:
                for resp in position['responsibilities']:
                    md.append(f"- {resp}")
                md.append("")

            # Achievements (handle both grouped and simple list formats)
            if position['achievements']:
                for achievement in position['achievements']:
                    # Handle grouped format (dict with category and items)
                    if isinstance(achievement, dict) and 'category' in achievement:
                        md.append(f"**{achievement['category']}:**")
                        for item in achievement['items']:
                            md.append(f"- {item}")
                        md.append("")
                    # Handle simple string format
                    elif isinstance(achievement, str):
                        md.append(f"- {achievement}")
                md.append("")

    # Key Initiatives (concise for 2-page resume)
    md.append("## Key Initiatives\n")
    # Show top 4 most recent/impactful projects only
    recent_projects = data['projects'][-4:] if not full_version else data['projects'][-6:]
    for project in reversed(recent_projects):  # Newest first
        period = f" ({project['period']})" if 'period' in project else ""
        # Single line: Name, Role, Period
        md.append(f"**{project['name']}**{period} – {project['role']}")
        # Single most impactful outcome only
        if project['outcomes']:
            md.append(f"  {project['outcomes'][0]}\n")
        else:
            md.append("")

    # Technical Skills
    md.append("## Technical Skills\n")
    tech_skills = data['skills']['technical']

    md.append(f"**AI/ML:** {', '.join(tech_skills['ai_ml'])}\n")
    md.append(f"**Analytics:** {', '.join(tech_skills['analytics'])}\n")
    md.append(f"**Data Engineering:** {', '.join(tech_skills['data_engineering'])}\n")
    md.append(f"**Tools & Platforms:** {', '.join(tech_skills['tools_platforms'])}\n")
    md.append(f"**Web/Digital:** {', '.join(tech_skills['web_digital'])}\n")

    # Therapeutic Areas (Pharma-specific prominence)
    md.append("## Therapeutic Area Expertise\n")
    for area in data['therapeutic_areas']:
        years = area['years_experience']
        md.append(f"**{area['area']}** ({years} years) - {area['expertise_level']}")
        if area.get('brands'):
            md.append(f"  - Brands: {', '.join(area['brands'])}")
        md.append("")

    # Education
    md.append("## Education\n")
    for edu in data['education']:
        degree_info = f"{edu['degree']} in {edu['field']}"
        if edu.get('concentration'):
            degree_info += f", {edu['concentration']}"
        md.append(f"**{degree_info}**")
        # Use end_date, format as year only
        grad_year = edu.get('end_date', 'Present')
        if grad_year and '-' in str(grad_year):
            grad_year = grad_year.split('-')[0]  # Extract year from YYYY-MM format
        md.append(f"{edu['institution']} | {grad_year}\n")

    # Languages
    if data.get('languages'):
        md.append("## Languages\n")
        lang_list = [f"{lang['language']} ({lang['proficiency']})" for lang in data['languages']]
        md.append(", ".join(lang_list) + "\n")

    # Footer
    md.append("---")
    md.append(f"\n*Resume generated from databank v{data['meta']['version']} on {datetime.now().strftime('%Y-%m-%d')}*")

    return "\n".join(md)

def main():
    # Parse arguments
    full_version = '--full' in sys.argv
    output_file = 'output/MarkSchulz_Resume.md'

    if '--output' in sys.argv:
        idx = sys.argv.index('--output')
        if idx + 1 < len(sys.argv):
            output_file = sys.argv[idx + 1]

    # Load data and generate
    data = load_resume_data()
    markdown = generate_markdown(data, full_version)

    # Ensure output directory exists
    Path(output_file).parent.mkdir(parents=True, exist_ok=True)

    # Write output
    with open(output_file, 'w') as f:
        f.write(markdown)

    print(f"✓ Resume markdown generated: {output_file}")
    print(f"  Version: {data['meta']['version']}")
    print(f"\nNext steps (with narrow margins for 2-page max):")
    print(f"\n  ATS DOCX:")
    print(f"    pandoc {output_file} -o output/MarkSchulz_Resume_ATS.docx -V geometry:margin=0.5in")
    print(f"\n  Professional PDF:")
    print(f"    pandoc {output_file} -o output/MarkSchulz_Resume_Professional.pdf -V geometry:margin=0.5in")
    print(f"\n  Or with wkhtmltopdf for better formatting:")
    print(f"    pandoc {output_file} -o output/MarkSchulz_Resume_Professional.pdf --pdf-engine=wkhtmltopdf -V margin-left=0.5in -V margin-right=0.5in -V margin-top=0.5in -V margin-bottom=0.5in")

if __name__ == '__main__':
    main()
