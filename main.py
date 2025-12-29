from datetime import datetime

# =====================
# CLASS PASIEN
# =====================
class Pasien:
    def __init__(self, nama, nik, alamat, no_telp, tgl_lahir):
        self.id_pasien = f"PSN{nik[-4:]}"
        self.nama = nama
        self.nik = nik
        self.alamat = alamat
        self.no_telp = no_telp
        self.tgl_lahir = tgl_lahir

    def tampilkan_info(self):
        return f"{self.id_pasien} - {self.nama}"


# =====================
# CLASS DOKTER
# =====================
class Dokter:
    def __init__(self, nama, spesialis, no_izin):
        self.id_dokter = f"DR{no_izin[-3:]}"
        self.nama = nama
        self.spesialis = spesialis
        self.no_izin = no_izin

    def tampilkan_info(self):
        return f"{self.id_dokter} - {self.nama} ({self.spesialis})"


# =====================
# CLASS JADWAL DOKTER
# =====================
class JadwalDokter:
    def __init__(self, dokter, hari, jam_mulai, jam_selesai):
        self.dokter = dokter
        self.hari = hari
        self.jam_mulai = jam_mulai
        self.jam_selesai = jam_selesai

    def tampilkan_jadwal(self):
        return f"{self.dokter.nama} - {self.hari} {self.jam_mulai}-{self.jam_selesai}"


# =====================
# CLASS PEMERIKSAAN
# =====================
class Pemeriksaan:
    def __init__(self, pasien, jadwal):
        self.pasien = pasien
        self.jadwal = jadwal
        self.nomor_antrian = f"A-{datetime.now().strftime('%H%M%S')}"
        self.diagnosa = ""
        self.resep = ""

    def isi_hasil_pemeriksaan(self, diagnosa, resep):
        self.diagnosa = diagnosa
        self.resep = resep

    def tampilkan_info(self):
        return f"Antrian: {self.nomor_antrian} | Pasien: {self.pasien.nama} | Dokter: {self.jadwal.dokter.nama}"


# =====================
# CLASS PEMBAYARAN
# =====================
class Pembayaran:
    def __init__(self, pemeriksaan, biaya_konsultasi=50000, biaya_tindakan=0):
        self.pemeriksaan = pemeriksaan
        self.biaya_konsultasi = biaya_konsultasi
        self.biaya_tindakan = biaya_tindakan
        self.total = self.hitung_total()
        self.tanggal = datetime.now().strftime('%d-%m-%Y')

    def hitung_total(self):
        return self.biaya_konsultasi + self.biaya_tindakan

    def struk(self):
        return f"""
        ===== STRUK PEMBAYARAN =====
        Tanggal: {self.tanggal}
        Pasien: {self.pemeriksaan.pasien.nama}
        Dokter: {self.pemeriksaan.jadwal.dokter.nama}
        Biaya Konsultasi: Rp{self.biaya_konsultasi}
        Biaya Tindakan: Rp{self.biaya_tindakan}
        TOTAL: Rp{self.total}
        """


# =====================
# CLASS REKAM MEDIS
# =====================
class RekamMedis:
    def __init__(self, pemeriksaan):
        self.pemeriksaan = pemeriksaan
        self.tanggal = datetime.now().strftime('%d-%m-%Y')

    def cetak(self):
        return f"""
        ===== REKAM MEDIS =====
        Tanggal: {self.tanggal}
        Pasien: {self.pemeriksaan.pasien.nama}
        Dokter: {self.pemeriksaan.jadwal.dokter.nama}
        Diagnosa: {self.pemeriksaan.diagnosa}
        Resep: {self.pemeriksaan.resep}
        """


# =====================
# DEMO / SIMULASI
# =====================
if __name__ == "__main__":
    # Registrasi Pasien & Dokter
    pasien1 = Pasien("Budi", "3509091234567890", "Jl. Melati", "082134567890", "1990-01-01")
    dokter1 = Dokter("dr. Siti", "Umum", "123456789")

    # Jadwal Praktik
    jadwal1 = JadwalDokter(dokter1, "Senin", "08:00", "12:00")

    # Pendaftaran Pemeriksaan
    periksa1 = Pemeriksaan(pasien1, jadwal1)
    periksa1.isi_hasil_pemeriksaan("Demam", "Paracetamol 3x1")

    # Pembayaran
    bayar1 = Pembayaran(periksa1, biaya_konsultasi=50000, biaya_tindakan=25000)

    # Rekam Medis
    rekam1 = RekamMedis(periksa1)

    # Output
    print(periksa1.tampilkan_info())
    print(bayar1.struk())
    print(rekam1.cetak())
