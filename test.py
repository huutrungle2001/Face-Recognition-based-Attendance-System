import PySimpleGUI as sg

print(sg.version)
print(sg)

sg.change_look_and_feel('Light Brown 1')

background = sg.LOOK_AND_FEEL_TABLE['LightBrown1']['BACKGROUND']

layout = [  [sg.Text('My Window')],
            [sg.Button('test', image_data=sg.DEFAULT_BASE64_ICON, border_width=0, use_ttk_buttons=True, button_color=('black',background)),
             sg.Button('Exit')]  ]

window = sg.Window('Window Title', layout, use_default_focus=False)

while True:             # Event Loop
    event, values = window.read()
    print(event, values)
    if event in (None, 'Exit'):
        break
    window['test'].update(image_data=sg.PSG_DEBUGGER_LOGO)
window.close()