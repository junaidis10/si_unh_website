import requests
import re
from bs4 import BeautifulSoup
import os

url = "https://si.unh.ac.id"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

alumni_list = []

# Based on the snippet found earlier
# <div class="swiper-slide">
#    <div class="testimonial-item">
#       <img src="assets/uploads/artikel/..." class="testimonial-img" alt="...">
#       <h3>...</h3>
#       <h4>...</h4>
#       <p>...</p>

for item in soup.find_all(class_='testimonial-item'):
    img_tag = item.find('img', class_='testimonial-img')
    img_url = url + "/" + img_tag['src'] if img_tag and img_tag.get('src') else None
    
    name_tag = item.find('h3')
    name = name_tag.get_text(strip=True) if name_tag else "Unknown"
    
    info_tag = item.find('h4')
    info = info_tag.get_text(strip=True) if info_tag else ""
    # Usually "2013, Project Manager, PT. Ridikc Industri Indonesia"
    parts = info.split(',', 1)
    tahun_lulus = 0
    pekerjaan = ""
    perusahaan = ""
    
    if len(parts) > 0:
        year_match = re.search(r'\d{4}', parts[0])
        if year_match:
            tahun_lulus = int(year_match.group())
        
        if len(parts) > 1:
            job_parts = parts[1].split(',', 1)
            pekerjaan = job_parts[0].strip()
            if len(job_parts) > 1:
                perusahaan = job_parts[1].strip()
            else:
                perusahaan = pekerjaan # sometimes it's just job
    
    testimoni_tag = item.find('p')
    # Filter out the star div if it exists inside p or sibling
    testimoni = ""
    if testimoni_tag:
        # Clone to not modify original
        p_content = testimoni_tag.get_text(strip=True)
        # Remove any leading/trailing quotes if they exist in text
        testimoni = re.sub(r'^["\']|["\']$', '', p_content)

    alumni_list.append({
        'nama': name,
        'tahun_lulus': tahun_lulus,
        'pekerjaan': pekerjaan,
        'perusahaan': perusahaan,
        'testimoni': testimoni,
        'img_url': img_url
    })

import json
print(json.dumps(alumni_list, indent=2))
