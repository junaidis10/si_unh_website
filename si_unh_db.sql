-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Mar 11, 2026 at 04:36 AM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `si_unh_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add slide', 7, 'add_slide'),
(26, 'Can change slide', 7, 'change_slide'),
(27, 'Can delete slide', 7, 'delete_slide'),
(28, 'Can view slide', 7, 'view_slide'),
(29, 'Can add sambutan', 8, 'add_sambutan'),
(30, 'Can change sambutan', 8, 'change_sambutan'),
(31, 'Can delete sambutan', 8, 'delete_sambutan'),
(32, 'Can view sambutan', 8, 'view_sambutan'),
(33, 'Can add visi misi', 9, 'add_visimisi'),
(34, 'Can change visi misi', 9, 'change_visimisi'),
(35, 'Can delete visi misi', 9, 'delete_visimisi'),
(36, 'Can view visi misi', 9, 'view_visimisi'),
(37, 'Can add prospek keunggulan', 10, 'add_prospekkeunggulan'),
(38, 'Can change prospek keunggulan', 10, 'change_prospekkeunggulan'),
(39, 'Can delete prospek keunggulan', 10, 'delete_prospekkeunggulan'),
(40, 'Can view prospek keunggulan', 10, 'view_prospekkeunggulan'),
(41, 'Can add dosen', 11, 'add_dosen'),
(42, 'Can change dosen', 11, 'change_dosen'),
(43, 'Can delete dosen', 11, 'delete_dosen'),
(44, 'Can view dosen', 11, 'view_dosen'),
(45, 'Can add document category', 12, 'add_documentcategory'),
(46, 'Can change document category', 12, 'change_documentcategory'),
(47, 'Can delete document category', 12, 'delete_documentcategory'),
(48, 'Can view document category', 12, 'view_documentcategory'),
(49, 'Can add document', 13, 'add_document'),
(50, 'Can change document', 13, 'change_document'),
(51, 'Can delete document', 13, 'delete_document'),
(52, 'Can view document', 13, 'view_document'),
(53, 'Can add news', 14, 'add_news'),
(54, 'Can change news', 14, 'change_news'),
(55, 'Can delete news', 14, 'delete_news'),
(56, 'Can view news', 14, 'view_news'),
(57, 'Can add gallery', 15, 'add_gallery'),
(58, 'Can change gallery', 15, 'change_gallery'),
(59, 'Can delete gallery', 15, 'delete_gallery'),
(60, 'Can view gallery', 15, 'view_gallery'),
(61, 'Can add prestasi', 16, 'add_prestasi'),
(62, 'Can change prestasi', 16, 'change_prestasi'),
(63, 'Can delete prestasi', 16, 'delete_prestasi'),
(64, 'Can view prestasi', 16, 'view_prestasi'),
(65, 'Can add penelitian', 17, 'add_penelitian'),
(66, 'Can change penelitian', 17, 'change_penelitian'),
(67, 'Can delete penelitian', 17, 'delete_penelitian'),
(68, 'Can view penelitian', 17, 'view_penelitian'),
(69, 'Can add akreditasi', 18, 'add_akreditasi'),
(70, 'Can change akreditasi', 18, 'change_akreditasi'),
(71, 'Can delete akreditasi', 18, 'delete_akreditasi'),
(72, 'Can view akreditasi', 18, 'view_akreditasi'),
(73, 'Can add alumni', 19, 'add_alumni'),
(74, 'Can change alumni', 19, 'change_alumni'),
(75, 'Can delete alumni', 19, 'delete_alumni'),
(76, 'Can view alumni', 19, 'view_alumni'),
(77, 'Can add job career', 20, 'add_jobcareer'),
(78, 'Can change job career', 20, 'change_jobcareer'),
(79, 'Can delete job career', 20, 'delete_jobcareer'),
(80, 'Can view job career', 20, 'view_jobcareer'),
(81, 'Can add link', 21, 'add_link'),
(82, 'Can change link', 21, 'change_link'),
(83, 'Can delete link', 21, 'delete_link'),
(84, 'Can view link', 21, 'view_link'),
(85, 'Can add page content', 22, 'add_pagecontent'),
(86, 'Can change page content', 22, 'change_pagecontent'),
(87, 'Can delete page content', 22, 'delete_pagecontent'),
(88, 'Can view page content', 22, 'view_pagecontent'),
(89, 'Can add mata kuliah', 23, 'add_matakuliah'),
(90, 'Can change mata kuliah', 23, 'change_matakuliah'),
(91, 'Can delete mata kuliah', 23, 'delete_matakuliah'),
(92, 'Can view mata kuliah', 23, 'view_matakuliah'),
(93, 'Can add survey response', 25, 'add_surveyresponse'),
(94, 'Can change survey response', 25, 'change_surveyresponse'),
(95, 'Can delete survey response', 25, 'delete_surveyresponse'),
(96, 'Can view survey response', 25, 'view_surveyresponse'),
(97, 'Can add Buku Panduan', 24, 'add_bukupanduan'),
(98, 'Can change Buku Panduan', 24, 'change_bukupanduan'),
(99, 'Can delete Buku Panduan', 24, 'delete_bukupanduan'),
(100, 'Can view Buku Panduan', 24, 'view_bukupanduan'),
(101, 'Can add survey kepuasan lulusan', 26, 'add_surveykepuasanlulusan'),
(102, 'Can change survey kepuasan lulusan', 26, 'change_surveykepuasanlulusan'),
(103, 'Can delete survey kepuasan lulusan', 26, 'delete_surveykepuasanlulusan'),
(104, 'Can view survey kepuasan lulusan', 26, 'view_surveykepuasanlulusan'),
(105, 'Can add survey kurikulum', 27, 'add_surveykurikulum'),
(106, 'Can change survey kurikulum', 27, 'change_surveykurikulum'),
(107, 'Can delete survey kurikulum', 27, 'delete_surveykurikulum'),
(108, 'Can view survey kurikulum', 27, 'view_surveykurikulum');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$720000$oiB0Eqi4gnlIYVbsEedMPD$nvFWId/1vrpRj7bOOihid0+H7F3jaaACGpqmbjyogtk=', '2026-03-11 02:14:18.820383', 1, 'junaidisurya', '', '', 'junaidis10@gmail.com', 1, 1, '2026-02-01 07:49:06.563792'),
(2, 'pbkdf2_sha256$720000$61gNMSnMjktDIdZshSyCt0$Wajn3kGvPppc4BRO0g2Y15IhyiwTF1xriNS7cpuSU6w=', NULL, 1, 'testadmin', '', '', '', 1, 1, '2026-02-21 15:58:39.027584');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `core_akreditasi`
--

CREATE TABLE `core_akreditasi` (
  `id` bigint(20) NOT NULL,
  `program` varchar(100) NOT NULL,
  `peringkat` varchar(20) NOT NULL,
  `nomor_sk` varchar(100) NOT NULL,
  `tanggal_sk` date NOT NULL,
  `masa_berlaku` date NOT NULL,
  `lembaga` varchar(100) NOT NULL,
  `certificate_file` varchar(100) NOT NULL,
  `is_active` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `core_akreditasi`
--

INSERT INTO `core_akreditasi` (`id`, `program`, `peringkat`, `nomor_sk`, `tanggal_sk`, `masa_berlaku`, `lembaga`, `certificate_file`, `is_active`) VALUES
(1, 'Program Studi Sistem Informasi', 'Baik Sekali', '080/SK/LAM-INFOKOM/Ak.B/S/XII/2023', '2023-12-17', '2028-12-17', 'LAM INFOKOM', 'akreditasi/Surat_Sertifikat_LAMINFOKOM.pdf', 1),
(2, 'Program Studi Sistem Informasi', 'B', '9747/SK/BAN-PT/Ak-PNB/S/VI/2021', '2020-09-02', '2023-05-08', 'BAN-PT', 'akreditasi/Sertifikat-SI-Update.jpg', 1),
(3, 'Program Studi Sistem Informasi', 'B', '1259/SK/BAN_PT/Akred/S/V/2018', '2018-05-08', '2023-05-08', 'BAN-PT', 'akreditasi/Sertifikat.pdf', 1);

-- --------------------------------------------------------

--
-- Table structure for table `core_alumni`
--

CREATE TABLE `core_alumni` (
  `id` bigint(20) NOT NULL,
  `nama` varchar(100) NOT NULL,
  `nim` varchar(20) NOT NULL,
  `tahun_lulus` int(11) NOT NULL,
  `pekerjaan` varchar(200) NOT NULL,
  `perusahaan` varchar(200) NOT NULL,
  `email` varchar(254) NOT NULL,
  `phone` varchar(20) NOT NULL,
  `photo` varchar(100) NOT NULL,
  `testimoni` longtext NOT NULL,
  `linkedin` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `core_alumni`
--

INSERT INTO `core_alumni` (`id`, `nama`, `nim`, `tahun_lulus`, `pekerjaan`, `perusahaan`, `email`, `phone`, `photo`, `testimoni`, `linkedin`) VALUES
(18, 'Arif Sucipto, S.Kom', 'N/A', 2017, 'Area Coordinator', 'Biznet', '', '', 'alumni/arif-sucipto-skom.jpeg', 'Alhamdulillah selama berkuliah di UNH, Saya dapat mengembang kan soft kill maupun hard skill saya dan membangun networking atau relasi sehingga ketika lulus saya dapat berkerja di perusahaan ternama atau Multinasional.', ''),
(19, 'Muhammad Puat, S.Kom', 'N/A', 2013, 'Project Manager', 'PT. Ridikc Industri Indonesia', '', '', 'alumni/muhammad-puat-skom_0ZKPpgC.jpeg', 'saya merasa sangat beruntung pernah menjadi bagian dari lingkungan akademis yang begitu mendukung perkembangan kompetensi di bidang teknologi dan manajemen. Ilmu yang saya dapatkan selama kuliah, mulai dari penguasaan teknologi hingga pengembangan soft skills seperti komunikasi, menjadi fondasi kuat dalam perjalanan karier saya hingga mencapai posisi Project Manager. Terima kasih kepada Universitas Nurdin Hamzah dan seluruh dosen yang telah membimbing saya. Saya bangga menjadi bagian dari keluarga besar UNH dan berharap kampus ini terus mencetak lulusan yang kompeten dan berdaya saing tinggi.', ''),
(20, 'Eko Kurniadi, S.Kom', 'N/A', 2013, 'Senior software Engineer (Mobile Tech Lead)', 'Silentmode Sdn. Bhd Malaysia', '', '', 'alumni/eko-kurniadi-skom.jpeg', 'STMIK Nurdin Hamzah Jambi memberikan saya fondasi yang kuat untuk meniti karier di dunia teknologi. Saat ini, saya bekerja sebagai Senior Software Engineer sekaligus Mobile Tech Lead di core team sebuah perusahaan penyedia software fuel retail yang memiliki klien besar seperti Petronas Malaysia, Shell Singapore, BHP Petrol, dan Jetty Philippines. Ilmu dan pengalaman yang saya peroleh di jurusan Sistem Informasi sangat membantu saya dalam mengembangkan solusi teknologi untuk mendukung industri retail bahan bakar', ''),
(21, 'AKP. Viktor Hamonangan, S.Kom', 'N/A', 2020, 'Kasat Sabhara', 'Polresta Muaro Jambi', '', '', 'alumni/akp-viktor-hamonangan-skom.png', 'Saya AKP. Viktor Hamonangan, S.Kom Kabag Log Polres Muaro Jambi, Alumni Sistem Informasi Universitas Nurdin Hamzah 2020 d.h STMIK Nurdin Hamzah, semasa kuliah di era Covid-19 dahalu, Kampus Universitas Nurdin Hamzah, khusus Program Studi Sistem Informasi cukup fleksibel dalam menawarkan sistem perkuliahan yang memungkin mahasiswa untuk kuliah sambil bekerja seperti saya, hal ini dapat menjadi solusi bagi mahasiswa yang ingin kuliah sambil bekerja. Anda Ingin berhasil seperti saya, saya sarankan kuliah aja di Sistem Informasi Universitas Nurdin Hamzah. “Maju Inovatif dan Berkarakter ”.', ''),
(22, 'Tetra Setiawan, S.Kom', 'N/A', 2020, 'Fungsional Umum', 'Kantor Imigrasi Kelas I TPI Jambi', '', '', 'alumni/tetra-setiawan-skom_rSWAsth.png', 'Saya Tetra Setiawan, Alumni Program Studi Sistem Informasi. Banyak hal menyenangkan yang aku dapatkan ketika berkuliah di kampus ini. Teman-teman yang baik, dosen yang sangat membimbing, dan pastinya ilmu serta pengalaman yang tidak tergantikan. Aku Bangga Menjadi Lulusan Universitas Nurdin Hamzah.', ''),
(23, 'Mila Sari, S.Kom', 'N/A', 2022, 'Staff', 'Kejaksaan Negeri Sungai Penuh', '', '', 'alumni/mila-sari-skom_Qv47JkS.jpeg', 'Saya Mila Sari, S.Kom, Alumni Sistem Informasi. “Studi di Universitas Nurdin Hamzah (UNH) telah membekali saya dengan berbagai keterampilan yg esensial. baik soft skills maupun hard skills. Sebagai alumni, saya merasakan ilmu yang diajarkan sangat relevan dengan kebutuhan era digital saat ini. Saya bangga menjadi lulusan sistem informasi Universitas Nurdin Hamzah dan berharap kampus ini terus mencetak lulusan yang berkualitas, inovatif, kreatif dan kolaboratif dibidang teknologi yg bermanfaat dan senantiasa lebih maju, unggul dan berkualitas”', ''),
(24, 'Andika Junial Perkasa, S.Kom', 'N/A', 2022, 'Penyusun Laporan Keuangan', 'Kantor Wilayah Kementerian Hukum dan HAM Jambi', '', '', 'alumni/andika-junial-perkasa-skom_x1DJpru.jpeg', 'Selama saya kuliah di Universitas Nurdin Hamzah Jambi Prodi Sistem Informasi.. saya mendapatkan banyak hasanah ilmu lagi yang bisa saya salurkan di dalam instansi ditempat kerja saya.. Universitas Nurdin Hamzah Jambi juga mempunyai sarana dan prasarana yg sangat baik sehingga memudahkan kan saya sebagai mahasiswa, dan dosen-dosen prodi Sistem Informasi pada Universitas Nurdin Hamzah Jambi sangat memahami betul bahan ajaran yang di berikan kepada mahasiswa, sehingga itu sangat-sangat berguna untuk saya dalam memahami bahan ajaran tersebut, selain itu Dosen-Dosen Prodi Sistem Informasi Universitas Nurdin Hamzah Jambi juga sangat membantu saya dalam diskusi ataupun tanya jawab tentang apa yang belum saya mengerti.. Sekali Lagi saya mengucapkan terima kasih untuk semua Dosen-Dosen Prodi Sistem Informasi Universitas Nurdin Hamzah Jambi atas segala ilmu yang telah diberikan ke saya dan juga harapan saya Universitas Nurdin Hamzah jambi semakin lebih baik dan besar kedepan nya..', ''),
(25, 'Titik Masrini, A.Md,.S.Kom', 'N/A', 2020, 'Pemeriksa Keimigrasian Lanjutan/Mahir', 'Kantor Imigrasi Kelas I TPI Jambi', '', '', 'alumni/titik-masrini-amdskom_hrIwqx4.jpeg', 'Saya Titik Masrini, A.Md,.S.Kom, Lulusan Program Studi Sistem Informasi Semasa berlajar di Kampus UNH Jambi kurang lebih dua tahun dan saat saya belajar di kampus UNH jambi saya tidak menemukan kendala apapun dan saat saya belajar selalu di bantu oleh para dosen UNH jika saya mendapatkan kendala atau saya mendapat kesulitan dlm mengerjakan tugas yg di berikan oleh dosen. Kampus UNH Jambi the best dan akan selalu menjadi rekomendasi buat anak” muda yg gemar akan IT. Sukses selalu UNH Jambi.', ''),
(26, 'Warmansyah, S.Kom', 'N/A', 2015, 'LOAN Service', 'Bank BTN', '', '', 'alumni/warmansyah-skom_BpotMtc.jpg', 'Saya Warmansyah, S.Kom Alumni Program Studi Sistem Informasi. Sekarang Menjadi Universitas Nurdin Hamzah d.h STMIK Nurdin Hamzah. Banyak hal menyenangkan yang aku dapatkan ketika berkuliah di kampus ini. Teman-teman yang baik, dosen yang sangat membimbing, dan pastinya ilmu serta pengalaman yang tidak tergantikan. Aku Bangga Menjadi Lulusan Universitas Nurdin Hamzah.', ''),
(27, 'Heri Zulkifli,S.Kom', 'N/A', 2020, 'Fungsional Tata Usaha', 'Kantor Imigrasi Kelas I TPI Jambi', '', '', 'alumni/heri-zulkifliskom_De1cHDZ.png', 'Halo, saya Heri Zulkifli, alumni Universitas Nurdin Hamzah dari Program Studi Sistem Informasi. Saat ini, saya menjabat sebagai Jabatan Fungsional Tata Usaha di Kantor Imigrasi Kelas I TPI Jambi. Pengalaman kuliah di Universitas Nurdin Hamzah tidak hanya memberikan saya pengetahuan akademis yang mendalam, dan \"Kuliah sambil kerja adalah bukti bahwa kamu adalah seorang yang tangguh\". , Terima Kasih Universitas Nurdin Hamzah Jambi Bergabunglah dengan Universitas Nurdin Hamzah dan wujudkan impianmu bersama kami!', ''),
(28, 'Hendika,S.Kom', 'N/A', 2022, 'Auditor Penyelia', 'Inspektorat Daerah Kabupaten Batang Hari', '', '', 'alumni/hendikaskom_evEhbo2.png', 'Menjadi mahasiswa Sistem Informasi Universitas Nurdin Hamzah adalah salah satu nikmat terbesar yang sangat saya syukuri . Belajar dengan berasaskan kekeluargaan, lingkungan yang mendukung dalam proses mengupdgrade diri menjadi lebih baik, serta banyak memberikan pengalaman dan keilmuan baru yang tidak banyak di ketahui orang, Dosen- Dosen yang Luar biasa selalu mau diajak sharing tentang segala macam kendala yang saya hadapi, teman-teman seperjuangan yang selalu saling membantu. Kuliah …. berbicara mengenai prospek kerja keinginan untuk pengembangan karier tentunya , apalagi bagi kami dikelas pekerja yang telah mengetahui apa apa yang menjadi tujuan dalam karir kedepannya , namun juga tetap mengedepankan perkembangan akhlak yang bisa membuat diri kita menjadi pribadi yang lebih baik lagi, serta Bertemu dengan dengan rekan-rekan sejawat dari tempat kerja yang berbeda sehingga memperluas wawasan dan relasi kerja . Di prodi sistem Informasi saya diajarkan bagaimana belajar menggunakan hati, di prodi ini saya dilatih agar menjadi lebih berani dalam menghadapi situasi kerja kedepannya . Saya bangga dan bersyukur bisa menjadi salah satu alumni dari prodi Sistem Informasi yang luar biasa ini …. Terima Kasih orang orang baik …', ''),
(29, 'Renol,S.Kom', 'N/A', 2022, 'Manager Divisi', 'PT Perkebunan Nusantara IV Regional 4 Jambi-Sumatera', '', '', 'alumni/renolskom_YcQMP6n.jpeg', 'Program Studi Saraja Sistem Informasi - Universitas Nurdin Hamzah (UNH), menurut saya adalah tempat terbaik untuk menuntut ilmu menjadi Sarjana Sistem Informasi (S.Kom) , karena selama saya belajar di UNH, saya banyak mendapatkan ilmu yang bermanfaat, dan juga pengetahuan seputar manajemen informatika dan komunikasi. Dosen-dosennya pun menurut saya berkualitas, mereka memberikan pengajaran sampai saya dan teman-teman menjadi bisa dan tentunya didukung dengan tempat kuliah yang bersih dan nyaman. Sebagai mahasiswa Sistem Informasi, kita tidak akan pernah luput dari kegiatan komputerisasi. Maka dari itu, laboratorium komputer disediakan untuk mahasiswa, dengan puluhan komputer yang cepat, siap untuk membantu mahasiswa dalam menyelesaikan berbagai macam tugas dan tentunya untuk aktivitas perkuliahan. Saat ini saya bekerja di PT Perkebunan Nusantara IV Regiona 4 Jambi-Sumatera (BUMN yang bergerak di bidang Perkebunan Kelapa Sawit). Ilmu-ilmu yang diajarkan sewaktu kuliah ternyata terpakai di tempat kerja saya. Saya mendapatkan pelajaran yang lengkap di Universitas Nurdin Hamzah, dari sisi hard-skill dan juga soft-skill yang berguna untuk saya. Semoga Universitas Nurdin Hamzah semakin maju dan terdepan dalam ‘mencetak’ sarjana-sarjana yang berkualitas dan handal.', ''),
(30, 'Ubaidillah, S.Kom', '16111096', 2016, 'Lurah Pasir Putih Kota Jambi', 'Pemrintahan', 'ubaidillah@gmail.com', '081527765482', 'alumni/Ubaidillah_S.Kom.png', 'Saya Ubaidillah, S.Kom. Saat ini menjabat sebagai Lurah Pasir Putih Kecematan Jambi Selatan Kota Jambi, Alumni Universitas Nurdin Hamzah Program Studi Sistem Informasi, Program Studi Sistem Informasi cukup fleksibel dalam menawarkan sistem perkuliahan yang manarik dan mempunyai prospek  kerja lulusan yang banyak  disamping itu, kampus juga didukung oleh sarana dan prasarana perkuliahan yang baik, sehingga mendukung  muda mudi untuk menjadi sukses di masa depan. Anda Ingin sukses seperti saya, saya kuliah aja di Sistem Informasi Universitas Nurdin Hamzah.', '');

-- --------------------------------------------------------

--
-- Table structure for table `core_document`
--

CREATE TABLE `core_document` (
  `id` bigint(20) NOT NULL,
  `title` varchar(200) NOT NULL,
  `description` longtext NOT NULL,
  `file` varchar(100) NOT NULL,
  `file_size` varchar(50) NOT NULL,
  `thumbnail` varchar(100) NOT NULL,
  `uploaded_at` datetime(6) NOT NULL,
  `download_count` int(11) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `uploaded_by_id` int(11) DEFAULT NULL,
  `category_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `core_document`
--

INSERT INTO `core_document` (`id`, `title`, `description`, `file`, `file_size`, `thumbnail`, `uploaded_at`, `download_count`, `is_active`, `uploaded_by_id`, `category_id`) VALUES
(1, 'Kurikulum Berbasis OBE/KKNI/SKKNI & APTIKOM', 'Program Studi Sistem Informasi mengajarkan landasan ilmu pengetahuan dan penerapan Teknologi Informasi dalam suatu organisasi. Terkait hal tersebut, kurikulum Program Studi Sistem Informasi bersifat khas karena dibangun di atas 3 (tiga) bidang yaitu: komputer, manajemen dan bisnis. Sehingga profil lulusan Program Studi Sistem Informasi memenuhi aspek sikap dan tata nilai, kompetensi umum dan kompetensi khusus sesuai Standar Kompetensi Kerja Nasional Indonesia (SKKNI) sebagaimana dirumuskan dalam Permendibud No. 49 Tahun 2014. Sehingga Peran dan kompetensi lulusan PS Sistem Informasi memenuhi aspek sikap dan tata nilai, sedangkan kompetensi utama sebagai penciri program studi sistem informasi, sesuai Kerangka Kualifikasi Nasional Indonesia (KKNI) sebagaimana dirumuskan dalam Permendikbud No. 49 Tahun 2014. Dengan mengacu pada deskripsi umum KKNI jenjang enam (6), maka peran dan kompetensi lulusan Program Studi Sistem Informasi yang mencakup aspek sikap, pengetahuan, keterampilan umum, dan keterampilan khusus. Kurikulum Program Studi Sistem Informasi Filkom UNH 2022 dirumuskan dengan tujuan menghasilkan lulusan yang mampu melaksanakan 5 (lima) peran, yaitu:\r\n1. Pengembangan Sistem Informasi (P-SI.1)\r\nPeran ini diharapkan memiliki kemampuan menerapkan konsep-konsep dasar dalam merencanakan yang meliputi pengembangan perangkat lunak dan keuangan, merancang, membangun dan mengevaluasi Sistem Informasi. Profesi Lulusan dari profil ini adalah Manajer Proyek SI/TI, Analis Sistem (System Analyst), Analis Sistem Bisnis (Business System Analyst), Perancangan Sistem (System Designer), Programmer, dan Arsitek Aplikasi (Application Architect), (Web Developer & System Integrator).\r\n2. Pengelola Sistem Informasi (P-SI.2)\r\nPeran ini diharapkan memiliki menerapkan konsep-konsep dasar dalam mengoperasikan, pengelolaan, evaluasi, serta pengembangan lanjut sistem Informasi untuk pengembangan organisasi/bisnis. Profesi Lulusan dari profil ini adalah Manajer Produk Digital, IT Service Desk Analyst, Manajer Layanan IT, IT Operation Supervisor, IT Service Analyst, Business Analyst, Data Entry Supervisor, e- Commerce Specialist, Help Desk Analyst, ICT Operation Support.\r\n3. Spesialis Basis Data dan Data Saint (P-SI.3)\r\nPeran lulusan yang mencakup perancang, pembangun, perawatan (termasuk updating), hingga analisis basis data. Profesi Lulusan dari profil ini adalah Database Designer, Database Programmer, Database Administrator, Analis Data (Data Analyst), Data Warehouse Analyst, dan Business Intelligence Analyst. adalah data scientist, business intelligence analyst and data engineer.\r\n4. Tata Kelola Sistem Informasi (P-SI.4)\r\nPeran ini diharapkan memiliki kemampuan menerapkan konsep dasar dalam mengevaluasi dan mendesain tata kelola sistem informasi sesuai dengan pedoman tata kelola IT/IS dalam rangka penyelarasan IT dan bisnis/organisasi. Profesi dari profil ini adalah Auditor IT/IS, Government Information Officer, Disaster Recovery Staff, Key Performance Indicator Analyst.\r\n5. Kewirausahaan (Entrepneurship) (P-SI.5)\r\nPeran ini, mahasiswa diharapkan sebagai agen perubahan dan pelopor bisnis\r\ndigital yang dapat melahirkan wirausahawan baru dan meningkatkan jumlah wirausaha di kalangan masyarakat. Peningkatan jumlah wirausaha diharapkan akan meningkatkan jumlah lapangan kerja dan mengurangi jumlah pengangguran.', 'documents/2026/02/NASKAH_AKADEMIK__KURIKULUM_BERBASIS_KERANGKA_KUALIFIKASI_NASIONAL_INDO_bCH9iJM.pdf', '', 'document_thumbnails/3802da8874e145923bb436a0f95da600.jpg', '2026-02-01 14:49:36.595383', 2, 1, 1, 4),
(3, 'Pembimbing Akademik', 'PEMBIMBING AKADEMIK\r\n\r\nPERAN & FUNGSI DOSEN PEMBIMBING AKADEMIK\r\n \r\nA.  Pendahuluan. \r\nPendidikan mempunyai peran penting untuk menjamin perkembangan dan kelangsungan kehidupan manusia, karena pendidikan pada dasarnya merupakan upaya menyiapkan peserta didik dimasa mendatang. Pendidikan juga merupakan proses pertumbuhan dimana individu diberi pertolongan untuk mengembangkan kemampuan, minat dan bakatnya,1 seperti tertulis bahwa tujuan pendidikan nasional adalah mencerdaskan kehidupan bangsa dan mengembangkan manusia seutuhnya yaitu manusia yang beriman dan bertaqwa kepada Tuhan Yang Mahas Esa dan berbudi pekerti luhur, memiliki pengetahuan dan ketrampilan, kesehatan jasmani dan rohani, kepribadian yang mantap dan mandiri serta rasa tanggung jawab kemasyarakatan dan kebangsaan. Universitas Nurdin Hamzah sebagai salah satu lembaga pendidikan tinggi terus berpacu untuk mewujudkan tujuan pendidikan nasional. Untuk itu, dosen dan mahasiswa sebagai subjek dan objek pendidikan perlu kerjasama, seiring dan sejalan dalam menuju cita-cita yang diidamkan. Bimbingan, motivasi, nasehat dan lain-lain hendaknya terus ditanamkan pada diri mahasiswa tersebut agar memiliki kepribadian yang mantap, disiplin dalam  belajar serta tekun dalam menggali ilmu pengetahuan. Dalam hal ini perguruan tinggi menunjuk tenaga pendidik tertentu u﻿ntuk memberikan bimbingan, motivasi serta naseh﻿at yang bersifat akademik kepada mahasiswa. Tenaga pendidik yang dimaksud adalah dosen pembimbing akademik (PA).\r\n\r\nB.  Peranan Dosen Pembimbing Akademik\r\nSecara umum peranan dan tugas  dosen Pembimbing akademik adalah sebagai berikut:\r\n1.     Memberi pengarahan kepada mahasiswa yang berada dibawah tanggung jawabnya dalam menyusun rencana dan beban studi serta membantu mahasiswa dalam memilih mata kuliah yang hendak diambil.\r\n2.     Memberi kesempatan kepada mahasiswa untuk membicarakan masalah-masalah yang dialami, khususnya yang berkenaan dengan studinya. \r\n3.     Membantu mahasiswa agar dapat mengembangkan sikap dan kebiasaan belajar yang baik dan terencana sesuai dengan ketentuan akademik.\r\n4.     Mengikuti perkembangan pendidikan mahasiswa yang dibimbing dengan baik\r\n5.     Memanggil mahasiswa bimbingannya untuk tujuan menasehati, mendorong dan membina bimbingannya\r\n6.     Mengarsipkan Copyan Kartu Hasil Studi (KHS) dari mahasiswa yang bersangkutan. \r\n\r\nC.  Peran & Fungsi Dosen Pembimbing Akademik\r\n1.   Peran dan Fungsi Dosen Pembimbing Akademik sebagai Nara Sumber:\r\na.    Memberi informasi tentang budaya kehidupan dan kebiasaan belajar di PT.\r\nb.    Memberi informasi tentang sarana dan prasarana belajar yang dapat diakses, terutama yang tersedia di Universitas Nurdin Hamzah.\r\nc.    Memberi informasi tentang pengalaman belajar kepada mahasiswa baik yang bersifat positif maupun yang negatif.\r\n2.  Peran dan Fungsi Dosen Pembimbing Akademik sebagai Pembimbing:\r\na.    Membantu mahasiswa dalam menyusun program studinya sesuai dengan minat dan kemampuan serta peraturan yang berlaku.\r\nb.    Menetapkan tingkat keberhasilan mahasiswa pada setiap akhir semester dan pada akhir masa studinya.\r\nc.    Menetapkan beban semester mahasiswa sesuai dengan ketentuan yang ditetapkan dalam buku panduan Universitas  Nurdin Hamzah.\r\nd.    Bertanggungjawab atas kebenaran KRS, sesuai dengan validasi dosen PA pada saat membubuhkan tanda tangan.\r\n3. Peran dan Fungsi Dosen Pembimbing Akademik sebagai Penasehat:\r\na.    Membantu mahasiswa dalam menghadapi masalah-masalah belajar.\r\nb.    Membantu mahasiswa dalam mengembangkan sikap dan perilaku yang baik.\r\nc.    Membina mahasiswa dalam mengembangkan sikap profesional pendidik sesuai dengan kode etik yang berlaku.\r\nd.    Membina mahasiswa dalam mengembangkan kepribadiannya sesuai dengan falsafah bangsa Indonesia (bermoral Pancasila). \r\ne.    Memberi rekomendasi tentang perkembangan dan tingkat keberhasilan mahasiswa bila diperlukan.\r\n4.  Peran dan Fungsi Dosen Pembimbing Akademik sebagai Motivator: \r\na.  Mendorong mahasiswa untuk belajar sesuai dengan kemampuan dan potensi yang dimilikinya.\r\nb.  Memberi saran dan anjuran kepada mahasiswa untuk memanfaatkan sarana dan prasarana belajar yang tersedia.\r\nc.  Menunjukkan jalan bagi upaya pengembangan minat dan potensi diri mahasiswa. \r\n5.  Peran dan Fungsi Dosen Pembimbing Akademik sebagai Model:\r\na.  Melaksanakan fungsi dan tugas kepenasehatan serta fungsi dan tugas dosen dengan sebaik-baiknya.\r\nb.  Mengutamakan kepentingan mahasiswa daripada kepentingan pribadinya.\r\nc.  Mematuhi norma dan kode etik pendidik dalam mengambil keputusan dan bertindak.\r\n \r\nSecara umum mekanisme dan prosedur dalam memberikan bimbingan, baik untuk  perencanaan studi maupun untuk pemecahan masalah, adalah seperti berikut ini:\r\n1. Menerima mahasiswa, secara fisik maupun psikis, dengan isyarat, perbuatan, maupun kata-kata yang dapat menciptakan suasana keakraban (rapport). Rasa percaya dan  hubungan pribadi yang erat ini dimaksudkan agar mahasiswa dapat terlepas dari perasaan takut dan hubungan dengan dosen pembimbing bersifat impersonal.\r\n2. Menciptakan hubungan baik (harmonis). Hubungan baik perlu diciptakan dosen  pembimbing dengan sikap ramah, penuh perhatian serta pembicaraan yang bersifat netral dan kekeluargaan agar mahasiswa tidak ragu untuk menyampaikan permasalahannya. Komunikasi antara pembimbing dan mahasiswa yang dilandasi perasaan saling menghargai, percaya dan terbuka akan menimbulkan suasana bebas dimana mahasiswa dapat menceritakan apa yang dialaminya. \r\n3. Menggali dan mengumpulkan informasi. Setelah terjalin hubungan baik, dosen pembinmbing menggali dan mengumpulkan informasi tentang diri mahasiswa beserta  permasalahannya.', 'documents/2026/02/PEMBIMBING_AKADEMIK.pdf', '', '', '2026-02-03 12:22:45.747472', 1, 1, 1, 8),
(4, 'Panduan Seminar Proposal Skripsi', 'Buku panduan seminar proposal skripsi berfungsi sebagai acuan resmi yang memuat tata cara, aturan, dan struktur penulisan ilmiah yang wajib diikuti mahasiswa. Panduan ini menjamin keseragaman format penulisan, mencegah kesalahan umum, dan mempercepat proses bimbingan serta kelayakan penelitian. \r\nFungsi utama buku panduan tersebut meliputi:\r\nPedoman Teknis Penulisan: Menjelaskan sistematika proposal, aturan sitasi, format margin, font, dan teknik penulisan.\r\nAcuan Prosedural: Menginformasikan alur pengajuan judul, syarat pendaftaran, dan kelengkapan dokumen seminar.\r\nStandar Kelayakan: Memastikan proposal disusun sesuai dengan kaidah etis dan standar akademik fakultas.\r\nAlat Bantu Penelitian: Memberikan arahan metodologi penelitian, teknik pengumpulan data, dan cara analisis.\r\nPenyamaan Persepsi: Menyeragamkan pemahaman antara mahasiswa dan dosen pembimbing untuk mempermudah proses bimbingan. \r\nDengan mematuhi buku panduan, mahasiswa dapat menyusun proposal secara sistematis dan memenuhi persyaratan akademik yang ditetapkan.', 'documents/2026/02/Panduan-Seminar-Skripsi-Update_2024.pdf', '', '', '2026-02-03 12:26:57.987168', 0, 1, 1, 8),
(5, 'Buku Panduan Skripsi Program Studi SI', 'Buku panduan skripsi berfungsi sebagai acuan baku dan rujukan utama bagi mahasiswa dalam menyusun skripsi agar sesuai standar akademik, sistematis, dan seragam. Panduan ini mencakup aturan teknis penulisan, struktur laporan, metode penelitian, serta prosedur administrasi, yang mempermudah proses bimbingan dan mempercepat penyelesaian skripsi. \r\nSecara rinci, berikut adalah fungsi utama buku panduan skripsi bagi mahasiswa:\r\nPedoman Teknis dan Format Penulisan: Menetapkan aturan format penulisan yang konsisten, seperti aturan font, margin, spasi, gaya sitasi, dan tata letak.\r\nAcuan Sistematika Struktur Skripsi: Memberikan kerangka kerja jelas mengenai bagian-bagian yang harus ada dalam proposal dan laporan skripsi (pendahuluan, tinjauan pustaka, metodologi, hasil, pembahasan).\r\nPanduan Metodologi dan Etika: Memberikan informasi teknik penelitian, pengumpulan data, analisis data, serta panduan etika penulisan (seperti menghindari plagiarisme).\r\nPanduan Prosedur Administrasi: Menjelaskan alur administratif, mulai dari pengajuan judul, seminar proposal, hingga ujian skripsi (munaqasyah).\r\nMeningkatkan Kualitas dan Efisiensi: Mengurangi kesalahan umum dalam penulisan, serta mempermudah mahasiswa dalam bimbingan karena adanya kesamaan persepsi dengan dosen pembimbing. \r\nDengan mematuhi buku panduan, mahasiswa diharapkan dapat menghasilkan skripsi yang ilmiah, valid, dan memenuhi standar institusi', 'documents/2026/02/Panduan_Skripsi_2023-2-Update2.pdf', '', '', '2026-02-03 12:30:00.800896', 0, 1, 1, 8),
(6, 'Pemrograman Berbasis Platform (P)', 'Mata kuliah Pemrograman Berbasis Platform (4 SKS) merupakan mata kuliah wajib program studi Sistem Informasi yang bertujuan membekali mahasiswa kemampuan merancang, mengembangkan, dan melakukan deployment aplikasi berbasis platform (khususnya web-based data application) menggunakan Python dan framework Streamlit. Mahasiswa akan mempelajari konsep dasar pemrograman Python, pengembangan antarmuka berbasis data (data-driven UI), pengelolaan state, integrasi sumber data eksternal (CSV, SQL, API), keamanan dasar aplikasi, serta deployment ke platform cloud. Mata kuliah ini menekankan pendekatan praktis berbasis proyek kecil dengan output aplikasi dashboard interaktif yang siap deploy, sekaligus menanamkan nilai integritas koding dan anti-plagiarisme.', 'documents/2026/02/RPS_Matakuliah__PBPF.pdf', '', '', '2026-02-07 12:53:30.146406', 0, 1, 1, 11),
(7, 'Pemrograman Berorientasi Objek', 'Mata kuliah Pemrograman Berorientasi Objek (4 SKS) Mata kuliah ini membekali mahasiswa kemampuan merancang dan mengembangkan perangkat lunak menggunakan paradigma Object Oriented Programming (OOP). Mahasiswa mempelajari konsep class, object, encapsulation, inheritance, polymorphism, abstraction, serta implementasi aplikasi berbasis objek menggunakan Python. Mata kuliah menekankan pendekatan project-based learning hingga menghasilkan Aplikasi berbasis OOP', 'documents/2026/02/RPS_Matakuliah__PBO.pdf', '', '', '2026-02-13 08:08:12.041895', 1, 1, 1, 11),
(8, 'Pemrograman Dasar', 'Mata kuliah Pemrograman Dasar merupakan fondasi utama bagi mahasiswa Program Studi Sistem Informasi untuk memahami logika komputasional dan teknik pemecahan masalah melalui pemrograman. Dengan menggunakan bahasaPython—yang dikenal karena sintaksisnya yang intuitif namun kuat—mahasiswa akan dipandu untuk bertransformasi dari seorang pengguna teknologi menjadi seorang pengembang solusi digital.', 'documents/2026/02/RPS_Matakuliah__Pemrograman_Dasar-1-4SKS_HeSgejP.pdf', '', '', '2026-02-18 06:21:15.096662', 6, 1, 1, 11);

-- --------------------------------------------------------

--
-- Table structure for table `core_documentcategory`
--

CREATE TABLE `core_documentcategory` (
  `id` bigint(20) NOT NULL,
  `name` varchar(200) NOT NULL,
  `slug` varchar(200) NOT NULL,
  `description` longtext NOT NULL,
  `icon` varchar(50) NOT NULL,
  `order` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `core_documentcategory`
--

INSERT INTO `core_documentcategory` (`id`, `name`, `slug`, `description`, `icon`, `order`) VALUES
(1, 'Pembimbing Akademik', 'pembimbing-akademik', 'Dokumen pembimbing akademik mahasiswa', 'fas fa-user-graduate', 1),
(2, 'Pembimbing Seminar', 'pembimbing-seminar', 'Dokumen pembimbing seminar proposal', 'fas fa-presentation', 2),
(3, 'Pembimbing Skripsi', 'pembimbing-skripsi', 'Dokumen pembimbing skripsi', 'fas fa-book', 3),
(4, 'Kurikulum Berbasis OBE – K22', 'kurikulum-berbasis-obe-k22', 'Kurikulum berbasis Outcome Based Education K22', 'fas fa-graduation-cap', 4),
(5, 'Kurikulum Berbasis KKNI – K17', 'kurikulum-berbasis-kkni-k17', 'Kurikulum berbasis KKNI K17', 'fas fa-certificate', 5),
(6, 'Laporan Evaluasi Diri', 'laporan-evaluasi-diri', 'LED Program Studi', 'fas fa-file-alt', 6),
(7, 'LKPS', 'lkps', 'Laporan Kinerja Program Studi', 'fas fa-chart-line', 7),
(8, 'Buku Panduan', 'buku-panduan', 'Buku panduan mahasiswa', 'fas fa-book-open', 8),
(9, 'Perkuliahan', 'perkuliahan', 'Dokumen perkuliahan gasal dan genap', 'fas fa-chalkboard-teacher', 9),
(10, 'Kegiatan Himasif', 'kegiatan-himasif', 'Dokumentasi kegiatan himpunan', 'fas fa-users', 10),
(11, 'Rencana Pembelajaran Semester (RPS)', 'rencana-pembelajaran-semester-rps', '', '', 11);

-- --------------------------------------------------------

--
-- Table structure for table `core_dosen`
--

CREATE TABLE `core_dosen` (
  `id` bigint(20) NOT NULL,
  `nidn` varchar(20) NOT NULL,
  `nama` varchar(100) NOT NULL,
  `kategori` varchar(20) NOT NULL,
  `photo` varchar(100) NOT NULL,
  `email` varchar(254) NOT NULL,
  `phone` varchar(20) NOT NULL,
  `pendidikan` varchar(200) NOT NULL,
  `bidang_keahlian` varchar(200) NOT NULL,
  `scholar_link` varchar(200) NOT NULL,
  `scopus_link` varchar(200) NOT NULL,
  `sinta_link` varchar(200) NOT NULL,
  `bio` longtext NOT NULL,
  `is_active` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `core_dosen`
--

INSERT INTO `core_dosen` (`id`, `nidn`, `nama`, `kategori`, `photo`, `email`, `phone`, `pendidikan`, `bidang_keahlian`, `scholar_link`, `scopus_link`, `sinta_link`, `bio`, `is_active`) VALUES
(1, '1010107601', 'Junaidi Surya,S.Kom.,M.Kom', 'tetap', 'dosen/dacae9d1d36d408d760702d066c5ec10.jpg', 'Junaidis10@gmail.com', '', 'S2- Ilmu Komputer', 'Information system,artificial inteligence (AL) Networking dan securi', 'https://scholar.google.co.id/citations?user=eivkj14AAAAJ&hl=id', '', 'https://sinta.kemdiktisaintek.go.id/authors/profile/6719438', '<p style=\"text-align:start\"><span style=\"font-size:medium\"><span style=\"font-family:&quot;Times New Roman&quot;,serif\"><span style=\"color:#000000\"><strong><span style=\"color:black\">Junaidi Surya, S.Kom., M.Kom.</span></strong></span></span></span></p>\r\n\r\n<p style=\"text-align:start\"><span style=\"font-size:medium\"><span style=\"font-family:&quot;Times New Roman&quot;,serif\"><span style=\"color:#000000\"><strong><span style=\"color:black\">Pendidikan Terakhir:</span></strong></span></span></span></p>\r\n\r\n<ul>\r\n	<li><span style=\"font-size:12pt\"><span style=\"font-family:&quot;Times New Roman&quot;,serif\"><span style=\"color:black\">S2-Magister Komputer (M.Kom) &ndash; Konsentrasi Sistem Informasi</span></span></span></li>\r\n	<li><span style=\"font-size:12pt\"><span style=\"font-family:&quot;Times New Roman&quot;,serif\"><span style=\"color:black\">Universitas Putra Indonesia &ldquo;YPTK&rdquo; Padang 2009</span></span></span></li>\r\n	<li><span style=\"font-size:12pt\"><span style=\"font-family:&quot;Times New Roman&quot;,serif\"><span style=\"color:black\">S1-Sistem Informatika (STMIK) Nurdin Hamzah 2002&shy;</span></span></span></li>\r\n</ul>\r\n\r\n<p style=\"text-align:start\"><span style=\"font-size:medium\"><span style=\"font-family:&quot;Times New Roman&quot;,serif\"><span style=\"color:#000000\"><strong><span style=\"color:black\">Profesi:</span></strong></span></span></span></p>\r\n\r\n<ul>\r\n	<li><span style=\"font-size:12pt\"><span style=\"font-family:&quot;Times New Roman&quot;,serif\"><span style=\"color:black\">Dosen Tetap di Fakultas Ilmu Komputer</span></span></span></li>\r\n	<li><span style=\"font-size:12pt\"><span style=\"font-family:&quot;Times New Roman&quot;,serif\"><span style=\"color:black\">Universitas Nurdin Hamzah &ndash; Jambi</span></span></span></li>\r\n	<li><span style=\"font-size:12pt\"><span style=\"font-family:&quot;Times New Roman&quot;,serif\"><span style=\"color:black\">Bidang Keahlian: Pemrograman Python, Sistem Informasi, OOP (Object-Oriented Programming), dan Software Engineering</span></span></span></li>\r\n</ul>\r\n\r\n<p><strong><span dir=\"ltr\" lang=\"EN-US\" style=\"font-size:11pt\"><span style=\"font-family:Calibri,sans-serif\"><span style=\"color:black\">Kontak:</span></span></span></strong><br />\r\n<span dir=\"ltr\" lang=\"EN-US\" style=\"font-size:11pt\"><span style=\"font-family:Calibri,sans-serif\"><span style=\"color:black\">&nbsp;&nbsp; Email:&nbsp;junaidis10@gmail.com</span></span></span></p>', 1),
(2, '1002057601', 'Sri Mulyati,S.Kom.,M.Kom', 'tetap', 'dosen/1dd9c9419bd74b58a4c87ce7a4918cf1.jpg', 'mulyatisri52@gmail.com', '', '', 'Data mining', '', '', 'https://sinta.kemdiktisaintek.go.id/authors/profile/6705174', '', 1),
(3, '1012066402', 'Ir.Mulyadi,M.Si', 'tetap', 'dosen/cd37f97b7d2642c2d8c57d9ad537b2da.png', 'mulyadiroesly@gmail.com', '', '', '', '', '', 'https://sinta.kemdiktisaintek.go.id/authors/profile/6066513', '', 1),
(4, '1022096701', 'DR. Ir.H Riswan,MMSI', 'tetap', 'dosen/9ded410ff06ee97dd91867a77ccafec5.jpg', '', '', '', 'sistem informasi', '', '', 'https://sinta.kemdiktisaintek.go.id/departments/profile/2941/101036/57201', '', 1),
(5, '1013047702', 'Ahmad Louis,S.Kom.,M.Kom', 'tetap', 'dosen/00e3eeeb469a4e39e2c45eab77f64200.jpeg', 'louis124fi@gmail.com', '', 'S2- Ilmu Komputer', 'Ilmu komputer ,Jaringan komputer', '', '', 'https://sinta.kemdiktisaintek.go.id/authors/profile/6719447', '', 1),
(6, '1004107801', 'Elzas,S.Kom,.M.Kom', 'tetap', 'dosen/9d23839360ee80cb227e44283b5766a0.png', '', '', '', 'ilmu komputer', '', '', 'https://sinta.kemdiktisaintek.go.id/authors/profile/6132071#!', '', 1),
(7, '1013058201', 'Irma Suana,S.Kom,.M.Kom', 'tetap', 'dosen/767bc572e7850e624660ecc4196284d7.jpg', '', '', '', 'sains', '', '', 'https://sinta.kemdiktisaintek.go.id/authors/profile/6705150', '', 1),
(8, '1016116802', 'Hj.Nilawati,M.Si', 'tetap', 'dosen/b759c627adeab8f6b7402c08f5b6fd19.jpg', '', '', '', 'sistem informasi', '', '', 'https://sinta.kemdiktisaintek.go.id/authors/profile/6138956', '', 1),
(9, '1005047201', 'Ir.Afrizal,ME', 'tetap', 'dosen/7953b752985d6e6cb0eba47998e1d4da.png', '', '', '', 'Manajemen', '', '', 'https://sinta.kemdiktisaintek.go.id/authors/profile/6719466#!', '', 1),
(10, '1008027601', 'Merti Megawaty,M.Pd', 'tetap', 'dosen/6904a855cc689156c9b409255f3ffffb.jpg', '', '', '', 'Bahasa Inggris,Pariwisata,sejarah,teknologi', '', '', 'https://sinta.kemdiktisaintek.go.id/authors/profile/6649593#!', '', 1),
(11, '1022088302', 'Windy Adriana,M.Ak', 'tetap', 'dosen/6a1794382119e3ccf1384f321b1f7685.png', '', '', '', 'Keuangan', '', '', 'https://sinta.kemdiktisaintek.go.id/authors/profile/6647695#!', '', 1),
(12, '1022108201', 'Dr. Darex Susanto, S.Kom., M.Kom', 'tetap', 'dosen/4b22db8731dc76bdec80fa8e669f8477.jpg', 'rexsamoy@gmail.com', '', 'S3 - Manajemen Kependidikan', 'Sistem Informasi', '', '', 'https://sinta.kemdiktisaintek.go.id/authors/profile/6719388', '', 1),
(13, '1017129001', 'Lailyn Puad, S.Kom., M.Kom', 'tetap', 'dosen/47879bae7dfde2af9ef162fa8a6e0358.jpg', 'lailynfuad@gmail.com', '', '', 'Informatika Medis, Cloud Computing', '', '', 'https://sinta.kemdiktisaintek.go.id/authors/profile/206356', '', 1);

-- --------------------------------------------------------

--
-- Table structure for table `core_gallery`
--

CREATE TABLE `core_gallery` (
  `id` bigint(20) NOT NULL,
  `title` varchar(200) NOT NULL,
  `description` longtext NOT NULL,
  `media_type` varchar(10) NOT NULL,
  `image` varchar(100) NOT NULL,
  `video_url` varchar(200) NOT NULL,
  `uploaded_at` datetime(6) NOT NULL,
  `is_active` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `core_gallery`
--

INSERT INTO `core_gallery` (`id`, `title`, `description`, `media_type`, `image`, `video_url`, `uploaded_at`, `is_active`) VALUES
(1, 'Smbutan Warek III', 'Pembekalan Peserta PHP', 'image', 'gallery/WhatsApp_Image_2026-01-31_at_10.20.54_2.jpeg', '', '2026-02-01 13:56:49.835446', 1),
(2, 'Membuat Jaringan Syaraf Tiruan mengenal  Tulisan dengan AI', 'Belajar membuat Membuat Jaringan Syaraf Tiruan, untuk mengenali angka dari inputan', 'video', 'gallery/Screen_Shot_2026-02-03_at_21.42.19.png', 'https://www.youtube.com/watch?v=WLmY9icEOQk', '2026-02-03 14:42:39.485185', 1);

-- --------------------------------------------------------

--
-- Table structure for table `core_jobcareer`
--

CREATE TABLE `core_jobcareer` (
  `id` bigint(20) NOT NULL,
  `company` varchar(200) NOT NULL,
  `position` varchar(200) NOT NULL,
  `location` varchar(200) NOT NULL,
  `job_type` varchar(50) NOT NULL,
  `description` longtext NOT NULL,
  `requirements` longtext NOT NULL,
  `salary_range` varchar(100) NOT NULL,
  `application_deadline` date NOT NULL,
  `contact_email` varchar(254) NOT NULL,
  `link` varchar(200) NOT NULL,
  `posted_date` datetime(6) NOT NULL,
  `is_active` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `core_link`
--

CREATE TABLE `core_link` (
  `id` bigint(20) NOT NULL,
  `name` varchar(100) NOT NULL,
  `url` varchar(200) NOT NULL,
  `kategori` varchar(20) NOT NULL,
  `icon` varchar(50) NOT NULL,
  `description` longtext NOT NULL,
  `order` int(11) NOT NULL,
  `is_active` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `core_link`
--

INSERT INTO `core_link` (`id`, `name`, `url`, `kategori`, `icon`, `description`, `order`, `is_active`) VALUES
(2, 'V-Class UNH', 'https://vclass.unh.ac.id', 'vclass', 'fas fa-chalkboard-teacher', 'Virtual Classroom', 2, 1),
(3, 'Open Journal System', 'https://ojs.unh.ac.id/', 'ojs', 'fas fa-book', 'Jurnal Ilmiah Online', 3, 1),
(7, 'SIAKAD', 'https://mhs.unh.ac.id', 'siakad', 'fas fa-graduation-cap', '', 0, 1),
(9, 'Laboratorium', 'https://unh.ac.id/id/fasilitas/sarana-prasarana/laboratorium-komputer/laboratorium-komputer.html', 'laboratorium', 'fas fa-flask', 'Laboratorium Komputer', 4, 1);

-- --------------------------------------------------------

--
-- Table structure for table `core_matakuliah`
--

CREATE TABLE `core_matakuliah` (
  `id` bigint(20) NOT NULL,
  `kode` varchar(20) NOT NULL,
  `nama` varchar(200) NOT NULL,
  `sks` int(11) NOT NULL,
  `semester` int(11) NOT NULL,
  `kategori` varchar(50) NOT NULL,
  `deskripsi` longtext NOT NULL,
  `order` int(11) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `materi_perkuliahan` longtext NOT NULL,
  `rps_document_id` bigint(20) DEFAULT NULL,
  `dosen_pengampu_legacy` longtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `core_matakuliah`
--

INSERT INTO `core_matakuliah` (`id`, `kode`, `nama`, `sks`, `semester`, `kategori`, `deskripsi`, `order`, `is_active`, `materi_perkuliahan`, `rps_document_id`, `dosen_pengampu_legacy`) VALUES
(145, 'SIKK1201', 'Pengantar Manajemen', 2, 1, 'Wajib', '', 0, 1, '', NULL, ''),
(146, 'FKPN1201', 'Aljabar Vektor dan Matriks', 2, 1, 'Wajib', '', 1, 1, '', NULL, ''),
(147, 'SIKK1302', 'Sistem Dan Teknologi Informasi', 3, 1, 'Wajib', '', 2, 1, '', NULL, ''),
(149, 'FKKK1402', 'Algorithma dan Pemrograman (P)', 4, 1, 'Wajib', '', 4, 1, '', NULL, ''),
(150, 'FKKK1403', 'Sistem Operasi dan Arsitektur Komputer (P)', 3, 1, 'Wajib', '', 5, 1, '', NULL, ''),
(151, 'SIPN2202', 'Pengantar Akuntansi', 2, 2, 'Wajib', '', 6, 1, '', NULL, ''),
(152, 'PK2201', 'Pendidikan Agama', 2, 2, 'Wajib', '', 7, 1, '', NULL, ''),
(153, 'NHPN2303', 'Statistika dan Penerapan', 3, 2, 'Wajib', '', 8, 1, '', NULL, ''),
(154, 'SIPN2204', 'Bahasa Inggris I', 3, 2, 'Wajib', '', 9, 1, '', NULL, ''),
(155, 'PK2204', 'Bahasa Indonesia', 2, 2, 'Wajib', '', 10, 1, '', NULL, ''),
(156, 'SIPN2205', 'Matematika Komputasi', 2, 2, 'Wajib', '', 11, 1, '', NULL, ''),
(157, 'SIKK2304', 'Algoritma dan Pemrograman (P II)', 3, 2, 'Wajib', '', 12, 1, '', NULL, ''),
(158, 'NHKK2302', 'Aplikasi Perkantoran (P)', 3, 2, 'Wajib', '', 13, 1, '', NULL, ''),
(159, 'SIKK3305', 'Sistem Informasi Manajemen', 3, 3, 'Wajib', '', 14, 1, '', NULL, ''),
(160, 'SIKK3306', 'Manajemen Investasi Teknologi Informasi', 3, 3, 'Wajib', '', 15, 1, '', NULL, ''),
(161, 'SIKK3207', 'Manajemen Proses Bisnis', 2, 3, 'Wajib', '', 16, 1, '', NULL, ''),
(162, 'SIKK3308', 'Konsep Sistem Informasi', 3, 3, 'Wajib', '', 17, 1, '', NULL, ''),
(163, 'PK3202', 'Pendidikan Pancasila', 2, 3, 'Wajib', '', 18, 1, '', NULL, ''),
(164, 'FKKB3304', 'Manajemen & Sistem Basis Data', 3, 3, 'Wajib', '', 19, 1, '', NULL, ''),
(165, 'SIKB3301', 'Pemrograman Berbasis Platform (P)', 4, 3, 'Wajib', '', 20, 1, '1. Kontrak Kuliah & Setup Tools\r\n2. Dasar Python dan Logika & Percabangan 3. Struktur Data & Fungsi File\r\n4. Streamlit Fundamental\r\n5. Widget Streamlit dan layout lanjutan\r\n6. State Management dan Data Processing 7. Database IntegraQon dan API\r\n8. Proyek Development and Presentasi Final', 6, ''),
(166, 'SIPN3306', 'Bahasa Inggris II', 2, 3, 'Wajib', '', 21, 1, '', NULL, ''),
(167, 'SIKB3302', 'Teknologi Basis Data', 3, 4, 'Wajib', '', 22, 1, '', NULL, ''),
(168, 'SIKK4309', 'Analisis dan Perancangan Sistem Informasi', 3, 4, 'Wajib', '', 23, 1, '', NULL, ''),
(169, 'FKKK4305', 'Komunikasi Data dan Jaringan Komputer (P)', 3, 4, 'Wajib', '', 24, 1, '', NULL, ''),
(170, 'SIKK4311', 'Tata Kelola Teknologi Informasi', 3, 4, 'Wajib', '', 25, 1, '', NULL, ''),
(171, 'SIKK4312', 'Manajemen Sains', 3, 4, 'Wajib', '', 26, 1, '', NULL, ''),
(172, 'PK4203', 'Pendidikan Kewarganegaraan', 2, 4, 'Wajib', '', 27, 1, '', NULL, ''),
(173, 'SIKK4213', 'Arsitektur SI/IT Perusahaan', 2, 4, 'Wajib', '', 28, 1, '', NULL, ''),
(174, 'SIKB4303', 'Matakuliah Pilihan 1', 3, 4, 'Wajib', '', 29, 1, '', NULL, ''),
(175, 'SIKM401', 'Lintas Prodi / MBKM', 0, 4, 'Wajib', '', 30, 1, '', NULL, ''),
(176, 'SIKK5314', 'Analisis dan Manajemen Jaringan (P)', 3, 5, 'Wajib', '', 31, 1, '', NULL, ''),
(177, 'SIKB5304', 'Audit Sistem informasi', 3, 5, 'Wajib', '', 32, 1, '', NULL, ''),
(178, 'SIKK5315', 'Manajemen Proyek SI', 3, 5, 'Wajib', '', 33, 1, '', NULL, ''),
(179, 'SIPN5307', 'Testing dan Implementasi Sistem Informasi', 3, 5, 'Wajib', '', 34, 1, '', NULL, ''),
(180, 'NHKK5203', 'Technopreneur', 2, 5, 'Wajib', '', 35, 1, '', NULL, ''),
(181, 'FKKK5406', 'Pemrograman berbasis Web (P)', 4, 5, 'Wajib', '', 36, 1, '', NULL, ''),
(182, 'SIKB5304', 'Matakuliah Pilihan 2', 3, 5, 'Wajib', '', 37, 1, '', NULL, ''),
(183, 'SIKM502', 'Lintas Prodi / MBKM', 0, 5, 'Wajib', '', 38, 1, '', NULL, ''),
(184, 'FKKK6307', 'Metode Penelitian', 3, 6, 'Wajib', '', 39, 1, '', NULL, ''),
(185, 'SIKK6316', 'Sistem Multimedia', 3, 6, 'Wajib', '', 40, 1, '', NULL, ''),
(186, 'FKKK6208', 'Komputer dan Masyarakat', 2, 6, 'Wajib', '', 41, 1, '', NULL, ''),
(187, 'SIKB6306', 'Sistem Pendukung Keputusan Berbasis Model', 3, 6, 'Wajib', '', 42, 1, '', NULL, ''),
(188, 'SIKB6407', 'Rekayasa Web', 4, 6, 'Wajib', '', 43, 1, '', NULL, ''),
(189, 'SIKB6307', 'Matakuliah Pilihan 3', 3, 6, 'Wajib', '', 44, 1, '', NULL, ''),
(190, 'SIKB6409', 'Matakuliah Pilihan 4', 4, 6, 'Wajib', '', 45, 1, '', NULL, ''),
(191, 'SIKM603', 'MBKM / Magang Industri Dll', 0, 6, 'Wajib', '', 46, 1, '', NULL, ''),
(192, 'FKPB7209', 'Etika Profesi', 2, 7, 'Wajib', '', 47, 1, '', NULL, ''),
(193, 'NHPB7404', 'Kerja Praktek', 4, 7, 'Wajib', '', 48, 1, '', NULL, ''),
(194, 'SIKK7217', 'Interpersonal Skill', 2, 7, 'Wajib', '', 49, 1, '', NULL, ''),
(195, 'SIKB7210', 'Interaksi Manusia dan Komputer', 2, 7, 'Wajib', '', 50, 1, '', NULL, ''),
(196, 'SIKB7311', 'Matakuliah Pilihan 5', 3, 7, 'Wajib', '', 51, 1, '', NULL, ''),
(197, 'SIKB7314', 'Matakuliah Pilihan 6', 3, 7, 'Wajib', '', 52, 1, '', NULL, ''),
(198, 'SIKM704', 'MBKM / Magang Industri Dll', 0, 7, 'Wajib', '', 53, 1, '', NULL, ''),
(199, 'SIKB8613', 'Skripsi', 6, 8, 'Wajib', '', 54, 1, '', NULL, ''),
(200, 'SIKB4301', 'Sistem Informasi Akuntansi', 3, 0, 'Pilihan (MP1)', '', 55, 1, '', NULL, ''),
(201, 'SIKB4302', 'Sistem Informasi Perbankan', 3, 0, 'Pilihan (MP1)', '', 56, 1, '', NULL, ''),
(202, 'SIKB4303', 'Konsep Data Mining', 3, 0, 'Pilihan (MP1)', '', 57, 1, '', NULL, ''),
(203, 'SIKB5304', 'Grafika Komputer & Pengolahan Citra', 3, 0, 'Pilihan (MP2)', '', 58, 1, '', NULL, ''),
(204, 'SIKB5305', 'Bisnis Digital', 3, 0, 'Pilihan (MP2)', '', 59, 1, '', NULL, ''),
(205, 'SIKB5306', 'Pengantar Model & Simulasi', 3, 0, 'Pilihan (MP2)', '', 60, 1, '', NULL, ''),
(206, 'SIKB6307', 'Rekayasa Perangkat Lunak', 3, 0, 'Pilihan (MP3)', '', 61, 1, '', NULL, ''),
(207, 'SIKB6308', 'Sistem Terdistribusi', 3, 0, 'Pilihan (MP3)', '', 62, 1, '', NULL, ''),
(208, 'SIKB6409', 'Pemrograman Berorientasi Objek', 4, 0, 'Pilihan (MP4)', '', 63, 1, '', NULL, ''),
(209, 'SIKB6410', 'Pemrograman Mobile', 4, 0, 'Pilihan (MP4)', '', 64, 1, '', NULL, ''),
(210, 'SIKB7311', 'Keamanan Sistem Informasi (P)', 3, 0, 'Pilihan (MP5)', '', 65, 1, '', NULL, ''),
(211, 'SIKB7312', 'Pemasaran Digital', 3, 0, 'Pilihan (MP5)', '', 66, 1, '', NULL, ''),
(212, 'SIKB7313', 'Pengantar Digital Forensic IT', 3, 0, 'Pilihan (MP6)', '', 67, 1, '', NULL, ''),
(213, 'SIKB7314', 'Sistem Cerdas', 3, 0, 'Pilihan (MP6)', '', 68, 1, '', NULL, ''),
(214, 'SIKB6409', 'Pemrograman Berorientasi Objek', 4, 6, '', 'Mata kuliah Pemrograman Berorientasi Objek (4 SKS) Mata kuliah ini membekali mahasiswa kemampuan merancang dan mengembangkan perangkat lunak menggunakan paradigma Object Oriented Programming (OOP). Mahasiswa mempelajari konsep class, object, encapsulation, inheritance, polymorphism, abstraction, serta implementasi aplikasi berbasis objek menggunakan Python. Mata kuliah menekankan pendekatan project-based learning hingga menghasilkan Aplikasi berbasis OOP', 0, 1, '1.	Kontrak Kuliah & Konsep Dasar OOP\r\n2.	Class & Object dalam pemrogrman OOP\r\n3.	Encapsulation & Access Modifier\r\n4.	Inheritance, Class Object dan Superclass\r\n5.	Polymorphism & Method Overriding dan Abstract Class & Method\r\n6.	Aplikasi OOP Sederhana\r\n7.	State Management dalam OOP\r\n8.	Integrasi dengan Modularitas', 7, ''),
(215, 'SIKK1403', 'Pemrograman Dasar (P)', 4, 1, 'Rencana Pembelajaran Semester', '', 3, 1, '1. Memahami kontrak perkuliahan dan pengenal tools aplikasi (Python,Jupyter dan Streamlit) 2. Menguasai konsep dasar penggunaan string variabel dan tipe data dasar.\r\n3. Mampu menggunakan operator aritmatika dalam proses matematika dan logika\r\n4. Mampu mengimplementasikan struktur percabangan, perulangan dan array\r\n5 Mampu mengelola data menggunakan paket, module dan fungsi\r\n6. Mampu merancang program sederhana , yang dapat terintegrasi dengan aplikasi dunia kerja dan industri', 8, '');

-- --------------------------------------------------------

--
-- Table structure for table `core_matakuliah_dosen_pengampu`
--

CREATE TABLE `core_matakuliah_dosen_pengampu` (
  `id` bigint(20) NOT NULL,
  `matakuliah_id` bigint(20) NOT NULL,
  `dosen_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `core_matakuliah_dosen_pengampu`
--

INSERT INTO `core_matakuliah_dosen_pengampu` (`id`, `matakuliah_id`, `dosen_id`) VALUES
(1, 215, 1),
(2, 215, 13);

-- --------------------------------------------------------

--
-- Table structure for table `core_news`
--

CREATE TABLE `core_news` (
  `id` bigint(20) NOT NULL,
  `title` varchar(200) NOT NULL,
  `slug` varchar(200) NOT NULL,
  `thumbnail` varchar(100) NOT NULL,
  `content` longtext NOT NULL,
  `published_date` datetime(6) NOT NULL,
  `updated_date` datetime(6) NOT NULL,
  `views` int(11) NOT NULL,
  `is_featured` tinyint(1) NOT NULL,
  `is_published` tinyint(1) NOT NULL,
  `author_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `core_news`
--

INSERT INTO `core_news` (`id`, `title`, `slug`, `thumbnail`, `content`, `published_date`, `updated_date`, `views`, `is_featured`, `is_published`, `author_id`) VALUES
(1, 'Ujian Semester Gasal 2025', 'ujian-semester-gasal-2025', 'news/3x4.jpeg', '<p>Ujian bagi mahasiswa sangat penting sebagai alat evaluasi pemahaman materi kuliah, penentu nilai akademik (IPK), dan tolok ukur kompetensi</p>\r\n\r\n<p>. Ujian juga melatih disiplin, manajemen waktu, serta kejujuran akademik. Selain itu, ujian merupakan persiapan mental menuju dunia kerja dan sarana memetakan kualitas pembelajaran.&nbsp;</p>', '2026-02-03 14:47:14.334728', '2026-02-13 08:22:59.749677', 8, 0, 1, 1);

-- --------------------------------------------------------

--
-- Table structure for table `core_pagecontent`
--

CREATE TABLE `core_pagecontent` (
  `id` bigint(20) NOT NULL,
  `page_name` varchar(100) NOT NULL,
  `title` varchar(200) NOT NULL,
  `content` longtext NOT NULL,
  `updated_at` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `core_penelitian`
--

CREATE TABLE `core_penelitian` (
  `id` bigint(20) NOT NULL,
  `title` varchar(300) NOT NULL,
  `jenis` varchar(20) NOT NULL,
  `peneliti` varchar(200) NOT NULL,
  `year` int(11) NOT NULL,
  `abstrak` longtext NOT NULL,
  `file` varchar(100) NOT NULL,
  `link` varchar(200) NOT NULL,
  `created_at` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `core_prestasi`
--

CREATE TABLE `core_prestasi` (
  `id` bigint(20) NOT NULL,
  `student_name` varchar(100) NOT NULL,
  `achievement` varchar(200) NOT NULL,
  `tingkat` varchar(20) NOT NULL,
  `year` int(11) NOT NULL,
  `description` longtext NOT NULL,
  `certificate` varchar(100) NOT NULL,
  `photo` varchar(100) NOT NULL,
  `date_achieved` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `core_prospekkeunggulan`
--

CREATE TABLE `core_prospekkeunggulan` (
  `id` bigint(20) NOT NULL,
  `title` varchar(200) NOT NULL,
  `description` longtext NOT NULL,
  `icon` varchar(50) NOT NULL,
  `order` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `core_prospekkeunggulan`
--

INSERT INTO `core_prospekkeunggulan` (`id`, `title`, `description`, `icon`, `order`) VALUES
(1, 'System Analyst', '<p>Menganalisis dan merancang sistem informasi untuk kebutuhan organisasi</p>', 'fas fa-project-diagram', 1),
(2, 'Database Administrator', '<p>Mengelola dan mengoptimalkan database perusahaan</p>', 'fas fa-database', 2),
(3, 'Business Intelligence Analyst', '<p>Menganalisis data untuk mendukung keputusan bisnis strategis</p>', 'fas fa-chart-bar', 3),
(4, 'IT Consultant', '<p>Memberikan konsultasi teknologi informasi untuk organisasi</p>', 'fas fa-laptop-code', 4),
(5, 'Project Manager', '<p>Mengelola proyek teknologi informasi dari perencanaan hingga implementasi</p>', 'fas fa-tasks', 5),
(6, 'Web Developer', '<p>Mengembangkan aplikasi web dan sistem informasi berbasis web</p>', 'fas fa-globe', 6);

-- --------------------------------------------------------

--
-- Table structure for table `core_sambutan`
--

CREATE TABLE `core_sambutan` (
  `id` bigint(20) NOT NULL,
  `title` varchar(200) NOT NULL,
  `ketua_name` varchar(100) NOT NULL,
  `ketua_photo` varchar(100) NOT NULL,
  `jabatan` varchar(100) NOT NULL,
  `content` longtext NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `updated_at` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `core_sambutan`
--

INSERT INTO `core_sambutan` (`id`, `title`, `ketua_name`, `ketua_photo`, `jabatan`, `content`, `is_active`, `updated_at`) VALUES
(1, 'Sambutan Ketua Program Studi', 'Junaidi Surya,S.Kom,M.Kom', 'sambutan/Junaidi_Surya2x3_.png', 'Ketua Program Studi Sistem Informasi', '<p>Kami dengan senang hati menyambut Anda di website Program Studi Sistem Informasi. Kami berharap fortal ini berfungsi sebagai jendela informatif bagi Mahasiswa, Dosen dan Masyarakat untuk&nbsp;&nbsp;memahami dan mempelajari lebih lanjut tentang kegiatan akademik, kegiatan kemahasiswaan, dan informasi seputar prestasi dan profile program studi. &nbsp;Program Studi Sistem Informasi berkomitmen untuk&nbsp;Menjadi program studi&nbsp; unggulan dan&nbsp;&nbsp;berdaya saing tinggi dalam bidang Technopreneurship, Manajemen&nbsp;&nbsp;&nbsp;Sistem Informasi dan Bisnis&nbsp;&nbsp;Digital&nbsp;&nbsp;Enterprise. Program Studi dalam proses belajar mengajar memadukan teori dan praktik untuk membekali mahasiswa dengan keterampilan yang dibutuhkan untuk menghadapi tantangan Industri 4.0.&nbsp;&nbsp;Kurikulum&nbsp;Program Studi Sistem Informasi mengajarkan landasan ilmu pengetahuan dan penerapan Teknologi Informasi dalam suatu organisasi,&nbsp;&nbsp;dengan kurikulum yang bersifat khas karena dibangun di atas 3 (tiga) pilar utama yaitu&nbsp;<strong>Komputer</strong>,&nbsp;<strong>Manajemen&nbsp;</strong>dan&nbsp;<strong>Bisnis</strong>.&nbsp;&nbsp;Sehingga profil lulusan Program Studi Sistem Informasi memenuhi aspek sikap dan tata nilai, dengan kompetensi umum dan kompetensi khusus sesuai Standar Kerangka Kualifikasi Nasional Indonesia (SKKNI), dan Kampus Merdeka. &nbsp;Program Studi percaya bahwa sistem informasi yang di hybridkan teknologi informasi adalah salah satu kunci untuk menyelesaikan berbagai tantangan global dan membangun masa depan yang lebih baik. Oleh karena itu, kami berkomitmen untuk mendidik dan membina mahasiswa agar menjadi tenaga profesional yang kompeten dan beretika serta mampu memberikan kontribusi positif bagi masyarakat, bangsa dan negara.&nbsp;Kami mengundang Anda untuk bergabung menjadi keluarga dan bagian dari Program Studi Sistem Informasi Universitas Nurdin Hamzah. Kami nyakin dengan bersama-sama, mari kita membangun masa depan cerah seperti yang kita mimpikan.</p>\r\n\r\n<p>Terima kasih telah mengunjungi website kami si.unh.ac.id. Kami berharap informasi yang tersedia dapat membantu Anda mendalami Program Studi Sistem Informasi lebih lanjut. Jangan ragu untuk menghubungi kami jika Anda memerlukan informasi lebih lanjut.</p>\r\n\r\n<p>Ketua Program Studi S1-Sistem Informasi</p>\r\n\r\n<p>Fakultas Ilmu Komputer - Universitas Nurdin Hamzah</p>\r\n\r\n<p>&nbsp;</p>\r\n\r\n<p>&nbsp;</p>\r\n\r\n<p>Junaidi Surya, M.Kom.<br />\r\nNUPTK : 2342754655131133</p>', 1, '2026-02-01 15:27:26.250066');

-- --------------------------------------------------------

--
-- Table structure for table `core_slide`
--

CREATE TABLE `core_slide` (
  `id` bigint(20) NOT NULL,
  `title` varchar(200) NOT NULL,
  `description` longtext NOT NULL,
  `image` varchar(100) NOT NULL,
  `link` varchar(200) NOT NULL,
  `order` int(11) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `created_at` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `core_slide`
--

INSERT INTO `core_slide` (`id`, `title`, `description`, `image`, `link`, `order`, `is_active`, `created_at`) VALUES
(2, 'Akreditasi', 'Status Peringkat Akreditasi', 'slides/2.jpg', '', 0, 1, '2026-02-01 13:34:47.786762'),
(3, '3', 'Program Studi Bersih Narkoba (Bersinar)', 'slides/gambar3.png', '', 0, 1, '2026-02-01 13:43:14.880913'),
(4, '11', 'Pendaftaran dan Jadwal', 'slides/Gambar1.png', '', 0, 1, '2026-02-09 07:22:26.948000');

-- --------------------------------------------------------

--
-- Table structure for table `core_surveykepuasanlulusan`
--

CREATE TABLE `core_surveykepuasanlulusan` (
  `id` bigint(20) NOT NULL,
  `email` varchar(254) NOT NULL,
  `nama_responden` varchar(255) NOT NULL,
  `nama_instansi` varchar(255) NOT NULL,
  `jabatan` varchar(100) NOT NULL,
  `integritas` varchar(20) NOT NULL,
  `keahlian_bidang` varchar(20) NOT NULL,
  `bahasa_inggris` varchar(20) NOT NULL,
  `penggunaan_it` varchar(20) NOT NULL,
  `komunikasi` varchar(20) NOT NULL,
  `kerjasama_tim` varchar(20) NOT NULL,
  `pengembangan_diri` varchar(20) NOT NULL,
  `waktu_tunggu` varchar(50) NOT NULL,
  `created_at` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `core_surveykepuasanlulusan`
--

INSERT INTO `core_surveykepuasanlulusan` (`id`, `email`, `nama_responden`, `nama_instansi`, `jabatan`, `integritas`, `keahlian_bidang`, `bahasa_inggris`, `penggunaan_it`, `komunikasi`, `kerjasama_tim`, `pengembangan_diri`, `waktu_tunggu`, `created_at`) VALUES
(1, 'yulicyani77@gmail.com', 'Yuli Chandra Yani', 'Pendidikan', 'Kepala Perpustaka SMAN5 Kota Jambi', 'Sangat Baik', 'Baik', 'Baik', 'Baik', 'Sangat Baik', 'Sangat Baik', 'Baik', 'WT < 3', '2026-02-13 07:30:44.076823');

-- --------------------------------------------------------

--
-- Table structure for table `core_surveykurikulum`
--

CREATE TABLE `core_surveykurikulum` (
  `id` bigint(20) NOT NULL,
  `nama_responden` varchar(255) NOT NULL,
  `kategori_responden` varchar(20) NOT NULL,
  `instansi` varchar(255) NOT NULL,
  `jabatan` varchar(100) NOT NULL,
  `email` varchar(254) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `responses_data` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL CHECK (json_valid(`responses_data`))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `core_surveykurikulum`
--

INSERT INTO `core_surveykurikulum` (`id`, `nama_responden`, `kategori_responden`, `instansi`, `jabatan`, `email`, `created_at`, `responses_data`) VALUES
(2, 'Drs. Ahmad Zulpa', 'pengguna', 'BTN', 'HDR', 'ahmadzulfa@gmail.com', '2026-02-21 15:47:17.225491', '{\"user_eval_integritas\": \"4\", \"user_eval_keahlian_si\": \"4\", \"user_eval_keahlian_teknis\": \"3\", \"user_eval_soft_skill\": \"3\", \"user_eval_adaptasi\": \"4\", \"user_skkni\": \"Sebagian Besar\", \"user_tech_gap\": \"Framework pemrograman (JavaScript, Python dan Jaraingan)\", \"user_techno_saran\": \"Perlu di buatkan wadah untuk mahasiswa untuk berkreasi\"}'),
(3, 'Reza Fahlevi,S.Kom', 'alumni', 'Samsung', 'Pengembang Model ', 'reza.fahlevi@gmail.com', '2026-02-21 16:15:23.804618', '{\"alumni_profil_kesesuaian\": \"Pengembang Sistem Informasi (System Analyst/Developer)\", \"alumni_cpl_sikap\": \"4\", \"alumni_cpl_konsep\": \"4\", \"alumni_cpl_teknis\": \"4\", \"alumni_cpl_data\": \"3\", \"alumni_cpl_tata_kelola\": \"4\", \"alumni_cpl_techno\": \"4\", \"alumni_mk_bermanfaat\": \"Pemrograman\\r\\nAlgoritma\\r\\nManajemen Proyek SI\", \"alumni_gap_analysis\": \"Analisis dampak teknologi dan pengaruhi kecerdasan buatan (AI)\", \"alumni_mbkm_eval\": \"Tidak Konsisten \"}');

-- --------------------------------------------------------

--
-- Table structure for table `core_surveyresponse`
--

CREATE TABLE `core_surveyresponse` (
  `id` bigint(20) NOT NULL,
  `status` varchar(50) NOT NULL,
  `lama_bergabung` varchar(50) NOT NULL,
  `pengetahuan_visi` varchar(50) NOT NULL,
  `sumber_informasi` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL CHECK (json_valid(`sumber_informasi`)),
  `frekuensi_sosialisasi` varchar(50) NOT NULL,
  `tingkat_paham` varchar(50) NOT NULL,
  `aspek_tercermin` varchar(50) NOT NULL,
  `bidang_tercermin` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL CHECK (json_valid(`bidang_tercermin`)),
  `dukungan_atmosfer` varchar(50) NOT NULL,
  `perlu_perbaikan` varchar(50) NOT NULL,
  `saran_kritik` longtext NOT NULL,
  `created_at` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `core_surveyresponse`
--

INSERT INTO `core_surveyresponse` (`id`, `status`, `lama_bergabung`, `pengetahuan_visi`, `sumber_informasi`, `frekuensi_sosialisasi`, `tingkat_paham`, `aspek_tercermin`, `bidang_tercermin`, `dukungan_atmosfer`, `perlu_perbaikan`, `saran_kritik`, `created_at`) VALUES
(1, 'dosen', '1-5 Tahun', 'Tahu', '[\"Situs Web\", \"Sosialisasi Pimpinan\", \"Buku Panduan\", \"Media Sosial\"]', 'Sering', 'Paham', 'Pendidikan', '[\"Teknologi Informasi\", \"Kewirausahaan\", \"Etika Profesi\"]', 'Ya', 'Ya', 'VMTS sudah sejalan, tapi harus memperhatikan mahasiswa dengan ekonomi lemah harus mendapatkan solusi, sehingga tidak terjadi putus studi', '2026-02-13 06:56:23.502718');

-- --------------------------------------------------------

--
-- Table structure for table `core_visimisi`
--

CREATE TABLE `core_visimisi` (
  `id` bigint(20) NOT NULL,
  `visi` longtext NOT NULL,
  `misi` longtext NOT NULL,
  `tujuan` longtext NOT NULL,
  `updated_at` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `core_visimisi`
--

INSERT INTO `core_visimisi` (`id`, `visi`, `misi`, `tujuan`, `updated_at`) VALUES
(1, '<p>Menjadi program studi&nbsp; unggul dan&nbsp;&nbsp;berdaya saing tinggi dalam Bidang Rekayasa Sistem Informasi&nbsp;&nbsp;dan Bisnis Digital&nbsp;&nbsp;berjiwa&nbsp;Technopreneur berskala Nasional tahun 2030.</p>', '<ol>\r\n	<li style=\"text-align:justify\"><span style=\"font-size:11pt\"><span style=\"font-family:Cambria,serif\">Menghasilkan lulusan yang profesional yang bertaqwa, bermoral, beretika, kompetitif, yang berjiwatechnopreneurship.</span></span></li>\r\n	<li style=\"text-align:justify\"><span style=\"font-size:11pt\"><span style=\"font-family:Cambria,serif\">Menghasilkan lulusan yang memiliki integritas dan kepribadian yang tinggi, terbuka dan memiliki tanggung jawab moral, terhadap perubahan perkembangan ilmu pengetahuan dan teknologi.</span></span></li>\r\n	<li style=\"text-align:justify\"><span style=\"font-size:11pt\"><span style=\"font-family:Cambria,serif\">Menghasilkan Lulusan yang memahami dan mengerti konsep ilmu komputer, manajemen dan bisnis.</span></span></li>\r\n	<li style=\"text-align:justify\"><span style=\"font-size:11pt\"><span style=\"font-family:Cambria,serif\">Menghasilkan Lulusan yang mampu dan dapat bekerja secara mandiri maupun dalam team work ( Organisasi).</span></span></li>\r\n	<li style=\"text-align:justify\"><span style=\"font-size:11pt\"><span style=\"font-family:Cambria,serif\">Menghasilkan karya dalam bentuk bisnis digital, dan rekayasa sistem informasi dan turunan melalui penelitian-penelitian serta pengabdian masyarakat.</span></span></li>\r\n</ol>', '<h4 style=\"text-align:start\"><span style=\"font-size:11pt\"><span style=\"font-family:&quot;Palatino Linotype&quot;,serif\"><span style=\"color:#000000\">Tujuan Umum Dan Tujuan Khusus</span></span></span></h4>\r\n\r\n<p style=\"text-align:start\"><span style=\"font-size:medium\"><span style=\"font-family:Calibri,sans-serif\"><span style=\"color:#000000\"><strong><span style=\"font-family:&quot;Palatino Linotype&quot;,serif\">Tujuan Umum</span></strong></span></span></span></p>\r\n\r\n<ol>\r\n	<li style=\"text-align:justify\"><span style=\"font-size:11pt\"><span style=\"font-family:Cambria,serif\">Menyiapkan mahasiswa dan lulusan yang memiliki kepribadian yang baik dalam menggunakan ilmu pengetahuan dan teknologi yang dikuasainya.</span></span></li>\r\n	<li style=\"text-align:justify\"><span style=\"font-size:11pt\"><span style=\"font-family:Cambria,serif\">Menyiapkan mahasiswa dan lulusan yang <span style=\"background-color:#fbfbfb\"><span style=\"color:black\">mampu untuk berpikir positive ,</span></span><span style=\"color:black\"> <span style=\"background-color:#fbfbfb\">bersikap kritis dan memberikan solusi pada suatu masalah (Organisasi).</span></span></span></span></li>\r\n	<li style=\"text-align:justify\"><span style=\"font-size:11pt\"><span style=\"font-family:Cambria,serif\">Menyiapkan mahasiswa dan lulusan yang memiliki kemampuan dalam mengembangkan, merumuskan dan memecahkan masalah umum kedalam bentuk sistem informasi dan menggunakan dalam suatu organisasi.</span></span></li>\r\n	<li style=\"text-align:justify\"><span style=\"font-size:11pt\"><span style=\"font-family:Cambria,serif\">Mengembangkan sikap toleransi dan berdaya saing yang tinggi dalam menciptakan lapangan kerja baru berupa bisnis digital.</span></span></li>\r\n	<li style=\"text-align:justify\"><span style=\"font-size:11pt\"><span style=\"font-family:Cambria,serif\">Meningkatkan Mutu Dosen, Lulusan, dan Luaran Program Studi</span></span></li>\r\n</ol>\r\n\r\n<h4 style=\"text-align:start\">&nbsp;</h4>\r\n\r\n<h4 style=\"text-align:start\"><span style=\"font-size:11pt\"><span style=\"font-family:&quot;Palatino Linotype&quot;,serif\"><span style=\"color:#000000\"><span dir=\"ltr\" lang=\"id\" style=\"color:#333333\">Tujuan khusus</span></span></span></span></h4>\r\n\r\n<ol>\r\n	<li style=\"text-align:justify\"><span style=\"font-size:11pt\"><span style=\"font-family:Cambria,serif\"><span dir=\"ltr\" lang=\"id\" style=\"color:black\">Program Studi</span><span dir=\"ltr\" lang=\"id\" style=\"color:black\"> mampu meningkatkan kegiatan, penghargaan dan prestasi Dosen, Tendik, Mahasiswa dan Lulusan di tingkat Nasional dan Internasional</span></span></span></li>\r\n	<li style=\"text-align:justify\"><span style=\"font-size:11pt\"><span style=\"font-family:Cambria,serif\"><span dir=\"ltr\" lang=\"id\" style=\"color:black\">Program Studi mampu meningkatkan ketersediaan sarana dan prasarana, linkungan kampus yang nyaman dan bertaraf Internasional</span></span></span></li>\r\n	<li style=\"text-align:justify\"><span style=\"font-size:11pt\"><span style=\"font-family:Cambria,serif\"><span dir=\"ltr\" lang=\"id\" style=\"color:black\">Meningkatkan Rata-rata IPK lulusan &gt;= 3.01 dan Meminimalkan mahasiswa Program Studi Sistem Informasi putus studi</span></span></span></li>\r\n</ol>\r\n\r\n<p style=\"text-align:start\">&nbsp;</p>', '2026-02-01 15:54:28.482627');

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2026-02-01 07:57:50.010907', '1', 'Program Studi Sistem Informasi - Baik Sekali', 1, '[{\"added\": {}}]', 18, 1),
(2, '2026-02-01 13:30:09.617778', '1', '1', 1, '[{\"added\": {}}]', 7, 1),
(3, '2026-02-01 13:34:06.971571', '1', '1', 2, '[{\"changed\": {\"fields\": [\"Description\"]}}]', 7, 1),
(4, '2026-02-01 13:34:47.789660', '2', 'Akreditasi', 1, '[{\"added\": {}}]', 7, 1),
(5, '2026-02-01 13:43:14.883342', '3', '3', 1, '[{\"added\": {}}]', 7, 1),
(6, '2026-02-01 13:56:49.839806', '1', 'Smbutan Warek III', 1, '[{\"added\": {}}]', 15, 1),
(7, '2026-02-01 14:06:10.324769', '5', 'Ahmad Louis,S.Kom.,M.Kom - 1013047702', 2, '[{\"changed\": {\"fields\": [\"Email\", \"Pendidikan\"]}}]', 11, 1),
(8, '2026-02-01 14:49:36.599316', '1', 'Kurikulum Berbasis OBE/KKNI/SKKNI & APTIKOM - Kurikulum Berbasis OBE – K22', 1, '[{\"added\": {}}]', 13, 1),
(9, '2026-02-01 15:27:26.252811', '1', 'Sambutan - Junaidi Surya,S.Kom,M.Kom', 1, '[{\"added\": {}}]', 8, 1),
(10, '2026-02-01 15:54:28.486682', '1', 'Visi & Misi Program Studi', 2, '[{\"changed\": {\"fields\": [\"Visi\", \"Misi\", \"Tujuan\"]}}]', 9, 1),
(11, '2026-02-02 01:36:41.883117', '1', 'Junaidi Surya,S.Kom.,M.Kom - 1010107601', 2, '[{\"changed\": {\"fields\": [\"Pendidikan\", \"Scholar link\", \"Bio\"]}}]', 11, 1),
(12, '2026-02-02 04:00:18.086410', '12', 'Dr. Darex Susanto, S.Kom., M.Kom - 1022108201', 2, '[{\"changed\": {\"fields\": [\"Pendidikan\"]}}]', 11, 1),
(13, '2026-02-03 04:53:28.095579', '11', 'SIKK3305 - Sistem Informasi Manajemen', 1, '[{\"added\": {}}]', 23, 1),
(14, '2026-02-03 04:54:04.771390', '12', 'SIKK3306 - Manajemen Investasi Teknologi Informasi', 1, '[{\"added\": {}}]', 23, 1),
(15, '2026-02-03 04:54:59.835319', '13', 'SIKK3207 - Manajemen Proses Bisnis', 1, '[{\"added\": {}}]', 23, 1),
(16, '2026-02-03 04:55:55.237644', '14', 'SIKK3308 - Konsep Sistem Informasi', 1, '[{\"added\": {}}]', 23, 1),
(17, '2026-02-03 04:56:29.068674', '15', 'PK3202 - Pendidikan Pancasila', 1, '[{\"added\": {}}]', 23, 1),
(18, '2026-02-03 04:57:12.819546', '16', 'FKKB3304 - Manajemen & Sistem Basis Data', 1, '[{\"added\": {}}]', 23, 1),
(19, '2026-02-03 04:57:45.482180', '17', 'SIKB3301 - Pemrograman Berbasis Platform (P)', 1, '[{\"added\": {}}]', 23, 1),
(20, '2026-02-03 04:58:23.881448', '18', 'SIPN3306 - Bahasa Inggris II', 1, '[{\"added\": {}}]', 23, 1),
(21, '2026-02-03 05:08:02.377554', '11', 'Rencana Pembelajaran Semester (RPS)', 1, '[{\"added\": {}}]', 12, 1),
(22, '2026-02-03 05:30:00.447896', '1', 'SIKK1302 - Sistem Dan Teknologi Informasi', 2, '[{\"changed\": {\"fields\": [\"Kode\", \"Nama\", \"Kategori\"]}}]', 23, 1),
(23, '2026-02-03 05:30:20.206893', '1', 'SIKK1302 - Sistem Dan Teknologi Informasi', 2, '[]', 23, 1),
(24, '2026-02-03 05:30:23.985375', '1', 'SIKK1302 - Sistem Dan Teknologi Informasi', 2, '[]', 23, 1),
(25, '2026-02-03 05:31:36.433550', '2', 'FKKK1402 - Algorithma dan Pemrograman (P)', 2, '[{\"changed\": {\"fields\": [\"Kode\", \"Nama\", \"Sks\", \"Kategori\"]}}]', 23, 1),
(26, '2026-02-03 05:32:31.513230', '3', 'FKPN1201 - Aljabar Vektor dan Matriks', 2, '[{\"changed\": {\"fields\": [\"Kode\", \"Nama\", \"Kategori\"]}}]', 23, 1),
(27, '2026-02-03 05:33:54.292497', '4', 'SIKK1201 - Pengantar Manajemen', 2, '[{\"changed\": {\"fields\": [\"Kode\", \"Nama\", \"Kategori\"]}}]', 23, 1),
(28, '2026-02-03 05:34:31.514874', '5', 'SIKK1403 - Pemrogramman Dasar (P)', 2, '[{\"changed\": {\"fields\": [\"Kode\", \"Nama\", \"Sks\", \"Kategori\"]}}]', 23, 1),
(29, '2026-02-03 05:35:59.852086', '19', 'FKKK1403 - Sistem Operasi dan Arsitektur Komputer (P)', 1, '[{\"added\": {}}]', 23, 1),
(30, '2026-02-03 05:38:56.781215', '19', 'FKKK1403 - Sistem Operasi dan Arsitektur Komputer (P)', 2, '[{\"changed\": {\"fields\": [\"Order\"]}}]', 23, 1),
(31, '2026-02-03 05:38:56.784030', '1', 'SIKK1302 - Sistem Dan Teknologi Informasi', 2, '[{\"changed\": {\"fields\": [\"Order\"]}}]', 23, 1),
(32, '2026-02-03 05:38:56.788100', '2', 'FKKK1402 - Algorithma dan Pemrograman (P)', 2, '[{\"changed\": {\"fields\": [\"Order\"]}}]', 23, 1),
(33, '2026-02-03 05:38:56.790025', '3', 'FKPN1201 - Aljabar Vektor dan Matriks', 2, '[{\"changed\": {\"fields\": [\"Order\"]}}]', 23, 1),
(34, '2026-02-03 05:38:56.792028', '4', 'SIKK1201 - Pengantar Manajemen', 2, '[{\"changed\": {\"fields\": [\"Order\"]}}]', 23, 1),
(35, '2026-02-03 05:38:56.793925', '5', 'SIKK1403 - Pemrogramman Dasar (P)', 2, '[{\"changed\": {\"fields\": [\"Order\"]}}]', 23, 1),
(36, '2026-02-03 06:16:24.071628', '2', 'RPS Pemrograman Dasar [4 SKS] - Rencana Pembelajaran Semester (RPS)', 1, '[{\"added\": {}}]', 13, 1),
(37, '2026-02-03 06:18:40.202432', '5', 'SIKK1403 - Pemrogramman Dasar (P)', 2, '[{\"changed\": {\"fields\": [\"Rps document\", \"Dosen pengampu\", \"Materi perkuliahan\"]}}]', 23, 1),
(38, '2026-02-03 06:28:46.499967', '20', 'MK001 - Pemrograman Dasar', 3, '', 23, 1),
(39, '2026-02-03 07:21:43.780515', '79', 'SIKK1403 - Pemrogramman Dasar (P)', 2, '[{\"changed\": {\"fields\": [\"Rps document\", \"Dosen pengampu\", \"Materi perkuliahan\"]}}]', 23, 1),
(40, '2026-02-03 12:22:45.752984', '3', 'Pembimbing - Buku Panduan', 1, '[{\"added\": {}}]', 24, 1),
(41, '2026-02-03 12:26:57.993812', '4', 'Panduan Seminar Proposal Skripsi - Buku Panduan', 1, '[{\"added\": {}}]', 24, 1),
(42, '2026-02-03 12:30:00.803853', '5', 'Buku Panduan Skripsi Program Studi SI - Buku Panduan', 1, '[{\"added\": {}}]', 24, 1),
(43, '2026-02-03 12:48:35.126808', '24', 'Andika Junial Perkasa, S.Kom (2022)', 2, '[]', 19, 1),
(44, '2026-02-03 12:59:21.436700', '30', 'Ubaidillah, S.Kom (2016)', 1, '[{\"added\": {}}]', 19, 1),
(45, '2026-02-03 13:02:12.090452', '30', 'Ubaidillah, S.Kom (2016)', 2, '[{\"changed\": {\"fields\": [\"Photo\"]}}]', 19, 1),
(46, '2026-02-03 13:37:07.211080', '3', 'Pembimbing Akademik - Buku Panduan', 2, '[{\"changed\": {\"fields\": [\"Title\"]}}]', 24, 1),
(47, '2026-02-03 14:42:39.486562', '2', 'Membuat Jaringan Syaraf Tiruan mengenal  Tulisan dengan AI', 1, '[{\"added\": {}}]', 15, 1),
(48, '2026-02-03 14:47:14.336336', '1', 'Ujian Semester Gasal 2025', 1, '[{\"added\": {}}]', 14, 1),
(49, '2026-02-03 14:48:30.099898', '1', 'Ujian Semester Gasal 2025', 2, '[{\"changed\": {\"fields\": [\"Thumbnail\"]}}]', 14, 1),
(50, '2026-02-07 12:38:44.264454', '148', 'SIKK1403 - Pemrogramman Dasar (P)', 2, '[{\"changed\": {\"fields\": [\"Rps document\", \"Dosen pengampu\", \"Materi perkuliahan\"]}}]', 23, 1),
(51, '2026-02-07 12:39:39.209914', '148', 'SIKK1403 - Pemrogramman Dasar (P)', 2, '[{\"changed\": {\"fields\": [\"Dosen pengampu\"]}}]', 23, 1),
(52, '2026-02-07 12:42:25.085649', '2', 'RPS Pemrograman Dasar [4 SKS] - Rencana Pembelajaran Semester (RPS)', 2, '[{\"changed\": {\"fields\": [\"File\"]}}]', 13, 1),
(53, '2026-02-07 12:43:08.353141', '148', 'SIKK1403 - Pemrogramman Dasar (P)', 2, '[{\"changed\": {\"fields\": [\"Deskripsi\"]}}]', 23, 1),
(54, '2026-02-07 12:53:30.149985', '6', 'Pemrograman Berbasis Platform (P) - Rencana Pembelajaran Semester (RPS)', 1, '[{\"added\": {}}]', 13, 1),
(55, '2026-02-07 12:55:00.083482', '165', 'SIKB3301 - Pemrograman Berbasis Platform (P)', 2, '[{\"changed\": {\"fields\": [\"Rps document\", \"Dosen pengampu\", \"Materi perkuliahan\"]}}]', 23, 1),
(56, '2026-02-07 13:14:00.484514', '2', 'Program Studi Sistem Informasi - \"B\"', 1, '[{\"added\": {}}]', 18, 1),
(57, '2026-02-07 13:15:45.808985', '2', 'Program Studi Sistem Informasi - B', 2, '[{\"changed\": {\"fields\": [\"Peringkat\"]}}]', 18, 1),
(58, '2026-02-07 13:20:16.076911', '3', 'Program Studi Sistem Informasi - B', 1, '[{\"added\": {}}]', 18, 1),
(59, '2026-02-07 13:25:08.322419', '2', 'Program Studi Sistem Informasi - B', 2, '[{\"changed\": {\"fields\": [\"Nomor sk\"]}}]', 18, 1),
(60, '2026-02-07 13:25:24.344558', '3', 'Program Studi Sistem Informasi - B', 2, '[{\"changed\": {\"fields\": [\"Nomor sk\"]}}]', 18, 1),
(61, '2026-02-09 05:22:56.388852', '1', '1', 2, '[{\"changed\": {\"fields\": [\"Image\"]}}]', 7, 1),
(62, '2026-02-09 06:10:01.215783', '1', '1', 2, '[{\"changed\": {\"fields\": [\"Image\"]}}]', 7, 1),
(63, '2026-02-09 07:21:33.014577', '1', '1', 3, '', 7, 1),
(64, '2026-02-09 07:22:26.950664', '4', '11', 1, '[{\"added\": {}}]', 7, 1),
(65, '2026-02-09 07:27:45.916125', '3', '3', 2, '[{\"changed\": {\"fields\": [\"Image\"]}}]', 7, 1),
(66, '2026-02-13 08:08:12.044521', '7', 'Pemrograman Berorientasi Objek - Rencana Pembelajaran Semester (RPS)', 1, '[{\"added\": {}}]', 13, 1),
(67, '2026-02-13 08:10:17.450672', '214', 'SIKB6409 - Pemrograman Berorientasi Objek', 1, '[{\"added\": {}}]', 23, 1),
(68, '2026-02-18 04:25:57.235784', '2', 'RPS Pemrograman Dasar [4 SKS] - Rencana Pembelajaran Semester (RPS)', 3, '', 13, 1),
(69, '2026-02-18 06:21:15.100320', '8', 'Pemrograman Dasar - Rencana Pembelajaran Semester (RPS)', 1, '[{\"added\": {}}]', 13, 1),
(70, '2026-02-18 06:23:53.429236', '215', 'SIKK1403 2 - Pemrogaman Dasar', 1, '[{\"added\": {}}]', 23, 1),
(71, '2026-02-18 06:24:37.680458', '215', 'SIKK1403 - Pemrogaman Dasar', 2, '[{\"changed\": {\"fields\": [\"Kode\"]}}]', 23, 1),
(72, '2026-02-18 06:28:36.219546', '148', 'SIKK1403 - Pemrogramman Dasar (P)', 3, '', 23, 1),
(73, '2026-02-18 06:29:11.954615', '215', 'SIKK1403 - Pemrograman Dasar (P)', 2, '[{\"changed\": {\"fields\": [\"Nama\", \"Order\"]}}]', 23, 1),
(74, '2026-02-21 16:04:43.696284', '1', 'Alumni - Test Alumni', 3, '', 27, 1),
(75, '2026-03-11 03:24:37.091501', '215', 'SIKK1403 - Pemrograman Dasar (P)', 2, '[{\"changed\": {\"fields\": [\"Dosen pengampu\"]}}]', 23, 1);

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(18, 'core', 'akreditasi'),
(19, 'core', 'alumni'),
(24, 'core', 'bukupanduan'),
(13, 'core', 'document'),
(12, 'core', 'documentcategory'),
(11, 'core', 'dosen'),
(15, 'core', 'gallery'),
(20, 'core', 'jobcareer'),
(21, 'core', 'link'),
(23, 'core', 'matakuliah'),
(14, 'core', 'news'),
(22, 'core', 'pagecontent'),
(17, 'core', 'penelitian'),
(16, 'core', 'prestasi'),
(10, 'core', 'prospekkeunggulan'),
(8, 'core', 'sambutan'),
(7, 'core', 'slide'),
(26, 'core', 'surveykepuasanlulusan'),
(27, 'core', 'surveykurikulum'),
(25, 'core', 'surveyresponse'),
(9, 'core', 'visimisi'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2026-02-01 05:39:45.316531'),
(2, 'auth', '0001_initial', '2026-02-01 05:39:46.075722'),
(3, 'admin', '0001_initial', '2026-02-01 05:39:46.216622'),
(4, 'admin', '0002_logentry_remove_auto_add', '2026-02-01 05:39:46.225633'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2026-02-01 05:39:46.235885'),
(6, 'contenttypes', '0002_remove_content_type_name', '2026-02-01 05:39:46.341949'),
(7, 'auth', '0002_alter_permission_name_max_length', '2026-02-01 05:39:46.417092'),
(8, 'auth', '0003_alter_user_email_max_length', '2026-02-01 05:39:46.444991'),
(9, 'auth', '0004_alter_user_username_opts', '2026-02-01 05:39:46.453273'),
(10, 'auth', '0005_alter_user_last_login_null', '2026-02-01 05:39:46.498968'),
(11, 'auth', '0006_require_contenttypes_0002', '2026-02-01 05:39:46.500960'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2026-02-01 05:39:46.515602'),
(13, 'auth', '0008_alter_user_username_max_length', '2026-02-01 05:39:46.551235'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2026-02-01 05:39:46.581040'),
(15, 'auth', '0010_alter_group_name_max_length', '2026-02-01 05:39:46.608477'),
(16, 'auth', '0011_update_proxy_permissions', '2026-02-01 05:39:46.643419'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2026-02-01 05:39:46.672400'),
(18, 'sessions', '0001_initial', '2026-02-01 05:39:46.727495'),
(19, 'core', '0001_initial', '2026-02-01 05:43:12.782395'),
(20, 'core', '0002_matakuliah', '2026-02-03 04:27:09.585912'),
(21, 'core', '0003_matakuliah_dosen_pengampu_matakuliah_is_active_and_more', '2026-02-03 05:49:40.677060'),
(22, 'core', '0004_surveyresponse_bukupanduan_alter_matakuliah_semester', '2026-02-13 06:51:04.692735'),
(23, 'core', '0005_surveykepuasanlulusan', '2026-02-13 07:17:18.079187'),
(24, 'core', '0006_surveykurikulum_matakuliah_dosen_pengampu_legacy_and_more', '2026-02-21 14:09:16.207022'),
(25, 'core', '0007_remove_surveykurikulum_kompetensi_lulusan_and_more', '2026-02-21 14:42:07.659409');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('5wtfonlzfov7jp7fn500xtc3naowt6yw', '.eJxVjMsOwiAQRf-FtSE8LBSX7vsNZJgZpGogKe3K-O_apAvd3nPOfYkI21ri1nmJM4mL0OL0uyXAB9cd0B3qrUlsdV3mJHdFHrTLqRE_r4f7d1Cgl2_N1iZv0bBLnlgFcNaY0QGCGhJROI9IzJhJe5WcZh8whwCZjTY6DEa8PwISOJU:1vmYfC:4CmiztCZiUVQAQ09QNsaJk0kM2Fj87DKziOJqFWLw6M', '2026-02-15 14:42:58.288764'),
('7fowvjr1lmqkj1lpnn5nqp9ottg3aqc9', '.eJxVjMsOwiAQRf-FtSE8LBSX7vsNZJgZpGogKe3K-O_apAvd3nPOfYkI21ri1nmJM4mL0OL0uyXAB9cd0B3qrUlsdV3mJHdFHrTLqRE_r4f7d1Cgl2_N1iZv0bBLnlgFcNaY0QGCGhJROI9IzJhJe5WcZh8whwCZjTY6DEa8PwISOJU:1vtpD0:NWts7uH614Kx-b1LXWH7a78l3yppuYauqIUwilB8g5o', '2026-03-07 15:47:54.310140'),
('a3jsbl3twcva7b03c3e9dqpcraxhiyj0', '.eJxVjMsOwiAQRf-FtSE8LBSX7vsNZJgZpGogKe3K-O_apAvd3nPOfYkI21ri1nmJM4mL0OL0uyXAB9cd0B3qrUlsdV3mJHdFHrTLqRE_r4f7d1Cgl2_N1iZv0bBLnlgFcNaY0QGCGhJROI9IzJhJe5WcZh8whwCZjTY6DEa8PwISOJU:1w095W:tbOJmZf01wm3qXBRveF5XyjvDWg1Poi3w1lyQRUwQA4', '2026-03-25 02:14:18.851605'),
('c3s3p52uzz6cyuddxtz4b0o64kqkctrm', '.eJxVjMsOwiAQRf-FtSE8LBSX7vsNZJgZpGogKe3K-O_apAvd3nPOfYkI21ri1nmJM4mL0OL0uyXAB9cd0B3qrUlsdV3mJHdFHrTLqRE_r4f7d1Cgl2_N1iZv0bBLnlgFcNaY0QGCGhJROI9IzJhJe5WcZh8whwCZjTY6DEa8PwISOJU:1vpJiD:w83DHweBG3hiQpCs12HH9PmX7IbeePKG1Rva__b0Yis', '2026-02-23 05:21:29.078890'),
('dvuj111uzplk5r1d21t8wi05sybauf1m', '.eJxVjMsOwiAQRf-FtSE8LBSX7vsNZJgZpGogKe3K-O_apAvd3nPOfYkI21ri1nmJM4mL0OL0uyXAB9cd0B3qrUlsdV3mJHdFHrTLqRE_r4f7d1Cgl2_N1iZv0bBLnlgFcNaY0QGCGhJROI9IzJhJe5WcZh8whwCZjTY6DEa8PwISOJU:1vnAB8:Pk2vGAqGL2cEQlxRvnwCtIVJ2g494ZbImtkD4SMjZYI', '2026-02-17 06:46:26.508057'),
('fh27jqw7t7rfcbba4ro2op3orwwxtdix', '.eJxVjMsOwiAQRf-FtSE8LBSX7vsNZJgZpGogKe3K-O_apAvd3nPOfYkI21ri1nmJM4mL0OL0uyXAB9cd0B3qrUlsdV3mJHdFHrTLqRE_r4f7d1Cgl2_N1iZv0bBLnlgFcNaY0QGCGhJROI9IzJhJe5WcZh8whwCZjTY6DEa8PwISOJU:1w08oK:PPmKFd2-K1v8aSkMHpCiRrWSaS4EBA4w6_r2X2fiw5s', '2026-03-25 01:56:32.284284'),
('gbr2bpm9bksl2dh90yrzsgw69yq9st41', '.eJxVjMsOwiAQRf-FtSE8LBSX7vsNZJgZpGogKe3K-O_apAvd3nPOfYkI21ri1nmJM4mL0OL0uyXAB9cd0B3qrUlsdV3mJHdFHrTLqRE_r4f7d1Cgl2_N1iZv0bBLnlgFcNaY0QGCGhJROI9IzJhJe5WcZh8whwCZjTY6DEa8PwISOJU:1vsZ4g:xoBs654MRdfmwKc4-LVwM9Q3uefbsKARKiTJPZxLzDs', '2026-03-04 04:22:06.530929'),
('k5qutrby61c1u17f92huxhtphs6oj8yr', '.eJxVjMsOwiAQRf-FtSE8LBSX7vsNZJgZpGogKe3K-O_apAvd3nPOfYkI21ri1nmJM4mL0OL0uyXAB9cd0B3qrUlsdV3mJHdFHrTLqRE_r4f7d1Cgl2_N1iZv0bBLnlgFcNaY0QGCGhJROI9IzJhJe5WcZh8whwCZjTY6DEa8PwISOJU:1vohVZ:y8UXocG2Wt5C3xHnq5XnDpi9IC_iWtKOGTZCsK8ftec', '2026-02-21 12:33:53.369142'),
('kosykygsyieut0sotjg64brvra1179r1', '.eJxVjMsOwiAQRf-FtSE8LBSX7vsNZJgZpGogKe3K-O_apAvd3nPOfYkI21ri1nmJM4mL0OL0uyXAB9cd0B3qrUlsdV3mJHdFHrTLqRE_r4f7d1Cgl2_N1iZv0bBLnlgFcNaY0QGCGhJROI9IzJhJe5WcZh8whwCZjTY6DEa8PwISOJU:1vqnvH:JxIZexGonWuwmuHVKFMdD7QXK_GIvjkRvbxRGccbFkM', '2026-02-27 07:49:07.657473'),
('oiu0sywkvkwqhccbpn0w8vlp5jrqqp0n', '.eJxVjMsOwiAQRf-FtSE8LBSX7vsNZJgZpGogKe3K-O_apAvd3nPOfYkI21ri1nmJM4mL0OL0uyXAB9cd0B3qrUlsdV3mJHdFHrTLqRE_r4f7d1Cgl2_N1iZv0bBLnlgFcNaY0QGCGhJROI9IzJhJe5WcZh8whwCZjTY6DEa8PwISOJU:1vnFDj:nHOrJuRzjJonrEYwae_tbDY0xp9aod-76PbIi881lvc', '2026-02-17 12:09:27.046326'),
('utxvyoahv9ew1mba1h200d24zinjg0xl', '.eJxVjMsOwiAQRf-FtSE8LBSX7vsNZJgZpGogKe3K-O_apAvd3nPOfYkI21ri1nmJM4mL0OL0uyXAB9cd0B3qrUlsdV3mJHdFHrTLqRE_r4f7d1Cgl2_N1iZv0bBLnlgFcNaY0QGCGhJROI9IzJhJe5WcZh8whwCZjTY6DEa8PwISOJU:1vxycY:BOzq2S5UxeZF7AGvtBbZ-_hvy_sn5a7KzdgSZbGf18Y', '2026-03-19 02:39:26.177615'),
('vq1yp89ai08cyl9zo77j3yeuisc67b1f', '.eJxVjMsOwiAQRf-FtSE8LBSX7vsNZJgZpGogKe3K-O_apAvd3nPOfYkI21ri1nmJM4mL0OL0uyXAB9cd0B3qrUlsdV3mJHdFHrTLqRE_r4f7d1Cgl2_N1iZv0bBLnlgFcNaY0QGCGhJROI9IzJhJe5WcZh8whwCZjTY6DEa8PwISOJU:1vqn70:XBvxcNPslNOPR_w7f2NoVOmxaYaPKbZByCMpAQsFJH8', '2026-02-27 06:57:10.239224');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `core_akreditasi`
--
ALTER TABLE `core_akreditasi`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `core_alumni`
--
ALTER TABLE `core_alumni`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `core_document`
--
ALTER TABLE `core_document`
  ADD PRIMARY KEY (`id`),
  ADD KEY `core_document_uploaded_by_id_b2667a66_fk_auth_user_id` (`uploaded_by_id`),
  ADD KEY `core_document_category_id_717e525b_fk_core_documentcategory_id` (`category_id`);

--
-- Indexes for table `core_documentcategory`
--
ALTER TABLE `core_documentcategory`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`),
  ADD UNIQUE KEY `slug` (`slug`);

--
-- Indexes for table `core_dosen`
--
ALTER TABLE `core_dosen`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `nidn` (`nidn`);

--
-- Indexes for table `core_gallery`
--
ALTER TABLE `core_gallery`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `core_jobcareer`
--
ALTER TABLE `core_jobcareer`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `core_link`
--
ALTER TABLE `core_link`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `core_matakuliah`
--
ALTER TABLE `core_matakuliah`
  ADD PRIMARY KEY (`id`),
  ADD KEY `core_matakuliah_rps_document_id_792017e8_fk_core_document_id` (`rps_document_id`);

--
-- Indexes for table `core_matakuliah_dosen_pengampu`
--
ALTER TABLE `core_matakuliah_dosen_pengampu`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `core_matakuliah_dosen_pe_matakuliah_id_dosen_id_81701cf3_uniq` (`matakuliah_id`,`dosen_id`),
  ADD KEY `core_matakuliah_dose_dosen_id_2c45e72c_fk_core_dose` (`dosen_id`);

--
-- Indexes for table `core_news`
--
ALTER TABLE `core_news`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `slug` (`slug`),
  ADD KEY `core_news_author_id_8287a902_fk_auth_user_id` (`author_id`);

--
-- Indexes for table `core_pagecontent`
--
ALTER TABLE `core_pagecontent`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `page_name` (`page_name`);

--
-- Indexes for table `core_penelitian`
--
ALTER TABLE `core_penelitian`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `core_prestasi`
--
ALTER TABLE `core_prestasi`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `core_prospekkeunggulan`
--
ALTER TABLE `core_prospekkeunggulan`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `core_sambutan`
--
ALTER TABLE `core_sambutan`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `core_slide`
--
ALTER TABLE `core_slide`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `core_surveykepuasanlulusan`
--
ALTER TABLE `core_surveykepuasanlulusan`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `core_surveykurikulum`
--
ALTER TABLE `core_surveykurikulum`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `core_surveyresponse`
--
ALTER TABLE `core_surveyresponse`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `core_visimisi`
--
ALTER TABLE `core_visimisi`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=109;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `core_akreditasi`
--
ALTER TABLE `core_akreditasi`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `core_alumni`
--
ALTER TABLE `core_alumni`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=31;

--
-- AUTO_INCREMENT for table `core_document`
--
ALTER TABLE `core_document`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `core_documentcategory`
--
ALTER TABLE `core_documentcategory`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `core_dosen`
--
ALTER TABLE `core_dosen`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `core_gallery`
--
ALTER TABLE `core_gallery`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `core_jobcareer`
--
ALTER TABLE `core_jobcareer`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `core_link`
--
ALTER TABLE `core_link`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `core_matakuliah`
--
ALTER TABLE `core_matakuliah`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=216;

--
-- AUTO_INCREMENT for table `core_matakuliah_dosen_pengampu`
--
ALTER TABLE `core_matakuliah_dosen_pengampu`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `core_news`
--
ALTER TABLE `core_news`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `core_pagecontent`
--
ALTER TABLE `core_pagecontent`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `core_penelitian`
--
ALTER TABLE `core_penelitian`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `core_prestasi`
--
ALTER TABLE `core_prestasi`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `core_prospekkeunggulan`
--
ALTER TABLE `core_prospekkeunggulan`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `core_sambutan`
--
ALTER TABLE `core_sambutan`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `core_slide`
--
ALTER TABLE `core_slide`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `core_surveykepuasanlulusan`
--
ALTER TABLE `core_surveykepuasanlulusan`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `core_surveykurikulum`
--
ALTER TABLE `core_surveykurikulum`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `core_surveyresponse`
--
ALTER TABLE `core_surveyresponse`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `core_visimisi`
--
ALTER TABLE `core_visimisi`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=76;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=28;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `core_document`
--
ALTER TABLE `core_document`
  ADD CONSTRAINT `core_document_category_id_717e525b_fk_core_documentcategory_id` FOREIGN KEY (`category_id`) REFERENCES `core_documentcategory` (`id`),
  ADD CONSTRAINT `core_document_uploaded_by_id_b2667a66_fk_auth_user_id` FOREIGN KEY (`uploaded_by_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `core_matakuliah`
--
ALTER TABLE `core_matakuliah`
  ADD CONSTRAINT `core_matakuliah_rps_document_id_792017e8_fk_core_document_id` FOREIGN KEY (`rps_document_id`) REFERENCES `core_document` (`id`);

--
-- Constraints for table `core_matakuliah_dosen_pengampu`
--
ALTER TABLE `core_matakuliah_dosen_pengampu`
  ADD CONSTRAINT `core_matakuliah_dose_dosen_id_2c45e72c_fk_core_dose` FOREIGN KEY (`dosen_id`) REFERENCES `core_dosen` (`id`),
  ADD CONSTRAINT `core_matakuliah_dose_matakuliah_id_6b112a2b_fk_core_mata` FOREIGN KEY (`matakuliah_id`) REFERENCES `core_matakuliah` (`id`);

--
-- Constraints for table `core_news`
--
ALTER TABLE `core_news`
  ADD CONSTRAINT `core_news_author_id_8287a902_fk_auth_user_id` FOREIGN KEY (`author_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
