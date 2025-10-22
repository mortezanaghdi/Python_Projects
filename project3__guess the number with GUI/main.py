if __name__ == "__main__":

    import customtkinter as ctk
    from guess import GuessGame

    # change default values
    ctk.set_appearance_mode("light")
    # ctk.set_default_color_theme("white")

    # build the window
    app = ctk.CTk()
    app.title("Guess The Number")
    app.geometry("400x250")

    app.grid_rowconfigure(0, weight=1)
    app.grid_rowconfigure(1, weight=1)
    app.grid_rowconfigure(2, weight=1)
    app.grid_columnconfigure(0, weight=1)
    app.grid_columnconfigure(1, weight=1)
    app.grid_columnconfigure(2, weight=1)

    game = GuessGame()

    entry_frame = ctk.CTkFrame(app)
    entry_frame.grid(row=1, column=1, sticky="nsew", padx=10, pady=10)

    entry_label = ctk.CTkLabel(entry_frame, text="Enter a number between 1 to 100")
    entry_label.pack(padx=20, pady=20)

    entry = ctk.CTkEntry(entry_frame, placeholder_text="34")
    entry.pack(pady=(5, 10))

    result_label = ctk.CTkLabel(entry_frame, text="")
    result_label.pack(pady=(5, 10))

    def check_input():
        try:
            guess = int(entry.get())
            feedback = game.check_guess(guess)
            result_label.configure(text=feedback)
        except:
            result_label.configure(text="Enter the valid number")

    button = ctk.CTkButton(entry_frame, text="Guess", command=check_input)
    button.pack(pady=(5, 10))

    app.mainloop()

else:
    print("you should not import this file")