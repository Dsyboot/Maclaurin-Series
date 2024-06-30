# Seccion grafica kivy
import kivy
from kivy.lang import Builder
from kivy.uix.scrollview import ScrollView
from kivy.properties import StringProperty, ColorProperty
from kivy.clock import Clock

# Seccion grafica kivymd
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout

# Otras librerias
import math, threading
from random import randint
from functions import Math, Solver

# Version del programa
__version__ = "0.1.0"
kivy.require("2.2.1") # Requerir la version mas estable

# Variable global para llevar el tiempo transcurrido
start_time = 0

def update_start_time(dt):
    global start_time
    start_time += dt
#end def

# Programar la actualización del tiempo transcurrido
Clock.schedule_interval(update_start_time, 0)

# Funcion para obtener un color RGB random
def get_rgb(speed=1):
    global start_time
    # Preparar calculos
    tm = start_time
    fr = 0.1 * speed
    fg = 0.05 * speed
    fb = 0.03 * speed
    
    # Calcular los valores RGB
    red = int(math.sin(2 * math.pi * fr * tm) * 127 + 128)
    green = int(math.sin(2 * math.pi * fg * tm) * 127 + 128)
    blue = int(math.sin(2 * math.pi * fb * tm) * 127 + 128)
    
    return (red, green, blue)
#end def

# Contenido del input de ecuaciones
class Content(MDBoxLayout):
    pass
#end class

# Contenido del input de ecuaciones (solo x)
class Content2(MDBoxLayout):
    pass
#end class

# MessageBox (extraido del proyecto personal "YoDo")
class MsgBox:
    def __init__(self):
        self.__result = None
        self.__event = None
    #end if
    
    def show(self, title, msg = None):
        def on_close_button_press(res, *args):
            nonlocal dialog
            dialog.dismiss()
            
            if res == self.__result and self.__event is not None:
                self.__event()
            #end if
        #end def
        
        if msg is None:
            dialog = MDDialog(
                title = title,
                buttons=[
                    MDFlatButton(
                        text="Cerrar",
                        on_press=lambda res: on_close_button_press("okey")
                    )
                ],
            )
            
            dialog.open()
        else:
            label = MDLabel(text=msg, halign="left", valign="top", adaptive_height = True)
            layout = MDBoxLayout(orientation='vertical', adaptive_height = True)
            layout.add_widget(label)
        
            dialog = MDDialog(
                title=f"{title}\n\n\n",
                type="custom",
                content_cls=ScrollView(always_overscroll = False, size_hint_y = 2.2),
                buttons=[
                    MDFlatButton(
                        text="Cerrar",
                        on_press=lambda res: on_close_button_press("okey")
                    )
                ],
            )
        
            dialog.content_cls.add_widget(layout)
            dialog.update_height()
            dialog.open()
        #end if
    #end def
    
    # Funcion para invocar una funcion en un resultado especifico
    def cus_event(self, result, fun):
        self.__result = result
        self.__event = fun
    #end def
#end class

# Controladora de pantallas
class ManScr(MDScreen):
    pass
#end class

# Pantalla de carga
class LoadingScreen(MDScreen):
    prog_name = StringProperty("Maclaurin Series")
    versi = StringProperty("v " + __version__)
    
    def on_enter(self, *args):
        ti = randint(3, 6)
        Clock.schedule_once(self.go_main, ti)
    #end def
        
    def go_main(self, dt):
        if self.manager.current == "load_screen":
            self.manager.current = "main_screen"
        #end if
    #end def
#end class

# Pantalla principal
class MainScreen(MDScreen):
    # Variables para el calculo
    ans = 0
    ecuation = StringProperty("")
    result = StringProperty(f"{ans}")
    solve = Solver() # Objeto de la clase Solver
    
    # Variables para el cursor
    blink_state = True
    blink_pos = None
    
    # Variables para otras cosas
    dialog = None
    border_color = ColorProperty((.2706, .7137, 0))
    grades_mode = StringProperty("RAD" if Math.inRadians else "DEG")
    prog_title = StringProperty(f"Series de Maclaurin ({'Radianes' if Math.inRadians else 'Grados'})")
    
    def on_enter(self, *args):
        self.blink_pos = len(self.ecuation)
        Clock.schedule_interval(self.update_color, 1/60)
        Clock.schedule_interval(self.blink_text, 0.5)
    #end def
    
    def update_color(self, dt):
        rgb = get_rgb(speed=2.5)
        color = (rgb[0] / 255, rgb[1] / 255, rgb[2] / 255, 1)  # Convertir a formato rgba
        self.border_color = color
    #end def
    
    def change_grades_mode(self):
        # Cambiar el modo de los grados
        Math.usesRadians(not Math.inRadians)
        
        # Establecer el texto
        self.grades_mode = "RAD" if Math.inRadians else "DEG"
        self.prog_title = f"Series de Maclaurin ({'Radianes' if Math.inRadians else 'Grados'})"
    #end def
    
    def blink_text(self, dt):
        # Eliminar el cursor si es visible
        if not self.blink_state:
            self.ecuation = self.ecuation[:self.blink_pos] + self.ecuation[self.blink_pos + 1:]
        
        # Activar el cursor
        if self.blink_state:
            # Poner el cursor en medio de la posicion
            self.ecuation = self.ecuation[:self.blink_pos] + "|" + self.ecuation[self.blink_pos:]
        
        # Invertir el valor del estado
        self.blink_state = not self.blink_state
    #end def
    
    def move_cursor(self, toRight : bool):
        # Eliminar el cursor antes de mover
        if not self.blink_state:
            self.ecuation = self.ecuation[:self.blink_pos] + self.ecuation[self.blink_pos + 1:]
        
        # Mover la posicion a la izquierda/derecha
        if not toRight and self.blink_pos > 0:
            self.blink_pos -= 1
        elif toRight and self.blink_pos < len(self.ecuation):
            self.blink_pos += 1
        
        # Hacer que el cursor siempre se mire
        self.blink_state = False
        self.ecuation = self.ecuation[:self.blink_pos] + "|" + self.ecuation[self.blink_pos:]
    #end def
    
    def show_ecuation_input(self, title, type = None, justX = False):
        def on_close_button_press(res, *args):
            x = self.dialog.content_cls.ids.eval.text
            
            if not justX:
                n = self.dialog.content_cls.ids.counts.text
            #end if
            self.dialog.dismiss()
            
            if res == "okey":
                x = "0" if x.strip() == "" else x
                
                if type is None:
                    if justX:
                        self.make_ecuation(title, x)
                    else:
                        n = "∞" if n.strip() == "" else n
                        self.make_ecuation(title, x, n)
                else:
                    if justX:
                        self.make_ecuation(type, x)
                    else:
                        n = "∞" if n.strip() == "" else n
                        self.make_ecuation(type, x, n)
            #end if
        #end def
        
        self.dialog = None
        if not self.dialog:
            self.dialog = MDDialog(
                type="custom",
                content_cls=Content() if not justX else Content2(),
                buttons=[
                    MDFlatButton(
                        text="CANCEL",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_press=lambda res: on_close_button_press("cancel")
                    ),
                    MDFlatButton(
                        text="OK",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_press=lambda res: on_close_button_press("okey")
                    ),
                ],
            )
        self.dialog.content_cls.ids.text_title.text = f"Insertar funcion: {title}"
        self.dialog.open()
    #end def
    
    def make_ecuation(self, ads: str, x=None, n=None):
        if ads == None:
            self.ecuation = ""
            self.result = "0"
            self.blink_pos = 0
        elif ads in ["+", "-", "*", "/", "%"]:
            self.ecuation = self.ecuation[:self.blink_pos] + f" {ads} " + self.ecuation[self.blink_pos:]
            self.blink_pos += len(f" {ads} ")
        elif ads in "0123456789":
            self.ecuation = self.ecuation[:self.blink_pos] + ads + self.ecuation[self.blink_pos:]
            self.blink_pos += len(ads)
        elif ads in [".", "(", ")", "e", "π", "τ", "ANS"]:
            self.ecuation = self.ecuation[:self.blink_pos] + ads + self.ecuation[self.blink_pos:]
            self.blink_pos += len(ads)
        elif ads in self.solve.functions.keys():
            if x is not None and n is not None:
                n = n.replace("inf", "∞")
                if ads == "sqrt" and n.strip() == "∞":
                    self.ecuation = self.ecuation[:self.blink_pos] + f"{ads}({x})" + self.ecuation[self.blink_pos:]
                    self.blink_pos += len(f"sqrt({x})")
                elif "∞" in n and ads == "pow":
                    self.ecuation = self.ecuation[:self.blink_pos] + f"{ads}({x}, 1)" + self.ecuation[self.blink_pos:]
                    self.blink_pos += len(f"{ads}({x}, 1)")
                else:
                    self.ecuation = self.ecuation[:self.blink_pos] + f"{ads}({x}, {n})" + self.ecuation[self.blink_pos:]
                    self.blink_pos += len(f"{ads}({x}, {n})")
                #end if
            elif x is not None:
                self.ecuation = self.ecuation[:self.blink_pos] + f"{ads}({x})" + self.ecuation[self.blink_pos:]
                self.blink_pos += len(f"{ads}({x})")
            #end if
        #end if
        
        # Forzar actualizacion de la textura
        self.ids.text_result.texture_update()
    #end def
    
    def call_solve(self):
        if hasattr(self, 'current_thread') and self.current_thread.is_alive():
            self.current_thread.join()  # Esperar a que el hilo actual termine
        #end if
        
        self.result_text = "Calculando..."
        
        # Iniciar un nuevo hilo
        self.current_thread = threading.Thread(target=self.solve_ecuation)
        self.current_thread.start()
    #end def
    
    def solve_ecuation(self):
        # Preparar los datos
        self.result = "Calculando..."
        self.solve.functions["ANS"] = self.ans
        
        # Reemplazar datos antes de evaluar
        tmp = self.ecuation.replace("π", "pi").replace("τ", "tau")
        tmp = tmp.replace("∞", "inf")
        tmp = tmp.replace("|", "") # Eliminar el cursor de la evaluacion
        
        # Obtener los valores
        if tmp.strip() == "":
            self.ans = 0
        else:
            self.ans, chain = self.solve.evaluate_expression(tmp) 
        #end if
        
        # Evitar el error de los digitos
        try:
            # Verificar la longitud de la respuesta
            if (len(str(self.ans)) > 251): # Limite de 250 digitos
                Clock.schedule_once(self.show_result, 0)
            else: # Solcion al error de texto negro
                self.result = f"{self.ans}".replace("inf", "∞")
            #end if
        except ValueError:
            self.result = "Demasiados digitos"
        #end try
    #end def
    
    def show_result(self, dt):
        base = MsgBox()
        base.show("Resultado", f"{self.ans}".replace("inf", "∞"))
        self.result = "Resultado extenso..."
    #end def
    
    def remove_ecuation(self):
        # Convertir la ecuación en una lista para facilitar la manipulación
        equation_list = list(self.ecuation)
        
        # Si hay caracteres antes del cursor, eliminar el carácter en la posición del cursor
        if self.blink_pos > 0:
            equation_list.pop(self.blink_pos - 1)
            self.blink_pos -= 1  # Actualizar la posición del cursor
        
        # Actualizar la ecuación con la lista modificada
        self.ecuation = "".join(equation_list)
        
        # Forzar actualizacion de la textura
        self.ids.text_result.texture_update()
    # end def
#end class

class Main(MDApp):
    def build(self):
        self.title = "Maclaurin Series"
        self.theme_cls.theme_style = "Dark"
        self.root = Builder.load_file("mac-gui.kv")
        
        self.root.ids.builderman.current = "load_screen"
        
        return self.root
    #end def
#end class

# Ejecutar solo si es la funcion principal
if __name__ == "__main__":
    Main().run()
#end if