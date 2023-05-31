import customtkinter as ctk

class GUI:
    def __init__(self) -> None:
        # Common variables
        self.m_commonNode = 5
        self.m_magicNode = 7
        self.m_rareNode = 10
        self.m_UserCount_Common = 0
        self.m_UserCount_Magic = 0
        self.m_UserCount_Rare = 0
        self.m_UserGlyphBonus = 0.0
        self.m_stat_total = 0
        self.m_glyph_bonus_total = 0.0

        # GUI Controls
        self.gui_form = None
        self.gui_lbl_section_glyph_nodes = None
        self.gui_lbl_commonNode = None
        self.gui_lbl_magicNode = None
        self.gui_lbl_rareNode = None

        self.gui_entry_commonNode = None
        self.gui_entry_magicNode = None
        self.gui_entry_rareNode = None

        self.gui_lbl_glyphbonus = None
        self.gui_entry_glyphbonus = None

        self.gui_bttn_calculate = None
        self.gui_bttn_clear = None

        self.gui_lbl_statTotal = None
        self.gui_lbl_glyphBonus = None

    def create_gui(cls):
        try:
            form = ctk.CTk()
            form.geometry("500x200")  # Width x Height
            form.title("Glyph Node Calculator")
            form.wm_attributes('-toolwindow', 'True')
            form.resizable(False, False)
            ctk.set_default_color_theme('dark-blue')
            ctk.set_appearance_mode('dark')

            cls.gui_form = form

            # Control Forms
            lbl_nodes_section_text = ctk.CTkLabel(form, text="Glyph Nodes Count:", anchor='nw')
            lbl_nodes_section_text.grid(column=0, row=0, columnspan=2, rowspan=2, padx=5, pady=5)
            cls.gui_lbl_section_glyph_nodes = lbl_nodes_section_text

            # Common Nodes
            lbl_common_node = ctk.CTkLabel(form, text='Common Node(s):', anchor='nw')
            lbl_common_node.grid(column=0, row=2, columnspan=2, rowspan=2, padx=5, pady=5)
            cls.gui_lbl_commonNode = lbl_common_node  # Assign class variable to the UI element
            entry_common_node = ctk.CTkEntry(form, width=40, placeholder_text='0')
            entry_common_node.grid(column=2, row=2, columnspan=2, rowspan=2, padx=5, pady=5)
            cls.gui_entry_commonNode = entry_common_node  # Assign class variable to the UI element

            # Magic Nodes
            lbl_magic_node = ctk.CTkLabel(form, text='Magic Node(s):', anchor='nw')
            lbl_magic_node.grid(column=0, row=4, columnspan=2, rowspan=2, padx=0, pady=5)
            cls.gui_lbl_magicNode = lbl_magic_node
            entry_magic_node = ctk.CTkEntry(form, width=40, placeholder_text='0')
            entry_magic_node.grid(column=2, row=4, columnspan=2, rowspan=2, padx=0, pady=5)
            cls.gui_entry_magicNode = entry_magic_node

            # Rare Nodes
            lbl_rare_node = ctk.CTkLabel(form, text='Rare Node(s):', anchor='nw')
            lbl_rare_node.grid(column=0, row=6, columnspan=2, rowspan=2, padx=0, pady=5)
            cls.gui_lbl_rareNode = lbl_rare_node
            entry_rare_node = ctk.CTkEntry(form, width=40, placeholder_text='0')
            entry_rare_node.grid(column=2, row=6, columnspan=2, rowspan=2, padx=0, pady=5)
            cls.gui_entry_rareNode = entry_rare_node

            # Glyph percentage
            lbl_glyph_percentage = ctk.CTkLabel(form, text='Glyph buff %:')
            lbl_glyph_percentage.grid(column=0, row=8, columnspan=2, rowspan=2, padx=0, pady=5)
            cls.gui_lbl_glyphBonus = lbl_glyph_percentage
            entry_glyph_percentage = ctk.CTkEntry(form, width=40, placeholder_text='0.0')
            entry_glyph_percentage.grid(column=2, row=8, columnspan=2, rowspan=2, padx=0, pady=5)
            cls.gui_entry_glyphbonus = entry_glyph_percentage

            # Confirm/clear buttons
            bttn_clear = ctk.CTkButton(form, text='Clear', width=300, command=lambda: cls.clear_calculations())
            bttn_clear.grid(column=8, row=2, columnspan=2, rowspan=2, padx=15, pady=5)
            cls.gui_bttn_clear = bttn_clear

            bttn_calculate = ctk.CTkButton(form, text='Calculate', width=300, command=lambda: cls.calculate_nodes())
            bttn_calculate.grid(column=8, row=4, columnspan=2, rowspan=2, padx=15, pady=5)
            cls.gui_bttn_calculate = bttn_calculate

            # Calculation Text
            lbl_output_stat_total = ctk.CTkLabel(form, text=f'Total Stat(s): {cls.m_stat_total}')
            lbl_output_stat_total.grid(column=8, row=6, columnspan=2, rowspan=2, padx=0, pady=5)
            cls.gui_lbl_statTotal = lbl_output_stat_total
            lbl_output_glyph_total = ctk.CTkLabel(form, text=f'Glyph Bonus Total: {cls.m_glyph_bonus_total} %')
            lbl_output_glyph_total.grid(column=8, row=8, columnspan=2, rowspan=2, padx=0, pady=5)
            cls.gui_lbl_glyphBonus = lbl_output_glyph_total

            form.mainloop()
        except Exception as e:
            print(e)

    def validate_int(var):
        value = var.get()
        if (value.isdigit()):
            return True
        elif value == "":
            return True
        else:
            return False

    def calculate_nodes(cls):
        # Get user inputs
        cls.m_UserCount_Common = cls.gui_entry_commonNode.get()
        cls.m_UserCount_Magic = cls.gui_entry_magicNode.get()
        cls.m_UserCount_Rare = cls.gui_entry_rareNode.get()
        cls.m_UserGlyphBonus = cls.gui_entry_glyphbonus.get()
        try:
            # convert inputs
            cls.m_UserCount_Common = int(cls.m_UserCount_Common)
            cls.m_UserCount_Magic = int(cls.m_UserCount_Magic)
            cls.m_UserCount_Rare = int(cls.m_UserCount_Rare)
            cls.m_UserGlyphBonus = float(cls.m_UserGlyphBonus)

            commonNodesStat = int(5 * cls.m_UserCount_Common)
            magicNodesStat = int(7 * cls.m_UserCount_Magic)
            rareNodesStat = int(10 * cls.m_UserCount_Rare)

            # Calculate Total stats
            cls.m_stat_total = int(commonNodesStat + magicNodesStat + rareNodesStat)

            # Calculate glyph bonus
            cls.m_glyph_bonus_total = ((cls.m_stat_total / 5) * cls.m_UserGlyphBonus)

            # Update UI Texts
            cls.gui_lbl_statTotal.configure(text=f'Total Stat(s): {cls.m_stat_total}')
            cls.gui_lbl_glyphBonus.configure(text=f'Glyph Bonus Total: {cls.m_glyph_bonus_total} %')
        except Exception as e:
            if (e == ValueError):
                print("Invalid input. Please enter valid integer values.")
                print(f"Error details: {e}")
                print(f"Problematic value: {cls.m_UserCount_Common}")
                print(f"Problematic value: {cls.m_UserCount_Magic}")
                print(f"Problematic value: {cls.m_UserCount_Rare}")

    def clear_calculations(cls):
        # Clear class variables for re-generation later
        cls.m_UserCount_Common = 0
        cls.m_UserCount_Magic = 0
        cls.m_UserCount_Rare = 0
        cls.m_UserGlyphBonus = 0
        cls.m_stat_total = 0
        cls.m_glyph_bonus_total = 0.0

        # Update GUI to reflect the changes
        cls.gui_lbl_statTotal.configure(text=f'Total Stat(s): {cls.m_stat_total}')
        cls.gui_lbl_glyphBonus.configure(text=f'Glyph Bonus Total: {cls.m_glyph_bonus_total} %')
        cls.gui_entry_commonNode.delete(0, 'end')
        cls.gui_entry_commonNode.insert(0, '')
        cls.gui_entry_commonNode.configure(placeholder_text='0')

        cls.gui_entry_magicNode.delete(0, 'end')
        cls.gui_entry_magicNode.insert(0, '')
        cls.gui_entry_magicNode.configure(placeholder_text='0')

        cls.gui_entry_rareNode.delete(0, 'end')
        cls.gui_entry_rareNode.insert(0, '')
        cls.gui_entry_rareNode.configure(placeholder_text='0')

        cls.gui_entry_glyphbonus.delete(0, 'end')
        cls.gui_entry_glyphbonus.insert(0, '')
        cls.gui_entry_glyphbonus.configure(placeholder_text='0.0')
