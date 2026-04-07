import re

file_path = 'templates/akademik.html'

with open(file_path, 'r') as f:
    content = f.read()

# Fix multi-line template tags
# This pattern matches {{ followed by whitespace (including newlines) and then some content and }}
# and consolidates it into a single line.
pattern = r'\{\{\s*\n\s*([^}]+?)\s*\}\}'
def consolidate(match):
    return '{{ ' + match.group(1).strip() + ' }}'

new_content = re.sub(pattern, consolidate, content)

# Also fix cases where the closing braces are on a separate line
pattern2 = r'\{\{\s*([^}]+?)\s*\n\s*\}\}'
new_content = re.sub(pattern2, consolidate, new_content)

# Special case for some common split tags if the above missed them
new_content = new_content.replace('{{\n                                        mk.sks }}', '{{ mk.sks }}')
new_content = new_content.replace('{{\n                                        mk.semester|default:"Pilihan" }}', '{{ mk.semester|default:"Pilihan" }}')

with open(file_path, 'w') as f:
    f.write(new_content)

print("Template tags consolidated.")
