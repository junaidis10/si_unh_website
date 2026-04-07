import re

file_path = 'templates/akademik.html'

with open(file_path, 'r') as f:
    content = f.read()

# Pattern for SKS spans
# Consolidates and reformats for robustness
sks_pattern = r'<span\s+class="([^"]+inline-block bg-gray-200 text-gray-700 w-6 h-6 rounded-full flex items-center justify-center font-bold mx-auto)">\s*\{\{\s*\n?\s*mk\.sks\s*\n?\s*\}\}\s*</span>'
def fix_sks_robust(match):
    return f'<span class="{match.group(1)}">\n                                        {{{{ mk.sks }}}}\n                                    </span>'

content = re.sub(sks_pattern, fix_sks_robust, content)

# Pattern for Semester spans
sem_pattern = r'<span\s+class="([^"]+py-1 px-3 rounded-full text-xs font-bold)">\s*\{\{\s*\n?\s*mk\.semester\|default:"Pilihan"\s*\n?\s*\}\}\s*</span>'
def fix_sem_robust(match):
    return f'<span class="{match.group(1)}">\n                                        {{{{ mk.semester|default:"Pilihan" }}}}\n                                    </span>'

content = re.sub(sem_pattern, fix_sem_robust, content)

# General cleanup for any other split tags I might have added
pattern_gen = r'\{\{\s*\n\s*([^}]+?)\s*\}\}'
content = re.sub(pattern_gen, lambda m: '{{ ' + m.group(1).strip() + ' }}', content)

with open(file_path, 'w') as f:
    f.write(content)

print("Template tags fixed with robust formatting.")
