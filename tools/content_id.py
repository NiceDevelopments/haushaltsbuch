"""Bahasa Indonesia (Welle 1, 24.11.2026). Fakta sama dengan content_en.py; nominal dalam rupiah
(tangkapan layar aplikasi berbahasa Indonesia memakai Rp, tanpa angka desimal).

Pencarian (saran Google, 24.11.2026): "aplikasi catatan keuangan (harian, offline, gratis, rumah
tangga)", "aplikasi pencatat pengeluaran (harian, bulanan, dan pemasukan)", "cara mengatur
keuangan bulanan rumah tangga". Nama di Google Play: "Anggaran Rumah Tangga Simpel".
Kata-kata aplikasi (tools/i18n/id.txt): Tersedia, Simpan, Urungkan, Riwayat, Analisis, Terpakai,
Sisa, Per hari, Pemasukan, Biaya tetap, Untuk dibelanjakan, Hapus iklan,
Bawa sisa, Bawa kekurangan, Tanpa kategori.
Pemindaian struk TIDAK ditampilkan di halaman ini (pemeriksaan 25.11.2026): pemindai tidak membaca nominal
rupiah (tanpa dua angka desimal, lihat ../CLAUDE.md dan store/gfx_texte_welt.py scan=False) dan fitur
ini juga tidak dipromosikan di Play Store Indonesia.
Panduan belum ada dalam bahasa Indonesia: halaman utama menautkan panduan berbahasa Inggris.
"""

APP = "Anggaran Rumah Tangga Simpel"

C = {
    "app_name": APP,
    "lang_name": "Bahasa Indonesia",
    "og_locale": "id_ID",
    "ui": {
        "skip": "Langsung ke konten",
        "nav": "Navigasi utama",
        "guides": "Panduan (bahasa Inggris)",
        "privacy": "Privasi (bahasa Inggris)",
        "imprint": "Info penerbit (bahasa Inggris)",
        "faq": "Pertanyaan umum",
        "toc": "Daftar isi",
        "crumbs": "Jejak navigasi",
        "updated": "Diperbarui:",
        "with_app": "Dengan aplikasi",
        "more_guides": "Panduan lainnya",
        "all_guides": "Lihat semua panduan (bahasa Inggris)",
        "play_soon": "Segera hadir di Google Play.",
        "play_cta": "Temukan di Google Play",
        "app_more": "Anggaran Rumah Tangga Simpel – sekilas tentang aplikasinya",
        "footer_tag": "Catatan keuangan untuk Android, benar-benar simpel.",
        "trademark": "Google Play dan Android adalah merek dagang Google LLC.",
    },

    "home": {
        "title": "Anggaran Rumah Tangga Simpel – aplikasi catatan keuangan offline",
        "desc": "Aplikasi pencatat pengeluaran Android: ketik nominal, simpan. Langsung terlihat sisa uang setelah biaya tetap – tanpa akun, tanpa bank.",
        "alt_names": ["Simple Household Budget", "Einfaches Haushaltsbuch"],
        "kicker": "Aplikasi anggaran untuk Android",
        "h1": "Anggaran Rumah Tangga Simpel",
        "lead": "Benar-benar simpel. Mencatat pengeluaran artinya: **ketik nominal, ketuk Simpan.** Satu angka besar menunjukkan berapa sisa uangmu bulan ini setelah biaya tetap. Tanpa akun, tanpa koneksi ke bank, tanpa cloud.",
        "meter_label": "Tersedia",
        "meter_num": "Rp2.450.000",
        "meter_cents": "",
        "meter_note": "Batang menunjukkan berapa yang sudah terpakai, garisnya menunjukkan sudah sejauh mana bulan berjalan.",
        "meter_aria": "Contoh: tersedia 2.450.000 rupiah. Batang terisi 38 persen, bulan sudah berjalan separuh.",
        "hero_shot": "id-home.webp",
        "shots": [
            ["id-home.webp", "Layar utama: “Tersedia Rp6.113.200” dengan huruf besar dan sebuah batang; di bawahnya nominal Rp15.000 sudah diketik, kolom Kategori dan Keterangan, tombol angka, dan tombol hijau Simpan."],
            ["id-history.webp", "Riwayat dalam mode gelap: pengeluaran per hari dengan keterangan, kategori, dan nominal."],
            ["id-summary.webp", "Analisis: Terpakai Rp1.896.800, Sisa Rp6.098.200, Per hari rata-rata Rp158.067, grafik per hari, dan rincian pemasukan, biaya tetap, dan untuk dibelanjakan."],
        ],
        "features": [
            {"kicker": "Catat", "h2": "Satu pengeluaran, dua ketukan",
             "body": ["Ketik nominal, ketuk Simpan – tidak ada lagi yang wajib. Kategori, keterangan, tanggal, dan catatan bersifat opsional dan bisa ditambahkan nanti.",
                      "Begitu disimpan, muncul **Urungkan**, kalau-kalau kamu salah ketik. Pengeluaran yang terlupa bisa ditambahkan nanti di riwayat, lengkap dengan tanggal dan jam."],
             "shot": "id-history.webp"},
            {"kicker": "Biaya tetap", "h2": "Cukup dicatat sekali, lalu lupakan",
             "body": ["Sewa, listrik, asuransi, langganan: saat pengaturan awal aplikasi menanyakan satu per satu – kosongkan saja kalau tidak punya. Biaya tahunan, misalnya asuransi atau pajak kendaraan, diberi tanggal jatuh tempo.",
                      "Setelah itu aplikasi sendiri yang memotong biaya tetapmu setiap bulan. Angka besar di layar utama adalah sisa uangmu yang sebenarnya."],
             "shot": "meter"},
            {"kicker": "Analisis", "h2": "Satu bulan dalam tiga angka",
             "body": ["Terpakai, sisa, rata-rata per hari. Ditambah grafik per hari dan rincian bulanmu: pemasukan, biaya tetap, untuk dibelanjakan.",
                      "Tanpa dasbor, tanpa dua belas grafik. Kalau mau, sisa uang bisa dibawa ke bulan berikutnya – di akhir bulan kedua, aplikasi menanyakannya satu kali."],
             "shot": "id-summary.webp"},
        ],
        "simple": {
            "kicker": "Prinsipnya",
            "h2": "Tujuannya: aplikasi anggaran paling simpel yang ada",
            "lead": "Setiap fitur baru harus lolos satu ujian: apakah mencatat pengeluaran masih secepat sebelumnya? Kalau tidak, fitur itu tidak masuk.",
            "points": [
                "**Satu kolom wajib per pengeluaran.** Nominalnya – yang lain opsional.",
                "**Satu angka, bukan dasbor.** Layar utama menunjukkan sisa uang yang masih tersedia bulan ini – biaya tetap sudah dipotong.",
                "**Yang jarang dipakai, belakangan.** Aplikasi tidak menanyakan tanggal atau catatan saat kamu mencatat pengeluaran – tambahkan nanti kalau perlu.",
                "**Tidak ada yang perlu diurus.** Tanpa akun, tanpa kata sandi, tanpa koneksi ke bank, tanpa langganan.",
            ],
            "more": "Metodenya, dengan atau tanpa aplikasi (bahasa Inggris): [How to keep a simple household budget](/en/guides/simple-household-budget/).",
        },
        "nots_h2": "Angka-angkamu tetap di HP-mu",
        "nots_lead": "Semua yang kamu catat hanya tersimpan di perangkatmu. Tidak ada server yang bisa menampung data keuanganmu.",
        "nots": [
            "**Tanpa akun, tanpa login** – buka aplikasinya dan langsung mulai.",
            "**Tanpa koneksi ke bank** – kamu tidak pernah memasukkan data login bank di mana pun.",
            "**Tanpa cloud, tanpa statistik pemakaian, tanpa laporan error.** Artinya juga tidak ada sinkronisasi antarperangkat.",
            "**{languages} bahasa**, dari Arab sampai Vietnam, termasuk bahasa Indonesia. Mata uang mengikuti wilayahmu – rupiah tanpa angka desimal.",
        ],
        "privacy_link": "Baca kebijakan privasi (bahasa Inggris)",
        "guides_h2": "Panduan untuk anggaran bulananmu (bahasa Inggris)",
        "guides_lead": "Berguna dengan atau tanpa aplikasi: menghitung anggaran harian, membuat daftar biaya tetap, menyiapkan tagihan tahunan. Untuk sementara hanya dalam bahasa Inggris.",
        "guide_cards": [
            ("Cara membuat catatan keuangan rumah tangga yang simpel, tanpa spreadsheet", "Tiga angka, tanpa kategori: versi paling kecil yang tetap berhasil."),
            ("Berapa yang boleh saya belanjakan per hari?", "Anggaran harianmu dalam tiga langkah – di awal bulan dan di pertengahan."),
            ("Daftar biaya tetap: apa saja, dan berapa sisanya?", "Daftar pos-pos umum dan jumlah yang menunjukkan sisa uangmu."),
            ("Cara memasukkan tagihan tahunan ke anggaran bulanan", "Asuransi, pajak kendaraan, dan iuran tahunan: dua cara agar tidak ada bulan yang tiba-tiba bikin kantong kering."),
            ("Aplikasi anggaran tanpa koneksi bank dan tanpa registrasi", "Apa yang kamu dapat, apa yang kamu lepas, dan cara memeriksa aplikasi sebelum memasangnya."),
            ("Mengatur anggaran dari gajian ke gajian", "Gajian tanggal 15 atau 28? Samakan bulan anggaranmu dengan tanggal gajian."),
            ("Uang sisa di akhir bulan – atau malah kurang?", "Bawa ke bulan depan, tabung, atau mulai dari nol: apa yang sebaiknya dilakukan dengan sisanya, dan apa yang membantu kalau kebablasan."),
            ("Cara mencatat pengeluaran dan tetap konsisten: 7 tips", "Kenapa kebanyakan orang menyerah setelah dua minggu – dan cara agar bertahan."),
        ],
        "faq": [
            ["Berapa harga aplikasinya?",
             ["Gratis digunakan. Setelah beberapa hari dan setelah kamu membuat catatan pertama, muncul banner iklan kecil. Pembelian sekali bayar “Hapus iklan” menghilangkannya selamanya; tidak ada langganan."]],
            ["Apakah saya perlu akun atau data bank?",
             ["Tidak. Tidak ada login dan tidak ada koneksi ke bank. Kamu sendiri yang mencatat pemasukan, biaya tetap, dan pengeluaran, dan semuanya tetap di HP-mu."]],
            ["Apakah setiap pengeluaran harus diberi kategori?",
             ["Tidak. Hanya nominal yang wajib. Kategori, keterangan, dan catatan bersifat opsional. Saat kamu mengetik keterangan, aplikasi menyarankan kategori yang cocok – dipelajari dari catatanmu sendiri, hanya di perangkat, dan bisa dimatikan."]],
            ["Bisakah saya memakai aplikasi di dua HP?",
             ["Tidak. Karena tidak ada cloud dan tidak ada server, aplikasi tidak menyinkronkan data antarperangkat. Itulah harga yang dibayar agar angka-angkamu tidak pernah keluar dari HP-mu."]],
            ["Apa yang terjadi dengan uang sisa di akhir bulan?",
             ["Kamu yang menentukan di pengaturan: “Bawa sisa” memindahkan sisa uang ke bulan berikutnya, “Bawa kekurangan” memotong kekurangan di bulan berikutnya. Masing-masing bisa dinyalakan atau dimatikan sendiri-sendiri."]],
            ["Apakah ada versi untuk iPhone?",
             ["Tidak. Anggaran Rumah Tangga Simpel dari Nice Developments hanya tersedia untuk Android, di Google Play."]],
        ],
        "final_h2": "Tahu sisa uangmu. Tanpa repot.",
        "final_body": "Satu angka, satu batang, dua ketukan per pengeluaran. Untuk Android.",
    },

    "guides": [],
}
