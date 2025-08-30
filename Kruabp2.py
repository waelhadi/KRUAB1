# -*- coding: utf-8 -*-
# ⚠️ واجهة تحذير ملوّنة — "فِكْرَك يا إبني؟ تحوّل الأداة حماية API دائمة؟ ما إلها حل؟"
# لا يحتاج لأي مكتبات خارجية. يعمل بألوان وتأثير غليتش وشريط تقدم.

import os, sys, time, random, shutil

# ===== إعداد ألوان ANSI (مع دعم TrueColor عند الإمكان) =====
RESET = "\033[0m"
BOLD  = "\033[1m"
DIM   = "\033[2m"
ITAL  = "\033[3m"

def rgb(r, g, b):
    return f"\033[38;2;{r};{g};{b}m"

def gradient_text(text, start=(255,0,80), end=(120,0,255)):
    """يطبّق تدرّج لوني على النص كاملاً."""
    if not text:
        return ""
    R1,G1,B1 = start
    R2,G2,B2 = end
    out = []
    n = max(1, len(text)-1)
    for i, ch in enumerate(text):
        t = i/float(n) if n>0 else 0
        r = int(R1 + (R2-R1)*t)
        g = int(G1 + (G2-G1)*t)
        b = int(B1 + (B2-B1)*t)
        out.append(rgb(r,g,b) + ch)
    return "".join(out) + RESET

def colorize(c, text):
    return c + text + RESET

RED  = rgb(255,40,70)
PURP = rgb(180,0,255)
CYAN = rgb(0,220,255)
YELL = rgb(255,190,0)
GREEN= rgb(0,220,120)
GRAY = rgb(140,140,160)

# ===== أدوات عرض =====
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def center(text):
    width = shutil.get_terminal_size((80, 20)).columns
    lines = text.splitlines()
    return "\n".join(line.center(width) for line in lines)

def slow_print(line, delay=0.005):
    for ch in line:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n"); sys.stdout.flush()

def glitch_line(base, cycles=12, per_char=0.002):
    """يعرض سطر مع تأثير غليتش عابر."""
    charset = "░▒▓█/\\|*#@&%$?!<>-_=+"
    for _ in range(cycles):
        glitched = []
        for ch in base:
            if ch.strip() and random.random() < 0.12:
                glitched.append(random.choice(charset))
            else:
                glitched.append(ch)
        sys.stdout.write("\r" + "".join(glitched))
        sys.stdout.flush()
        time.sleep(per_char * max(1, len(base)))
    sys.stdout.write("\r" + base + "\n")
    sys.stdout.flush()

def progress_bar(label, total=32, speed=(0.01, 0.04), fail_at=None, mark="█"):
    width = shutil.get_terminal_size((80, 20)).columns
    bar_len = max(20, min(50, width - len(label) - 18))
    sys.stdout.write(center(colorize(CYAN, f"{label}")) + "\n")
    filled = 0
    status = ""
    for i in range(total+1):
        filled = int(bar_len * (i/total))
        bar = mark * filled + GRAY + "░"*(bar_len-filled) + RESET
        pct = f"{int((i/total)*100):3d}%"
        sys.stdout.write("\r" + center(f"[{bar}] {pct} {status}"))
        sys.stdout.flush()
        if fail_at is not None and i == fail_at:
            status = colorize(RED, "✖ فشل")
            time.sleep(0.5)
            break
        time.sleep(random.uniform(*speed))
    if fail_at is None:
        status = colorize(GREEN, "✔ تم")
        sys.stdout.write("\r" + center(f"[{mark*bar_len}] 100% {status}\n"))
    else:
        sys.stdout.write("\n")
    sys.stdout.flush()

# ===== محتوى العرض =====
header = """
███████╗██╗  ██╗██╗  ██╗██████╗  █████╗  ██████╗ ███████╗
██╔════╝╚██╗██╔╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝ ██╔════╝
█████╗   ╚███╔╝  ╚███╔╝ ██████╔╝███████║██║  ███╗█████╗  
██╔══╝   ██╔██╗  ██╔██╗ ██╔══██╗██╔══██║██║   ██║██╔══╝  
███████╗██╔╝ ██╗██╔╝ ██╗██║  ██║██║  ██║╚██████╔╝███████╗
╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝
""".strip("\n")

shield = r"""
      .-----.
     /       \
    |  (•) (•)|
    |    ^    |   ⛨
    |  \___/  |
     \  ---  /
      '-----'
""".rstrip()

lines = [
    "فِكْرَك يا إبني؟",
    "تحوّل الأداة حماية API دائمة؟",
    "ما إلها حل؟"
]

checks = [
    ("تهيئة البيئة", True),
    ("فحص التوقيع X-Gorgon", False),
    ("فحص الطابع X-Khronos", False),
    ("طبقة Anti-Bot", False),
    ("محاكاة الجهاز", True),
    ("مزامنة الوقت", True),
    ("تحليل التشفير", False)
]

# ===== تشغيل العرض =====
def main():
    clear()
    # رأس ملوّن مع تدرّج
    slow_print(center(BOLD + gradient_text("⚠ نظام التحذير المتقدم — API Protection", (255,0,60), (120,0,255)) + RESET), 0.002)
    print()
    for h in header.splitlines():
        print(center(gradient_text(h, (255, 0, 80), (120, 0, 255))))
        time.sleep(0.015)

    print()
    for s in lines:
        glitch_line(center(BOLD + gradient_text(s, (255,80,0), (255,0,180)) + RESET), cycles=10, per_char=0.0015)
        time.sleep(0.15)

    print()
    print(center(PURP + shield + RESET))
    print(center(DIM + "— طبقة حماية API: مُفعّلة • وضع القفل: دائم —" + RESET))
    print()

    # مسارات الفحص
    for i, (label, ok) in enumerate(checks, 1):
        if ok:
            progress_bar(f"[{i}/{len(checks)}] {label}", total=random.randint(24,36))
            slow_print(center(colorize(GREEN, "نتيجة: نجاح ✅")), 0.0015)
        else:
            # افشل بشكل “مخيف”
            progress_bar(f"[{i}/{len(checks)}] {label}", total=32, fail_at=random.randint(10, 24))
            slow_print(center(colorize(RED, "نتيجة: فشل ✖")), 0.0015)
        print()

    # خلاصة
    title = "تقرير نهائي"
    slow_print(center(BOLD + gradient_text(title, (255,120,0), (255,0,140)) + RESET), 0.002)
    print(center("حالة النظام: " + colorize(RED, "مُؤمَّن بالكامل • قفل دائم")))
    print(center("المسار البديل: " + colorize(YELL, "إعادة تصميم المنطق — لا يوجد حل سحري")))
    print(center("نصيحة: " + colorize(CYAN, "العب داخل القواعد • راقب الحدود • حدّث تواقيعك القانونيّة")))
    print()

    # شريط إنهاء
    progress_bar("إنهاء الجلسة بأمان", total=20)
    print(center(GRAY + ITAL + "تم الإغلاق. اضغط Enter للخروج..." + RESET))
    try:
        input()
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()
