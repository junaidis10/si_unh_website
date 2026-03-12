import os
import django
import requests
from django.core.files.base import ContentFile
from django.utils.text import slugify

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'si_unh.settings')
django.setup()

from core.models import Alumni

# Data extracted from si.unh.ac.id
ALUMNI_DATA = [
  {
    "nama": "Arif Sucipto, S.Kom",
    "tahun_lulus": 2017,
    "pekerjaan": "Area Coordinator",
    "perusahaan": "Biznet",
    "testimoni": "Alhamdulillah selama berkuliah di UNH, Saya dapat mengembang kan soft kill maupun hard skill saya dan membangun networking atau relasi sehingga ketika lulus saya dapat berkerja di perusahaan ternama atau Multinasional.",
    "img_url": "https://si.unh.ac.id/assets/uploads/artikel/0c592f584a904d60ad903f807df87ddd.jpeg"
  },
  {
    "nama": "Muhammad Puat, S.Kom",
    "tahun_lulus": 2013,
    "pekerjaan": "Project Manager",
    "perusahaan": "PT. Ridikc Industri Indonesia",
    "testimoni": "saya merasa sangat beruntung pernah menjadi bagian dari lingkungan akademis yang begitu mendukung perkembangan kompetensi di bidang teknologi dan manajemen. Ilmu yang saya dapatkan selama kuliah, mulai dari penguasaan teknologi hingga pengembangan soft skills seperti komunikasi, menjadi fondasi kuat dalam perjalanan karier saya hingga mencapai posisi Project Manager. Terima kasih kepada Universitas Nurdin Hamzah dan seluruh dosen yang telah membimbing saya. Saya bangga menjadi bagian dari keluarga besar UNH dan berharap kampus ini terus mencetak lulusan yang kompeten dan berdaya saing tinggi.",
    "img_url": "https://si.unh.ac.id/assets/uploads/artikel/6422be3cd2ab9a2c8839a0f78c832b07.jpeg"
  },
  {
    "nama": "Eko Kurniadi, S.Kom",
    "tahun_lulus": 2013,
    "pekerjaan": "Senior software Engineer (Mobile Tech Lead)",
    "perusahaan": "Silentmode Sdn. Bhd Malaysia",
    "testimoni": "STMIK Nurdin Hamzah Jambi memberikan saya fondasi yang kuat untuk meniti karier di dunia teknologi. Saat ini, saya bekerja sebagai Senior Software Engineer sekaligus Mobile Tech Lead di core team sebuah perusahaan penyedia software fuel retail yang memiliki klien besar seperti Petronas Malaysia, Shell Singapore, BHP Petrol, dan Jetty Philippines. Ilmu dan pengalaman yang saya peroleh di jurusan Sistem Informasi sangat membantu saya dalam mengembangkan solusi teknologi untuk mendukung industri retail bahan bakar",
    "img_url": "https://si.unh.ac.id/assets/uploads/artikel/d4488a02c3073764263129f852906c98.jpeg"
  },
  {
    "nama": "AKP. Viktor Hamonangan, S.Kom",
    "tahun_lulus": 2020,
    "pekerjaan": "Kasat Sabhara",
    "perusahaan": "Polresta Muaro Jambi",
    "testimoni": "Saya AKP. Viktor Hamonangan, S.Kom Kabag Log Polres Muaro Jambi, Alumni Sistem Informasi Universitas Nurdin Hamzah 2020 d.h STMIK Nurdin Hamzah, semasa kuliah di era Covid-19 dahalu, Kampus Universitas Nurdin Hamzah, khusus Program Studi Sistem Informasi cukup fleksibel dalam menawarkan sistem perkuliahan yang memungkin mahasiswa untuk kuliah sambil bekerja seperti saya, hal ini dapat menjadi solusi bagi mahasiswa yang ingin kuliah sambil bekerja. Anda Ingin berhasil seperti saya, saya sarankan kuliah aja di Sistem Informasi Universitas Nurdin Hamzah. \u201cMaju Inovatif dan Berkarakter \u201d.",
    "img_url": "https://si.unh.ac.id/assets/uploads/artikel/5e23c4c5ed0b13d0f7a883c0fddd3774.png"
  },
  {
    "nama": "Tetra Setiawan, S.Kom",
    "tahun_lulus": 2020,
    "pekerjaan": "Fungsional Umum",
    "perusahaan": "Kantor Imigrasi Kelas I TPI Jambi",
    "testimoni": "Saya Tetra Setiawan, Alumni Program Studi Sistem Informasi. Banyak hal menyenangkan yang aku dapatkan ketika berkuliah di kampus ini. Teman-teman yang baik, dosen yang sangat membimbing, dan pastinya ilmu serta pengalaman yang tidak tergantikan. Aku Bangga Menjadi Lulusan Universitas Nurdin Hamzah.",
    "img_url": "https://si.unh.ac.id/assets/uploads/artikel/d6f3d95f3fe51ea97554fdfb7f9c37d0.png"
  },
  {
    "nama": "Mila Sari, S.Kom",
    "tahun_lulus": 2022,
    "pekerjaan": "Staff",
    "perusahaan": "Kejaksaan Negeri Sungai Penuh",
    "testimoni": "Saya Mila Sari, S.Kom, Alumni Sistem Informasi. \u201cStudi di Universitas Nurdin Hamzah (UNH) telah membekali saya dengan berbagai keterampilan yg esensial. baik soft skills maupun hard skills. Sebagai alumni, saya merasakan ilmu yang diajarkan sangat relevan dengan kebutuhan era digital saat ini. Saya bangga menjadi lulusan sistem informasi Universitas Nurdin Hamzah dan berharap kampus ini terus mencetak lulusan yang berkualitas, inovatif, kreatif dan kolaboratif dibidang teknologi yg bermanfaat dan senantiasa lebih maju, unggul dan berkualitas\u201d",
    "img_url": "https://si.unh.ac.id/assets/uploads/artikel/8583e8fff6e8607830a5c4de31894bc2.jpeg"
  },
  {
    "nama": "Andika Junial Perkasa, S.Kom",
    "tahun_lulus": 2022,
    "pekerjaan": "Penyusun Laporan Keuangan",
    "perusahaan": "Kantor Wilayah Kementerian Hukum dan HAM Jambi",
    "testimoni": "Selama saya kuliah di Universitas Nurdin Hamzah Jambi Prodi Sistem Informasi.. saya mendapatkan banyak hasanah ilmu lagi yang bisa saya salurkan di dalam instansi ditempat kerja saya.. Universitas Nurdin Hamzah Jambi juga mempunyai sarana dan prasarana yg sangat baik sehingga memudahkan kan saya sebagai mahasiswa, dan dosen-dosen prodi Sistem Informasi pada Universitas Nurdin Hamzah Jambi sangat memahami betul bahan ajaran yang di berikan kepada mahasiswa, sehingga itu sangat-sangat berguna untuk saya dalam memahami bahan ajaran tersebut, selain itu Dosen-Dosen Prodi Sistem Informasi Universitas Nurdin Hamzah Jambi juga sangat membantu saya dalam diskusi ataupun tanya jawab tentang apa yang belum saya mengerti.. Sekali Lagi saya mengucapkan terima kasih untuk semua Dosen-Dosen Prodi Sistem Informasi Universitas Nurdin Hamzah Jambi atas segala ilmu yang telah diberikan ke saya dan juga harapan saya Universitas Nurdin Hamzah jambi semakin lebih baik dan besar kedepan nya..",
    "img_url": "https://si.unh.ac.id/assets/uploads/artikel/508b18d4c059a4d8f5c33272498c3a17.jpeg"
  },
  {
    "nama": "Titik Masrini, A.Md,.S.Kom",
    "tahun_lulus": 2020,
    "pekerjaan": "Pemeriksa Keimigrasian Lanjutan/Mahir",
    "perusahaan": "Kantor Imigrasi Kelas I TPI Jambi",
    "testimoni": "Saya Titik Masrini, A.Md,.S.Kom, Lulusan Program Studi Sistem Informasi Semasa berlajar di Kampus UNH Jambi kurang lebih dua tahun dan saat saya belajar di kampus UNH jambi saya tidak menemukan kendala apapun dan saat saya belajar selalu di bantu oleh para dosen UNH jika saya mendapatkan kendala atau saya mendapat kesulitan dlm mengerjakan tugas yg di berikan oleh dosen. Kampus UNH Jambi the best dan akan selalu menjadi rekomendasi buat anak\u201d muda yg gemar akan IT. Sukses selalu UNH Jambi.",
    "img_url": "https://si.unh.ac.id/assets/uploads/artikel/0f53eeb7a2a71e64611acac597ffd485.jpeg"
  },
  {
    "nama": "Warmansyah, S.Kom",
    "tahun_lulus": 2015,
    "pekerjaan": "LOAN Service",
    "perusahaan": "Bank BTN",
    "testimoni": "Saya Warmansyah, S.Kom Alumni Program Studi Sistem Informasi. Sekarang Menjadi Universitas Nurdin Hamzah d.h STMIK Nurdin Hamzah. Banyak hal menyenangkan yang aku dapatkan ketika berkuliah di kampus ini. Teman-teman yang baik, dosen yang sangat membimbing, dan pastinya ilmu serta pengalaman yang tidak tergantikan. Aku Bangga Menjadi Lulusan Universitas Nurdin Hamzah.",
    "img_url": "https://si.unh.ac.id/assets/uploads/artikel/dd8a870d996ffdda93d838a4b686a0cf.jpg"
  },
  {
    "nama": "Heri Zulkifli,S.Kom",
    "tahun_lulus": 2020,
    "pekerjaan": "Fungsional Tata Usaha",
    "perusahaan": "Kantor Imigrasi Kelas I TPI Jambi",
    "testimoni": "Halo, saya Heri Zulkifli, alumni Universitas Nurdin Hamzah dari Program Studi Sistem Informasi. Saat ini, saya menjabat sebagai Jabatan Fungsional Tata Usaha di Kantor Imigrasi Kelas I TPI Jambi. Pengalaman kuliah di Universitas Nurdin Hamzah tidak hanya memberikan saya pengetahuan akademis yang mendalam, dan \"Kuliah sambil kerja adalah bukti bahwa kamu adalah seorang yang tangguh\". , Terima Kasih Universitas Nurdin Hamzah Jambi Bergabunglah dengan Universitas Nurdin Hamzah dan wujudkan impianmu bersama kami!",
    "img_url": "https://si.unh.ac.id/assets/uploads/artikel/3dbe6f2e55815d9d8ad627e238e5eae8.png"
  },
  {
    "nama": "Hendika,S.Kom",
    "tahun_lulus": 2022,
    "pekerjaan": "Auditor Penyelia",
    "perusahaan": "Inspektorat Daerah Kabupaten Batang Hari",
    "testimoni": "Menjadi mahasiswa Sistem Informasi Universitas Nurdin Hamzah adalah salah satu nikmat terbesar yang sangat saya syukuri . Belajar dengan berasaskan kekeluargaan, lingkungan yang mendukung dalam proses mengupdgrade diri menjadi lebih baik, serta banyak memberikan pengalaman dan keilmuan baru yang tidak banyak di ketahui orang, Dosen- Dosen yang Luar biasa selalu mau diajak sharing tentang segala macam kendala yang saya hadapi, teman-teman seperjuangan yang selalu saling membantu. Kuliah \u2026. berbicara mengenai prospek kerja keinginan untuk pengembangan karier tentunya , apalagi bagi kami dikelas pekerja yang telah mengetahui apa apa yang menjadi tujuan dalam karir kedepannya , namun juga tetap mengedepankan perkembangan akhlak yang bisa membuat diri kita menjadi pribadi yang lebih baik lagi, serta Bertemu dengan dengan rekan-rekan sejawat dari tempat kerja yang berbeda sehingga memperluas wawasan dan relasi kerja . Di prodi sistem Informasi saya diajarkan bagaimana belajar menggunakan hati, di prodi ini saya dilatih agar menjadi lebih berani dalam menghadapi situasi kerja kedepannya . Saya bangga dan bersyukur bisa menjadi salah satu alumni dari prodi Sistem Informasi yang luar biasa ini \u2026. Terima Kasih orang orang baik \u2026",
    "img_url": "https://si.unh.ac.id/assets/uploads/artikel/5c1f69b5d6a90eae131e2000dbca1ad1.png"
  },
  {
    "nama": "Renol,S.Kom",
    "tahun_lulus": 2022,
    "pekerjaan": "Manager Divisi",
    "perusahaan": "PT Perkebunan Nusantara IV Regional 4 Jambi-Sumatera",
    "testimoni": "Program Studi Saraja Sistem Informasi - Universitas Nurdin Hamzah (UNH), menurut saya adalah tempat terbaik untuk menuntut ilmu menjadi Sarjana Sistem Informasi (S.Kom) , karena selama saya belajar di UNH, saya banyak mendapatkan ilmu yang bermanfaat, dan juga pengetahuan seputar manajemen informatika dan komunikasi. Dosen-dosennya pun menurut saya berkualitas, mereka memberikan pengajaran sampai saya dan teman-teman menjadi bisa dan tentunya didukung dengan tempat kuliah yang bersih dan nyaman. Sebagai mahasiswa Sistem Informasi, kita tidak akan pernah luput dari kegiatan komputerisasi. Maka dari itu, laboratorium komputer disediakan untuk mahasiswa, dengan puluhan komputer yang cepat, siap untuk membantu mahasiswa dalam menyelesaikan berbagai macam tugas dan tentunya untuk aktivitas perkuliahan. Saat ini saya bekerja di PT Perkebunan Nusantara IV Regiona 4 Jambi-Sumatera (BUMN yang bergerak di bidang Perkebunan Kelapa Sawit). Ilmu-ilmu yang diajarkan sewaktu kuliah ternyata terpakai di tempat kerja saya. Saya mendapatkan pelajaran yang lengkap di Universitas Nurdin Hamzah, dari sisi hard-skill dan juga soft-skill yang berguna untuk saya. Semoga Universitas Nurdin Hamzah semakin maju dan terdepan dalam \u2018mencetak\u2019 sarjana-sarjana yang berkualitas dan handal.",
    "img_url": "https://si.unh.ac.id/assets/uploads/artikel/32a22210435ddf3ce3843e1f0cddc466.jpeg"
  }
]

def populate():
    print("Clearing existing alumni records...")
    Alumni.objects.all().delete()
    
    media_path = os.path.join(django.conf.settings.MEDIA_ROOT, 'alumni')
    if not os.path.exists(media_path):
        os.makedirs(media_path)
        print(f"Created directory: {media_path}")

    for data in ALUMNI_DATA:
        print(f"Processing: {data['nama']}")
        
        alumnus = Alumni(
            nama=data['nama'],
            nim='N/A', # Placeholder as it's required in model
            tahun_lulus=data['tahun_lulus'],
            pekerjaan=data['pekerjaan'],
            perusahaan=data['perusahaan'],
            testimoni=data['testimoni']
        )
        
        # Download image
        if data['img_url']:
            try:
                response = requests.get(data['img_url'], timeout=10)
                if response.status_code == 200:
                    ext = data['img_url'].split('.')[-1]
                    if '?' in ext: ext = ext.split('?')[0]
                    file_name = f"{slugify(data['nama'])}.{ext}"
                    alumnus.photo.save(file_name, ContentFile(response.content), save=False)
                    print(f"  Downloaded photo: {file_name}")
                else:
                    print(f"  Failed to download photo. Status: {response.status_code}")
            except Exception as e:
                print(f"  Error downloading photo: {e}")
        
        alumnus.save()
        print(f"  Saved record for {data['nama']}")

if __name__ == '__main__':
    populate()
    print("Population complete!")
