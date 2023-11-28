# импорт необходимых пакетов
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.dialog import MDDialog
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.uix.popup import Popup
from kivymd.uix.pickers import MDDatePicker, MDTimePicker
from kivy.utils import platform
import webbrowser
from kivymd.uix.button import MDRaisedButton

# Код на языке kv
KV = '''
# объявление экрана
MDScreen:
    # создание в нижней части экрана навигацию
    MDBottomNavigation: 

        # создание навигационной кнопки в нижней части экрана:
        MDBottomNavigationItem: 
            name: 'screen 1' 
            text: 'Техобслуживание и каталог' 
            icon: 'wrench' 

            # выбор экрана 1
            # создание метки
            MDGridLayout:
                cols: 1
                spacing: "10dp"
                padding: "10dp"
            
                MDLabel:
                    text: "Выберите марку автомобиля:"
                    halign: "center"
                    
                MDRaisedButton:
                    text: "Toyota"
                    on_release: app.open_parts_catalog("Toyota")
                
                MDRaisedButton:
                    text: "Nissan"
                    on_release: app.open_parts_catalog("Nissan")

                MDRaisedButton:
                    text: "Audi"
                    on_release: app.open_parts_catalog("Audi")

                MDRaisedButton:
                    text: "Ford"
                    on_release: app.open_parts_catalog("Ford")
                    
                MDRaisedButton:
                    text: "Hyundai"
                    on_release: app.open_parts_catalog("Hyundai")           
                    
                MDRaisedButton:
                    text: "Lexus"
                    on_release: app.open_parts_catalog("Lexus")
                
                MDRaisedButton:
                    text: "Kia"
                    on_release: app.open_parts_catalog("Kia")
                
                MDRaisedButton:
                    text: "Chevrolet"
                    on_release: app.open_parts_catalog("Chevrolet")
                    
                MDRaisedButton:
                    text: "Infiniti"
                    on_release: app.open_parts_catalog("Infiniti")
                    
        # создание навигационной кнопки в нижней части экрана:
        MDBottomNavigationItem: 
            name: 'screen 2' 
            text: 'ОСАГО' 
            icon: 'passport' 

            # выбор экрана 1
            # создание метки
            MDLabel: 
                id: osago_info_label
                text: 'Здесь будет информация о ОСАГО' 
                halign: 'center' 

                MDRaisedButton:
                    text: 'Ввести ОСАГО'
                    on_release: app.open_osago_input()

        # создание навигационной кнопки в нижней части экрана:
        MDBottomNavigationItem: 
            name: 'screen 3' 
            text: 'Напоминания' 
            icon: 'bell' 

            MDBoxLayout:
                orientation: 'vertical'
                padding: "20dp"

                MDLabel:
                    id: reminder_label
                    text: ''
                    halign: 'center'

                MDRaisedButton:
                    text: 'Добавить напоминание'
                    on_release: app.open_reminder_input()

        # создание навигационной кнопки в нижней части экрана:
        MDBottomNavigationItem: 
            name: 'screen 4' 
            text: 'Помощь' 
            icon: 'help' 

            # выбор экрана 4
            # создание метки
            MDBoxLayout:
                orientation: 'vertical'
                padding: "10dp"

                MDLabel:
                    text: 'Здесь полезная информация для водителей. Для открытия ссылок, нажимайте на иконки.'
                    halign: 'center'

                MDList:
                    OneLineIconListItem:
                        text: '- Как правильно парковаться'
                        IconLeftWidget:
                            icon: 'car'
                            on_release: app.open_url('https://www.autonews.ru/news/62f26f629a79475fb9a6bf56')

                    OneLineIconListItem:
                        text: '- Как управлять автомобилем на скользкой дороге'
                        IconLeftWidget:
                            icon: 'car-traction-control'
                            on_release: app.open_url('https://65.mchs.gov.ru/deyatelnost/press-centr/novosti/4587065')

                    OneLineIconListItem:
                        text: '- Правила дорожного движения в городе'
                        IconLeftWidget:
                            icon: 'traffic-light'
                            on_release: app.open_url('https://www.drom.ru/pdd/pdd/')
                            
                    OneLineIconListItem:
                        text: '- Как менять свечу зажигания'
                        IconLeftWidget:
                            icon: 'engine'
                            on_release: app.open_url('https://autoexpertjournal.ru/zamena-svechej-zazhiganiya/')
                    
                    OneLineIconListItem:
                        text: '- Советы начинающему водителю (сборник)'
                        IconLeftWidget:
                            icon: 'book'
                            on_release: app.open_url('https://pikabu.ru/story/sovetyi_nachinayushchemu_voditelyu_sbornik_7838158')
                    
                    OneLineIconListItem:
                        text: '- Как подготовить машину к зиме в Якутии'
                        IconLeftWidget:
                            icon: 'car-wash'
                            on_release: app.open_url('https://ysia.ru/zimovka-avto-v-yakutske-kak-podgotovit-mashinu-i-skolko-eto-stoit/')
'''


# App class
class MyApp_Car(MDApp):

    def build(self):
        #
        screen = Builder.load_string(KV)

        self.reminder_date = None  # добавил атрибут reminder_date
        self.reminder_time = None
        self.reminders = []

        # возвращающийся главный экран
        return screen

    def open_url(self, url):
        import webbrowser
        webbrowser.open(url)

    def open_osago_input(self):
        content = MDTextField(hint_text="Введите информацию по ОСАГО")
        dialog = MDDialog(
            title="Ввод информации по ОСАГО",
            type="custom",
            content_cls=content,
            buttons=[
                MDFlatButton(
                    text="Отмена",
                    on_release=self.close_dialog
                ),
                MDFlatButton(
                    text="Сохранить",
                    on_release=lambda *args: self.save_osago_info(content.text)
                )
            ]
        )
        dialog.open()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.date_dialog_opened = False
        self.time_dialog_opened = False
        self.reminder_category = None

    def open_reminder_input(self):
        # Создание комбинированного списка с категориями напоминаний
        category_spinner = Spinner(
            text='Выберите категорию напоминания',
            values=('Замена фильтра (-ов)', 'Замена масла', 'Замена элементов ходовой части автомобиля', 'Замена шин', 'Другое ТО')
        )

        # Создание диалога выбора даты
        date_dialog = MDDatePicker(on_save=self.set_reminder_date)
        date_dialog.bind(on_save=lambda *args: self.dismiss_dialog(date_dialog, 'date'))
        self.date_dialog_opened = True

        # Создание диалога выбора времени
        time_dialog = MDTimePicker()
        time_dialog.bind(time=self.set_reminder_time)
        time_dialog.bind(on_dismiss=lambda *args: self.dismiss_dialog(time_dialog, 'time'))
        self.time_dialog_opened = True

        # Создание диалога для отображения выбранной категории и даты/времени напоминания
        dialog = MDDialog(
            title="Добавить напоминание",
            type="custom",
            content_cls=BoxLayout(orientation='vertical', padding="10dp", spacing="10dp", size_hint_y=None),
            buttons=[
                MDFlatButton(
                    text="Отмена",
                    on_release=self.close_dialog
                ),
                MDFlatButton(
                    text="Сохранить",
                    on_release=lambda *args: self.save_reminder(category_spinner.text, dialog)
                )
            ],
            auto_dismiss=False
        )
        dialog.content_cls.add_widget(category_spinner)
        dialog.open()
        date_dialog.open()
        time_dialog.open()

    def dismiss_dialog(self, dialog, dialog_type):
        if dialog_type == 'date':
            self.date_dialog_opened = False
        elif dialog_type == 'time':
            self.time_dialog_opened = False

        if not self.date_dialog_opened and not self.time_dialog_opened:
            dialog.dismiss()

    def save_reminder(self, category, dialog):
        reminder = {
            'category': category,
            'date': self.reminder_date,
            'time': self.reminder_time
        }
        self.reminders.append(reminder)
        self.update_reminder_label()
        dialog.dismiss()

    def update_reminder_label(self):
        label_text = ""
        for reminder in self.reminders:
            category = reminder['category']
            date = reminder['date']
            time = reminder['time']
            label_text += f"Напоминание: Категория - {category}, Дата - {date}, Время - {time}\n\n"
        self.root.ids.reminder_label.text = label_text

    def set_reminder_date(self, date):
        self.reminder_date = date.strftime("%d.%m.%Y")
        self.root.ids.reminder_label.text = f"Напоминание: Категория - {self.reminder_category}, Дата - {self.reminder_date}, Время - {self.reminder_time}"

    def set_reminder_time(self, instance, time):
        self.reminder_time = time.strftime("%H:%M")
        self.root.ids.reminder_label.text = f"Напоминание: Категория - {self.reminder_category}, Дата - {self.reminder_date}, Время - {self.reminder_time}"

    def close_dialog(self, instance):
        instance.parent.parent.dismiss()
        self.update_reminder_label()

    def save_osago_info(self, info):
        self.root.ids.osago_info_label.text = info

    def open_parts_catalog(self, brand):
        if brand == "Toyota":
            webbrowser.open("https://toyota.epc-data.com/")
        if brand == "Nissan":
            webbrowser.open("https://nissan.epc-data.com/")
        if brand == "Лада":
            webbrowser.open("https://www.lada-image.ru/products/catalog/")
        if brand == "Audi":
            webbrowser.open("https://audi.7zap.com/ru/rdw/")
        if brand == "Ford":
            webbrowser.open("https://ford.catalogs-parts.com/#%7Bclient:1;page:models;lang:ru;category:car%7D")
        if brand == "Hyundai":
            webbrowser.open("https://hyundai.catalogs-parts.com/#%7Bclient:1;page:models;lang:ru;catalog:eur%7D")
        if brand == "Lexus":
            webbrowser.open("https://lexus.epc-data.com/")
        if brand == "Kia":
            webbrowser.open("https://kia.catalogs-parts.com/#%7Bclient:1;page:models;lang:ru;catalog:eur%7D")
        if brand == "Chevrolet":
            webbrowser.open("https://chevrolet.catalogs-parts.com/#%7Bclient:1;page:models;lang:ru%7D")
        if brand == "Infiniti":
            webbrowser.open("https://infiniti.catalogs-parts.com/#%7Bclient:1;page:models;lang:ru;catalog:el%7D")


app = MyApp_Car()
app.run()