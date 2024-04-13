import pyautogui
import time

log1 = "C:/Users/ariel/Desktop/bot/log1.txt"
log2 = "C:/Users/ariel/Desktop/botnew/secondbot/log2.txt"
incall_flag = "C:/Users/ariel/Desktop/bot/log.txt"



def check_bye():
    var1 = True
    var2 = True
    target_color = (251, 166, 28)
    tolerance = 10
    pixel_1 = pyautogui.pixel(734, 254)
    pixel_2 = pyautogui.pixel(1546, 399)
    print("Detected color:", pixel_1) 
    print("Detected color:", pixel_1)  # Debugging output
    for i in range(3):  # Check each RGB channel separately
        if not (target_color[i] - tolerance <= pixel_1[i] <= target_color[i] + tolerance):
            var1 = False
    for i in range(3):  # Check each RGB channel separately
        if not (target_color[i] - tolerance <= pixel_2[i] <= target_color[i] + tolerance):
            var2 = False
    return (var1 and var2)



# Function to check if incoming call is detected
def incoming_call_chrome():
    # Check if the pixel color at the specified position matches the target color
    target_color = (35, 165, 89)  # Provided color
    tolerance = 10  # Tolerance level for color matching
    pixel_color = pyautogui.pixel(673, 414)  # Provided position
    # print("Detected color:", pixel_color)  # Debugging output
    for i in range(3):  # Check each RGB channel separately
        if not (target_color[i] - tolerance <= pixel_color[i] <= target_color[i] + tolerance):
            return False
    return True


def incoming_call_edge():
    # Check if the pixel color at the specified position matches the target color
    target_color = (35, 165, 89)  # Provided color
    tolerance = 10  # Tolerance level for color matching
    pixel_color = pyautogui.pixel(1606, 492)  # Provided position
    # print("Detected color:", pixel_color)  # Debugging output
    for i in range(3):  # Check each RGB channel separately
        if not (target_color[i] - tolerance <= pixel_color[i] <= target_color[i] + tolerance):
            return False
    return True


def check_if_answer_chrome():
    target_color = (251, 167, 27)
    tolerance = 10
    pixel_color = pyautogui.pixel(734, 254)
    #print("Detected color:", pixel_color)  # Debugging output
    for i in range(3):  # Check each RGB channel separately
        if not (target_color[i] - tolerance <= pixel_color[i] <= target_color[i] + tolerance):
            return False
    return True


def check_if_answer_edge():
    target_color = (251, 167, 27)
    tolerance = 10
    pixel_color = pyautogui.pixel(1546, 399)
    # print("Detected color:", pixel_color)  # Debugging output
    for i in range(3):  # Check each RGB channel separately
        if not (target_color[i] - tolerance <= pixel_color[i] <= target_color[i] + tolerance):
            return False
    return True


# Function to answer the call
def answer_call_chrome():
    # Click on a specific location to answer the call
    pyautogui.click(673, 414)  # Provided position
    print("Clicked to answer call")  # Debugging output
    # Optionally, add code to handle the call (e.g., mute microphone)


def answer_call_edge():
    # Click on a specific location to answer the call
    pyautogui.click(1606, 492)  # Provided position
    print("Clicked to answer call")  # Debugging output
    # Optionally, add code to handle the call (e.g., mute microphone)


def calling_cause_call_chrome():
    # Check if the pixel color at the specified position matches the target color
    target_color = (181, 186, 193)  # Provided color
    tolerance = 10  # Tolerance level for color matching
    pixel_color = pyautogui.pixel(422, 188)  # Provided position
    # print("Detected color:", pixel_color)  # Debugging output
    for i in range(3):  # Check each RGB channel separately
        if not (target_color[i] - tolerance <= pixel_color[i] <= target_color[i] + tolerance):
            return False
    return True

def calling_cause_call_edge():
    # Check if the pixel color at the specified position matches the target color
    target_color = (181, 186, 193)  # Provided color
    tolerance = 10  # Tolerance level for color matching
    pixel_color = pyautogui.pixel(1396, 265)  # Provided position
    # print("Detected color:", pixel_color)  # Debugging output
    for i in range(3):  # Check each RGB channel separately
        if not (target_color[i] - tolerance <= pixel_color[i] <= target_color[i] + tolerance):
            return False
    return True


def dial_respond_chrome():
    # Click on a specific location to answer the call
    pyautogui.click(422, 188)  # Provided position
    print("Clicked to call")  # Debugging output
    # Optionally, add code to handle the call (e.g., mute microphone)

def dial_respond_edge():
    # Click on a specific location to answer the call
    pyautogui.click(1396, 265)  # Provided position
    print("Clicked to call")  # Debugging output
    # Optionally, add code to handle the call (e.g., mute microphone)


def hang_up_chrome():
    target_color = (218, 55, 60)  # Provided color
    tolerance = 10  # Tolerance level for color matching
    pixel_color = pyautogui.pixel(870, 421)  # Provided position
    # print("Detected color:", pixel_color)  # Debugging output
    for i in range(3):  # Check each RGB channel separately
        if not (target_color[i] - tolerance <= pixel_color[i] <= target_color[i] + tolerance):
            return False
    return True


def hang_up_edge():
    target_color = (218, 55, 60)  # Provided color
    tolerance = 10  # Tolerance level for color matching
    pixel_color = pyautogui.pixel(1830, 450)  # Provided position
    # print("Detected color:", pixel_color)  # Debugging output
    for i in range(3):  # Check each RGB channel separately
        if not (target_color[i] - tolerance <= pixel_color[i] <= target_color[i] + tolerance):
            return False
    return True



# Main loop to continuously monitor for incoming calls
while True:
    ###
    # pixel_color = pyautogui.pixel(870, 421)  # Provided position
    # print("Detected color:", pixel_color)
    ###
    with open(log1, 'r') as file:
        call_init = file.read()
    with open(log2, 'r') as file:
        call_init2 = file.read()
    with open(incall_flag, 'r') as file:
        call_flag = file.read()

    if call_flag == 'incall':
        while(check_bye()):
            time.sleep(1)
        if hang_up_edge():
            pyautogui.click(1830, 450)  # Provided position
            print("Hanged up")
            with open(incall_flag, 'w') as file:
                file.write('')
        if hang_up_chrome():
            pyautogui.click(870, 421)  # Provided position
            print("Hanged up")
            with open(incall_flag, 'w') as file:
                file.write('')

######  We initiating  ##########
    if incoming_call_chrome():
        with open(log1, 'w') as file:
            file.write('calling')
        with open(log2, 'r') as file:
            respond = file.read()
            if respond == 'ok':
                answer_call_chrome()
                with open(log2, 'w') as file:
                    file.write('')
                with open(log1, 'w') as file:
                    file.write('')
                with open(incall_flag, 'w') as file:
                    file.write('incall')


######  Them initiating  ##########
    if call_init2 == 'calling':
        if calling_cause_call_chrome():
            dial_respond_chrome()
        if check_if_answer_chrome():
            with open(log1, 'w') as file:
                file.write('ok')
            with open(log2, 'w') as file:
                file.write('')








    if incoming_call_edge():
        with open(log2, 'w') as file:
            file.write('calling')
        with open(log1, 'r') as file:
            respond = file.read()
        if respond == 'ok':
            answer_call_edge()
            with open(log2, 'w') as file:
                file.write('')
            with open(log1, 'w') as file:
                file.write('')
            with open(incall_flag, 'w') as file:
                file.write('incall')



    if call_init == 'calling':
        if calling_cause_call_edge():
            dial_respond_edge()
        if check_if_answer_edge():
            with open(log2, 'w') as file:
                file.write('ok')
            with open(log1, 'w') as file:
                file.write('')


    time.sleep(1)  
