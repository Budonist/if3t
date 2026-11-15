"""Lokale Drei-Domain-Vorschau; keine Änderung der Veröffentlichungsdateien."""
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from functools import partial
from threading import Thread
import io

ROOT = Path(__file__).resolve().parents[1] / 'site'
DOMAINS = {'https://www.if3t.de': 'http://127.0.0.1:8000', 'https://sonnenstand-app.if3t.de': 'http://127.0.0.1:8001', 'https://sektoren-app.if3t.de': 'http://127.0.0.1:8002'}

class Handler(SimpleHTTPRequestHandler):
    def send_head(self):
        path = Path(self.translate_path(self.path))
        if path.is_dir():
            path = path / 'index.html'
        if path.is_file() and path.suffix == '.html':
            data = path.read_text()
            for domain, local in DOMAINS.items():
                data = data.replace(domain, local)
            encoded = data.encode()
            self.send_response(200)
            self.send_header('Content-Type', 'text/html; charset=utf-8')
            self.send_header('Content-Length', str(len(encoded)))
            self.end_headers()
            return io.BytesIO(encoded)
        return super().send_head()

if __name__ == '__main__':
    servers = []
    try:
        for port, area in enumerate(['main', 'sonnenstand-app', 'sektoren-app'], 8000):
            server = ThreadingHTTPServer(('127.0.0.1', port), partial(Handler, directory=str(ROOT / area)))
            servers.append(server)
            Thread(target=server.serve_forever, daemon=True).start()
            print(f'{area}: Port {port}', flush=True)
        from threading import Event
        Event().wait()
    except KeyboardInterrupt:
        pass
    finally:
        for server in servers:
            server.shutdown()
            server.server_close()
