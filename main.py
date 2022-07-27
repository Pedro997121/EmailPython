from time import sleep
import pyautogui


#Abrir navegador
pyautogui.hotkey("win", "r"), pyautogui.write("Opera"), pyautogui.press("Enter")

#Esperar um pouco pra iniciar o navegador, dependendo do computador o comando sleep deve ser maior.
sleep(1)

#Abrir nova aba, Acessar a barra de url, digitar o email.
pyautogui.hotkey("ctrl", "t"), pyautogui.hotkey("Ctrl", "l"), pyautogui.write("https://outlook.live.com/mail/0/"), pyautogui.press("Enter")

sleep(2)

#Clickar em mandar email. (Muda de acordo com o tamanho da tela do monitor)
pyautogui.click(x=185, y=165)
sleep(1)

#destinatário
pyautogui.write("email@outlook.com")
pyautogui.press("Tab")

#Assunto
pyautogui.write("Assunto")
pyautogui.press("Tab")

#Mensagem
pyautogui.write("""
                
                
            *Mensagem*    
                
                
                """)
#Enviar email
pyautogui.click(x=368, y=658)

