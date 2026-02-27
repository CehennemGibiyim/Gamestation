"""
Lüx Mallar & Kraliyet Oyuncakları — Kar Hesaplama Paneli
Tkinter GUI | Python 3.x | 18 Tema + Borderless
"""

import tkinter as tk
from tkinter import messagebox
import json, os, math

SETTINGS_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "lux_settings.json")

DEFAULT_SETTINGS = {
    "alis_vergi": 2.0, "alis_komisyon": 0.5,
    "satis_vergi": 2.0, "satis_komisyon": 0.5,
    "kdv": 0.0, "tema": 0,
}

DEFAULT_ITEMS = [
    # (kategori, tier, oyun_ici_fiyat, vergi_kesilmis_net, alis_fiyati, adet)
    ("Lux Mallar",           "T4", 960,    820,    920,    48000),
    ("Lux Mallar",           "T5", 4800,   4683,   4100,   48000),
    ("Lux Mallar",           "T6", 24000,  23415,  23100,  48000),
    ("Kraliyet Oyuncaklari", "T6", 9600,   9366,   9200,   48000),
    ("Kraliyet Oyuncaklari", "T7", 48000,  46830,  41000,  48000),
    ("Kraliyet Oyuncaklari", "T8", 240000, 234150, 231000, 48000),
]

THEMES = [
    {"name": "Midnight Obsidian",  "swatch": ["#0D1117","#58A6FF","#E3B341"],
     "bg":"#0D1117","bg2":"#161B22","bg3":"#21262D","accent":"#58A6FF","accent2":"#3FB950",
     "danger":"#F85149","gold":"#E3B341","text":"#E6EDF3","text2":"#8B949E",
     "border":"#30363D","input_bg":"#0A0D12","header":"#161B22","sep":"#21262D"},

    {"name": "Neon Tokyo",         "swatch": ["#0A0A0F","#FF2D78","#FFE600"],
     "bg":"#0A0A0F","bg2":"#12121A","bg3":"#1A1A28","accent":"#FF2D78","accent2":"#00FFAA",
     "danger":"#FF6B35","gold":"#FFE600","text":"#F0F0FF","text2":"#7070AA",
     "border":"#2A2A3F","input_bg":"#06060C","header":"#0F0F18","sep":"#1A1A28"},

    {"name": "Arctic Frost",       "swatch": ["#EBF4FF","#2B6CB0","#B7791F"],
     "bg":"#EBF4FF","bg2":"#DBEAFE","bg3":"#BFDBFE","accent":"#2B6CB0","accent2":"#276749",
     "danger":"#C53030","gold":"#B7791F","text":"#1A202C","text2":"#4A5568",
     "border":"#93C5FD","input_bg":"#FFFFFF","header":"#DBEAFE","sep":"#BFDBFE"},

    {"name": "Deep Ocean",         "swatch": ["#04111F","#00B4D8","#FFB703"],
     "bg":"#04111F","bg2":"#071929","bg3":"#0D2137","accent":"#00B4D8","accent2":"#06D6A0",
     "danger":"#EF233C","gold":"#FFB703","text":"#CAF0F8","text2":"#4895EF",
     "border":"#023E8A","input_bg":"#020C15","header":"#051525","sep":"#0D2137"},

    {"name": "Forest Dusk",        "swatch": ["#0B1A10","#52B788","#F4D35E"],
     "bg":"#0B1A10","bg2":"#122219","bg3":"#1A3022","accent":"#52B788","accent2":"#95D5B2",
     "danger":"#D62828","gold":"#F4D35E","text":"#D8F3DC","text2":"#74C69D",
     "border":"#2D6A4F","input_bg":"#060E09","header":"#0D2016","sep":"#1A3022"},

    {"name": "Crimson Dusk",       "swatch": ["#130009","#FF4D6D","#FFCCD5"],
     "bg":"#130009","bg2":"#1E0010","bg3":"#2A0015","accent":"#FF4D6D","accent2":"#FF8FA3",
     "danger":"#FF0A54","gold":"#FFCCD5","text":"#FFF0F3","text2":"#FF8FA3",
     "border":"#590D22","input_bg":"#0D0007","header":"#1A000D","sep":"#2A0015"},

    {"name": "Hacker Terminal",    "swatch": ["#000000","#00FF41","#FFFF00"],
     "bg":"#000000","bg2":"#001100","bg3":"#002200","accent":"#00FF41","accent2":"#39FF14",
     "danger":"#FF0000","gold":"#FFFF00","text":"#00FF41","text2":"#007A1E",
     "border":"#004400","input_bg":"#000800","header":"#000F00","sep":"#002200"},

    {"name": "Rose Gold Luxe",     "swatch": ["#1A0A10","#E8A0BF","#FFD700"],
     "bg":"#1A0A10","bg2":"#251219","bg3":"#321A23","accent":"#E8A0BF","accent2":"#C9184A",
     "danger":"#FF4D6D","gold":"#FFD700","text":"#FFE5EC","text2":"#D4A5B5",
     "border":"#6D2B3D","input_bg":"#120008","header":"#1E0D13","sep":"#321A23"},

    {"name": "Solarized Dark",     "swatch": ["#002B36","#268BD2","#B58900"],
     "bg":"#002B36","bg2":"#073642","bg3":"#0D4654","accent":"#268BD2","accent2":"#2AA198",
     "danger":"#DC322F","gold":"#B58900","text":"#FDF6E3","text2":"#657B83",
     "border":"#586E75","input_bg":"#00212B","header":"#01313D","sep":"#0D4654"},

    {"name": "Purple Haze",        "swatch": ["#0E0018","#BD93F9","#F1FA8C"],
     "bg":"#0E0018","bg2":"#160025","bg3":"#200035","accent":"#BD93F9","accent2":"#8BE9FD",
     "danger":"#FF5555","gold":"#F1FA8C","text":"#F8F8F2","text2":"#6272A4",
     "border":"#44475A","input_bg":"#080010","header":"#120020","sep":"#200035"},

    {"name": "Copper Steam",       "swatch": ["#1A0F00","#CD7F32","#FFD700"],
     "bg":"#1A0F00","bg2":"#261600","bg3":"#331D00","accent":"#CD7F32","accent2":"#B8860B",
     "danger":"#CC3300","gold":"#FFD700","text":"#F5DEB3","text2":"#A0785A",
     "border":"#6B3A2A","input_bg":"#120A00","header":"#1E1200","sep":"#331D00"},

    {"name": "Ice Crystal",        "swatch": ["#EEF5FF","#0066CC","#AA7700"],
     "bg":"#EEF5FF","bg2":"#DCEEFF","bg3":"#C0D8FF","accent":"#0066CC","accent2":"#007755",
     "danger":"#CC0033","gold":"#AA7700","text":"#001133","text2":"#335588",
     "border":"#88AACC","input_bg":"#F5FAFF","header":"#D0E8FF","sep":"#C0D8FF"},

    {"name": "Sunset Vibes",       "swatch": ["#1A0505","#FF6B35","#FFD700"],
     "bg":"#1A0505","bg2":"#250A00","bg3":"#351200","accent":"#FF6B35","accent2":"#FFD166",
     "danger":"#EF233C","gold":"#FFD700","text":"#FFF3E0","text2":"#C07040",
     "border":"#7A3010","input_bg":"#110300","header":"#1E0600","sep":"#351200"},

    {"name": "Cyber Silver",       "swatch": ["#0A0A0A","#C0C0C0","#00FFFF"],
     "bg":"#0A0A0A","bg2":"#141414","bg3":"#1E1E1E","accent":"#C0C0C0","accent2":"#00FFFF",
     "danger":"#FF3333","gold":"#FFD700","text":"#E8E8E8","text2":"#707070",
     "border":"#333333","input_bg":"#050505","header":"#111111","sep":"#1E1E1E"},

    {"name": "Sakura Night",       "swatch": ["#0D0510","#FF85A1","#FFCEF3"],
     "bg":"#0D0510","bg2":"#160A18","bg3":"#1F1022","accent":"#FF85A1","accent2":"#FFC8DD",
     "danger":"#FF3366","gold":"#FFCEF3","text":"#FFF0F8","text2":"#C080A0",
     "border":"#4A1A35","input_bg":"#09030C","header":"#130715","sep":"#1F1022"},

    {"name": "Golden Hour",        "swatch": ["#1A1000","#FFB300","#FF6D00"],
     "bg":"#1A1000","bg2":"#241800","bg3":"#302200","accent":"#FFB300","accent2":"#FF6D00",
     "danger":"#DD2222","gold":"#FFDD00","text":"#FFF8E1","text2":"#A07830",
     "border":"#604010","input_bg":"#110C00","header":"#1C1400","sep":"#302200"},

    {"name": "Teal Matrix",        "swatch": ["#001A1A","#00CED1","#7FFFD4"],
     "bg":"#001A1A","bg2":"#002626","bg3":"#003333","accent":"#00CED1","accent2":"#7FFFD4",
     "danger":"#FF4444","gold":"#ADFF2F","text":"#E0FFFF","text2":"#20B2AA",
     "border":"#006666","input_bg":"#001010","header":"#001F1F","sep":"#003333"},

    {"name": "Lava Lamp",          "swatch": ["#0F0500","#FF4500","#FF8C00"],
     "bg":"#0F0500","bg2":"#190800","bg3":"#250D00","accent":"#FF4500","accent2":"#FF8C00",
     "danger":"#FF0000","gold":"#FFAA00","text":"#FFE8D0","text2":"#AA5520",
     "border":"#552200","input_bg":"#0A0300","header":"#140600","sep":"#250D00"},
]


def fmt(n):
    try:
        return f"{int(round(n)):,}".replace(",", ".")
    except:
        return "?"


def load_settings():
    if os.path.exists(SETTINGS_FILE):
        try:
            with open(SETTINGS_FILE) as f:
                d = json.load(f)
            s = DEFAULT_SETTINGS.copy()
            s.update(d)
            return s
        except:
            pass
    return DEFAULT_SETTINGS.copy()


def save_settings_to_file(s):
    with open(SETTINGS_FILE, "w") as f:
        json.dump(s, f, indent=2)


class LuxApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.settings = load_settings()
        self.current_theme = int(self.settings.get("tema", 0)) % len(THEMES)
        self.T = THEMES[self.current_theme]
        self._maximized = False
        self._prev_geo = None
        self._drag_x = 0
        self._drag_y = 0
        self._tooltip_win = None

        self.overrideredirect(True)
        self.attributes("-alpha", 0.96)
        self.geometry("1300x860")

        self._build_items()
        self._build_ui()
        self._recalc()
        self._center()

    def _center(self):
        self.update_idletasks()
        w = self.winfo_width()
        h = self.winfo_height()
        x = (self.winfo_screenwidth()  - w) // 2
        y = (self.winfo_screenheight() - h) // 2
        self.geometry(f"{w}x{h}+{x}+{y}")

    def _build_items(self):
        self.items = []
        for (kat, tier, oyun_fiyat, net_fiyat, alis, adet) in DEFAULT_ITEMS:
            self.items.append({
                "kat": kat, "tier": tier,
                "oyun_fiyat": tk.DoubleVar(value=oyun_fiyat),
                "net_fiyat":  tk.DoubleVar(value=net_fiyat),
                "alis":       tk.DoubleVar(value=alis),
                "adet":       tk.IntVar(value=adet),
            })

    def _apply_theme(self, idx):
        self.current_theme = idx % len(THEMES)
        self.T = THEMES[self.current_theme]
        self.settings["tema"] = self.current_theme
        for w in self.winfo_children():
            w.destroy()
        self._build_ui()
        self._recalc()

    # ── Tüm UI ──────────────────────────────────────────────────────────────
    def _build_ui(self):
        T = self.T
        self.configure(bg=T["border"])

        # 1px dış kenarlık
        outer = tk.Frame(self, bg=T["border"], padx=1, pady=1)
        outer.pack(fill="both", expand=True)

        inner = tk.Frame(outer, bg=T["bg"])
        inner.pack(fill="both", expand=True)

        self._build_titlebar(inner)
        tk.Frame(inner, bg=T["border"], height=1).pack(fill="x")

        main = tk.Frame(inner, bg=T["bg"])
        main.pack(fill="both", expand=True)

        left = tk.Frame(main, bg=T["bg2"], width=275)
        left.pack(side="left", fill="y")
        left.pack_propagate(False)
        self._build_settings(left)

        tk.Frame(main, bg=T["border"], width=1).pack(side="left", fill="y")

        right = tk.Frame(main, bg=T["bg"])
        right.pack(side="left", fill="both", expand=True)
        self._build_main(right)

    # ── Başlık Çubuğu ────────────────────────────────────────────────────────
    def _build_titlebar(self, parent):
        T = self.T
        tb = tk.Frame(parent, bg=T["header"])
        tb.pack(fill="x")

        for w in [tb]:
            w.bind("<ButtonPress-1>", self._drag_start)
            w.bind("<B1-Motion>",     self._drag_motion)

        # Sol: yıldız + başlık
        lf = tk.Frame(tb, bg=T["header"])
        lf.pack(side="left", padx=(14, 6))
        for w in [lf]:
            w.bind("<ButtonPress-1>", self._drag_start)
            w.bind("<B1-Motion>",     self._drag_motion)

        star_c = tk.Canvas(lf, width=22, height=22, bg=T["header"], highlightthickness=0)
        star_c.pack(side="left", pady=11, padx=(0, 8))
        self._draw_star(star_c, 11, 11, 9, 5, T["gold"])
        star_c.bind("<ButtonPress-1>", self._drag_start)
        star_c.bind("<B1-Motion>",     self._drag_motion)

        title_l = tk.Label(lf, text="LUX MALLAR  KAR HESAPLAMA PANELI",
                           font=("Consolas", 11, "bold"),
                           bg=T["header"], fg=T["gold"])
        title_l.pack(side="left", pady=11)
        title_l.bind("<ButtonPress-1>", self._drag_start)
        title_l.bind("<B1-Motion>",     self._drag_motion)

        # Sağ kısım
        rf = tk.Frame(tb, bg=T["header"])
        rf.pack(side="right", padx=(0, 10))

        # Pencere butonları (kapat/küçült/büyüt)
        def win_btn(color, cmd, hover):
            c = tk.Canvas(rf, width=14, height=14, bg=T["header"],
                          highlightthickness=0, cursor="hand2")
            c.pack(side="right", padx=3, pady=13)
            c.create_oval(1, 1, 13, 13, fill=color, outline="", tags="dot")
            c.bind("<Button-1>", lambda e: cmd())
            c.bind("<Enter>",  lambda e, hc=hover: (c.delete("all"), c.create_oval(1,1,13,13,fill=hc,outline="")))
            c.bind("<Leave>",  lambda e, oc=color: (c.delete("all"), c.create_oval(1,1,13,13,fill=oc,outline="")))
            return c

        win_btn("#F85149", self.destroy,         "#FF7B72")
        win_btn("#E3B341", self._minimize,        "#FFD060")
        win_btn("#3FB950", self._toggle_maximize, "#56D364")

        # Ayırıcı
        tk.Frame(rf, bg=T["border"], width=1).pack(side="right", fill="y", pady=8, padx=8)

        # Versiyon
        tk.Label(rf, text="v2.0  Python GUI",
                 font=("Consolas", 8), bg=T["header"], fg=T["text2"]).pack(
                 side="right", padx=(0, 6), pady=13)

        tk.Frame(rf, bg=T["border"], width=1).pack(side="right", fill="y", pady=8, padx=8)

        # Tema ikonları
        dots_f = tk.Frame(tb, bg=T["header"])
        dots_f.pack(side="right", padx=(0, 4))
        dots_f.bind("<ButtonPress-1>", self._drag_start)
        dots_f.bind("<B1-Motion>",     self._drag_motion)

        self.theme_dots = []
        for i, th in enumerate(THEMES):
            c = tk.Canvas(dots_f, width=22, height=22,
                          bg=T["header"], highlightthickness=0, cursor="hand2")
            c.pack(side="left", padx=2, pady=11)
            self._draw_dot(c, th, selected=(i == self.current_theme), bg=T["header"])
            c.bind("<Button-1>", lambda e, idx=i: self._apply_theme(idx))
            c.bind("<Enter>",  lambda e, cn=c, th_=th, idx=i: self._dot_enter(cn, th_, idx))
            c.bind("<Leave>",  lambda e, cn=c, th_=th, idx=i: self._dot_leave(cn, th_, idx))
            self.theme_dots.append(c)

    def _draw_dot(self, canvas, th, selected=False, bg="#161B22"):
        colors = th["swatch"]
        canvas.delete("all")
        cx, cy, r = 11, 11, 9
        # 3 dilim
        canvas.create_arc(cx-r, cy-r, cx+r, cy+r, start=90,  extent=120, fill=colors[0], outline="")
        canvas.create_arc(cx-r, cy-r, cx+r, cy+r, start=210, extent=120, fill=colors[1], outline="")
        canvas.create_arc(cx-r, cy-r, cx+r, cy+r, start=330, extent=120, fill=colors[2], outline="")
        # Kenarlık
        border_c = "#FFFFFF" if selected else th["border"]
        width    = 2 if selected else 1
        canvas.create_oval(cx-r-1, cy-r-1, cx+r+1, cy+r+1, outline=border_c, width=width)

    def _dot_enter(self, canvas, th, idx):
        self._draw_dot(canvas, th, selected=True, bg=self.T["header"])
        # Tooltip
        self._hide_tooltip()
        x = canvas.winfo_rootx() + 11
        y = canvas.winfo_rooty() + 30
        self._tooltip_win = tk.Toplevel(self)
        self._tooltip_win.overrideredirect(True)
        self._tooltip_win.geometry(f"+{x}+{y}")
        T = self.T
        f = tk.Frame(self._tooltip_win, bg=T["bg3"],
                     highlightthickness=1, highlightbackground=T["border"])
        f.pack()
        tk.Label(f, text=th["name"], font=("Consolas", 8),
                 bg=T["bg3"], fg=T["text"], padx=8, pady=3).pack()

    def _dot_leave(self, canvas, th, idx):
        self._draw_dot(canvas, th, selected=(idx == self.current_theme), bg=self.T["header"])
        self._hide_tooltip()

    def _hide_tooltip(self):
        if self._tooltip_win:
            try:
                self._tooltip_win.destroy()
            except:
                pass
            self._tooltip_win = None

    def _draw_star(self, canvas, cx, cy, r_outer, r_inner, color):
        pts = []
        for i in range(10):
            a = math.radians(i * 36 - 90)
            r = r_outer if i % 2 == 0 else r_inner
            pts += [cx + r * math.cos(a), cy + r * math.sin(a)]
        canvas.create_polygon(pts, fill=color, outline="")

    def _drag_start(self, e):
        self._drag_x = e.x_root - self.winfo_x()
        self._drag_y = e.y_root - self.winfo_y()

    def _drag_motion(self, e):
        if not self._maximized:
            self.geometry(f"+{e.x_root - self._drag_x}+{e.y_root - self._drag_y}")

    def _minimize(self):
        self.overrideredirect(False)
        self.iconify()
        self.bind("<Map>", lambda e: self._restore_bl())

    def _restore_bl(self):
        self.overrideredirect(True)
        self.unbind("<Map>")

    def _toggle_maximize(self):
        if self._maximized:
            self.geometry(self._prev_geo)
            self._maximized = False
        else:
            self._prev_geo = self.geometry()
            sw = self.winfo_screenwidth()
            sh = self.winfo_screenheight()
            self.geometry(f"{sw}x{sh}+0+0")
            self._maximized = True

    # ── Ayarlar Paneli ───────────────────────────────────────────────────────
    def _build_settings(self, parent):
        T = self.T

        def sec(text, color=None):
            c = color or T["accent"]
            tk.Label(parent, text=text, font=("Consolas", 9, "bold"),
                     bg=T["bg2"], fg=c, anchor="w").pack(fill="x", padx=14, pady=(12, 0))
            tk.Frame(parent, bg=c, height=1).pack(fill="x", padx=14, pady=(2, 5))

        def row_field(lbl_txt, var):
            row = tk.Frame(parent, bg=T["bg2"])
            row.pack(fill="x", padx=14, pady=2)
            tk.Label(row, text=lbl_txt, font=("Consolas", 8),
                     bg=T["bg2"], fg=T["text2"], width=22, anchor="w").pack(side="left")
            e = tk.Entry(row, textvariable=var, font=("Consolas", 9),
                         bg=T["input_bg"], fg=T["accent"],
                         insertbackground=T["accent"], relief="flat",
                         bd=0, width=8, justify="right",
                         highlightthickness=1,
                         highlightbackground=T["border"],
                         highlightcolor=T["accent"])
            e.pack(side="left", ipady=4, ipadx=4)
            tk.Label(row, text="%", font=("Consolas", 8),
                     bg=T["bg2"], fg=T["text2"]).pack(side="left", padx=3)
            e.bind("<FocusOut>", lambda ev: self._recalc())
            e.bind("<Return>",   lambda ev: self._recalc())
            return e

        tk.Label(parent, text="  AYARLAR",
                 font=("Consolas", 12, "bold"),
                 bg=T["bg2"], fg=T["gold"]).pack(anchor="w", padx=14, pady=(14, 2))
        tk.Frame(parent, bg=T["gold"], height=2).pack(fill="x", padx=14, pady=(0, 4))

        self._sv = {}
        sec("ALIS VERGILERI")
        for key, lbl_txt in [("alis_vergi", "Alis Genel Vergi"),
                              ("alis_komisyon", "Alis Komisyon/Ek")]:
            v = tk.StringVar(value=str(self.settings[key]))
            row_field(lbl_txt, v)
            v.trace_add("write", lambda *a, k=key, vv=v: self._sv_changed(k, vv))
            self._sv[key] = v

        sec("SATIS VERGILERI")
        for key, lbl_txt in [("satis_vergi", "Satis Genel Vergi"),
                              ("satis_komisyon", "Satis Komisyon/Ek"),
                              ("kdv", "KDV / Diger")]:
            v = tk.StringVar(value=str(self.settings[key]))
            row_field(lbl_txt, v)
            v.trace_add("write", lambda *a, k=key, vv=v: self._sv_changed(k, vv))
            self._sv[key] = v

        sec("VERGI OZETI", T["accent2"])
        self.lbl_buy_rate  = tk.Label(parent, text="", font=("Consolas", 8),
                                      bg=T["bg2"], fg=T["accent2"], anchor="w")
        self.lbl_buy_rate.pack(fill="x", padx=14, pady=1)
        self.lbl_sell_rate = tk.Label(parent, text="", font=("Consolas", 8),
                                      bg=T["bg2"], fg=T["accent2"], anchor="w")
        self.lbl_sell_rate.pack(fill="x", padx=14, pady=1)

        tk.Frame(parent, bg=T["border"], height=1).pack(fill="x", padx=14, pady=10)

        save_btn = tk.Button(parent, text="  Ayarlari Kaydet",
                             font=("Consolas", 9, "bold"),
                             bg=T["accent"], fg=T["bg"],
                             activebackground=T["gold"], activeforeground=T["bg"],
                             relief="flat", bd=0, pady=8, cursor="hand2",
                             command=self._save_settings)
        save_btn.pack(fill="x", padx=14)

        tk.Frame(parent, bg=T["border"], height=1).pack(fill="x", padx=14, pady=10)
        sec("FORMUL")
        formul = (
            "Alis Maliyeti =\n"
            "  alis_fiyat x adet\n"
            "  x (1 + alis% + kom%)\n\n"
            "Net Satis =\n"
            "  son_fiyat x adet\n"
            "  x (1 - satis% - kom%\n"
            "       - kdv%)\n\n"
            "Kazanc = Net Satis\n"
            "       - Alis Maliyeti"
        )
        tk.Label(parent, text=formul, font=("Consolas", 8),
                 bg=T["bg2"], fg=T["text2"],
                 justify="left", anchor="w").pack(fill="x", padx=14)

    # ── Ana Panel ────────────────────────────────────────────────────────────
    def _build_main(self, parent):
        T = self.T

        hdr = tk.Frame(parent, bg=T["bg3"], pady=5)
        hdr.pack(fill="x")
        cols = [
            ("KATEGORI / TIER", 18, "w"),
            ("OYUN ICI FIYAT",   13, "e"),
            ("VERGISIZ NET",     13, "e"),
            ("ALIS FIYATI",      11, "e"),
            ("ADET",              9, "e"),
            ("ALIS MALIYETI",    14, "e"),
            ("NET SATIS",        14, "e"),
            ("NET KAZANC",       14, "e"),
            ("",                  3, "c"),
        ]
        for txt, w, anc in cols:
            tk.Label(hdr, text=txt, font=("Consolas", 8, "bold"),
                     bg=T["bg3"], fg=T["text2"],
                     width=w, anchor=anc).pack(side="left", padx=4)

        tk.Frame(parent, bg=T["border"], height=1).pack(fill="x")

        wrap = tk.Frame(parent, bg=T["bg"])
        wrap.pack(fill="both", expand=True)

        canvas = tk.Canvas(wrap, bg=T["bg"], highlightthickness=0)
        sb = tk.Scrollbar(wrap, orient="vertical", command=canvas.yview)
        self._rows_frame = tk.Frame(canvas, bg=T["bg"])
        self._rows_frame.bind("<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=self._rows_frame, anchor="nw")
        canvas.configure(yscrollcommand=sb.set)
        canvas.pack(side="left", fill="both", expand=True)
        sb.pack(side="right", fill="y")
        canvas.bind_all("<MouseWheel>",
            lambda e: canvas.yview_scroll(-1 if e.delta > 0 else 1, "units"))

        self._build_rows()

        tk.Frame(parent, bg=T["gold"], height=2).pack(fill="x")
        sum_f = tk.Frame(parent, bg=T["bg3"], padx=14, pady=10)
        sum_f.pack(fill="x")
        self._build_summary(sum_f)

    def _build_rows(self):
        T = self.T
        for w in self._rows_frame.winfo_children():
            w.destroy()
        self.row_widgets = []

        for idx, item in enumerate(self.items):
            # Her satirin ustunde kategori + tier baslik bandi
            hdr_band = tk.Frame(self._rows_frame, bg=T["bg3"])
            hdr_band.pack(fill="x", pady=(8, 0))
            left_hdr = tk.Frame(hdr_band, bg=T["bg3"])
            left_hdr.pack(side="left", fill="x", expand=True)
            tk.Label(left_hdr,
                     text=f"   {item['kat'].upper()}  ▸  {item['tier']}",
                     font=("Consolas", 9, "bold"),
                     bg=T["bg3"], fg=T["gold"],
                     pady=3, anchor="w").pack(side="left", padx=8)
            tk.Frame(hdr_band, bg=T["gold"], height=1).pack(fill="x", padx=8, pady=(0,0))

            bg_r = T["bg2"] if idx % 2 == 0 else T["bg"]
            row_f = tk.Frame(self._rows_frame, bg=bg_r)
            row_f.pack(fill="x")
            ww = {}

            # Sadece tier goster solda
            tk.Label(row_f,
                     text=f"  {item['tier']}",
                     font=("Consolas", 11, "bold"),
                     bg=bg_r, fg=T["accent"],
                     width=18, anchor="w").pack(side="left", padx=4, pady=7)

            for key, var, w_s in [("oyun_fiyat", item["oyun_fiyat"], 13), ("net_fiyat", item["net_fiyat"], 13),
                                   ("alis", item["alis"], 11), ("adet", item["adet"], 9)]:
                e = tk.Entry(row_f, textvariable=var, font=("Consolas", 9),
                             bg=T["input_bg"], fg=T["accent"],
                             insertbackground=T["accent"],
                             relief="flat", bd=0, width=w_s, justify="right",
                             highlightthickness=1,
                             highlightbackground=T["border"],
                             highlightcolor=T["accent"])
                e.pack(side="left", padx=4, pady=7, ipady=4)
                e.bind("<FocusOut>", lambda ev: self._recalc())
                e.bind("<Return>",   lambda ev: self._recalc())
                ww[key] = e

            for key, w_s, fg_c in [("maliyet", 14, T["text"]),
                                    ("net_satis", 14, T["text"]),
                                    ("kazanc", 14, T["accent2"])]:
                lbl = tk.Label(row_f, text="--", font=("Consolas", 9, "bold"),
                               bg=bg_r, fg=fg_c, width=w_s, anchor="e")
                lbl.pack(side="left", padx=4, pady=7)
                ww[key] = lbl

            det_btn = tk.Button(row_f, text="v",
                                font=("Consolas", 8),
                                bg=T["bg3"], fg=T["text2"],
                                relief="flat", bd=0, cursor="hand2", padx=4,
                                command=lambda i=idx: self._toggle_detail(i))
            det_btn.pack(side="left", padx=4)
            ww["det_btn"] = det_btn

            det_f = tk.Frame(self._rows_frame, bg=T["sep"], pady=4)
            ww["det_frame"]   = det_f
            ww["det_visible"] = False
            ww["bg_r"]        = bg_r

            self.row_widgets.append(ww)

    def _toggle_detail(self, idx):
        ww = self.row_widgets[idx]
        if ww["det_visible"]:
            ww["det_frame"].pack_forget()
            ww["det_btn"].config(text="v")
            ww["det_visible"] = False
        else:
            ww["det_frame"].pack(fill="x")
            ww["det_btn"].config(text="^")
            ww["det_visible"] = True

    def _build_summary(self, parent):
        T = self.T
        top = tk.Frame(parent, bg=T["bg3"])
        top.pack(fill="x")

        self.lbl_sum_maliyet   = self._sum_box(top, "TOPLAM MALIYET",   T["danger"])
        self.lbl_sum_net_satis = self._sum_box(top, "TOPLAM NET SATIS", T["accent"])
        self.lbl_sum_kazanc    = self._sum_box(top, "NET TOPLAM KAZANC",T["gold"], big=True)

        cat_row = tk.Frame(parent, bg=T["bg3"])
        cat_row.pack(fill="x", pady=(8, 0))
        self.lbl_kat = {}
        for kat in ["Lux Mallar", "Kraliyet Oyuncaklari"]:
            box = tk.Frame(cat_row, bg=T["bg2"], padx=12, pady=8)
            box.pack(side="left", padx=(0, 8))
            tk.Label(box, text=kat, font=("Consolas", 8),
                     bg=T["bg2"], fg=T["text2"]).pack(anchor="w")
            lbl = tk.Label(box, text="--",
                           font=("Consolas", 10, "bold"),
                           bg=T["bg2"], fg=T["accent2"])
            lbl.pack(anchor="w")
            self.lbl_kat[kat] = lbl

    def _sum_box(self, parent, title, color, big=False):
        T = self.T
        box = tk.Frame(parent, bg=T["bg2"], padx=14, pady=10)
        box.pack(side="left", padx=(0, 10))
        tk.Label(box, text=title, font=("Consolas", 8),
                 bg=T["bg2"], fg=T["text2"]).pack(anchor="w")
        font = ("Consolas", 14, "bold") if big else ("Consolas", 11, "bold")
        lbl = tk.Label(box, text="--", font=font, bg=T["bg2"], fg=color)
        lbl.pack(anchor="w")
        return lbl

    # ── Hesaplama ────────────────────────────────────────────────────────────
    def _get_rates(self):
        def pct(k):
            try:
                return float(self._sv[k].get()) / 100.0
            except:
                return self.settings.get(k, 0) / 100.0
        return (pct("alis_vergi") + pct("alis_komisyon"),
                pct("satis_vergi") + pct("satis_komisyon") + pct("kdv"))

    def _recalc(self):
        T = self.T
        r_buy, r_sell = self._get_rates()

        self.lbl_buy_rate.config(text=f"Toplam Alis  : %{r_buy*100:.2f}")
        self.lbl_sell_rate.config(text=f"Toplam Satis : %{r_sell*100:.2f}")

        totals = {"maliyet": 0.0, "net_satis": 0.0, "kazanc": 0.0}
        kat_k  = {"Lux Mallar": 0.0, "Kraliyet Oyuncaklari": 0.0}

        for idx, item in enumerate(self.items):
            try:
                oyun_fiyat = float(item["oyun_fiyat"].get())
                net_fiyat  = float(item["net_fiyat"].get())
                alis = float(item["alis"].get())
                adet = int(item["adet"].get())
            except:
                continue

            maliyet        = alis * adet * (1 + r_buy)
            net_satis      = net_fiyat * adet
            kazanc         = net_satis - maliyet
            alis_ham       = alis * adet
            alis_vergi_tl  = alis_ham * r_buy
            satis_ham      = oyun_fiyat * adet
            satis_vergi_tl = satis_ham * r_sell

            ww = self.row_widgets[idx]
            ww["maliyet"].config(text=fmt(maliyet) + " TL")
            ww["net_satis"].config(text=fmt(net_satis) + " TL")
            kc = T["accent2"] if kazanc >= 0 else T["danger"]
            ww["kazanc"].config(text=fmt(kazanc) + " TL", fg=kc)

            df = ww["det_frame"]
            for ch in df.winfo_children():
                ch.destroy()

            lines = [
                (f"Alis Ham Toplam",              f"{fmt(alis_ham)} TL",        T["text"]),
                (f"  + Alis Vergi+Kom (%{r_buy*100:.2f})", f"+ {fmt(alis_vergi_tl)} TL", T["danger"]),
                (f"  = Toplam Alis Maliyeti",     f"  {fmt(maliyet)} TL",       T["text"]),
                ("",                              "",                            T["text"]),
                (f"Oyun Ici Fiyat Toplam",        f"{fmt(satis_ham)} TL",       T["text"]),
                (f"  - Satis Vergi+Kom (%{r_sell*100:.2f})", f"- {fmt(satis_vergi_tl)} TL", T["danger"]),
                (f"  = Vergisiz Net Satis",       f"  {fmt(net_satis)} TL",     T["text"]),
                ("",                              "",                            T["text"]),
                ("NET KAZANC",                    f"{fmt(kazanc)} TL",          kc),
            ]
            for dl, dv, dc in lines:
                dr = tk.Frame(df, bg=T["sep"])
                dr.pack(fill="x")
                tk.Label(dr, text=dl, font=("Consolas", 8),
                         bg=T["sep"], fg=T["text2"],
                         width=34, anchor="w").pack(side="left", padx=(22, 0))
                tk.Label(dr, text=dv, font=("Consolas", 8, "bold"),
                         bg=T["sep"], fg=dc,
                         width=22, anchor="e").pack(side="left")

            totals["maliyet"]   += maliyet
            totals["net_satis"] += net_satis
            totals["kazanc"]    += kazanc
            if item["kat"] in kat_k:
                kat_k[item["kat"]] += kazanc

        self.lbl_sum_maliyet.config(text=fmt(totals["maliyet"])   + " TL")
        self.lbl_sum_net_satis.config(text=fmt(totals["net_satis"]) + " TL")
        tc = T["gold"] if totals["kazanc"] >= 0 else T["danger"]
        self.lbl_sum_kazanc.config(text=fmt(totals["kazanc"]) + " TL", fg=tc)
        for kat, lbl in self.lbl_kat.items():
            v = kat_k.get(kat, 0)
            lbl.config(text=fmt(v) + " TL",
                       fg=T["accent2"] if v >= 0 else T["danger"])

    def _sv_changed(self, key, var):
        try:
            self.settings[key] = float(var.get())
        except:
            pass
        self._recalc()

    def _save_settings(self):
        for key, var in self._sv.items():
            try:
                self.settings[key] = float(var.get())
            except:
                pass
        self.settings["tema"] = self.current_theme
        save_settings_to_file(self.settings)
        messagebox.showinfo("Kaydedildi",
                            "Ayarlar basariyla kaydedildi.\nlux_settings.json dosyasina yazildi.")


if __name__ == "__main__":
    app = LuxApp()
    app.mainloop()
