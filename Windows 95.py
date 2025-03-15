import tkinter as tk
from tkinter import messagebox, filedialog, colorchooser
import time
import random
import tkinter.font as tkfont

# BootScreen: Boot screen with terminal style message and mobile key button.
# شاشة الإقلاع: واجهة تشبه Terminal مع زر مفتاح للموبايل.
class BootScreen:
    def __init__(self, root, on_finish_callback):
        self.root = root
        self.on_finish_callback = on_finish_callback
        self.window = tk.Toplevel(root)
        self.window.overrideredirect(True)
        self.window.geometry("1024x768")
        self.window.configure(bg="black")
        
        self.finished = False  # Flag to prevent تنفيذ finish أكثر من مرة
        
        # Create a frame to hold text widget and mobile key button
        # إنشاء إطار يحتوي على عنصر النص وزر المفتاح للموبايل
        frame = tk.Frame(self.window, bg="black")
        frame.pack(expand=True, fill="both")
        
        self.text_widget = tk.Text(frame, bg="black", fg="lime", font=("Consolas", 12))
        self.text_widget.pack(expand=True, fill="both")
        self.text_widget.insert(tk.END, "Booting Windows 95 Simulator...\n")
        self.text_widget.insert(tk.END, "Initializing system...\n")
        self.text_widget.insert(tk.END, "Loading drivers...\n")
        self.text_widget.insert(tk.END, "\nPress Enter to continue...\n")
        self.text_widget.config(state="disabled")
        
        # Bind Enter key (for physical keyboards)
        # ربط مفتاح Enter (للوحات المفاتيح)
        self.window.bind("<Return>", self.finish)
        
        # Add a mobile key button to allow mobile users to proceed
        # إضافة زر مفتاح للموبايل للسماح بالدخول عند النقر
        self.mobile_key_button = tk.Button(frame, text="Enter / إدخال", command=self.finish,
                                           font=("Consolas", 12), bg="black", fg="lime", bd=0)
        self.mobile_key_button.pack(side="bottom", pady=10)
        
        # اضف مؤقت 20 ثانية لاستدعاء finish تلقائيًا إذا لم يتم الضغط
        self.timer_id = self.window.after(20000, self.finish)

    def finish(self, event=None):
        if self.finished:
            return
        self.finished = True
        try:
            self.window.after_cancel(self.timer_id)
        except Exception:
            pass
        self.window.destroy()
        self.on_finish_callback()

# LoginScreen: Simple login screen with welcome message.
# شاشة تسجيل الدخول: واجهة تسجيل دخول بسيطة برسالة ترحيب.
class LoginScreen:
    def __init__(self, root, on_login_callback):
        self.root = root
        self.on_login_callback = on_login_callback
        self.window = tk.Toplevel(root)
        self.window.title("Login / تسجيل الدخول")
        self.window.geometry("400x300")
        self.window.configure(bg="lightblue")
        tk.Label(self.window, text="Welcome to Windows 95 Simulator\nمرحباً بكم في محاكاة Windows 95", 
                 font=("Tahoma", 12), bg="lightblue").pack(pady=20)
        tk.Button(self.window, text="Login / تسجيل الدخول", command=self.login, font=("Tahoma", 12)).pack(pady=20)

    def login(self):
        # Close login screen and proceed
        # إغلاق شاشة تسجيل الدخول والمتابعة
        self.window.destroy()
        self.on_login_callback()

# Windows95Simulator: Main simulator window with desktop, taskbar and applications.
# محاكي Windows 95: النافذة الرئيسية التي تحتوي على سطح المكتب وشريط المهام والتطبيقات.
class Windows95Simulator:
    def __init__(self, root):
        self.root = root
        self.root.title("Windows 95 Simulator")
        self.root.geometry("1024x768")
        self.root.resizable(True, True)
        
        # Default language: English
        # اللغة الافتراضية: الإنجليزية
        self.current_lang = 'en'
        self.lang_data = {
            'ar': {
                'start': 'ابدأ',
                'my_computer': 'جهاز الكمبيوتر',
                'recycle_bin': 'سلة المحذوفات',
                'notepad': 'المفكرة',
                'paint': 'الرسام',
                'calculator': 'الآلة الحاسبة',
                'minesweeper': 'كاشف الألغام',
                'control_panel': 'لوحة التحكم',
                'settings': 'إعدادات النظام',
                'programs': 'البرامج',
                'shutdown': 'إيقاف التشغيل',
                'language': 'اللغة',
                'switch_language': 'تبديل اللغة',
                'new': 'جديد',
                'open': 'فتح',
                'save': 'حفظ',
                'exit': 'خروج',
                'switch_to_english': 'التبديل إلى الإنجليزية',
                'switch_to_arabic': 'التبديل إلى العربية',
                'system_settings': 'إعدادات النظام',
                'system_info': 'معلومات النظام',
                'change_desktop_color': 'تغيير لون الخلفية',
                'about': 'حول',
                'word': 'وورد',
                'excel': 'إكسل',
                'bold': 'عريض',
                'italic': 'مائل',
                'underline': 'تحته خط'
            },
            'en': {
                'start': 'Start',
                'my_computer': 'My Computer',
                'recycle_bin': 'Recycle Bin',
                'notepad': 'Notepad',
                'paint': 'Paint',
                'calculator': 'Calculator',
                'minesweeper': 'Minesweeper',
                'control_panel': 'Control Panel',
                'settings': 'Settings',
                'programs': 'Programs',
                'shutdown': 'Shutdown',
                'language': 'Language',
                'switch_language': 'Switch Language',
                'new': 'New',
                'open': 'Open',
                'save': 'Save',
                'exit': 'Exit',
                'switch_to_english': 'Switch to English',
                'switch_to_arabic': 'Switch to Arabic',
                'system_settings': 'System Settings',
                'system_info': 'System Info',
                'change_desktop_color': 'Change Desktop Color',
                'about': 'About',
                'word': 'Word',
                'excel': 'Excel',
                'bold': 'Bold',
                'italic': 'Italic',
                'underline': 'Underline'
            }
        }
        
        # Desktop (Canvas) with Windows 95 style background.
        # سطح المكتب (Canvas) مع خلفية بنمط Windows 95.
        self.desktop = tk.Canvas(self.root, bg='#008080', highlightthickness=0)
        self.desktop.pack(fill='both', expand=True)
        
        self.desktop_icons = {}
        self.create_icons()
        self.create_taskbar()
        
        self.start_menu = None
        self.update_clock()

    def create_icons(self):
        # Function to create desktop icons and store references for language updates.
        # دالة لإنشاء أيقونات سطح المكتب وتخزين المراجع لتحديث اللغة.
        def create_icon(key, x, y, command):
            frame = tk.Frame(self.desktop, bg='#008080')
            frame.place(x=x, y=y)
            btn = tk.Button(frame, text=self.lang_data[self.current_lang][key],
                            command=command, width=12, relief='raised', bg='#C0C0C0')
            btn.pack()
            lbl = tk.Label(frame, text=self.lang_data[self.current_lang][key],
                           bg='#008080', fg='white')
            lbl.pack()
            self.desktop_icons[key] = {'button': btn, 'label': lbl}

        create_icon('my_computer', 50, 50, self.open_my_computer)
        create_icon('recycle_bin', 50, 150, self.open_recycle_bin)
        create_icon('notepad', 50, 250, self.open_notepad)
        create_icon('paint', 50, 350, self.open_paint)
        create_icon('calculator', 50, 450, self.open_calculator)
        create_icon('minesweeper', 50, 550, self.open_minesweeper)
        create_icon('control_panel', 200, 50, self.open_control_panel)
        create_icon('settings', 200, 150, self.open_settings)
        create_icon('word', 200, 250, self.open_word)
        create_icon('excel', 200, 350, self.open_excel)

    def create_taskbar(self):
        # Taskbar creation with Start button, mobile Key button, and clock.
        # إنشاء شريط المهام مع زر Start، وزر Key للموبايل، والساعة.
        self.taskbar = tk.Frame(self.root, bg='gray', height=30)
        self.taskbar.pack(side='bottom', fill='x')
        
        self.start_button = tk.Button(self.taskbar, text=self.lang_data[self.current_lang]['start'],
                                      command=self.toggle_start_menu, bg='#C0C0C0', relief='raised', padx=10, pady=2)
        self.start_button.pack(side='left', padx=5, pady=2)
        
        self.key_button = tk.Button(self.taskbar, text="Key", command=self.open_mobile_keyboard,
                                    bg='black', fg='white', bd=2, relief='raised', highlightbackground='green', padx=10, pady=2)
        self.key_button.pack(side='left', padx=5, pady=2)
        
        self.clock_label = tk.Label(self.taskbar, bg='gray', fg='white', font=("Tahoma", 10))
        self.clock_label.pack(side='right', padx=10)

    def update_clock(self):
        # Update the clock label every second.
        # تحديث الساعة كل ثانية.
        now = time.strftime("%I:%M:%S %p")
        self.clock_label.config(text=now)
        self.root.after(1000, self.update_clock)

    def toggle_start_menu(self):
        # Toggle the start menu visibility.
        # تبديل ظهور قائمة البداية.
        if self.start_menu and self.start_menu.winfo_exists():
            self.start_menu.destroy()
        else:
            self.open_start_menu()

    def open_start_menu(self):
        # Open the start menu with various application shortcuts.
        # فتح قائمة البداية مع اختصارات التطبيقات.
        self.start_menu = tk.Toplevel(self.root)
        self.start_menu.overrideredirect(True)
        x = self.root.winfo_rootx()
        y = self.root.winfo_rooty() + self.root.winfo_height() - 30 - 300
        self.start_menu.geometry(f"250x300+{x}+{y}")
        self.start_menu.config(bg='#C0C0C0')
        
        tk.Button(self.start_menu, text=self.lang_data[self.current_lang]['programs'], anchor='w',
                  command=self.open_programs_menu, bg='#C0C0C0', relief='flat').pack(fill='x', padx=5, pady=2)
        tk.Button(self.start_menu, text=self.lang_data[self.current_lang]['my_computer'], anchor='w',
                  command=self.open_my_computer, bg='#C0C0C0', relief='flat').pack(fill='x', padx=5, pady=2)
        tk.Button(self.start_menu, text=self.lang_data[self.current_lang]['notepad'], anchor='w',
                  command=self.open_notepad, bg='#C0C0C0', relief='flat').pack(fill='x', padx=5, pady=2)
        tk.Button(self.start_menu, text=self.lang_data[self.current_lang]['paint'], anchor='w',
                  command=self.open_paint, bg='#C0C0C0', relief='flat').pack(fill='x', padx=5, pady=2)
        tk.Button(self.start_menu, text=self.lang_data[self.current_lang]['calculator'], anchor='w',
                  command=self.open_calculator, bg='#C0C0C0', relief='flat').pack(fill='x', padx=5, pady=2)
        tk.Button(self.start_menu, text=self.lang_data[self.current_lang]['minesweeper'], anchor='w',
                  command=self.open_minesweeper, bg='#C0C0C0', relief='flat').pack(fill='x', padx=5, pady=2)
        tk.Button(self.start_menu, text=self.lang_data[self.current_lang]['word'], anchor='w',
                  command=self.open_word, bg='#C0C0C0', relief='flat').pack(fill='x', padx=5, pady=2)
        tk.Button(self.start_menu, text=self.lang_data[self.current_lang]['excel'], anchor='w',
                  command=self.open_excel, bg='#C0C0C0', relief='flat').pack(fill='x', padx=5, pady=2)
        tk.Button(self.start_menu, text=self.lang_data[self.current_lang]['control_panel'], anchor='w',
                  command=self.open_control_panel, bg='#C0C0C0', relief='flat').pack(fill='x', padx=5, pady=2)
        tk.Button(self.start_menu, text=self.lang_data[self.current_lang]['settings'], anchor='w',
                  command=self.open_settings, bg='#C0C0C0', relief='flat').pack(fill='x', padx=5, pady=2)
        tk.Button(self.start_menu, text=self.lang_data[self.current_lang]['shutdown'], anchor='w',
                  command=self.shutdown, bg='#C0C0C0', relief='flat').pack(fill='x', padx=5, pady=2)

    def open_programs_menu(self):
        # Open the programs submenu from the start menu.
        # فتح قائمة البرامج الفرعية من قائمة البداية.
        programs_menu = tk.Toplevel(self.start_menu)
        programs_menu.title(self.lang_data[self.current_lang]['programs'])
        programs_menu.geometry("150x250")
        programs_menu.config(bg='#C0C0C0')
        programs_menu.transient(self.start_menu)
        
        tk.Button(programs_menu, text=self.lang_data[self.current_lang]['notepad'], anchor='w',
                  command=self.open_notepad, bg='#C0C0C0', relief='flat').pack(fill='x', padx=5, pady=2)
        tk.Button(programs_menu, text=self.lang_data[self.current_lang]['paint'], anchor='w',
                  command=self.open_paint, bg='#C0C0C0', relief='flat').pack(fill='x', padx=5, pady=2)
        tk.Button(programs_menu, text=self.lang_data[self.current_lang]['calculator'], anchor='w',
                  command=self.open_calculator, bg='#C0C0C0', relief='flat').pack(fill='x', padx=5, pady=2)
        tk.Button(programs_menu, text=self.lang_data[self.current_lang]['minesweeper'], anchor='w',
                  command=self.open_minesweeper, bg='#C0C0C0', relief='flat').pack(fill='x', padx=5, pady=2)
        tk.Button(programs_menu, text=self.lang_data[self.current_lang]['word'], anchor='w',
                  command=self.open_word, bg='#C0C0C0', relief='flat').pack(fill='x', padx=5, pady=2)
        tk.Button(programs_menu, text=self.lang_data[self.current_lang]['excel'], anchor='w',
                  command=self.open_excel, bg='#C0C0C0', relief='flat').pack(fill='x', padx=5, pady=2)
        tk.Button(programs_menu, text=self.lang_data[self.current_lang]['my_computer'], anchor='w',
                  command=self.open_my_computer, bg='#C0C0C0', relief='flat').pack(fill='x', padx=5, pady=2)

    def shutdown(self):
        # Confirm shutdown and destroy root window.
        # تأكيد الإيقاف وإغلاق النافذة الرئيسية.
        prompt = "Are you sure you want to shutdown?" if self.current_lang == 'en' else "هل أنت متأكد أنك تريد إيقاف التشغيل؟"
        if messagebox.askyesno(self.lang_data[self.current_lang]['shutdown'], prompt):
            self.root.destroy()

    def open_my_computer(self):
        # Open My Computer window with drive information.
        # فتح نافذة جهاز الكمبيوتر مع معلومات الأقراص.
        win = tk.Toplevel(self.root)
        win.title(self.lang_data[self.current_lang]['my_computer'])
        win.geometry("400x300")
        win.config(bg='white')
        info = "Drives:\n\nC:\nD:\nE:\n" if self.current_lang=='en' else "أقراص ثابتة:\n\nC:\nD:\nE:\n"
        tk.Label(win, text=info, font=("Tahoma", 10), bg='white').pack(padx=10, pady=10)

    def open_recycle_bin(self):
        # Open Recycle Bin window.
        # فتح نافذة سلة المحذوفات.
        win = tk.Toplevel(self.root)
        win.title(self.lang_data[self.current_lang]['recycle_bin'])
        win.geometry("300x200")
        win.config(bg='white')
        text = "Recycle Bin is empty" if self.current_lang=='en' else "سلة المحذوفات فارغة"
        tk.Label(win, text=text, font=("Tahoma", 10), bg='white').pack(padx=10, pady=10)

    def open_notepad(self):
        # Open Notepad application.
        # فتح تطبيق المفكرة.
        win = tk.Toplevel(self.root)
        win.title(self.lang_data[self.current_lang]['notepad'])
        win.geometry("600x400")
        menu_bar = tk.Menu(win)
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label=self.lang_data[self.current_lang]['new'],
                              command=lambda: text_area.delete(1.0, tk.END))
        file_menu.add_command(label=self.lang_data[self.current_lang]['open'],
                              command=lambda: self.open_file(text_area))
        file_menu.add_command(label=self.lang_data[self.current_lang]['save'],
                              command=lambda: self.save_file(text_area))
        file_menu.add_separator()
        file_menu.add_command(label=self.lang_data[self.current_lang]['exit'], command=win.destroy)
        menu_bar.add_cascade(label="File" if self.current_lang=='en' else "ملف", menu=file_menu)
        win.config(menu=menu_bar)
        text_area = tk.Text(win, wrap='word', font=("Consolas", 11))
        text_area.pack(expand=True, fill='both')

    def open_file(self, text_area):
        # Open file dialog and load file content.
        # فتح ملف باستخدام حوار الملفات وتحميل المحتوى.
        file_path = filedialog.askopenfilename()
        if file_path:
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()
            text_area.delete(1.0, tk.END)
            text_area.insert(tk.END, content)

    def save_file(self, text_area):
        # Save file using save dialog.
        # حفظ الملف باستخدام حوار الحفظ.
        file_path = filedialog.asksaveasfilename(defaultextension=".txt")
        if file_path:
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(text_area.get(1.0, tk.END))
            msg = "File saved successfully" if self.current_lang=='en' else "تم حفظ الملف بنجاح"
            messagebox.showinfo("Info", msg)

    def open_paint(self):
        # Open Paint application.
        # فتح تطبيق الرسام.
        win = tk.Toplevel(self.root)
        win.title(self.lang_data[self.current_lang]['paint'])
        win.geometry("600x400")
        win.config(bg='white')
        canvas = tk.Canvas(win, bg="white")
        canvas.pack(expand=True, fill='both')
        canvas.old_x = None
        canvas.old_y = None

        def reset(event):
            # Reset drawing coordinates.
            # إعادة تعيين إحداثيات الرسم.
            canvas.old_x = None
            canvas.old_y = None

        def draw(event):
            # Draw line on canvas.
            # رسم خط على اللوحة.
            if canvas.old_x and canvas.old_y:
                canvas.create_line(canvas.old_x, canvas.old_y, event.x, event.y,
                                   width=2, fill='black', capstyle=tk.ROUND, smooth=True)
            canvas.old_x = event.x
            canvas.old_y = event.y

        canvas.bind('<B1-Motion>', draw)
        canvas.bind('<ButtonRelease-1>', reset)

    def open_calculator(self):
        # Open Calculator application.
        # فتح تطبيق الآلة الحاسبة.
        win = tk.Toplevel(self.root)
        win.title(self.lang_data[self.current_lang]['calculator'])
        win.geometry("300x400")
        win.resizable(True, True)
        calc_expression = tk.StringVar()
        entry = tk.Entry(win, textvariable=calc_expression, font=("Consolas", 20),
                         bd=5, relief='sunken', justify='right')
        entry.grid(row=0, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")

        def btn_click(value):
            # Append digit or operator to expression.
            # إضافة رقم أو عملية إلى التعبير.
            current = calc_expression.get()
            calc_expression.set(current + str(value))

        def calculate():
            # Evaluate the expression.
            # تقييم التعبير.
            try:
                result = str(eval(calc_expression.get()))
                calc_expression.set(result)
            except Exception:
                calc_expression.set("Error")

        def clear():
            # Clear the expression.
            # مسح التعبير.
            calc_expression.set("")

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
        ]
        for (text, row, col) in buttons:
            action = (lambda x=text: calculate()) if text == '=' else (lambda x=text: btn_click(x))
            tk.Button(win, text=text, font=("Consolas", 18), command=action,
                      width=5, height=2).grid(row=row, column=col, padx=3, pady=3)

        tk.Button(win, text="C", font=("Consolas", 18), command=clear,
                  width=5, height=2).grid(row=5, column=0, columnspan=4, padx=3, pady=3)

    def open_minesweeper(self):
        # Open Minesweeper game.
        # فتح لعبة كاشف الألغام.
        win = tk.Toplevel(self.root)
        win.title(self.lang_data[self.current_lang]['minesweeper'])
        rows, cols, num_mines = 8, 8, 10
        board = [[{'mine': False, 'count': 0, 'revealed': False} for _ in range(cols)] for _ in range(rows)]
        buttons = [[None for _ in range(cols)] for _ in range(rows)]

        mine_positions = random.sample(range(rows * cols), num_mines)
        for pos in mine_positions:
            r = pos // cols
            c = pos % cols
            board[r][c]['mine'] = True

        for r in range(rows):
            for c in range(cols):
                if board[r][c]['mine']:
                    continue
                count = 0
                for i in range(max(0, r - 1), min(rows, r + 2)):
                    for j in range(max(0, c - 1), min(cols, c + 2)):
                        if board[i][j]['mine']:
                            count += 1
                board[r][c]['count'] = count

        frame = tk.Frame(win)
        frame.pack()

        def reveal(r, c):
            # Reveal cell content.
            # إظهار محتوى الخانة.
            if board[r][c]['revealed']:
                return
            board[r][c]['revealed'] = True
            btn = buttons[r][c]
            if board[r][c]['mine']:
                btn.config(text="*", bg="red")
                msg = "Game Over!" if self.current_lang=='en' else "انتهت اللعبة!"
                messagebox.showinfo(self.lang_data[self.current_lang]['minesweeper'], msg)
                for i in range(rows):
                    for j in range(cols):
                        if board[i][j]['mine']:
                            buttons[i][j].config(text="*", bg="red")
                return
            else:
                count = board[r][c]['count']
                btn.config(text=str(count) if count > 0 else "", bg="lightgrey", relief='sunken')
                if count == 0:
                    for i in range(max(0, r - 1), min(rows, r + 2)):
                        for j in range(max(0, c - 1), min(cols, c + 2)):
                            if not board[i][j]['revealed']:
                                reveal(i, j)

        for r in range(rows):
            for c in range(cols):
                btn = tk.Button(frame, width=3, height=1,
                                command=lambda r=r, c=c: reveal(r, c))
                btn.grid(row=r, column=c)
                buttons[r][c] = btn

        tk.Button(win, text="Reset", command=lambda: [win.destroy(), self.open_minesweeper()]).pack(pady=5)

    def open_control_panel(self):
        # Open Control Panel window.
        # فتح لوحة التحكم.
        win = tk.Toplevel(self.root)
        win.title(self.lang_data[self.current_lang]['control_panel'])
        win.geometry("400x300")
        win.config(bg='white')

        def show_system_info():
            # Show system information.
            # عرض معلومات النظام.
            info = ("OS: Windows 95 Simulator\nVersion: 1.0\nDeveloped with Tkinter" 
                    if self.current_lang=='en' else 
                    "نظام التشغيل: محاكاة Windows 95\nالإصدار: 1.0\nتم التطوير باستخدام Tkinter")
            messagebox.showinfo(self.lang_data[self.current_lang]['system_info'], info)

        def change_desktop_color():
            # Change desktop background color.
            # تغيير لون خلفية سطح المكتب.
            color = colorchooser.askcolor(title=self.lang_data[self.current_lang]['change_desktop_color'])
            if color[1]:
                self.desktop.config(bg=color[1])

        def show_about():
            # Show about information.
            # عرض معلومات حول البرنامج.
            about_text = ("Windows 95 Simulator\nCreated by ChatGPT" 
                          if self.current_lang=='en' else 
                          "محاكاة Windows 95\nتم إنشاؤها بواسطة ChatGPT")
            messagebox.showinfo(self.lang_data[self.current_lang]['about'], about_text)

        tk.Button(win, text=self.lang_data[self.current_lang]['system_info'],
                  command=show_system_info, width=25, bg='#C0C0C0').pack(pady=10)
        tk.Button(win, text=self.lang_data[self.current_lang]['change_desktop_color'],
                  command=change_desktop_color, width=25, bg='#C0C0C0').pack(pady=10)
        tk.Button(win, text=self.lang_data[self.current_lang]['about'],
                  command=show_about, width=25, bg='#C0C0C0').pack(pady=10)

    def open_settings(self):
        # Open Settings window.
        # فتح نافذة الإعدادات.
        win = tk.Toplevel(self.root)
        win.title(self.lang_data[self.current_lang]['system_settings'])
        win.geometry("500x400")
        win.config(bg='white')

        tk.Label(win, text="Settings / الإعدادات", font=("Tahoma", 14), bg='white').pack(pady=10)

        tk.Label(win, text=self.lang_data[self.current_lang]['language'] + ":", font=("Tahoma", 12),
                 bg='white').pack(pady=5)
        lang_btn_text = (self.lang_data[self.current_lang]['switch_to_english'] 
                         if self.current_lang=='ar' 
                         else self.lang_data[self.current_lang]['switch_to_arabic'])
        tk.Button(win, text=lang_btn_text, command=self.switch_language, bg='#C0C0C0', relief='raised').pack(pady=5)

        tk.Button(win, text=self.lang_data[self.current_lang]['change_desktop_color'],
                  command=lambda: self.change_desktop_background(), bg='#C0C0C0', relief='raised').pack(pady=5)

        self.key_button_visible = tk.BooleanVar(value=True)
        tk.Checkbutton(win, text="Show Key Button / إظهار زر Key", variable=self.key_button_visible, bg='white',
                       command=self.toggle_key_button).pack(pady=5)

        tk.Label(win,
                 text="(Additional settings can be added here) / (يمكن إضافة إعدادات إضافية هنا)",
                 bg='white', fg='gray').pack(pady=20)

    def toggle_key_button(self):
        # Toggle visibility of the Key button on the taskbar.
        # تبديل ظهور زر Key على شريط المهام.
        if self.key_button_visible.get():
            self.key_button.pack(side='left', padx=5, pady=2)
        else:
            self.key_button.pack_forget()

    def change_desktop_background(self):
        # Change the desktop background color.
        # تغيير لون خلفية سطح المكتب.
        color = colorchooser.askcolor(title=self.lang_data[self.current_lang]['change_desktop_color'])
        if color[1]:
            self.desktop.config(bg=color[1])

    def switch_language(self):
        # Switch between English and Arabic.
        # تبديل اللغة بين الإنجليزية والعربية.
        self.current_lang = 'en' if self.current_lang=='ar' else 'ar'
        self.update_ui_language()
        if self.start_menu and self.start_menu.winfo_exists():
            self.start_menu.destroy()
        msg = "Switched to English" if self.current_lang=='en' else "تم التبديل إلى العربية"
        messagebox.showinfo("Info", msg)

    def update_ui_language(self):
        # Update UI elements to reflect current language.
        # تحديث عناصر الواجهة لتتناسب مع اللغة الحالية.
        self.start_button.config(text=self.lang_data[self.current_lang]['start'])
        for key, widgets in self.desktop_icons.items():
            new_text = self.lang_data[self.current_lang].get(key, key)
            widgets['button'].config(text=new_text)
            widgets['label'].config(text=new_text)

    def open_word(self):
        # Open Word application with enhanced features.
        # فتح تطبيق وورد مع ميزات محسنة.
        win = tk.Toplevel(self.root)
        win.title(self.lang_data[self.current_lang]['word'])
        win.geometry("800x600")
        
        # Create menu bar
        # إنشاء شريط القوائم
        menu_bar = tk.Menu(win)
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label=self.lang_data[self.current_lang]['new'],
                              command=lambda: text_area.delete(1.0, tk.END))
        file_menu.add_command(label=self.lang_data[self.current_lang]['open'],
                              command=lambda: self.open_file(text_area))
        file_menu.add_command(label=self.lang_data[self.current_lang]['save'],
                              command=lambda: self.save_file(text_area))
        file_menu.add_separator()
        file_menu.add_command(label=self.lang_data[self.current_lang]['exit'], command=win.destroy)
        menu_bar.add_cascade(label="File" if self.current_lang=='en' else "ملف", menu=file_menu)
        win.config(menu=menu_bar)
        
        # Create a toolbar for text formatting
        # إنشاء شريط أدوات لتنسيق النص
        toolbar = tk.Frame(win, bg='#E0E0E0')
        toolbar.pack(side='top', fill='x')
        
        bold_btn = tk.Button(toolbar, text=self.lang_data[self.current_lang]['bold'], command=lambda: self.apply_text_tag(text_area, "bold"))
        bold_btn.pack(side='left', padx=2, pady=2)
        italic_btn = tk.Button(toolbar, text=self.lang_data[self.current_lang]['italic'], command=lambda: self.apply_text_tag(text_area, "italic"))
        italic_btn.pack(side='left', padx=2, pady=2)
        underline_btn = tk.Button(toolbar, text=self.lang_data[self.current_lang]['underline'], command=lambda: self.apply_text_tag(text_area, "underline"))
        underline_btn.pack(side='left', padx=2, pady=2)
        
        # Create text area with scroll bar
        # إنشاء منطقة النص مع شريط التمرير
        text_frame = tk.Frame(win)
        text_frame.pack(fill='both', expand=True)
        scrollbar = tk.Scrollbar(text_frame)
        scrollbar.pack(side='right', fill='y')
        text_area = tk.Text(text_frame, wrap='word', font=("Consolas", 12), yscrollcommand=scrollbar.set)
        text_area.pack(expand=True, fill='both')
        scrollbar.config(command=text_area.yview)
        
        # Define text formatting tags
        # تعريف علامات تنسيق النص
        bold_font = tkfont.Font(text_area, text_area.cget("font"))
        bold_font.configure(weight="bold")
        text_area.tag_configure("bold", font=bold_font)
        
        italic_font = tkfont.Font(text_area, text_area.cget("font"))
        italic_font.configure(slant="italic")
        text_area.tag_configure("italic", font=italic_font)
        
        underline_font = tkfont.Font(text_area, text_area.cget("font"))
        underline_font.configure(underline=1)
        text_area.tag_configure("underline", font=underline_font)

    def apply_text_tag(self, text_area, tag_name):
        # Apply formatting tag to the selected text in Word.
        # تطبيق علامة تنسيق على النص المحدد في وورد.
        try:
            current_tags = text_area.tag_names("sel.first")
            # If tag already exists, remove it; otherwise, add it
            # إذا كانت العلامة موجودة بالفعل، قم بإزالتها؛ وإلا أضفها
            if tag_name in current_tags:
                text_area.tag_remove(tag_name, "sel.first", "sel.last")
            else:
                text_area.tag_add(tag_name, "sel.first", "sel.last")
        except tk.TclError:
            # No text selected
            # لا يوجد نص محدد
            pass

    def open_excel(self):
        # Open Excel application with an enhanced grid.
        # فتح تطبيق إكسل مع شبكة محسنة.
        win = tk.Toplevel(self.root)
        win.title(self.lang_data[self.current_lang]['excel'])
        win.geometry("800x600")
        
        # Create a frame for the grid and headers
        # إنشاء إطار للشبكة والعناوين
        grid_frame = tk.Frame(win)
        grid_frame.pack(fill='both', expand=True)
        
        rows, cols = 15, 10  # Increased grid size for realism
        # Create headers for columns
        # إنشاء رؤوس للأعمدة
        for c in range(1, cols+1):
            header = tk.Label(grid_frame, text=chr(64+c), borderwidth=1, relief="solid", width=10)
            header.grid(row=0, column=c, sticky="nsew")
        # Create headers for rows
        # إنشاء رؤوس للصفوف
        for r in range(1, rows+1):
            header = tk.Label(grid_frame, text=str(r), borderwidth=1, relief="solid", width=5)
            header.grid(row=r, column=0, sticky="nsew")
            
        # Create grid cells as Entry widgets
        # إنشاء خلايا الشبكة باستخدام Entry
        cells = {}
        for r in range(1, rows+1):
            for c in range(1, cols+1):
                e = tk.Entry(grid_frame, width=10, font=("Consolas", 10), borderwidth=1, relief="solid")
                e.grid(row=r, column=c, sticky="nsew")
                cells[(r,c)] = e
        
        # Configure grid weights for resizing
        # ضبط أوزان الشبكة للسماح بإعادة التحجيم
        for c in range(cols+1):
            grid_frame.columnconfigure(c, weight=1)
        for r in range(rows+1):
            grid_frame.rowconfigure(r, weight=1)
        
        # Status bar to show selected cell coordinates (optional)
        # شريط الحالة لعرض إحداثيات الخلية المحددة (اختياري)
        status = tk.Label(win, text="Ready", bd=1, relief="sunken", anchor="w")
        status.pack(side="bottom", fill="x")
        
        def cell_selected(event, r, c):
            status.config(text=f"Selected cell: {chr(64+c)}{r}" if self.current_lang=='en' else f"الخلية المحددة: {r},{chr(64+c)}")
        
        # Bind cell click event
        # ربط حدث النقر على الخلية
        for (r, c), entry in cells.items():
            entry.bind("<FocusIn>", lambda e, r=r, c=c: cell_selected(e, r, c))

    def open_mobile_keyboard(self):
        # Open Mobile Keyboard window.
        # فتح نافذة الكيبورد للموبايل.
        win = tk.Toplevel(self.root)
        win.title("Mobile Keyboard / لوحة مفاتيح الموبايل")
        win.geometry("400x200")
        win.config(bg='black')
        tk.Label(win, text="Mobile Keyboard / لوحة مفاتيح الموبايل", bg='black', fg='lime', font=("Consolas", 14)).pack(pady=10)
        entry = tk.Entry(win, font=("Consolas", 16))
        entry.pack(pady=10, padx=10, fill='x')
        entry.focus_set()
        tk.Button(win, text="Done / تم", command=win.destroy, font=("Consolas", 12)).pack(pady=10)

def main():
    # Main function to start the simulator.
    # الدالة الرئيسية لبدء المحاكي.
    root = tk.Tk()
    root.withdraw()  # Hide main window during boot
    def start_login():
        LoginScreen(root, start_system)
    def start_system():
        root.deiconify()
        Windows95Simulator(root)
    BootScreen(root, on_finish_callback=start_login)
    root.mainloop()

if __name__ == '__main__':
    main()