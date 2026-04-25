import os

def get_cookies_opts(cookies_file=None):
    if cookies_file and os.path.exists(cookies_file):
        print(f"[Cookies] Usando archivo: {cookies_file}")
        return {"cookiefile": cookies_file}
    
    print("[Cookies] No se encontró cookies.txt. Continuando sin cookies.")
    return {}