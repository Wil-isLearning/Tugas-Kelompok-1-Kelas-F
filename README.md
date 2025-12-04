A. Judul Program: Nama aplikasi yang jelas.



B. Pendahuluan: Memberikan gambaran umum tentang perangkat lunak dan Penjelasan mengenai apa fungsi program tersebut.



C. Fitur Utama: Daftar fitur yang dimiliki program.



D. Panduan Instalasi: Langkah-langkah untuk mengunduh dan menyiapkan program (misal: git clone, install library). 



E. Panduan Menjalankan: Perintah untuk menjalankan / konfigurasi program (misal: python app.py).



F. Dokumentasi Teknis: Rancangan sistem menggunakan diagram flowchart disertai penjelasan

Flowchart program dalam format mermaid.
```mermaid
flowchart TD
    A[Mulai] --> B[Inisialisasi Display]
    B --> C[Inisialisasi CalculatorLogic]
    C --> D[Inisialisasi ButtonPanel]
    D --> E[Pengguna menekan tombol]

    E --> F{Jenis input?}

    F --> G[Angka atau Titik]
    G --> H[Tambahkan ke ekspresi]
    H --> E

    F --> I[Operator]
    I --> J[Tambahkan operator ke ekspresi]
    J --> E

    F --> K[Tombol C]
    K --> L[Hapus ekspresi]
    L --> E

    F --> M[Tombol √]
    M --> N[Tambah operasi akar ke ekspresi]
    N --> E

    F --> O[Tombol =]
    O --> P[Hitung ekspresi dengan eval]

    P --> Q{Error?}

    Q --> R[Tampilkan Error]
    R --> E

    Q --> S[Tampilkan hasil perhitungan]
    S --> E

    E --> T[Selesai]
```


G. Daftar Kontributor (Tabel): Nama, NIM, Link Agun git masing-masing anggota kelompok yang mengerjakan.

daftar tabel
| Nama Anggota | NIM | Link Akun Github |
|--------------|------|------------------|
| Wilson Doringin (Project Maintainer) | 250211060115 | https://github.com/Wil-isLearning |
| Rey Jeheskiel Tumurang | 250211060071 | https://github.com/rey27-zx |
| Brian Junianto Kabo | 250211060032 | https://github.com/briankabo |

link repository kami
| Link Repository | https://github.com/Wil-isLearning/Tugas-Kelompok-1-Kelas-F |


