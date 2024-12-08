import customtkinter as ctk
from tkinter import filedialog, messagebox


class GBAEditorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Emerald Seaglass Starter Injector v0.1")
        self.root.geometry("400x400")  # Increased window size for better spacing

        ctk.set_appearance_mode("System")  # Use system appearance (light/dark)
        ctk.set_default_color_theme("blue")  # Set color theme

        self.create_widgets()

    def create_widgets(self):
        # Title Label
        title_label = ctk.CTkLabel(self.root, text="Emerald Seaglass Starter Injector", font=("Arial", 20, "bold"))
        title_label.pack(pady=10)

        # Upload file button
        upload_button = ctk.CTkButton(self.root, text="Select Emerald Seaglass .GBA File", command=self.upload_file)
        upload_button.pack(pady=10)

        # Dropdowns for Starters
        self.starter1_var = ctk.StringVar(value="Select First Starter:")
        starter1_dropdown = ctk.CTkOptionMenu(
            self.root,
            variable=self.starter1_var,
            values=self.get_hex_options(),
            width=300
        )
        starter1_dropdown.pack(pady=10)

        self.starter2_var = ctk.StringVar(value="Select Second Starter:")
        starter2_dropdown = ctk.CTkOptionMenu(
            self.root,
            variable=self.starter2_var,
            values=self.get_hex_options(),
            width=300
        )
        starter2_dropdown.pack(pady=10)

        self.starter3_var = ctk.StringVar(value="Select Third Starter:")
        starter3_dropdown = ctk.CTkOptionMenu(
            self.root,
            variable=self.starter3_var,
            values=self.get_hex_options(),
            width=300
        )
        starter3_dropdown.pack(pady=10)

        # Submit Button
        submit_button = ctk.CTkButton(self.root, text="Modify and Save", command=self.modify_file)
        submit_button.pack(pady=20)

    def upload_file(self):
        self.filepath = filedialog.askopenfilename(filetypes=[("GBA Files", "*.gba")])
        if self.filepath:
            messagebox.showinfo("File Selected", f"File {self.filepath} uploaded successfully.")
        else:
            messagebox.showerror("Error", "No file selected!")

    def get_hex_options(self):
        # Predefined hex options for simplicity
        return [
            "Select an Option",
            "0100 - Bulbasaur", "0200 - Ivysaur", "0300 - Venusaur", "0400 - Charmander", "0500 - Charmeleon",
            "0600 - Charizard", "0700 - Squirtle", "0800 - Wartortle", "0900 - Blastoise", "0A00 - Caterpie",
            "0B00 - Metapod", "0C00 - Butterfree", "0D00 - Weedle", "0E00 - Kakuna", "0F00 - Beedrill",
            "1000 - Pidgey", "1100 - Pidgeotto", "1200 - Pidgeot", "1300 - Rattata", "1400 - Raticate",
            "1500 - Spearow", "1600 - Fearow", "1700 - Ekans", "1800 - Arbok", "1900 - Pikachu", "1A00 - Raichu",
            "1B00 - Sandshrew", "1C00 - Sandslash", "1D00 - Nidoran (Female)", "1E00 - Nidorina", "1F00 - Nidoqueen",
            "2000 - Nidoran (Male)", "2100 - Nidorino", "2200 - Nidoking", "2300 - Clefairy", "2400 - Clefable",
            "2500 - Vulpix", "2600 - Ninetales", "2700 - Jigglypuff", "2800 - Wigglytuff", "2900 - Zubat", "2A00 - Golbat",
            "2B00 - Oddish", "2C00 - Gloom", "2D00 - Vileplume", "2E00 - Paras", "2F00 - Parasect", "3000 - Venonat",
            "3100 - Venomoth", "3200 - Diglett", "3300 - Dugtrio", "3400 - Meowth", "3500 - Persian", "3600 - Psyduck",
            "3700 - Golduck", "3800 - Mankey", "3900 - Primeape", "3A00 - Growlithe", "3B00 - Arcanine", "3C00 - Poliwag",
            "3D00 - Poliwhirl", "3E00 - Poliwrath", "3F00 - Abra", "4000 - Kadabra", "4100 - Alakazam", "4200 - Machop",
            "4300 - Machoke", "4400 - Machamp", "4500 - Bellsprout", "4600 - Weepinbell", "4700 - Victreebel", "4800 - Tentacool",
            "4900 - Tentacruel", "4A00 - Geodude", "4B00 - Graveler", "4C00 - Golem", "4D00 - Ponyta", "4E00 - Rapidash","4F00 - Slowpoke",
            "5000 - Slowbro", "5100 - Magnemite", "5200 - Magneton", "5300 - Farfetch'd", "5400 - Doduo", "5500 - Dodrio", "5600 - Seel",
            "5700 - Dewgong", "5800 - Grimer", "5900 - Muk", "5A00 - Shellder", "5B00 - Cloyster", "5C00 - Gastly", "5D00 - Haunter",
            "5E00 - Gengar", "5F00 - Onix", "6000 - Drowzee", "6100 - Hypno", "6200 - Krabby", "6300 - Kingler", "6400 - Voltorb",
            "6500 - Electrode", "6600 - Exeggcute", "6700 - Exeggutor", "6800 - Cubone", "6900 - Marowak", "6A00 - Hitmonlee",
            "6B00 - Hitmonchan", "6C00 - Lickitung", "6D00 - Koffing", "6E00 - Weezing", "6F00 - Rhyhorn", "7000 - Rhydon",
            "7100 - Chansey", "7200 - Tangela", "7300 - Kangaskhan", "7400 - Horsea", "7500 - Seadra", "7600 - Goldeen", "7700 - Seaking",
            "7800 - Staryu", "7900 - Starmie", "7A00 - Mr. Mime", "7B00 - Scyther", "7C00 - Jynx", "7D00 - Electabuzz", "7E00 - Magmar",
            "7F00 - Pinsir", "8000 - Tauros", "8100 - Magikarp", "8200 - Gyarados", "8300 - Lapras", "8400 - Ditto", "8500 - Eevee",
            "8600 - Vaporeon", "8700 - Jolteon", "8800 - Flareon", "8900 - Porygon", "8A00 - Omanyte", "8B00 - Omastar", "8C00 - Kabuto",
            "8D00 - Kabutops", "8E00 - Aerodactyl", "8F00 - Snorlax", "9000 - Articuno", "9100 - Zapdos", "9200 - Moltres", "9300 - Dratini",
            "9400 - Dragonair", "9500 - Dragonite", "9600 - Mewtwo", "9700 - Mew",

            "9800 - Chikorita", "9900 - Bayleef", "9A00 - Meganium", "9B00 - Cyndaquil", "9C00 - Quilava", "9D00 - Typhlosion",
            "9E00 - Totodile", "9F00 - Croconaw", "A000 - Feraligatr", "A100 - Sentret", "A200 - Furret", "A300 - Hoothoot",
            "A400 - Noctowl", "A500 - Ledyba", "A600 - Ledian", "A700 - Spinarak", "A800 - Ariados", "A900 - Crobat", "AA00 - Chinchou",
            "AB00 - Lanturn", "AC00 - Pichu", "AD00 - Cleffa", "AE00 - Igglybuff", "AF00 - Togepi", "B000 - Togetic", "B100 - Natu",
            "B200 - Xatu", "B300 - Mareep", "B400 - Flaaffy", "B500 - Ampharos", "B600 - Bellossom", "B700 - Marill", "B800 - Azumarill",
            "B900 - Sudowoodo", "BA00 - Politoed", "BB00 - Hoppip", "BC00 - Skiploom", "BD00 - Jumpluff", "BE00 - Aipom", "BF00 - Sunkern",
            "C000 - Sunflora", "C100 - Yanma", "C200 - Wooper", "C300 - Quagsire", "C400 - Espeon", "C500 - Umbreon", "C600 - Murkrow",
            "C700 - Slowking", "C800 - Misdreavus", "C900 - Unown", "CA00 - Wobbuffet", "CB00 - Girafarig", "CC00 - Pineco","CD00 - Forretress",
            "CE00 - Dunsparce", "CF00 - Gligar", "D000 - Steelix", "D100 - Snubbull", "D200 - Granbull", "D300 - Qwilfish", "D400 - Scizor",
            "D500 - Shuckle", "D600 - Heracross", "D700 - Sneasel", "D800 - Teddiursa", "D900 - Ursaring", "DA00 - Slugma", "DB00 - Magcargo",
            "DC00 - Swinub", "DD00 - Piloswine", "DE00 - Corsola", "DF00 - Remoraid", "E000 - Octillery", "E100 - Delibird", "E200 - Mantine",
            "E300 - Skarmory", "E400 - Houndour", "E500 - Houndoom", "E600 - Kingdra", "E700 - Phanpy", "E800 - Donphan", "E900 - Porygon2",
            "EA00 - Stantler", "EB00 - Smeargle", "EC00 - Tyrogue", "ED00 - Hitmontop", "EE00 - Smoochum", "EF00 - Elekid", "F000 - Magby",
            "F100 - Miltank", "F200 - Blissey", "F300 - Raikou", "F400 - Entei", "F500 - Suicune", "F600 - Larvitar", "F700 - Pupitar",
            "F800 - Tyranitar", "F900 - Lugia", "FA00 - Ho-oh", "FB00 - Celebi",

            "FC00 - Treecko", "FD00 - Grovyle", "FE00 - Sceptile", "FF00 - Torchic", "0001 - Combusken", "0101 - Blaziken", "0201 - Mudkip",
            "0301 - Marshtomp", "0401 - Swampert", "0501 - Poochyena", "0601 - Mightyena", "0701 - Zigzagoon", "0801 - Linoone", "0901 - Wurmple",
            "0A01 - Silcoon",  "0B01 - Beautifly",  "0C01 - Cascoon",  "0D01 - Dustox",  "0E01 - Lotad",  "0F01 - Lombre",  "1001 - Ludicolo",
            "1101 - Seedot",  "1201 - Nuzleaf",  "1301 - Shiftry",  "1401 - Taillow",  "1501 - Swellow",  "1601 - Wingull",  "1701 - Pelipper",
            "1801 - Ralts",  "1901 - Kirlia",  "1A01 - Gardevoir",  "1B01 - Surskit",  "1C01 - Masquerain",  "1D01 - Shroomish",  "1E01 - Breloom",
            "1F01 - Slakoth",  "2001 - Vigoroth",  "2101 - Slaking",  "2201 - Nincada",  "2301 - Ninjask",  "2401 - Shedinja",  "2501 - Whismur",
            "2601 - Loudred",  "2701 - Exploud",  "2801 - Makuhita",  "2901 - Hariyama",  "2A01 - Azurill",  "2B01 - Nosepass",  "2C01 - Skitty",
            "2D01 - Delcatty",  "2E01 - Sableye",  "2F01 - Mawile",  "3001 - Aron",  "3101 - Lairon",  "3201 - Aggron",  "3301 - Meditite",  "3401 - Medicham",
            "3501 - Electrike",  "3601 - Manectric",  "3701 - Plusle",  "3801 - Minun",  "3901 - Volbeat",  "3A01 - Illumise",  "3B01 - Roselia",  "3C01 - Gulpin",
            "3D01 - Swalot",  "3E01 - Carvanha",  "3F01 - Sharpedo",  "4001 - Wailmer",  "4101 - Wailord",  "4201 - Numel",  "4301 - Camerupt",  "4401 - Torkoal",
            "4501 - Spoink",  "4601 - Grumpig",  "4701 - Spinda",  "4801 - Trapinch",  "4901 - Vibrava",  "4A01 - Flygon",  "4B01 - Cacnea",  "4C01 - Cacturne",
            "4D01 - Swablu",  "4E01 - Altaria",  "4F01 - Zangoose",  "5001 - Seviper",  "5101 - Lunatone",  "5201 - Solrock",  "5301 - Barboach",  "5401 - Whiscash",
            "5501 - Corphish",  "5601 - Crawdaunt",  "5701 - Baltoy",  "5801 - Claydol",  "5901 - Lileep",  "5A01 - Cradily",  "5B01 - Anorith",  "5C01 - Armaldo",
            "5D01 - Feebas",  "5E01 - Milotic",  "5F01 - Castform (Normal)",  "6001 - Kecleon",  "6101 - Shuppet",  "6201 - Banette",  "6301 - Duskull",
            "6401 - Dusclops", "6501 - Tropius", "6601 - Chimecho", "6701 - Absol", "6801 - Wynaut", "6901 - Snorunt", "6A01 - Glalie", "6B01 - Spheal",
            "6C01 - Sealeo", "6D01 - Walrein", "6E01 - Clamperl", "6F01 - Huntail", "7001 - Gorebyss", "7101 - Relicanth", "7201 - Luvdisc", "7301 - Bagon",
            "7401 - Shelgon", "7501 - Salamence", "7601 - Beldum", "7701 - Metang", "7801 - Metagross", "7901 - Regirock", "7A01 - Regice", "7B01 - Registeel",
            "7C01 - Latias", "7D01 - Latios", "7E01 - Kyogre", "7F01 - Groudon", "8001 - Rayquaza", "8101 - Jirachi", "8201 - Deoxys (Normal)",

            "B801 - Happiny", "BE01 - Munchlax", "5C05 - Farigiraf", "D801 - Gliscor", "CD01 - Weavile", "D901 - Mamoswine", "8303 - Wyrdeer",
            "DB01 - Gallade", "DC01 - Probopass", "DD01 - Dusknoir", "DE01 - Froslass", "CE01 - Magnezone", "5A05 - Annihalape",
            "CF01 - Lickilicky", "D001 - Rhyperior", "D101 - Tangrowth", "8503 - Ursaluna", "D601 - Leafeon", "D701 - Glaceon", "BC02 - Sylveon",
            "4105 - Tinkatink", "4205 - Tinkatuff", "4305 - Tinkaton", "9601 - Budew", "9701 - Roserade", "A801 - Ambipom", "AD01 - Mismagius",
            "AE01 - Honchcrow", "B101 - Chingling", "B601 - Bonsly", "B701 - Mime Jr.", "4803 - Applin", "4903 - Flapple", "4A03 - Appletun",
            "8005 - Dipplin", "9205 - Hydrapple", "BE03 - Raichu (Alolan)", "BF03 - Sandshrew (Alolan)", "C003 - Sandslash (Alolan)", "C103 - Vulpix (Alolan)",
            "C203 - Ninetales (Alolan)", "C303 - Diglett (Alolan)", "C403 - Dugtrio (Alolan)", "C503 - Meowth (Alolan)", "C603 - Persian (Alolan)", "C703 - Geodude (Alolan)", 
            "C803 - Graveler (Alolan)", "C903 - Golem (Alolan)", "CA03 - Grimer (Alolan)", "CB03 - Muk (Alolan)", "CC03 - Exeggutor (Alolan)", "CD03 - Marowak (Alolan)",
            "D201 - Electivire", "D301 - Magmortar", "DA01 - Porygon Z", "D401 - Togekiss", "D501 - Yanmega", "5D05 - Dudunsparce (2 Segment)", "5E05 - Dudunsparce (3 Segment)",
            "8403 - Kleavor", "FF03 - Spiky Eared Pichu"
        ]

    def is_valid_hex(self, hex_value):
        """Validate if the given hex value is a valid 2-byte hexadecimal."""
        try:
            if len(hex_value) == 4 and int(hex_value, 16) <= 0xFFFF:
                return True
            return False
        except ValueError:
            return False

    def modify_file(self):
        if not hasattr(self, 'filepath') or not self.filepath:
            messagebox.showerror("Error", "No file uploaded!")
            return

        # Validate dropdown selections
        starters = [self.starter1_var.get(), self.starter2_var.get(), self.starter3_var.get()]
        hex_values = [starter.split(" - ")[0] for starter in starters if starter != "Select an Option"]

        if len(hex_values) < 3:
            messagebox.showerror("Error", "Please select hex values for all starters!")
            return

        # Validate hex values
        if not all(self.is_valid_hex(hex_val) for hex_val in hex_values):
            messagebox.showerror("Error", "One or more hex values are invalid!")
            return

        try:
            with open(self.filepath, 'rb') as f:
                file_data = f.read()

            # Define offsets
            offsets = [0x009606C8, 0x009606CA, 0x009606CC]

            # Replace values at specified offsets
            for offset, hex_value in zip(offsets, hex_values):
                byte_data = bytes.fromhex(hex_value)
                file_data = file_data[:offset] + byte_data + file_data[offset + len(byte_data):]

            # Save the modified file
            save_path = filedialog.asksaveasfilename(defaultextension=".gba", filetypes=[("GBA Files", "*.gba")])
            if save_path:
                with open(save_path, 'wb') as f:
                    f.write(file_data)
                messagebox.showinfo("Success", f"File saved as {save_path}.")
            else:
                messagebox.showerror("Error", "Save operation canceled.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while modifying the file: {e}")


if __name__ == "__main__":
    root = ctk.CTk()
    app = GBAEditorApp(root)
    root.mainloop()