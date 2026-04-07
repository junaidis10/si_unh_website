import re

file_path = 'templates/akademik.html'

with open(file_path, 'r') as f:
    content = f.read()

# Pattern to find the broken spans for SKS
# It looks for the class, then the {{, then newline/spaces, then the variable, then }}
sks_pattern = r'(<span\s+class="[^"]+inline-block bg-gray-200 text-gray-700 w-6 h-6 rounded-full flex items-center justify-center font-bold mx-auto">)\{\{\s*\n\s*mk\.sks\s*\}\}'
def fix_sks(match):
    return match.group(1) + '{{ mk.sks }}'

content = re.sub(sks_pattern, fix_sks, content)

# Pattern for Semester
sem_pattern = r'(<span\s+class="[^"]+py-1 px-3 rounded-full text-xs font-bold">)\{\{\s*\n\s*mk\.semester\|default:"Pilihan"\s*\}\}'
def fix_sem(match):
    return match.group(1) + '{{ mk.semester|default:"Pilihan" }}'

content = re.sub(sem_pattern, fix_sem, content)

# General fallback for any other split tags
pattern_gen = r'\{\{\s*\n\s*([^}]+?)\s*\}\}'
content = re.sub(pattern_gen, lambda m: '{{ ' + m.group(1).strip() + ' }}', content)

with open(file_path, 'w') as f:
    f.write(content)

print("Template tags fixed permanently with flat formatting.")
