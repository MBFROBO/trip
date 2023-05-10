from typing import Optional, Tuple, Union
import customtkinter
from main import create_dataset, neural_model

import time
import tkinter
import tkinter.messagebox
from tkinter import ttk
customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk, tkinter.Tk, create_dataset):
    def __init__(self):
        super().__init__()
        # configure window
        self.title("neuarl_app")
        self.geometry(f"{1100}x{580}")
        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)
        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Neural App", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, command=self.learned, text= 'Обучить')
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, command=self.prediction, text= 'Прогноз')
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_event, text = 'Справка (QA)')
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Тема:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="Масштаб интерфейса:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

        # create main entry and button
        # self.entry = customtkinter.CTkEntry(self, placeholder_text="CTkEntry")
        # self.entry.grid(row=3, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")

        # self.main_button_1 = customtkinter.CTkButton(master=self, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"))
        # self.main_button_1.grid(row=3, column=3, padx=(20, 20), pady=(20, 20), sticky="nsew")

        # create textbox
        self.textbox = customtkinter.CTkTextbox(self, width=150)
        self.textbox.grid(row=0, column=1, padx=(25, 25), pady=(20, 20), sticky="nsew")

        self.scaling_label2 = customtkinter.CTkLabel(self, text="Терминал", anchor="w")
        self.scaling_label2.grid(row=1, column=1, padx=25, pady=(0, 0), sticky="nsew")

        self.textbox1 = customtkinter.CTkTextbox(self, width=150)
        self.textbox1.grid(row=2, column=1, padx=(25, 25), pady=(10, 20), sticky="nsew")

        # create tabview
        # self.tabview = customtkinter.CTkTabview(self, width=250)
        # self.tabview.grid(row=0, column=2, padx=(20, 0), pady=(20, 0), sticky="nsew")
        # self.tabview.add("CTkTabview")
        # self.tabview.add("Tab 2")
        # self.tabview.add("Tab 3")
        # self.tabview.tab("CTkTabview").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs
        # self.tabview.tab("Tab 2").grid_columnconfigure(0, weight=1)

        # self.optionmenu_1 = customtkinter.CTkOptionMenu(self.tabview.tab("CTkTabview"), dynamic_resizing=False,
        #                                                 values=["Value 1", "Value 2", "Value Long Long Long"])
        # self.optionmenu_1.grid(row=0, column=0, padx=20, pady=(20, 10))
        # self.combobox_1 = customtkinter.CTkComboBox(self.tabview.tab("CTkTabview"),
        #                                             values=["Value 1", "Value 2", "Value Long....."])
        # self.combobox_1.grid(row=1, column=0, padx=20, pady=(10, 10))
        # self.string_input_button = customtkinter.CTkButton(self.tabview.tab("CTkTabview"), text="Open CTkInputDialog",
        #                                                    command=self.open_input_dialog_event)
        # self.string_input_button.grid(row=2, column=0, padx=20, pady=(10, 10))
        # self.label_tab_2 = customtkinter.CTkLabel(self.tabview.tab("Tab 2"), text="CTkLabel on Tab 2")
        # self.label_tab_2.grid(row=0, column=0, padx=20, pady=20)

        # create radiobutton frame
        # self.radiobutton_frame = customtkinter.CTkFrame(self)
        # self.radiobutton_frame.grid(row=0, column=3, padx=(20, 20), pady=(20, 0), sticky="nsew")
        # self.radio_var = tkinter.IntVar(value=0)
        # self.label_radio_group = customtkinter.CTkLabel(master=self.radiobutton_frame, text="CTkRadioButton Group:")
        # self.label_radio_group.grid(row=0, column=2, columnspan=1, padx=10, pady=10, sticky="")
        # self.radio_button_1 = customtkinter.CTkRadioButton(master=self.radiobutton_frame, variable=self.radio_var, value=0)
        # self.radio_button_1.grid(row=1, column=2, pady=10, padx=20, sticky="n")
        # self.radio_button_2 = customtkinter.CTkRadioButton(master=self.radiobutton_frame, variable=self.radio_var, value=1)
        # self.radio_button_2.grid(row=2, column=2, pady=10, padx=20, sticky="n")
        # self.radio_button_3 = customtkinter.CTkRadioButton(master=self.radiobutton_frame, variable=self.radio_var, value=2)
        # self.radio_button_3.grid(row=3, column=2, pady=10, padx=20, sticky="n")

        # create slider and progressbar frame
        # self.slider_progressbar_frame = customtkinter.CTkFrame(self, fg_color="transparent")
        # self.slider_progressbar_frame.grid(row=1, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")
        # self.slider_progressbar_frame.grid_columnconfigure(0, weight=1)
        # self.slider_progressbar_frame.grid_rowconfigure(4, weight=1)
        # self.seg_button_1 = customtkinter.CTkSegmentedButton(self.slider_progressbar_frame)
        # self.seg_button_1.grid(row=0, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")
        # self.progressbar_1 = customtkinter.CTkProgressBar(self.slider_progressbar_frame)
        # self.progressbar_1.grid(row=1, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")
        # self.progressbar_2 = customtkinter.CTkProgressBar(self.slider_progressbar_frame)
        # self.progressbar_2.grid(row=2, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")
        # self.slider_1 = customtkinter.CTkSlider(self.slider_progressbar_frame, from_=0, to=1, number_of_steps=4)
        # self.slider_1.grid(row=3, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")
        # self.slider_2 = customtkinter.CTkSlider(self.slider_progressbar_frame, orientation="vertical")
        # self.slider_2.grid(row=0, column=1, rowspan=5, padx=(10, 10), pady=(10, 10), sticky="ns")
        # self.progressbar_3 = customtkinter.CTkProgressBar(self.slider_progressbar_frame, orientation="vertical")
        # self.progressbar_3.grid(row=0, column=2, rowspan=5, padx=(10, 20), pady=(10, 10), sticky="ns")

        # # create scrollable frame
        # self.scrollable_frame = customtkinter.CTkScrollableFrame(self, label_text="CTkScrollableFrame")
        # self.scrollable_frame.grid(row=1, column=2, padx=(20, 0), pady=(20, 0), sticky="nsew")
        # self.scrollable_frame.grid_columnconfigure(0, weight=1)
        # self.scrollable_frame_switches = []
        # for i in range(100):
        #     switch = customtkinter.CTkSwitch(master=self.scrollable_frame, text=f"CTkSwitch {i}")
        #     switch.grid(row=i, column=0, padx=10, pady=(0, 20))
        #     self.scrollable_frame_switches.append(switch)

        # # create checkbox and switch frame
        # self.checkbox_slider_frame = customtkinter.CTkFrame(self)
        # self.checkbox_slider_frame.grid(row=1, column=3, padx=(20, 20), pady=(20, 0), sticky="nsew")
        # self.checkbox_1 = customtkinter.CTkCheckBox(master=self.checkbox_slider_frame)
        # self.checkbox_1.grid(row=1, column=0, pady=(20, 0), padx=20, sticky="n")
        # self.checkbox_2 = customtkinter.CTkCheckBox(master=self.checkbox_slider_frame)
        # self.checkbox_2.grid(row=2, column=0, pady=(20, 0), padx=20, sticky="n")
        # self.checkbox_3 = customtkinter.CTkCheckBox(master=self.checkbox_slider_frame)
        # self.checkbox_3.grid(row=3, column=0, pady=20, padx=20, sticky="n")

        # # set default values
        # # self.sidebar_button_3.configure(state="enabled", text="Справка (QA)")
        # self.checkbox_3.configure(state="disabled")
        # self.checkbox_1.select()
        # self.scrollable_frame_switches[0].select()
        # self.scrollable_frame_switches[4].select()
        # self.radio_button_3.configure(state="disabled")
        # self.appearance_mode_optionemenu.set("Dark")
        # self.scaling_optionemenu.set("100%")
        # self.optionmenu_1.set("CTkOptionmenu")
        # self.combobox_1.set("CTkComboBox")
        # self.slider_1.configure(command=self.progressbar_2.set)
        # self.slider_2.configure(command=self.progressbar_3.set)
        # self.progressbar_1.configure(mode="indeterminnate")
        # self.progressbar_1.start()
        self.textbox.insert("0.0", "Приложение для прогнозирования давления в шинах\n\n" + "Прогнозирование давления в шине происходит за счёт 20-ти (на данный момент) входных параметрах. В них входит химический состав почвы, скорость передвижения техники и другие. Нейросеть возвращает бинарный классификатор, дающий понятие о том, какого давления нужны шины (нормального или низкого).\n\n")
        # self.seg_button_1.configure(values=["CTkSegmentedButton", "Value 2", "Value 3"])
        # self.seg_button_1.set("Value 2")

    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(text="Введите выходные данные", title="Прогнозирование по параметрам")
        dialog.geometry('550x350')
        print("CTkInputDialog:", dialog.get_input())

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def sidebar_button_event(self):
        print("sidebar_button click")

    def prediction(self):
        # dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="CTkInputDialog",)
        # dialog.geometry('550x350')
        # print("Скорость (км/ч):", dialog.get_input())
        # speed = dialog.get_input()

        class dialog_frame(customtkinter.CTk):
            def __init__(self):
                super().__init__()
                self.title('Прогнозирование по входным параметрам')
                self.geometry(f"{640}x{450}")
                self.grid_columnconfigure((0, 1), weight=0)
                self.grid_columnconfigure((2, 3), weight=0)
                self.grid_rowconfigure((0, 1, 2, 3,4), weight=1)

                self.entry = customtkinter.CTkEntry(self, placeholder_text="Скорость")
                self.entry.grid(row=0, column=0, columnspan=1, padx=(10, 10), pady=(10, 10), sticky="nsew")
                self.entry1 = customtkinter.CTkEntry(self, placeholder_text="CTkEntry")
                self.entry1.grid(row=0, column=1, columnspan=1, padx=(10, 10), pady=(10, 10), sticky="nsew")
                self.entry2 = customtkinter.CTkEntry(self, placeholder_text="CTkEntry")
                self.entry2.grid(row=0, column=2, columnspan=1, padx=(10, 10), pady=(10, 10), sticky="nsew")
                self.entry3 = customtkinter.CTkEntry(self, placeholder_text="CTkEntry")
                self.entry3.grid(row=0, column=3, columnspan=1, padx=(10, 10), pady=(10, 10), sticky="nsew")
                self.entry4 = customtkinter.CTkEntry(self, placeholder_text="CTkEntry")
                self.entry4.grid(row=1, column=0, columnspan=1, padx=(10, 10), pady=(10, 10), sticky="nsew")
                self.entry5 = customtkinter.CTkEntry(self, placeholder_text="CTkEntry")
                self.entry5.grid(row=1, column=1, columnspan=1, padx=(10, 10), pady=(10, 10), sticky="nsew")
                self.entry6 = customtkinter.CTkEntry(self, placeholder_text="CTkEntry")
                self.entry6.grid(row=1, column=2, columnspan=1, padx=(10, 10), pady=(10, 10), sticky="nsew")
                self.entry7 = customtkinter.CTkEntry(self, placeholder_text="CTkEntry")
                self.entry7.grid(row=1, column=3, columnspan=1, padx=(10, 10), pady=(10, 10), sticky="nsew")
                self.entry8 = customtkinter.CTkEntry(self, placeholder_text="CTkEntry")
                self.entry8.grid(row=2, column=0, columnspan=1, padx=(10, 10), pady=(10, 10), sticky="nsew")
                self.entry9 = customtkinter.CTkEntry(self, placeholder_text="CTkEntry")
                self.entry9.grid(row=2, column=1, columnspan=1, padx=(10, 10), pady=(10, 10), sticky="nsew")
                self.entry10 = customtkinter.CTkEntry(self, placeholder_text="Скорость")
                self.entry10.grid(row=2, column=2, columnspan=1, padx=(10, 10), pady=(10, 10), sticky="nsew")
                self.entry11 = customtkinter.CTkEntry(self, placeholder_text="CTkEntry")
                self.entry11.grid(row=2, column=3, columnspan=1, padx=(10, 10), pady=(10, 10), sticky="nsew")
                self.entry12 = customtkinter.CTkEntry(self, placeholder_text="CTkEntry")
                self.entry12.grid(row=3, column=0, columnspan=1, padx=(10, 10), pady=(10, 10), sticky="nsew")
                self.entry13 = customtkinter.CTkEntry(self, placeholder_text="CTkEntry")
                self.entry13.grid(row=3, column=1, columnspan=1, padx=(10, 10), pady=(10, 10), sticky="nsew")
                self.entry14 = customtkinter.CTkEntry(self, placeholder_text="CTkEntry")
                self.entry14.grid(row=3, column=2, columnspan=1, padx=(10, 10), pady=(10, 10), sticky="nsew")
                self.entry15 = customtkinter.CTkEntry(self, placeholder_text="CTkEntry")
                self.entry15.grid(row=3, column=3, columnspan=1, padx=(10, 10), pady=(10, 10), sticky="nsew")
                self.entry16 = customtkinter.CTkEntry(self, placeholder_text="CTkEntry")
                self.entry16.grid(row=4, column=0, columnspan=1, padx=(10, 10), pady=(10, 10), sticky="nsew")
                self.entry17 = customtkinter.CTkEntry(self, placeholder_text="CTkEntry")
                self.entry17.grid(row=4, column=1, columnspan=1, padx=(10, 10), pady=(10, 10), sticky="nsew")
                self.entry18 = customtkinter.CTkEntry(self, placeholder_text="CTkEntry")
                self.entry18.grid(row=4, column=2, columnspan=1, padx=(10, 10), pady=(10, 10), sticky="nsew")
                self.entry19 = customtkinter.CTkEntry(self, placeholder_text="CTkEntry")
                self.entry19.grid(row=4, column=3, columnspan=1, padx=(10, 10), pady=(10, 10), sticky="nsew")



                self.button = customtkinter.CTkButton(self, command=self.submit_forms, text='Подтвердить')
                self.button.grid(row=5, column=0, padx=(10, 10), pady=(10, 10), sticky="ew")

            def submit_forms(self):

                speed = self.entry.get()
                entr1 = self.entry1.get()
                entr2 = self.entry2.get()
                entr3 = self.entry3.get()
                entr4 = self.entry4.get()
                entr5 = self.entry5.get()
                entr6 = self.entry6.get()
                entr7 = self.entry7.get()
                entr8 = self.entry8.get()
                entr9 = self.entry9.get()
                entr10 = self.entry.get()
                entr11 = self.entry1.get()
                entr12 = self.entry2.get()
                entr13 = self.entry3.get()
                entr14 = self.entry4.get()
                entr15 = self.entry5.get()
                entr16 = self.entry6.get()
                entr17 = self.entry7.get()
                entr18 = self.entry8.get()
                entr19 = self.entry9.get()

        d = dialog_frame()




    def learned(self):
        cr = create_dataset()
        cr.data_ground_config()
        x_train_trip, x_test_trip, y_train_trip, y_test_trip  = cr.data_trip_config()
        nm = neural_model(x_test_trip, x_train_trip, y_train_trip, y_test_trip)
        nm.neural_model()
        gen = nm.learn() 
        for i in gen:
            self.textbox1.insert("0.0", f'Epoch: {str(i[0] + 1)} Loss: {str(i[1])}\n')
            

if __name__ == "__main__":
    app = App()
    app.mainloop()